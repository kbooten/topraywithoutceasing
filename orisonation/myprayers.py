template = {

	"a basic need":{
		0:"May you",  ## basic
		1:"Yea, for", ## for (analysis of need)
		2:"May it be so, though",  ## although (caveat)
		3:"You", ## you cry out, you look (needful action)
		4:"?",  ## question
		5:"May you not", ## not (negation)
		6:"Await the {BLANK} {BLANK} of {BLANK}",  ## nouns
		7:"", ## callback
	},

	"something to not be prayed for":None, ### no prayer
}



myprayers = {

	"a hug":{
		0:"May you be {enrobed_clothed_wrapped} in {NN.mercy.truth.care.tenderness.warmth}", 
		1:["Yea, for your {NN.heart.life.room} is without {NN.friend.lover.family.touch}","Yea, for your {NN.body.arm.face.back.breast.butt} is {JJ.cold.lonely.pensive}"],
		2:"May it be so, though the {NN.land.mind.existence} is {JJ.empty} of {NNS.friends.companions.fingers}", 
		3:"You cry out in a {JJ.lonely} {NN.room.cottage.temple.mind}", 
		4:"Who does not feel {JJ.forgotten.cold.sad.broken}?", 
		5:"May you not find the {NN.night} {JJ.lonely}", 
		6:"Nay, await the {NN.warm} {NN.embrace} of {JJ.beloved} {NNS.recognition}, Selah",  
		7:", the bodies in nearness {VBG.BREATHING}", ## callback
	},


	"to cry in my bed":{
		0:["May your tears {VB.flow.water} like the {NN.rainfall}","May you find {NN.solace} in your {JJ.comfortable} {NN.place}"],  ## basic
		1:["Yea, for your eyes become {JJ.full.wet}","Yea, for {NN.sadness} seeks its {NN.expression}","Yea, for your {NNS.dreams} are {JJ.ruined} {NN.dirt}"], ## for (analysis of need)
		2:"May it be so, though your {NNS.tears} remain {JJ.hidden}",  ## although (caveat)
		3:"You become a {NN.ball}", ## you cry out, you look (needful action)
		4:"Who will hear the wailing of your {NN.face}?",  ## question
		5:"May you not keep this {NN.pain} in your {NN.heart}", ## not (negation)
		6:"Await the {JJ.sleepy} {NN.mercy} of {NN.exhaustion}",  ## nouns
		7:", and may you {VB.dream} of {NN.sugar.forgiveness.mercy}", ## callback
	},

	"a friend":{
		0:"May you find a {JJ.true.eternal.clear} {NN.friend.assistant.advisor.mirror}",  ## basic
		1:"Yea, for you are {JJ.sick.tired} of {VBG.talking} to yourself", ## for (analysis of need)
		2:"May it be so, though it is {JJ.difficult} to {VB.make} {NNS.friends}",  ## although (caveat)
		3:"You go to the {NN.city.party.bar} wearing your {NN.smile} and {JJ.clothes}", ## you cry out, you look (needful action)
		4:"Who will speak your {NN.name} and visit your {NN.house.mother.father.party}?",  ## question
		5:"May you not become {JJ.strange} before them, filling them with {NN.disgust}", ## not (negation)
		6:"Await the {JJ.soft} {NN.companionship} of the {NN.tribe.friends.colleagues}",  ## nouns
		7:",a {NN.friend} to call {NN.friend}", ## callback
	},


	"to get some food":{
		0:"May you eat this {NN.food.energy.power}",  ## basic
		1:"Yea, for you {VB.hunger} for {NN.nutrition}", ## for (analysis of need)
		2:"May it be so, though the {NN.cupboard.land} is {JJ.empty.starving}",  ## although (caveat)
		3:"You {VB.hunt} in your {NN.cave}", ## you cry out, you look (needful action)
		4:"Where is the {NN.taste}?  Where the {NN.chef} of {NN.nutrition}?",  ## question
		5:"May you not eat merely {NN.water.dirt}, that which lacks {NN.fat}", ## not (negation)
		6:"Await the {JJ.fat.delicious} {NN.embrace.kindness} of {NN.fat.bread}",  ## nouns
		7:"and be filled as the {NNS.rivers.stomachs} are filled", ## callback
	},


	"to be asleep":{
		0:"May you {VB.sleep.dream.vanish}, and may your {body_mind_soul_heart_frame_joints_knees_teeth_bone_bones_breast_fingers} be {JJ.rested.healed.calm.recovered}",  ## basic
		1:"Yea, for you have labored long, {VBG.working} the {NN.store.field.tool}", ## for (analysis of need)
		2:"May it be so, though your {NN.work} does not {VB.die}",  ## although (caveat)
		3:"Your {NNS.eyes.arms.thoughts} are {JJ.heavy.tired}; they are like a {NN.stone.mud}", ## you cry out, you look (needful action)
		4:"How many hours does the {NN.king} {VB.demand}?",  ## question
		5:"May you not {VB.die} before you find your {NN.pillow}", ## not (negation)
		6:"Await the {JJ.empty.soft} {JJ.mercy.bed} of your {NN.mind.room.dream}",  ## nouns
		7:"and tomorrow {VB.awake} to the {NN.morning}", ## callback
	},

	"to sleep for days":{ ##duplicate
		0:"May you {VB.sleep.dream.vanish}, and may your {body_mind_soul_heart_frame_joints_knees_teeth_tooth_bone_bones} be {JJ.rested.healed.calm}",  ## basic
		1:"Yea, for you have labored long, {VBG.working} the {NN.store.field.tool}", ## for (analysis of need)
		2:"May it be so, though your {NN.work} does not {VB.die}",  ## although (caveat)
		3:"Your {NNS.eyes.arms.thoughts} are {JJ.heavy.tired}; they are like a {NN.stone.mud}", ## you cry out, you look (needful action)
		4:"How many hours does the {NN.king} {VB.demand}?",  ## question
		5:"May you not {VB.die} before you find your {NN.pillow}", ## not (negation)
		6:"Await the {JJ.empty.soft} {JJ.mercy.bed} of your {NN.mind.room.dream}",  ## nouns
		7:"and tomorrow {VB.awake} to the {NN.morning}", ## callback
	},


	#duplicate
	"to go to bed":{
		0:"May you {VB.sleep.dream.vanish}, and may your {body_mind_soul_heart_frame_joints_knees_teeth_tooth_bone_bones} be {JJ.rested.healed.calm}",  ## basic
		1:"Yea, for you have labored long, {VBG.working} the {NN.store.field.tool}", ## for (analysis of need)
		2:"May it be so, though your {NN.work} does not {VB.die}",  ## although (caveat)
		3:"Your {NNS.eyes.arms} are {JJ.heavy.tired}; they are like a {NN.stone}", ## you cry out, you look (needful action)
		4:"How many hours does the {NN.king} {VB.demand}?",  ## question
		5:"May you not {VB.die} before you find your {NN.pillow.bed}", ## not (negation)
		6:"Await the {JJ.empty.soft} {JJ.mercy.bed} of your {NN.mind.room.dream}",  ## nouns
		7:"and tomorrow {VB.awake} to the {NN.morning}", ## callback
	},


	"go on vacation":{
		0:"May you leave this {JJ.wicked.boring.long.painful} {NN.land.life.existence.work.task}",  ## basic
		1:"Yea, for you long to see other {NNS.mountains.faces}", ## for (analysis of need)
		2:"May it be so, though a {NN.journey.boat.escape} costs many {NNS.coins}",  ## although (caveat)
		3:"You {JJ.save} your {NN.vacation} {NNS.days}", ## you cry out, you look (needful action)
		4:"Will you go to the land of {NN.ice} or {NN.desert}?",  ## question
		5:"May you not forget to {VB.pack.bring} your {NN.dress.friend.book}", ## not (negation)
		6:"Await the {NN.sight.discovery.kindness} of {JJ.new.sudden} {VB.breathing.looking}",  ## nouns
		7:"and leave your {NN.computer.toil.taxes} behind", ## callback
	},

	## duplicate
	"a break from everything":{
		0:"May you leave this {JJ.wicked.boring.long.painful} {NN.land.life.existence.work.task}",  ## basic
		1:"Yea, for you long to see other {NNS.mountains.faces}", ## for (analysis of need)
		2:"May it be so, though a {NN.journey.boat.escape} costs many {NNS.coins}",  ## although (caveat)
		3:"You {JJ.save} your {NN.vacation} {NNS.days}", ## you cry out, you look (needful action)
		4:"Will you go to the land of {NN.ice} or {NN.desert}?",  ## question
		5:"May you not forget to {VB.pack.bring} your {NN.dress.friend.book}", ## not (negation)
		6:"Await the {NN.sight.discovery.kindness} of {JJ.new.sudden} {VB.breathing.looking}",  ## nouns
		7:"and leave your {NN.computer.toil.taxes} behind", ## callback
	},

	"to go to the doctor":{
		0:"May you go to your {NN.doctor.teacher} of the {NN.mind.body.tooth.bone.arm.skin.heart}",  ## basic
		1:"Yea, for your {NN.mind.body.tooth.bone.arm.skin} is {JJ.swollen.broken.insane.rotten}", ## for (analysis of need)
		2:"May it be so, though your {NN.insurance} is {JJ.uncertain.weak.expensive}",  ## although (caveat)
		3:"You note the {NNS.symptoms}, the way your {NN.mind.body.tooth.bone.arm.skin} does {VB.crumble.shake.glow.leak}", ## you cry out, you look (needful action)
		4:"When will your {NN.mind.body.tooth.bone.arm.skin} become {JJ.healed.perfect}?",  ## question
		5:"May you not {VB.wait} until the {JJ.dreadful} {NN.season}", ## not (negation)
		6:"Await the {VBG.healing} {NN.touch.tool} of {NN.wisdom.education.care}",  ## nouns
		7:"who knows every {NN.flower.ox} of your {NN.garden.city.farm}", ## callback
	},



	"somebody to talk to":{
		0:"May you find a {VBG.listening.caring.loving} {NN.friend.therapist.ear.speaker.mother}",  ## basic
		1:"Yea, for your {NNS.problems.words.stories} within you are {JJ.heavy.bitter} {NN.acid.metal.weight}", ## for (analysis of need)
		2:"May it be so, though your {NNS.friends} are so {JJ.busy}",  ## although (caveat)
		3:"You send {NNS.letters}; you receive {NN.silence}", ## you cry out, you look (needful action)
		4:"Who will {VB.take.carry} your {NN.burden}?",  ## question
		5:"May you not {VB.sit} {JJ.alone}", ## not (negation)
		6:"Await the {JJ.comforting} {NN.face.emptiness} of a {NN.listener}",  ## nouns
		7:["who will {VB.understand} you","and be not {JJ.forsaken}"], ## callback
	},



	"to talk to a therapist":{ ## duplicate
		0:"May you find a {VBG.listening.trusting.adoring} {NN.friend.therapist.ear.speaker.mother}",  ## basic
		1:"Yea, for your {NNS.problems.words.stories} within you are {JJ.heavy.bitter} {NN.acid.metal.weight}", ## for (analysis of need)
		2:"May it be so, though your {NNS.friends} are so {JJ.busy}",  ## although (caveat)
		3:"You send {NNS.letters}; you receive {NN.silence}", ## you cry out, you look (needful action)
		4:"Who will {VB.take.carry} your {NN.burden}?",  ## question
		5:"May you not {VB.sit} {JJ.alone}", ## not (negation)
		6:"Await the {JJ.comforting} {NN.face.emptiness} of a {NN.listener}",  ## nouns
		7:["who will {VB.understand} you","and be not {JJ.forsaken}"], ## callback
	},


	"someone who will want to love me":{
		0:"May you find your {JJ.true.always.fitting.missing.mystical} {NN.lover.betrothed.body.piece.element}",  ## basic
		1:"Yea, for a person shall not be {JJ.alone} as the {NN.castle.tree.wolf}", ## for (analysis of need)
		2:"May it be so, though your {NN.personality} is {JJ.difficult}",  ## although (caveat)
		3:"You try many {NNS.lovers}; all of them {VB.judge}", ## you cry out, you look (needful action)
		4:"Where is the one {VBD.made} for you?",  ## question
		5:"May you not {VB.live} {JJ.alone}", ## not (negation)
		6:"Await the {JJ.warm.true} {NN.robe.smile} of {NN.love}",  ## nouns
		7:"hidden in the {JJ.tall} {NN.grasses.buildings.forests}", ## callback
	},


	"a girlfriend":{
		0:"May you find utmost {JJ.true.fitting.missing.mystical} {NN.lover.woman.wife.adorer}",  ## basic
		1:"Yea, for a person shall not be {JJ.alone} as the {NN.castle.tree.wolf}", ## for (analysis of need)
		2:"May it be so, though your {NN.personality} is {JJ.difficult}",  ## although (caveat)
		3:"You try many {NNS.lovers}; all of them {VB.judge}", ## you cry out, you look (needful action)
		4:"Where is the one {VBD.made} for you?",  ## question
		5:"May you not {VB.live} {JJ.alone}", ## not (negation)
		6:"Await the {JJ.warm.true} {NN.robe.smile} of {NN.love}",  ## nouns
		7:"hidden in the {JJ.tall} {NN.grasses.buildings.forests}", ## callback
	},


	"a boyfriend":{ #duplicate
		0:"May you find an utmost {JJ.true.fitting.missing.mystical} {NN.lover.man.husband.adorer}",  ## basic
		1:"Yea, for a person shall not be {JJ.alone} as the {NN.castle.tree.wolf}", ## for (analysis of need)
		2:"May it be so, though your {NN.personality} is {JJ.difficult}",  ## although (caveat)
		3:"You try many {NNS.lovers}; all of them {VB.judge}", ## you cry out, you look (needful action)
		4:"Where is the one {VBD.made} for you?",  ## question
		5:"May you not {VB.live} {JJ.alone}", ## not (negation)
		6:"Await the {JJ.warm.true} {NN.robe.smile} of {NN.love}",  ## nouns
		7:"hidden in the {JJ.tall} {NN.grasses.buildings.forests}", ## callback
	},


	"to stop saying stupid gossip":{
		0:"May you be {JJ.silent.wise.kind.truthful.holy.pure}",  ## basic
		1:"Yea, for your words are {NN.empty}", ## for (analysis of need)
		2:"May it be so, though yor mouth is like a {NN.river} {JJ.unceasing}",  ## although (caveat)
		3:"You {VB.bite} your {NN.tongue}", ## you cry out, you look (needful action)
		4:"Who is your friend?",  ## question
		5:"May you not {VB.spill} your {JJ.idle} {NNS.stories.words}", ## not (negation)
		6:"{Manifest_Show} the {NN.strength} of self-{NN.control}",  ## nouns
		7:"and spare others your {NN.noise}", ## callback
	},


	"to watch a show":{
		0:"May you be {JJ.entertained} by a {NN.dance.story.conflict.actor.character.vista.scenery}",  ## basic
		1:"Yea, for your own life is too much to {VB.consider}", ## for (analysis of need)
		2:"May it be so, though so many are {JJ.stupid} {NN.chatter}",  ## although (caveat)
		3:"You {VB.travel} to a {NN.world} that is pure {NN.fantasy}", ## you cry out, you look (needful action)
		4:"Who will be your {NN.character} most {JJ.beloved}?",  ## question
		5:"May you not become {JJ.bored}", ## not (negation)
		6:"Await the {NN.glow} of the {NN.machine.square.stage}",  ## nouns
		7:"and {VB.feel} the {NN.range} of {NNS.emotions}", ## callback
	},



	"to download and catch up on a movie":{
	#duplicate
		0:"May you be {JJ.entertained} by a {NN.dance.story.conflict.actor.character.vista.scenery}",  ## basic
		1:"Yea, for your own life is too much to {VB.consider}", ## for (analysis of need)
		2:"May it be so, though so many are {JJ.stupid} {NN.chatter}",  ## although (caveat)
		3:"You {VB.travel} to a {NN.world} that is pure {NN.fantasy}", ## you cry out, you look (needful action)
		4:"Who will be your {NN.character} most {JJ.beloved}?",  ## question
		5:"May you not become {JJ.bored}", ## not (negation)
		6:"Await the {NN.glow} of the {NN.machine.square.stage}",  ## nouns
		7:"and {VB.feel} the {NN.range} of {NNS.emotions}", ## callback
	},


	"to smoke weed":{
		0:"May you {VB.consume.smoke.drink.enjoy} this {NN.weed.drug.poison.insanity.dream}",  ## basic
		1:"Yea, for your {NN.life.work} has been {JJ.stressful}", ## for (analysis of need)
		2:"May it be so, though so you cannot find the man who will {VB.sell} {NN.weed}",  ## although (caveat)
		3:"You arrange your {NN.fire} and your {NN.weed}", ## you cry out, you look (needful action)
		4:"Who will {VB.supply} you in your time of {NN.need}?",  ## question
		5:"May you not grow too {JJ.paranoid.sleepy}", ## not (negation)
		6:"Await the {NN.smoke} of the {NN.weed.fire}",  ## nouns
		7:["and {VB.breathe} a {VB.mercy} into your {NNS.lungs}","and may it be called {blue_sour_green_purple_cherry_strawberry} {NN.fruit.doctor.tree}"], ## callback
	},


	"to drink some beer":{
		0:"May you {VB.consume.drink.enjoy} this {NN.wine.drug.poison.insanity.dream}",  ## basic
		1:"Yea, for your {NN.life.work} has been {JJ.stressful}", ## for (analysis of need)
		2:"May it be so, though the last time you were like a {JJ.drunken} {NN.monster.wolf.cow}",  ## although (caveat)
		3:"You bid goodbye to your {NN.brain}", ## you cry out, you look (needful action)
		4:"Who will {VB.supply} you in your time of {NN.need}?",  ## question
		5:"May you not grow too {JJ.uncontrolled.angry}", ## not (negation)
		6:"Await the {NN.relaxation} of the {NN.poison}",  ## nouns
		7:", the {NN.wine.liquid} of the {NN.grain.grape.seed.corn}", ## callback
	},



	"to sleep less":{
		0:"May you {VB.wake.open.alert.rise}",  ## basic
		1:"Yea, for you cannot {VB.escape} your {NN.life}", ## for (analysis of need)
		2:"May it be so, though you wish to {VB.escape} your {NN.life}",  ## although (caveat)
		3:"You {VB.confront} the {NNS.demons} who would lure you into your bed", ## you cry out, you look (needful action)
		4:"How much {NN.life} does {VB.escape} us while we {VB.sleep}?",  ## question
		5:"May you not {VB.close} your {NNS.eyes}", ## not (negation)
		6:"Await the {BLANK} {BLANK} of {BLANK}",  ## nouns
		7:"and greet the {NN.sun}", ## callback
	},


	"to eat less":{
		0:"May you stop {VBG.eating.burying} all the {NN.grain.beef.misery.emotion.energy.fat}",  ## basic
		1:"Yea, for you are not {JJ.hungry}; nay, you are {JJ.bored.lonely.sad}", ## for (analysis of need)
		2:["May it be so, though the {JJ.sugar} tastes like a {NN.miracle}","May it be so, though you have no other {NN.pleasure}","May it be so, though you have already {bought_purchased} this {NN.food.pantry.farm}"],  ## although (caveat)
		3:"You push the {NNS.cookies} into the outer {NN.darkness}, saying {No_Away_Vanish}!", ## you cry out, you look (needful action)
		4:"How many minutes will your inner-{NN.strength} {VB.endure}?",  ## question
		5:"May you not {VB.yield} to the {NN.demon} of {NN.sugar.salt.fat.meat.deliciousness}", ## not (negation)
		6:"Instead await the {NN.taste} of {NN.balance}",  ## nouns
		7:"with your {VBG.clawing} {NNS.arms.teeth}", ## callback
	},



	# "to stop eating this food":{
	# 	0:"May you stop {VBG.eating} this {NN.food}",  ## basic
	# 	1:"Yea, for it is like {NN.poison} unto the {NNS.coils} of your {NN.gut}", ## for (analysis of need)
	# 	2:["May it be so, though the {JJ.food} tastes like a {NN.miracle}",],  ## although (caveat)
	# 	3:"You push the {NNS.cookies} into the outer {NN.darkness}, saying {No_Away_Vanish}!", ## you cry out, you look (needful action)
	# 	4:"How many minutes will your inner-{NN.strength} {VB.endure}?",  ## question
	# 	5:"May you not forget that this is like {NN.poison} unto the {NNS.coils}", ## not (negation)
	# 	6:"Abjure, and await the {NN.peace} of the {NN.body}",  ## nouns
	# 	7:"except on the day of the {NN.feast} of the {NN.king}", ## callback
	# },



	"to be pampered":{
		0:"May you be {VBD.adorned.savored.painted}",  ## basic
		1:"Yea, for every person is as precious as a {NN.baby.gem.forest}", ## for (analysis of need)
		2:"May it be so, though your {NN.toil.pain} does not cease, and your {NNS.hands.arms.muscles} {VB.crack.weep.freeze}",  ## although (caveat)
		3:"You search your stores for {NN.balm.honey.blush.juice.paint}", ## you cry out, you look (needful action)
		4:"Who will annoint your {NN.face.body.chest} with {NN.balm.honey.blush.juice}?",  ## question
		5:"May your {NN.skin.face} not grow {JJ.rough.ugly} as the {NN.desert.forest}'s {NN.floor.texture.textile}", ## not (negation)
		6:"Await the {JJ.fragrant.smooth.hot.cold} {NN.oil.rock.sand.touch.prick} of {Nineveh_Egypt_Beeroth_Ataroth}",  ## nouns
		7:"and {VBD.celebrated.cherished.exalted} by yourself and the {NN.city.world.man.woman}", ## callback
	},


	"to be massaged and rubbed":{
		0:"May you be {VBD.touched.opened.cured} by a {JJ.delicate.attentive.intelligent} {NN.finger.palm.orb.scepter.rock}",  ## basic
		1:"Yea, for your {NN.muscles} are so {JJ.tired} and {JJ.sore}", ## for (analysis of need)
		2:"May it be so, though your have no {NN.doctor} of {NNS.hands} to {VB.touch} you",  ## although (caveat)
		3:"You try to {VB.rub} your own {NNS.arms.feet.muscles.chakras} with {NN.oil.care}", ## you cry out, you look (needful action)
		4:"Who will annoint your {NN.face.body} with {NN.balm.honey.blush.juice}?",  ## question
		5:"May your {NN.skin} not grow {JJ.rough} as the {NN.desert}'s {NN.floor}", ## not (negation)
		6:"Await the {JJ.fragrant} {NN.touch} from your {NN.head.crown.star} to your {NN.foot.root}",  ## nouns
		7:"and may the {NN.castle.lock} of your {NN.pain.tension.labor} {VB.fall.unravel}", ## callback
	},

	"to be alone":{
		0:"May you be {JJ.alone.pure}",  ## basic
		1:"Yea, for you look upon the {NN.city.crowd} with {NN.hatred}", ## for (analysis of need)
		2:"May it be so, though your {NN.phone} will not {halt_cease} its {VBG.beeping}",  ## although (caveat)
		3:"You {VB.hide} in the {NN.shadow.closet.cave}", ## you cry out, you look (needful action)
		4:"Where will you find {NN.solitude}?",  ## question
		5:"May you not be caught in the {NN.storm} of the {NN.market.crowd}", ## not (negation)
		6:"Await the {NN.silence} of your {JJ.dark} {NN.apartment}",  ## nouns
		7:"and play {NNS.games} on your phone, or read {NNS.books}", ## callback
	},


	"to stop spending money":{
		0:"May you {VB.save.bury} your {NNS.dollars.benefits}",  ## basic
		1:"Yea, for you have {NNS.taxes.bills} to pay", ## for (analysis of need)
		2:"May it be so, though you rejoice in the {NN.song} of the {NN.market}",  ## although (caveat)
		3:"You bury your {NNS.dollars} in the {NN.sand}; you foresake the {NN.market}", ## you cry out, you look (needful action)
		4:"Where do your {NNS.dollars} {VB.go}?",  ## question
		5:"May you not purchase a {NN.dog.house.scarf} or the {NN.house.gadget} you {adore_crave}", ## not (negation)
		6:"Await the {NN.bounty} of {NN.peace}",  ## nouns
		7:"for tomorrow's {NN.problem.terror}", ## callback
	},


	"to stop drinking weed":{
		0:"May you stop consuming this {NN.drug.poison.dream.tree.honey}",  ## basic
		1:"Yea, for you have been too {JJ.drunk} to {VB.function}", ## for (analysis of need)
		2:"May it be so, though you love this {NN.drug} as the the shepherd loves the sheep",  ## although (caveat)
		3:"You weep, seeing your {NN.blood} as a {JJ.dirty} {NN.water}", ## you cry out, you look (needful action)
		4:"Where do your {NNS.dollars} {VB.go}?",  ## question
		5:"May you not be {JJ.drunk.poisoned}, {VBG.stumbling} through the night", ## not (negation)
		6:"Await the {NN.righteousness} of the ex-{NN.drunkard}",  ## nouns
		7:"which is your {NN.king}", ## callback
	},


	# "to stop drinking weed":{
	# 	0:"May you stop consuming this {NN.drug}",  ## basic
	# 	1:"Yea, for you have been too {JJ.drunk} to {VB.function}", ## for (analysis of need)
	# 	2:"May it be so, though you love this {NN.drug} as the the shepherd loves the sheep",  ## although (caveat)
	# 	3:"You weep, seeing your {NN.blood} as a {JJ.dirty} {NN.water}", ## you cry out, you look (needful action)
	# 	4:"Where do your {NNS.dollars} {VB.go}?",  ## question
	# 	5:"May you not be {JJ.drunk.poisoned}, {VBG.stumbling} through the night", ## not (negation)
	# 	6:"Await the {NN.righteousness} of the ex-{NN.drunkard}",  ## nouns
	# 	7:"which is your {NN.king}", ## callback
	# },


	"stop being lazy":{
		0:"May you be {JJ.active.fast.strong.alive}",  ## basic
		1:"Yea, for the {NN.grain} lies {JJ.abandoned} in the {NN.field}", ## for (analysis of need)
		2:"May it be so, though your {NN.butt} is {JJ.comfortable}",  ## although (caveat)
		3:"You tell your body to {VB.leap} and take up your {NN.shield.tool}", ## you cry out, you look (needful action)
		4:"Who has one {NN.ounce} of {JJ.energy} remaining?",  ## question
		5:"May you not let the day turn to {NN.dust}, the {NN.sun} grow {JJ.dark}", ## not (negation)
		6:"Await the {NN.trumpet} of your {NN.toil}",  ## nouns
		7:"on the {NN.face} of the earth", ## callback
	},


	"gain weight":{
		0:"May you become {JJ.heavy.rocky.indestructable.glorious}",  ## basic
		1:"Yea, for the {NN.body} does nearly {VB.vanish}", ## for (analysis of need)
		2:"May it be so, though your {NNS.habits} are {JJ.dangrous}",  ## although (caveat)
		3:"You tell your body to {VB.sit} like the {NN.bear.ox}", ## you cry out, you look (needful action)
		4:"Whose {NN.face.belly.butt} does not {VB.wither} like {NN.grass}?",  ## question
		5:"May you not continue to {VB.wither} like the {NN.grass} of {Egypt_Samaria}", ## not (negation)
		6:"Await the {VBG.growing} of your {NN.face.butt.}",  ## nouns
		7:"and may your {NN.spirit.soul} be {JJ.solid}", ## callback
	},


	"lose weight":{
		0:"May you become {JJ.light.grassy.watery}",  ## basic
		1:"Yea, for the {NN.soul} is {JJ.heavy} enough", ## for (analysis of need)
		2:"May it be so, though your {NNS.habits} are {JJ.dangrous}",  ## although (caveat)
		3:"You tell your body to {VB.leap} like the {NN.gazelle}", ## you cry out, you look (needful action)
		4:"Whose {NN.face.belly.butt} has not the {NN.bounty} of Jacob's {NN.granary}?",  ## question
		5:"May you not continue to {VB.store} {NN.energy}", ## not (negation)
		6:"Await the {VBG.withering} of your {NN.face}",  ## nouns
		7:"and may your {NN.spirit.soul} be {JJ.light}", ## callback
	},



	"stop procrastinating and being lazy":{
		0:"May you {VB.leap.return} to your {NN.labor.machine.rock.field.employer}}",  ## basic
		1:"Yea, for your {NN.toil} is {JJ.infinite}, and the {NN.hour} is an {JJ.old} {NN.taste.tree.song.widow}", ## for (analysis of need)
		2:"May it be so, though you would rather {VB.observe} your {NN.television.phone}",  ## although (caveat)
		3:"You tell your body to become a {NN.city.legion} of {NNS.ants.chariots}", ## you cry out, you look (needful action)
		4:"Whose {NN.boss} has not gazed upon them with {NN.shame}}?",  ## question
		5:"May you not wait another {JJ.precious} {NN.second.hour}", ## not (negation)
		6:"Await the {JJ.true} {VBG.judgment} of the {NN.clock}",  ## nouns
		7:"with a {NN.warrior}'s {NN.courage}", ## callback
	},


	"to get some clothes":{
		0:"May you find {NNS.clothes} of {JJ.red.blue.rich.foreign.leather} {NN.fabric.texture.glow}",  ## basic
		1:"Yea, for a {NN.body} was not mean to be {JJ.naked} in the {NN.market} or at the {NN.temple}", ## for (analysis of need)
		2:"May it be so, though you would rather save your {JJ.precious} {NNS.dollars}",  ## although (caveat)
		3:"You cover your {NNS.loins} with a {NN.veil}; you feel human {NN.shame}", ## you cry out, you look (needful action)
		4:"Who is not like a {NN.peacock}, with beautiful {NNS.feathers}?",  ## question
		5:"May you not continue to wear this {JJ.plain} {NN.bag}", ## not (negation)
		6:"Await the {JJ.true} {VBG.covering} of the {NN.thread}",  ## nouns
		7:"and feel {JJ.handsome} as a {NN.husband}", ## callback
	},


	"to dump this jerk boyfriend girlfriend":{
		0:"May you escape across the {NN.river.forest.city.year} and be {JJ.free.safe.confident}",  ## basic
		1:"Yea, for this {NN.person} is not a {NN.balm.shield} nor a {NN.help.lover}", ## for (analysis of need)
		2:"May it be so, though you are not {JJ.sure}",  ## although (caveat)
		3:"You practice the {JJ.honest.harsh} {NNS.words} of {NN.escape}", ## you cry out, you look (needful action)
		4:"Who has not found themselves in the {NN.bed.house} of a {NN.enemy}?",  ## question
		5:"May you not lose your {NN.bravery.resove}, not wilt like a {JJ.wet.cowardly} {NN.fish.bread.reed}", ## not (negation)
		6:"Await the life that has been woven for you, whether {JJ.alone} or with a {NN.spouse}",  ## nouns
		7:"and sleep alone in your bed of {NN.silence.peace.care.protection}", ## callback
	},


	"to learn how to":{
		0:"May you become {JJ.wise.talented} like a {JJ.old.wise} {NN.magician.teacher.officer.animal.weather}",  ## basic
		1:"Yea, for each {NN.soul} is  {NN.work} in {NN.progress}", ## for (analysis of need)
		2:"May it be so, though now you may be {JJ.ignorant} as a {NN.donkey.bird}",  ## although (caveat)
		3:"You {VB.beg} the {NN.teacher} to give you {NN.truth}", ## you cry out, you look (needful action)
		4:"Who will take the time to {VB.instuct} your {NN.mind}?",  ## question
		5:"May you not lose your {NN.energy} to {VB.learn}", ## not (negation)
		6:"Await the {NN.enlargement} of your {NNS.skills}",  ## nouns
		7:"and {VB.accomplish} what you were put on this {NN.planet} to {VB.accomplish}", ## callback
	},



	# "excitement and entertainment":{

	# },


	# "justice":{

	# },

	"to not overthink":{
		0:"May you not {VB.overthink.consider} your {NN.life.decision}",  ## basic
		1:"Yea, for your {VBG.thinking} is utterly {JJ.useless}", ## for (analysis of need)
		2:"May it be so, though your {NN.brain} is your only way to {VB.escape} this {NN.difficulty}",  ## although (caveat)
		3:"You tell your {NN.brain} to {VB.sleep}", ## you cry out, you look (needful action)
		4:"Whose {NNS.thoughts} have not gone {VBG.roaming.conquering} like {NNS.horses.warriors}?",  ## question
		5:"May you not {VB.think} so many {JJ.evil} {NNS.thoughts.songs}", ## not (negation)
		6:"Await the {JJ.cool} {VBG.feeling} of a {JJ.empty} {NN.box}",  ## nouns
		7:"and instead find {NN.peace}", ## callback	
	},


	# "to stop getting frustrated":{

	# },


	"to move to a new apartment or house":{
		0:"May you have {NN.shelter.warmth} and feel {JJ.safe.sturdy}",  ## basic
		1:"Yea, for you deserve a place to {VB.sleep} and {VB.pray} in {NN.peace}", ## for (analysis of need)
		2:"May it be so, though rents are {JJ.high.exalted.terrible}, and you are no {NN.king.queen}",  ## although (caveat)
		3:"You practice the {JJ.honest.harsh} {NNS.words} of {NN.escape}", ## you cry out, you look (needful action)
		4:"Who has not found themselves in the {NN.bed.house} of a {NN.enemy}?",  ## question
		5:"May you not lose your {NN.bravery.resolve}, not wilt like a {JJ.wet.cowardly} {NN.fish.bread.reed}", ## not (negation)
		6:"Await the life that has been woven for you, whether {JJ.alone} or with a {NN.spouse}",  ## nouns
		7:"and sleep alone in your bed of {NN.silence.peace.care.protection}", ## callback	
	},



	"to visit my family and friends":{
		0:"May you be {VBD.embraced.recognized} by your {JJ.true.beloved.chosen.given} {NN.family.belonging.holiday}",  ## basic
		1:"Yea, for you should not be left {NN.alone} without any {NNS.stories} recounted around the {NN.table}", ## for (analysis of need)
		2:"May it be so, though we are {JJ.separated} by {NNS.wires} and {NNS.screens}",  ## although (caveat)
		3:"You {NN.face}{NN.time} your {JJ.loved} {NNS.people}", ## you cry out, you look (needful action)
		4:"When will you get to see their {JJ.round.smiling.radiant} {NNS.faces}?",  ## question
		5:"May you not weigh {NN.work} over {NN.family}; may you instead be {NN.wise}", ## not (negation)
		6:"Await the {JJ.familiar} {NN.laughter} of your {NN.family}",  ## nouns
		7:"and bring them {NNS.presents}", ## callback	
	},


	"to become calm":{
		0:"May you be {JJ.calm.cool.wise}",  ## basic
		1:"Yea, for your {NN.heart} does {VB.beat}", ## for (analysis of need)
		2:"May it be so, though this {NN.era} is so {JJ.stressful}",  ## although (caveat)
		3:"You try to {VB.remember} your {VBG.breathing} {NNS.exercises}", ## you cry out, you look (needful action)
		4:"When will you {VB.find} {NN.peace}?",  ## question
		5:"May you not {VB.dwell} in your {JJ.rapid} {NNS.worries}", ## not (negation)
		6:"Await the {JJ.soft} {NN.breath} of {NN.peace}",  ## nouns
		7:"and your {NN.heart} {JJ.content}", ## callback		
	},


	"to get a car":{
		0:"May you find your {JJ.golden.blue.fast.foreign} {NN.chariot.car.mobility}",  ## basic
		1:"Yea, for your {NNS.legs} are {JJ.tired}, and your {NN.work} far in the {NN.distance.desert.city}", ## for (analysis of need)
		2:"May it be so, though a {NN.chariot} costs much {NN.gold.wheat.time}}",  ## although (caveat)
		3:"You try to {VB.run} like a {JJ.drunk.fast} {NN.horse.river.warrior}", ## you cry out, you look (needful action)
		4:"When will you be home in time for your {NN.dinner.love.theater}?",  ## question
		5:"May you not {VB.walk} without {NNS.wheels}", ## not (negation)
		6:"Await the {JJ.loud} {NN.engine} of {NN.speed}",  ## nouns
		7:"and be {JJ.safe.fast.happy.sexy.free}", ## callback			
	},


	"to not be sick":{
		0:"May you be {JJ.healed.perfect.alive}",  ## basic
		1:"Yea, for your {NN.body.mind.skin} feels like {NN.mud.glue.fire.vomit.blood}", ## for (analysis of need)
		2:"May it be so, though a your {NN.body.skin.foot.tongue} is {JJ.hot.wet} like a {NN.sea.cow.fire.lance.ogre.cough}",  ## although (caveat)
		3:"You try to {VB.heal} by {VBG.consuming} many {NNS.medicines.liquids.prayers}", ## you cry out, you look (needful action)
		4:"When will these {NNS.demons} return to their {NN.cave.temple.hell}?",  ## question
		5:"May you not {VB.wake} and still be {JJ.ill}", ## not (negation)
		6:"Await the {JJ.fast} {NN.dawn} of {NN.blood}",  ## nouns
		7:"and return to the world of the {NN.working.laughing.talking.kissing}", ## callback			
	},


	# "to go shopping":{
	# 	0:"May you find your {JJ.golden.blue.fast} {NN.chariot}",  ## basic
	# 	1:"Yea, for your {NNS.legs} are {JJ.tired}, and your {NN.work} far in the {NN.distance.desert.city}", ## for (analysis of need)
	# 	2:"May it be so, though a {NN.chariot} costs much {NN.gold.wheat.time}}",  ## although (caveat)
	# 	3:"You try to {VB.run} like a {JJ.drunk.fast} {NN.horse.river.warrior}", ## you cry out, you look (needful action)
	# 	4:"When will you be home in time for your {NN.dinner.love.theater}?",  ## question
	# 	5:"May you not {VB.walk} without {NNS.wheels}", ## not (negation)
	# 	6:"Await the {JJ.loud} {NN.engine} of {NN.speed}",  ## nouns
	# 	7:"and be {JJ.safe.fast.happy.sexy.free}", ## callback			
	# },



	# "to not be bored":{
	
	#},


	# "to be needed and appreciated":{
	
	#},


	"to get a haircut and do my hair and skin":{
		0:"May your {NN.body.hair.skin} be {JJ.beautiful} and {JJ.controllable.smooth}",  ## basic
		1:"Yea, for you look in the {NN.mirror} and see a {JJ.unruly.snake} {NN.snake.nest.spill}", ## for (analysis of need)
		2:"May it be so, though then a stranger must {VB.cut.touch} your {NN.head.hair.skin}",  ## although (caveat)
		3:"You wash yourself clean with {NN.soap}; you brush it with {NNS.feathers}", ## you cry out, you look (needful action)
		4:"Shall you cover your {NN.head.face} with a {NN.scarf} of {NN.shame}?",  ## question
		5:"May you not feel your {NN.hair.skin} torn out like {NN.roots}", ## not (negation)
		6:"Await the feeling of the {NN.sword} and the {NN.soap}",  ## nouns
		7:"and feel {JJ.radiant}", ## callback		
	},



	"to get my lashes lips fingernails done":{ ## plural of above
		0:"May your {NNS.eyelashes.lips.fingernails} be {JJ.beautiful} and {JJ.controllable.smooth}",  ## basic
		1:"Yea, for you look in the {NN.mirror} and see a {JJ.unruly.snake} {NN.snake.nest.spill}", ## for (analysis of need)
		2:"May it be so, though then a stranger must {VB.cut.touch} your {NN.head.hair.skin}",  ## although (caveat)
		3:"You wash yourself clean with {NN.soap}; you brush it with {NNS.feathers}", ## you cry out, you look (needful action)
		4:"Shall you cover your {NNS.eyelashes.lips.fingernails} with a {NN.cloth.ribbon.mask} of {NN.shame}?",  ## question
		5:"May you not feel your {{NNS.eyelashes.lips.fingernails} torn out like {NN.roots}", ## not (negation)
		6:"Await the feeling of the {NN.sword} and the {NN.soap}",  ## nouns
		7:"and feel {JJ.radiant}", ## callback		
	},



	# "to clean my room house":{
	# 	0:"May your {NN.room.house} be {JJ.clean}",  ## basic
	# 	1:"Yea, for you {VB.live} in a {NN.wasteland}, where {NN.disorder} does {VB.reign}", ## for (analysis of need)
	# 	2:"May it be so, though how can a person {VB.build} a {NN.castle.temple.system} from {NN.chaos}",  ## although (caveat)
	# 	3:"You begin to put in order your {NNS.possessions.books.clothes.machines}", ## you cry out, you look (needful action)
	# 	4:"Shall you sort the {NNS.possessions.books.clothes.machines} into two piles, one for the {JJ.evil.desired} and another for the {JJ.pure.unwanted}?",  ## question
	# 	5:"May you not feel like your {NN.life} is beyond your {NN.control}; know that you are under {NN.control}", ## not (negation)
	# 	6:"Await the feeling the {NN.world} sorted into {NNS.silos}, the {NN.floor} made {JJ.clean}",  ## nouns
	# 	7:"and may your {NN.soul} also feel {JJ.clean}", ## callback		
	# },


	"to clean my":{
		0:"May it be {JJ.clean}",  ## basic
		1:"Yea, for you {VB.live} in a {NN.wasteland}, where {NN.disorder} does {VB.reign}", ## for (analysis of need)
		2:"May it be so, though how can a person {VB.build} a {NN.castle.temple.system} from {NN.chaos}",  ## although (caveat)
		3:"You begin to put in order your {NNS.possessions.books.clothes.machines}", ## you cry out, you look (needful action)
		4:"Shall you sort the {NNS.possessions.books.clothes.machines} into two piles, one for the {JJ.evil.desired} and another for the {JJ.pure.unwanted}?",  ## question
		5:"May you not feel like your {NN.life} is beyond your {NN.control}; know that you are under {NN.control}", ## not (negation)
		6:"Await the feeling the {NN.world} sorted into {NNS.silos}, the {NN.floor} made {JJ.clean}",  ## nouns
		7:"and may your {NN.soul} also feel {JJ.clean}", ## callback		
	},



	"to take care of my":{
		0:"May it be {VBD.protected} and {VBD.loved.cleaned}",  ## basic
		1:"Yea, for you {VB.live} in a {NN.wasteland}, where {NN.disorder} does {VB.reign}", ## for (analysis of need)
		2:"May it be so, though how can a person {VB.build} a {NN.castle.temple.system} from {NN.chaos}",  ## although (caveat)
		3:"You begin to put in order your {NNS.possessions.books.clothes.machines}", ## you cry out, you look (needful action)
		4:"Shall you sort the {NNS.possessions.books.clothes.machines} into two piles, one for the {JJ.evil.desired} and another for the {JJ.pure.unwanted}?",  ## question
		5:"May you not feel like your {NN.life} is beyond your {NN.control}; know that you are under {NN.control}", ## not (negation)
		6:"Await the feeling the {NN.world} sorted into {NNS.silos}, the {NN.floor} made {JJ.clean}",  ## nouns
		7:"and may your {NN.soul} also feel {JJ.clean}", ## callback		
	},


	"to cut these bad people out of my life":{
		0:"May you be {JJ.free} of the {NN.enemy}",  ## basic
		1:"Yea, for you ought rather be {JJ.alone} like a {NN.olive} in the {NN.desert}", ## for (analysis of need)
		2:"May it be so, though you crave the companionship even of {JJ.evil} {NNS.snakes}",  ## although (caveat)
		3:"You take comfort in being {JJ.alone}, for you are never {JJ.alone}", ## you cry out, you look (needful action)
		4:"Who shall not become {JJ.hurt} when in the company of {NNS.snakes} with {NN.venom}?",  ## question
		5:"May you not let them {VB.tempt} you into {NN.evil}", ## not (negation)
		6:"Await the peace of a {NN.monk}, devoted to {NN.goodness}",  ## nouns
		7:"and may you find {JJ.holy} {NNS.advisors}", ## callback	
	},


	# "to have some more strength energy":{
	
	#},

	"someplace to live":{
		0:"May you find shelter beneath a {NN.tree.town.castle}",  ## basic
		1:"Yea, for you cannot sleep in the {JJ.open} {NN.field.street}", ## for (analysis of need)
		2:"May it be so, though to buy a {NN.house} is so {JJ.expensive}",  ## although (caveat)
		3:"You search the {NNS.magazines}", ## you cry out, you look (needful action)
		4:"How many {NNS.windows}?  Will the floor be {NN.carpet} or {NN.wood}?",  ## question
		5:"May you not {NN.wander} through {Egypt_Samaria} like a {NN.stranger}", ## not (negation)
		6:"Await the {NN.darkness} your of shelter's {NN.shadow}",  ## nouns
		7:"and feel {JJ.safe} as the {NN.king}'s {NN.treasure.daughter.rose.cow}", ## callback	
	},


	"to achieve my dreams":{
		0:"May you come into the {NN.land.house.nest} of your {NN.desire.dream.purpose.heaven}",  ## basic
		1:"Yea, for you cannot stop your {NN.quest} until having tasted the {NN.candy} of your {NN.desire.dream.purpose.heaven}", ## for (analysis of need)
		2:"May it be so, though everywhere your {NNS.enemies.friends.circumstances} work to {VB.thwart} your {NNS.dreams}",  ## although (caveat)
		3:"You {VB.struggle}, and your {NN.brow} drips with {NN.sweat}", ## you cry out, you look (needful action)
		4:"How many {NNS.years} will you {VB.wander} in the {JJ.unsuccessful} {NN.swamp}?",  ## question
		5:"May you not {VB.depart} this {NN.world} a {NN.loser}", ## not (negation)
		6:"Await the {NN.salvation} your of {NN.success}",  ## nouns
		7:"like a {NN.queen} covered in {NN.gold.ointment}", ## callback		
	},


	"to have sex":{
		0:"May you become {JJ.joined}",  ## basic
		1:"Yea, for a {NN.body} longs for the {NN.honey} of {NNS.arms.fingers.lips.juices.kisses.fruits}", ## for (analysis of need)
		2:"May it be so, though {NNS.bodies} are made {JJ.separate} by {NN.disease} and {NN.misery} ",  ## although (caveat)
		3:["You {VB.clean} your {NN.body} with {JJ.sexy} {NN.soap}","You send a {NN.message} to your {JJ.sensual} {NN.friend}"], ## you cry out, you look (needful action)
		4:"Who will {VB.touch} your {NN.body}?",  ## question
		5:"May you not be {JJ.dishonorable.awkward} in your {JJ.pursuit}", ## not (negation)
		6:"Await the {JJ.honey} {NN.touch} of the {JJ.honey} {NN.harp}",  ## nouns
		7:"in {NN.understanding}", ## callback
	},



	"a kiss":{ ## semi duplicate
		0:"May you become {JJ.joined} at the {NN.mouth}",  ## basic
		1:"Yea, for a {NN.body} longs for the {JJ.chaste} {NN.encounter}", ## for (analysis of need)
		2:"May it be so, though {NNS.bodies} are made {JJ.separate} by {NN.disease} and {NN.misery} ",  ## although (caveat)
		3:"You prepare your lips with {NNS.ointments} of {NN.fragrance.oil}", ## you cry out, you look (needful action)
		4:"Who will {VB.discover} your {NNS.lips}?",  ## question
		5:"May you not be {JJ.dishonorable.awkward} in your {JJ.pursuit}", ## not (negation)
		6:"Await the {JJ.honey} {NN.kiss} of the {JJ.honey} {NN.tongue}",  ## nouns
		7:"in {NN.understanding}", ## callback
	},



	"to exercise and work out":{
		0:"May you become {JJ.strong}",  ## basic
		1:"Yea, for you are too {JJ.weak} and need the {NN.muscle} of a {NN.bear}", ## for (analysis of need)
		2:"May it be so, though you are {JJ.lazy} and out of {NN.energy}",  ## although (caveat)
		3:"You try to {VB.motivate} yourself; listen for your {JJ.bold} {NN.trumpet}", ## you cry out, you look (needful action)
		4:"How many {NNS.cows} must you {VB.lift}?",  ## question
		5:"May you not sit and {VB.read} or {VB.dream} of {NNS.cakes}", ## not (negation)
		6:"Await the {NN.growth} of {NN.fiber.muscle}",  ## nouns
		7:"like a {NN.tree} made of {NNS.men.iron}", ## callback
	},


	"to let out my sadness":{
		0:"May you {VB.weep}",  ## basic
		1:"Yea, for it feels better to let your {NN.emotion} tell its {NN.truth} ", ## for (analysis of need)
		2:"May it be so, though your {NN.mom.teacher.spouse} tells you to be {JJ.calm.normal}",  ## although (caveat)
		3:"You try to weep, but your tears are {JJ.trapped}", ## you cry out, you look (needful action)
		4:"How much {NN.water} will flow from your {NN.face}",  ## question
		5:"May you not be greedy or withold your {NN.face}'s {NN.water}", ## not (negation)
		6:"Await the {JJ.hot} {NN.ending} of {NN.crying}",  ## nouns
		7:"though know your {NN.life} is {JJ.precious}", ## callback
	},


	"to forget about my sadness":{
		0:"May you be {JJ.happy.blessed.treasured}",  ## basic
		1:"Yea, for {NN.sadness} is not worth the {NN.time} it does {VB.consume}", ## for (analysis of need)
		2:"May it be so, though your may need {NN.medication} for your {NN.brain}",  ## although (caveat)
		3:"You try to {VB.distract} yourself from yourself, as one {NN.hand.leg.spouse} from the other", ## you cry out, you look (needful action)
		4:"Why cannot you {VB.free} yourself from the {NN.storm} of your {JJ.sad} {NN.heart}?",  ## question
		5:"May you not {VB.dwell} in the {NN.prison} of your {NNS.mistakes}", ## not (negation)
		6:"Await the {JJ.fresh} {NN.start} of {NN.joy}",  ## nouns
		7:"for to {VB.forget} what is {JJ.awful} is mercy", ## callback
	},


	"prayers answers help miracle":{
		0:"May you find {NN.grace.mercy.truth}",  ## basic
		1:"Yea, for your needs are beyond your {NN.capacity}", ## for (analysis of need)
		2:"May it be so, though you have few {NNS.followers}",  ## although (caveat)
		3:"You beg for the {NN.stranger}'s help; Selah", ## you cry out, you look (needful action)
		4:"Who has not cried out to the {NNS.heavens.listeners}?",  ## question
		5:"May you not be {JJ.forgotten} or lose {NN.hope}", ## not (negation)
		6:"Await the {JJ.holy} {NNS.voices} of {NNS.strangers}",  ## nouns
		7:"and be seen by {NNS.eyes} of {NN.gold.power.friendship}", ## callback
	},



	"to win and succeed":{
		0:"May you {VB.conquer}",  ## basic
		1:"Yea, for the {NN.world} is a place of {JJ.fierce} {NN.struggle}", ## for (analysis of need)
		2:"May it be so, though you may have lost your last {NN.rose.contest.test}",  ## although (caveat)
		3:"You {VB.prepare}, you focus on the {NN.prize.target}", ## you cry out, you look (needful action)
		4:"Who can stand in your {NN.path}?",  ## question
		5:"May you not be {JJ.defeated}", ## not (negation)
		6:"Await the {NN.sweet} {JJ.taste} of {NN.victory}",  ## nouns
		7:"your {NNS.enemies}", ## callback
	},



	"a better attitude":{
		0:"May you face the {world_fight} with the bravery of a {NN.warrior.ox.king.sword}",  ## basic
		1:"Yea, for the {NN.world} is a place of {NN.struggle}; the {NN.soul} must have its {NN.armor}", ## for (analysis of need)
		2:"May it be so, though have let your {NN.soul} become like a {JJ.wilted} {JJ.flower} ",  ## although (caveat)
		3:"You look in the mirror at a {NN.hero}, {VBG.shining} with {NN.power}", ## you cry out, you look (needful action)
		4:"Who is more deserving of {NN.money.freedom.success.love} than you are?",  ## question
		5:"May you not retreat into your {NN.gloom}", ## not (negation)
		6:"Await the {NN.horizon} of your {NN.becoming}",  ## nouns
		7:"who knows how to {VB.survive}", ## callback
	},


	"to get a vaccine":{
		0:"May they {VB.impale.cure} your {NN.body.arm}",  ## basic
		1:"Yea, for the {NN.sickness} is {JJ.relentless}", ## for (analysis of need)
		2:"May it be so, though they say you are not {JJ.important} enough",  ## although (caveat)
		3:"You wear your {NN.mask}, you {VB.wash} your {NNS.hands} in {NN.honey.soap.salt}", ## you cry out, you look (needful action)
		4:"Who is more deserving of {NN.health.life} than you are?",  ## question
		5:"May you endure until they {VB.proclaim} your {NN.name}", ## not (negation)
		6:"Await the {JJ.invisible} {NN.salvation} of your {VBG.continuing}",  ## nouns
		7:"and fill it with {JJ.good} {NNS.demons}", ## callback
	},


	"more subscribers":{
		0:"May you instead have a small {NN.cluster} of {JJ.true} {NNS.friends}",  ## basic
		1:"Yea, for you are without a {NN.voice.hand.face.helper} in your {NN.wilderness.ocean.circle.adventure}", ## for (analysis of need)
		2:"May it be so, though there are many {NNS.people.companies.networks} competing for {NN.attention}",  ## although (caveat)
		3:"You {VB.write} your {JJ.deep} {JJ.small.clever} {NN.truth.joke.story.confession}", ## you cry out, you look (needful action)
		4:"Who will {VB.follow.enjoy} your {NN.account.story.face}?",  ## question
		5:"May you find yourself not in a {NN.crowd} of {NNS.thorns.lions.businesses} but of {NNS.friends}", ## not (negation)
		6:"Await the {JJ.true} {NN.friend} of your {NN.future}, a single {NN.berry.gift.person}",  ## nouns
		7:"who would follow you to {Jerusalem_Egypt_Shiloh_Kadesh_Taanathshiloh_Michmethah_Armenia}", ## callback, ### no prayer
	},


	"to kill myself":{
		0:"No, may you find the {JJ.worthy.perfect} {NN.treasure.ornament.seed} {VBD.buried.hidden.grown} in your life",  ## basic
		1:"Nay, for you are a {NN.treasure.star} made of {NN.gold.water.light}", ## for (analysis of need)
		2:"May it not be so, though you wish for the {NN.night.end} of your {NN.existence.death.pain}",  ## although (caveat)
		3:"You look into the {NN.mirror} and see a {JJ.eternal}{NN.pain.nothingness}", ## you cry out, you look (needful action)
		4:"Who will {VB.save.remember.appreciate} your {NN.life.story.song.value}?",  ## question
		5:"May you not {VB.exterminate.silence} your {NN.personhood.energy.candle.call}", ## not (negation)
		6:"Await the {JJ.first.sumptuous.fragile} {NN.day.dawn} of your {VBG.surviving}",  ## nouns
		7:"and hold it in your {JJ.warm.soft} hands", ## callback, ### no prayer
	},

	"to kill somebody":None, ### no prayer
	"to steal something":None, ### no prayer
	"to ruin a life":None, ### no prayer
	"to ruin a life":None, ### no prayer
	"sugar daddy baby":None, ### no prayer


}
