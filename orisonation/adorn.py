import json

import re

import inflect
inflect = inflect.engine()

with open('biblical_data/bible_adj2noun.json','r') as f: 
	adj2noun = json.load(f)

with open('biblical_data/bible_noun2adj.json','r') as f: 
	noun2adj_ = json.load(f)
noun2adj = {tuple(k.split("***")):v for k,v in list(noun2adj_.items())}

with open('biblical_data/bible_lemma2svophrases.json','r') as f:
	lemma2svos = json.load(f)

with open('biblical_data/bible_verb_and_prepphrase.json','r') as f:
	bible_verb_and_prepphrase_ = json.load(f)

from collections import defaultdict
bible_verb_and_prepphrase = defaultdict(list)
for i in bible_verb_and_prepphrase_:
	bible_verb_and_prepphrase[tuple(i[0])].append(i[1:])

with open('biblical_data/bible_nouns_and_prep_or_reclphrase.json','r') as f:
	bible_nouns_and_prep_or_reclphrase_ = json.load(f)

from collections import defaultdict
bible_nouns_and_prep_or_reclphrase = defaultdict(list)
for i in bible_nouns_and_prep_or_reclphrase_:
	bible_nouns_and_prep_or_reclphrase[tuple(i[0])].append(i[1:])


### spacy


import spacy
nlp = spacy.load('en')

from nltk.corpus import stopwords
stops = stopwords.words('english')
stops += ['someone','somebody','something','thing']


import random

from nltk import pos_tag,tokenize


## custom join

def betterjoin(listoftokens):
	astring = " ".join(listoftokens)
	astring = astring.replace(" ,",",")
	astring = astring.replace(" .",".")
	astring = re.sub(" n't","n't",astring)
	astring = re.sub(" '(?=[A-Za-z])","'",astring) ## should handle you 'll and other stuff (uses lookahead)
	astring = astring.strip()
	return astring

## pos tag

from nltk import tokenize,pos_tag

def get_tagged(astring):
	tagged = pos_tag(tokenize.casual_tokenize(astring))
	return tagged


## adorn with adj

def get_noun_adj_pair(core):
	needed_nouns = [(token,tag) for token,tag in core if tag in ["NNS","NN"]]
	for n in needed_nouns:
		try:
			adjs = noun2adj[n]
			adjs = [a for a in adjs if a.lower() not in stops]
			if n[1]=="NNS":
				thisorthose="those"
			else:
				thisorthose="this"
			return (thisorthose,n,random.choice(adjs))
		except:
			pass


def adorn_noun_with_adj(astring):
	core = get_tagged(astring)
	thisorthose, n,adj = get_noun_adj_pair(core)
	if random.choice([True,False]):
		str_rep = "%s %s so %s" % (thisorthose,n[0],adj)
	else:
		str_rep = "%s %s %s" % (thisorthose,adj,n[0])
	return str_rep


## adorn with noun comparison

def get_noun_adj_othernouns(astring):
	doc = nlp(astring)
	adj_noun_pairs = [(a.text.lower(),a.head.text.lower(),a.head.tag_) for a in doc if a.dep_=="amod" and a.text.lower() not in stops]
	for adj,noun,nounpos in adj_noun_pairs:	
		comparison_nouns = adj2noun[adj]
		if nounpos == "NNS":
			thisorthose = "those"
		else:
			thisorthose = "this"
		return (thisorthose,noun,adj,comparison_nouns)


def adorn_adj_with_noun(astring):
	thisorthose,noun,adj,other_nouns = get_noun_adj_othernouns(astring)
	other_noun = random.choice(other_nouns[:10])[0]  ## choose from top
	str_rep  = "behold---%s %s %s as a %s" % (thisorthose,noun,adj,other_noun)
	if inflect.singular_noun(other_noun): ## weirdly, returns False if already singular
		str_rep = str_rep.replace(" as a"," as")
	# str_rep = re.sub(r' a ([aeiou])',r' an \1',str_rep)
	return str_rep



## add prep/recl phrase to noun

def get_prep_recl_phrase_for_noun(core):
	nouns = [(token,tag) for token,tag in core if tag in ["NNS","NN"]]
	random.shuffle(nouns)
	for noun in nouns:
		try:
			phrase = random.choice(bible_nouns_and_prep_or_reclphrase[noun])
			if noun[1]=="NNS":
				thisorthat="those"
			else:
				thisorthat="this"
			return thisorthat,noun,phrase
		except:
			pass


