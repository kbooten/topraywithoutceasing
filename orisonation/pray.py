## old code for sent2vec, keeping it in case it turns out this model worked better
# import sent2vec
# model = sent2vec.Sent2vecModel()
# path = 'wiki_unigrams.bin'
# print("****Loading sent2vec model: %s" % path)
# model.load_model(path)
# print("****Loaded")
# from sklearn.metrics.pairwise import cosine_similarity


## load sentence vector model
print("****Loading sbert model")
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
print("****Loaded")
import torch

## load word vector model
import gensim
word2vec_path = "shrunkenvectors_200000.bin"
print("****Loading word2vec model: %s" % word2vec_path)
word2vec = gensim.models.KeyedVectors.load_word2vec_format(word2vec_path, binary=True)
print("****Loaded")


## import prayers (but still need to add "I need ")
import myprayers


## embed
keys = [p for p in myprayers.myprayers]
key_embeddings = model.encode(["I need "+p for p in myprayers.myprayers], convert_to_tensor=True) ## set up for sbert


## biblical adornments
from adorn import adorn


## proverbs
import json
with open("biblical_data/proverbs_paired_to_tensors.json","r") as f:
    proverbs = json.load(f)

proverbs_embedded = torch.load("biblical_data/proverbs_embedded.pt")


## import and process my special vocab words
import myvocabulary
## ditch words that aren't in word to vec (ignoring, for now, alias words as in "house>habitation")
myvocabulary_filtered = {}
for pos in myvocabulary.myvocabulary:
    words_without_alias = [w.split(">")[0] for w in myvocabulary.myvocabulary[pos]]
    myvocabulary_filtered[pos]=[w for w in words_without_alias if w in word2vec]


import re
import random
from numpy import mean
import importlib ## for reloading
from nltk import tokenize



def get_close_proverb_sbert(prayer):
    """
    calculates the most similar need from proverbs using sent2vec
    returns one of the most common
    """
    query_embedding = model.encode(prayer, convert_to_tensor=True)
    #return query_embedding
    cos_scores = util.pytorch_cos_sim(query_embedding, proverbs_embedded)[0]
    cos_scores = cos_scores.cpu()
    score,top_match_indx = torch.topk(cos_scores, k=20)
    matching_proverbs = [proverbs[i] for i in top_match_indx]
    while True:
        if random.random()>.85: ## 
            return matching_proverbs[0]
        else:
            last = matching_proverbs.pop(0)
            matching_proverbs.append(last)


def proverbialize(prayer):
    """
    gets a close proverb and reformats
    """
    close_proverb = get_close_proverb_sbert(prayer)
    return "%s<br>for it is written:<br>%s" % (prayer,close_proverb)


def reload():
    """
    reload the prayer templates and the vocab
    (useful for development)
    """
    importlib.reload(myprayers)
    importlib.reload(myvocabulary)
    for pos in myvocabulary.myvocabulary:
        myvocabulary_filtered[pos]=[w for w in myvocabulary.myvocabulary[pos] if w in word2vec]


def remove_i_need(astring):
    """
    man oh man I just NEED a new computer -> a new computer
    """
    astring = re.sub(re.compile("^.+?need", re.IGNORECASE)," ",astring)
    astring = astring.strip()
    return astring
        
def homogenize(astring):
    """
    man oh man I just NEED a new computer -> I need a new computer
    """
    without_i_need = remove_i_need(astring)
    return "I need %s" % without_i_need


def try_to_get_word2vec_sim(w0,w1):
    """
    a wrapper for word2vec.similarity that returns None when a word is oov
    """
    try:
        return word2vec.similarity(w0,w1)
    except:
        return None


def max_similarity(word,list_of_tokens):
    """
    for a word, gets the most greatest cosine similarity it has with any word in list_of_tokens
    """
    values = [try_to_get_word2vec_sim(word,token) for token in list_of_tokens]
    values = [v for v in values if v !=None]
    if values==[]:
        return None
    return max(values)  


def try_to_convert_boring_to_interesting_word(boring_word,probability=.8):
    """
    """
    try:
        more_interesting_words = myvocabulary.boringword2interestingword[boring_word]
        if random.random()<probability:
            return random.choice(more_interesting_words)
        else:
            return boring_word
    except:
        return boring_word


def tune_one_list_according_to_max_similarity_to_another_list(words_to_sort,tuner_list,threshold=None):
    """
    given a list of words, words_to_sort, sorts of list in order of maximum semantic proximity with a word in tuner_list

    """
    word_and_max_similarity = [(word,max_similarity(word,tuner_list)) for word in words_to_sort]
    word_and_max_similarity = [(word,max_sim) for word,max_sim in word_and_max_similarity if max_sim!=None] ## may not need to do this
    if word_and_max_similarity==[]:
        return []
    word_and_max_similarity.sort(key=lambda x: x[1], reverse=True) ## most to least max similar
    if threshold==None:
        return [word for word,max_sim in word_and_max_similarity]
    else:
        return [word for word,max_sim in word_and_max_similarity if max_sim>=threshold]