def adorn_noun_with_phrase(astring):
	core = get_tagged(astring)
	thisorthat,noun,phrase = get_prep_recl_phrase_for_noun(core)
	phrase = phrase[0]
	phrase_str = betterjoin([token for token,tag in phrase])
	# phrase_str = re.sub(r'^that ',"",phrase_str,flags=re.IGNORECASE) ## some begin "that"
	# phrase_str = re.sub(r'^if ',"",phrase_str,flags=re.IGNORECASE) ## some begin "if"
	phrase_str = re.sub(r', old man$',"",phrase_str,flags=re.IGNORECASE) ## some begin "that"
	noun_str = noun[0]
	str_rep = "%s %s %s" % (thisorthat,noun_str,phrase_str)
	return str_rep


## add prep phrase to verb

from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 

def get_prep_phrase_for_verb(core):
	verbs = [(token,tag) for token,tag in core if tag.startswith("V")]
	random.shuffle(verbs)
	for verb in verbs:
		try:
			phrase = random.choice(bible_verb_and_prepphrase[verb])[0]
			return verb,phrase
			# if noun[1]=="NNS":
			# 	thisorthat="those"
			# else:
			# 	thisorthat="this"
			# return thisorthat,noun,phrase
		except:
			pass


def adorn_verb_with_phrase(astring):
	core = get_tagged(astring)
	verb,phrase = get_prep_phrase_for_verb(core)
	phrase_str = betterjoin([token for token,tag in phrase])
	str_rep = " %s %s. (Selah.)" % (verb[0],phrase_str)
	return str_rep



## SVO parallelism

from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer() 

def get_s_v_o(astring):
	core = get_tagged(astring)
	verbs = [(token,tag) for token,tag in core if tag.startswith("V")]
	verb_pos_lemmas = [(token,tag,lemmatizer.lemmatize(token)) for token,tag in verbs]
	verb_pos_lemmas = [(v,p,l) for v,p,l in verb_pos_lemmas if v not in stops]
	for v,p,l in verb_pos_lemmas:
		try:
			svos = lemma2svos[l]
			return random.choice(svos)
		except:
			pass 


def adorn_svo_parallelism(astring):
	svo = get_s_v_o(astring)
	svo_tokens = []
	for token,tag in svo:
		if tag in ["NNP","NNPS"]:
			token = token.title()
		svo_tokens.append(token)#[token.upper() if tag in ["NNP","NNPS"] else token for token,tag in svo]
	str_rep = betterjoin(svo_tokens)
	# str_rep = re.sub(r'^that ',"",str_rep,flags=re.IGNORECASE) ## some begin "that"
	str_rep = re.sub(r'^so that ',"",str_rep,flags=re.IGNORECASE) ## some begin "that"
	# str_rep = re.sub(r'^if ',"",str_rep,flags=re.IGNORECASE) ## some begin "if"
	# str_rep = re.sub(r'^and ',"",str_rep,flags=re.IGNORECASE) ## some begin "if"
	# str_rep = re.sub(r'^but ',"",str_rep,flags=re.IGNORECASE) ## some begin "if"
	# str_rep = re.sub(r'^though ',"",str_rep,flags=re.IGNORECASE) ## some begin "if"
	# str_rep = re.sub(r'^for ',"",str_rep,flags=re.IGNORECASE) ## some begin "if"
	str_rep = re.sub(r', old man$',"",str_rep,flags=re.IGNORECASE) ## some begin "that"
	return "as "+str_rep


def get_one_ok_adornment(astring):
	funcs = [
			adorn_svo_parallelism,
			adorn_noun_with_phrase,
			adorn_adj_with_noun,
			adorn_verb_with_phrase,
			adorn_noun_with_adj,
			]

	random.shuffle(funcs)

	for f in funcs:
		try:
			return 	f(astring)
		except:
			pass
	return None



def adorn(astring,prob=1.0):
	"""
	adorn an element, perhaps limited to some probability of doing so
	"""
	adornment = get_one_ok_adornment(astring)
	if not adornment:
		return astring
	if random.random()<prob:
		return "%s<br>%s" % (astring,adornment)
	return astring



## MAIN

def main():
	prayers = ["May you have found the hand",]
				#"Yea, may you always run to your sweet maker."]
	for i in prayers:
		print(adorn(i,.9))

if __name__ == '__main__':
	main()