def get_word_based_on_pos_and_vector(pos,keysetters,ineed,threshold=.42,probability=.8, top_n=4):
    """
    a confusing function
    tries to find a word of a specific pos that is similar to one or more words, called keysetters
    this similarity is cosine distance on word vectors, with a threshold applied 
    ranks the top_n of these similar-enough words according to second comparison: max similarity to word in ineed statement
    if this fails, simply orders list by proximity of words to keysetters
    if this fails, simply return the first keysetter, assumed to be a valid input
    returns one option, using randomness to add variation

    so, for instance, given the pos "NN", the keysetter ["food"], and the statement: "I need some sushi"
    this function should try to create a list of words like "bread," "meat," and "fish"
    and return "fish" because it is close to "sushi"
    """
    default_word = keysetters[0]
    options = myvocabulary_filtered[pos]
    #options = [w.split(">")[0] for w in options]## this is not necessary; already filtered
    options = list(set(options))
    try:
        options_sorted_according_to_keysetters = tune_one_list_according_to_max_similarity_to_another_list(options,keysetters,threshold)
        try:
            ### must have at least n
            options_tuned_according_to_need = tune_one_list_according_to_max_similarity_to_another_list(options_sorted_according_to_keysetters[:top_n],[w.lower() for w in tokenize.casual_tokenize(ineed) if w.isalpha()])
            options_sorted = options_tuned_according_to_need
        except:
            options_sorted = options_sorted_according_to_keysetters
        while True: 
            if random.random()<=probability:
                return options_sorted[0]
            else:
                ## cycle
                first = options_sorted.pop(0)
                options_sorted.append(first)
    except:
        return default_word


def process_string(astring,ineed):
    """
    fill out a template string
    """
    ## simple options, {this_orthat}
    simples = re.findall(r'{(?:\w+_)+\w+}',astring)
    for s in simples:
        s2 = s.lstrip("{").rstrip("}")
        choices = s2.split("_")
        astring = astring.replace(s,random.choice(choices))
    ## complicated options, {NN.food.spicy}
    complicateds = re.findall(r'{\w+\..+?}',astring)
    for c in complicateds:
        c2 = c.lstrip("{").rstrip("}")
        pos_and_keys = c2.split(".")
        pos = pos_and_keys[0]
        keys = pos_and_keys[1:]
        choice = get_word_based_on_pos_and_vector(pos,keys,ineed)
        choice = try_to_convert_boring_to_interesting_word(choice) ## try to replace with an interesting word
        astring = astring.replace(c,choice)
    return astring



# def get_closest_match_sent2vec(ineed):
#     """
#     calculates the most similar need from my custom needs using sent2vec
#     returns dict with need and similarity score
#     """
#     key_and_score = [(key,cosine_similarity(model.embed_sentence(ineed),model.embed_sentence(adorn(key)))) for key in myprayers.myprayers]
#     key_and_score.sort(key=lambda x: x[1],reverse=True)
#     return {"need":key_and_score[0][0],"score":key_and_score[0][1]}


def get_closest_match_sbert(ineed):
    """
    calculates the most similar need from my custom needs using sent2vec
    returns dict with need and similarity score
    """
    query_embedding = model.encode(ineed, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, key_embeddings)[0]
    cos_scores = cos_scores.cpu()
    score,top_match_indx = torch.topk(cos_scores, k=1) 
    matching_key = keys[int(top_match_indx)]
    score = float(score)
    return {"need":matching_key,"score":score}


def fix(astring):
    """
    "a eagle" -> "an eagle"
    """
    astring = re.sub(r"\ba ([AEIOUaeiou])",r"an \1",astring)
    return astring


def pray(ineed,homog=True):
    """
    tries to match a statement like "I need a hug" to my custom needs
    returns a prayer dictionary for closest match, including generated prayer
    """
    if homog==True:
        ineed = homogenize(ineed)
    match = get_closest_match_sbert(ineed)
    ### if it is banned
    if myprayers.myprayers[match['need']]==None: ## i've banned it.
        return {"need":match['need'],"score":match['score'],"banned":True}
    prayers=myprayers.myprayers[match['need']].copy() ## copy so i can overwrite
    ## mostly this will happen
    for p in prayers:
        prayer = prayers[p]
        if type(prayer)==list: ## a list to randomly choose from
            prayer = random.choice(prayer)
        ### either ADORN or (rarely) ADD PROVERB
        if random.random()<.92: ## most of the time
            prayers[p]=adorn(fix(process_string(prayer,ineed)))
        else: ## rarely add a proverb
            prayers[p]=proverbialize(fix(process_string(prayer,ineed)))
    return {"need":match['need'],"score":match['score'],"banned":False,"prayers":prayers,'template':myprayers.myprayers[match['need']]}


def pray_with_simplification(ineed,homog=True,threshold=.7,min_tokens=2):
    """
    will try to find match, taking off a token until there is a match, i.e.

    I need to dance the rhumba at the Stork Club
    I need to dance the rhumba at the Stork
    I need to dance the rhumba at 
    I need to dance the rhumba 
    I need to dance the

    or not enough tokens left (after the first instance of "need")
    returns a prayer dict if successful
    returns None if unsuccessful
    """
    while True:
        ineed = homogenize(ineed)
        prayer = pray(ineed,homog=False)## already one
        if prayer["score"]>=threshold:
            return prayer
        ## delete last word-ish and make sure long enough
        deeni = ineed[::-1] ## reverse
        ineed_new = deeni.split(" ",1)[1][::-1]
        if ineed==ineed_new:
            return None
        ineed = ineed_new
        if len(tokenize.casual_tokenize(ineed.split("need",1)[1]))<min_tokens: ## must have at least n tokens after "I need"
            return None


def main():
    print(pray("I really need to sleep"))
    # print(pray_with_simplification("I really need some sushi even though i'm so hungry"))
    # print(pray_with_simplification("Man I need a friend"))
    # print(pray_with_simplification("Man I need somebody who will love me"))


if __name__ == '__main__':
    main()