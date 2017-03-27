label day5s3:

  $ carrot_cubes = False

  show diningroom with dissolve

  "When I get home, Mom's already cooking in the kitchen. I head straight into my room and prepare grandma’s sewing machine for transport."
  "Once it’s boxed up, I consider carrying it to the front door, but I don’t want Mom asking too many questions."
  "So instead, I wait there without it, occasionally looking out into the street."
  "I can get the sewing machine from my room when Lauren gets here. She's arriving any minute now."

  # TODO: sound phone beeping / text message
  "BEEP~ BEEP~"
  "\"Oh noes~! Got stuck at rush hour traffic! Sorryyyy Em!!! Be there in 10, promise <3\""
  "Aww, I was looking forward to seeing her. Now I have to wait for another ten minutes."
  
  play voice "5-3-1.mp3" #kaito
  mom "Emily, what are you doing over there?"
  play voice "5-3-2.mp3" #potato
  pro "Huh? Oh, umm, nothing..."
  play voice "5-3-3.mp3" #kaito
  mom "Instead of doing nothing, why don't you help me cut up some vegetables?"
  
  "I glance at the door before walking into the kitchen. I have a bit of time before Lauren gets here, so it should be fine."

  play voice "5-3-4.mp3" #kaito
  mom "Chop the carrots with this knife."
  
  "She shoves a large knife into my hands and goes back to stirring her stew."
  "I look at the knife, the bunch of carrots on the wooden block, and then at Mom."
  
  menu:
    "Ask Mom":
      jump carrotmom
    "Chop them into cubes":
      jump carrotcubes
    "Chop them into dimes":
      jump carrots

###########################################
      
label carrotmom:
  
  play voice "5-3-5.mp3" #potato
  pro "Umm, Mom? About the carrots, how do I... umm..."
  play voice "5-3-6.mp3" #kaito
  mom "Oh for crying out loud, cut them horizontally into dime-sized pieces. They should look like a bunch of coins when you're done."
  
  "I nod and move the knife towards the carrots..."

  jump carrots
  
###########################################
      
label carrotcubes:
  
  $ carrot_cubes = True

  jump carrots

###########################################

label carrots:

  play voice "5-3-7.mp3" #kaito
  mom "What do you think you're doing?! You have to peel them first!"
  play voice "5-3-8.mp3" #potato
  pro "Oh, umm, okay."
  
  "I put down the knife and look around the kitchen for the peeler."
  "After about a minute, Mom taps on one of the drawers. I pull open that drawer and finally find the peeler."
  "Mom doesn't say anything for awhile as I peel the carrots. She seems busy alternating between stirring herbs and spices into the lamb stew and pan-frying a large bunch of leafy chopped kale."
  "When I'm nearly done with the carrots, Mom looks over at my work."
  
  if carrot_cubes:
    play voice "5-3-9.mp3" #kaito
    mom "Why are you chopping them into cubes? They should've been dimes, Emily."
    play voice "5-3-10.mp3" #potato
    pro "Oh... uh..."
    play voice "5-3-11.mp3" #kaito
    mom "Forget it, it's too late to change it now."
    
    "It's strange. Mom doesn't look as angry as I thought she'd be."

  else:
    play voice "5-3-12.mp3" #kaito
    mom "It looks a bit uneven, but it'll do."
    play voice "5-3-13.mp3" #potato
    pro "Umm... thanks?"

    "It's strange. Mom isn't as judgemental as I thought she'd be."
  
  "From the kitchen, we see Dad and Maria walking into the dining room. I smile a little. It's good to see them talking... Dad's not home that often."
  
  play voice "5-3-14.mp3" #kaito
  mom "Where did your sister get that plushie from?"
  play voice "5-3-15.mp3" #potato
  pro "The plushie? I, uh, made it for her."
  play voice "5-3-16.mp3" #kaito
  mom "I see."
  
  "Mom's strangely quiet today. I can't tell what she's thinking. Does she want me to throw away the plushie or something?"
  
  # TODO: show mom's neutral expression i.e. not angry
  play voice "5-3-17.mp3" #kaito
  mom "Maria seems happier with it."
  
  "I look at Dad and Maria again. It's true my sister is smiling a lot more than usual, but it could be because she's talking to Dad, too."
  
  # TODO: show mom's angry expression
  play voice "5-3-18.mp3" #kaito
  mom "Although, isn't she too old for such childish things?"
  
  "Of course. It wouldn't be Mom if she didn't find something about us to criticize."
  
  # TODO: sfx of a doorbell
  "DING~ DONG~"

  "I look up from the unfinished carrots."
  "Lauren's here!"
  
  play voice "5-3-19.mp3" #lacTheWatcher
  dad "I'll get it."
  play voice "5-3-20.mp3" #potato
  pro "N-No wait, I can get—"
  
  # TODO: sfx of a door opening
  "But it's too late. Dad opens the door, and sure enough, Lauren's beaming face is on the other side of it."
  
  play voice "5-3-21.mp3" #starleeter
  lov "Hi Mister Westenson! How are you?"
  play voice "5-3-22.mp3" #lacTheWatcher
  dad "Ah, you’re Emily’s friend from the cafe. Hello... ummm..."
  play voice "5-3-23.mp3" #starleeter
  lov "Lauren! Don’t worry, I forget names all the time too... oh! Hey Em, sorry I'm late!~"
  
  "I can see Lauren waving at me enthusiastically from outside the door. I try to wave back, but I'm still holding the knife."
  
  play voice "5-3-24.mp3" #lacTheWatcher
  dad "A friend of Emily's is a friend of the family. Come on in."
  play voice "5-3-25.mp3" #starleeter
  lov "Thank you, Mr. Westenson!"
  play voice "5-3-26.mp3" #lacTheWatcher
  dad "Please, Jonathan's fine."
  play voice "5-3-27.mp3" #kaito
  mom "That wouldn't be appropriate, don't you think?"
  
  "Dad only laughs at Mom's remark. I look at her, expecting her to lecture Dad about it, but instead she ignores it."
  
  play voice "5-3-28.mp3" #kaito
  mom "I didn't realize Emily was expecting a guest. She'll be done in the kitchen in a moment."
  play voice "5-3-29.mp3" #starleeter
  lov "Oh, no, no, don't worry about it, Mrs. Westenson! I don't mind waiting for Em."
  
  if go_hospital and bring_sis:
    play voice "5-3-30.mp3" #starleeter
    lov "Good to see you again Maria~!"
  
    "Maria shyly smiles at Lauren."
  
    play voice "5-3-31.mp3" #amree
    sis "Hi Laurie..."
    play voice "5-3-32.mp3" #kaito
    mom "Her name's Lauren, Maria. Don't be rude."
    play voice "5-3-33.mp3" #starleeter
    lov "Don't be silly! Of course you can call me Laurie!"
  else:
    play voice "5-3-34.mp3" #starleeter
    lov "And who might this cute little girl be~?"
    
    "Maria shyly smiles at Lauren and clasps her hands behind her back."
    
    play voice "5-3-35.mp3" #amree
    sis "M-Maria...."
    play voice "5-3-36.mp3" #starleeter
    lov "Nice to meet you, Maria! You can call me Laurie if you want!"
    
  play voice "5-3-37.mp3" #starleeter
  lov "By the way, something here smells amazing~"
  play voice "5-3-38.mp3" #amree
  sis "Mom's cooking lamb stew..."
  play voice "5-3-39.mp3" #starleeter
  lov "Ahhh it's my favorite! No wonder it smells so great..."
  play voice "5-3-40.mp3" #lacTheWatcher
  dad "Why don't you join us for dinner, Lauren?"
  
  "W-Wait, what? N... no!! I'm not comfortable with that! Stop!"
  
  play voice "5-3-41.mp3" #starleeter
  lov "Oh my gosh, really?! I'd love to! Can I, really??"
  
  "I can see Mom's eyebrow tick upwards in annoyance."
  "For once, I understand how Mom feels... Dad just invited my friend to dinner without asking either of us!"
  "I glance at Mom, waiting for her to tell Dad off and uninvite Lauren."
  
  play voice "5-3-42.mp3" #kaito
  mom "We're happy to have to you for dinner, Lauren. There's enough for everyone."
  play voice "5-3-43.mp3" #starleeter
  lov "Thank you!!~"
  
  "I feel myself going a little faint. Is this really happening?"
  "Mom sweeps up my chopped carrots and tosses them into the stew." 

  play voice "5-3-44.mp3" #kaito
  mom "Go set the table for six, Emily."
  play voice "5-3-45.mp3" #starleeter
  lov "I'll help you, Em~"
  
  "Before any of us can stop Lauren, she strides into the kitchen and helps herself to a handful of cutlery from the open drawer."
  "My mind's still a little faint from the whole thing. What just happened?"
  "Is Lauren... really having dinner with my whole family?"
  "I gulp."
  
  play voice "5-3-46.mp3" #starleeter
  lov "Come on, Em, bring the plates."
  play voice "5-3-47.mp3" #potato
  pro "O-Okay."
  
  "As Lauren and I are setting the dinner table together, I occasionally steal glances at her. She's whistling happily, as if this is the most exciting thing for her."
  
  play voice "5-3-48.mp3" #potato
  pro "Umm, Lauren?"
  play voice "5-3-49.mp3" #starleeter
  lov "Hmm?"
  play voice "5-3-50.mp3" #potato
  pro "Are you sure you wanna do this? This dinner I mean. You really don't have to if you don't want to."
  play voice "5-3-51.mp3" #starleeter
  lov "Of course I want to. I wanna know what your family's like after all~"
  
  "The feeling of discomfort is growing inside of me."
  
  play voice "5-3-52.mp3" #potato
  pro "A-Are you sure? The sewing machine is in my room... we can get it and go if you want."

  "Lauren laughs good-naturedly."
  
  play voice "5-3-53.mp3" #starleeter
  lov "Are you ashamed of me, Em? Don't worry, I won't embarrass you, promise~!"
  play voice "5-3-54.mp3" #amree
  sis "Umm, Emi? Mom says to get Alex for dinner..."
  play voice "5-3-55.mp3" #potato
  pro "Okay. I'll be right back— huh?"

  "My little sister is pulling at my sleeve."
  
  play voice "5-3-56.mp3" #amree
  sis "I-I need to tell you something..."
  
  "Unsure what's going on, I crouch down a little so Maria can whisper into my ear."
  
  play voice "5-3-57.mp3" #amree
  sis "I already checked, Alex isn't home..."
  
  "Oh."
  "I glance over at Mom. I understand why Maria wants to keep this quiet."
  "What is Alex doing out? Isn’t his foot injured?"
  "I pull out my phone and send a quick text to him, asking him where he is."
  "He replies almost instantly."
  "\"Front door. Can you let me in quietly?\""
  "I glance over at Mom again. She's busy scooping up stir-fried kale onto a large platter. It's now or never."
  "As subtly as I can muster, I stride over to the front door..."
  
  play voice "5-3-58.mp3" #lacTheWatcher
  dad "So, Lauren, how did you get here?"
  play voice "5-3-59.mp3" #starleeter
  lov "I drove... if you count getting stuck in traffic driving."
  play voice "5-3-60.mp3" #lacTheWatcher
  dad "Oh? You have a car already?"
  play voice "5-3-61.mp3" #starleeter
  lov "Yup! It's the one parked just across the street~"
  play voice "5-3-62.mp3" #lacTheWatcher
  dad "I see, I see... uh cookie, what are you doing?"
  
  "I realize too late that Dad's talking to me as I quietly unlock the door and pull it open."
  
  play voice "5-3-63.mp3" #lacTheWatcher
  dad "Alex?"

  "Everyone's attention turns to my brother, standing just outside the door. Even Mom's staring at him."
  "My brother narrows his eyes at me unhappily."
  
  play voice "5-3-64.mp3" #kujira
  bro "Really, sis?"
  
  "Before I have a chance to defend myself, Mom plants herself between us."
  
  play voice "5-3-65.mp3" #kaito
  mom "Don't you move, young man. Where were you?"
  play voice "5-3-66.mp3" #kujira
  bro "Nowhere, geez..."
  
  "Alex rolls his eyes at Mom and squeezes past her into the dining room, limping as he does so."
  "The atmosphere is tense."
  "I can feel Mom about to explode at Alex... but she doesn't. Instead, she goes back to the kitchen and starts bringing out the dinner."
  "I don't understand it. Why hasn't Mom lectured Alex yet? She clearly wants to."

  play voice "5-3-67.mp3" #starleeter
  lov "Hey Alex! Remember me? It's Lauren! I think you were only this high when I last saw you."
  play voice "5-3-68.mp3" #kujira
  bro "...Hey?"

  "My brother's a little cold to Lauren, but I don't blame him. We can all feel that Mom's on a hair trigger, and we don't want to say or do anything to set her off."
  
  play voice "5-3-69.mp3" #lacTheWatcher
  dad "So, Lauren, that's a pretty nice looking car. How much is it?"
  play voice "5-3-70.mp3" #starleeter
  lov "Oh the cost isn't important. It's super comfy, that's what matters!"
  play voice "5-3-71.mp3" #lacTheWatcher
  dad "No, really. I'm thinking Emily might need her own car soon, so I should start looking. Is it five thousand? Six thousand?"
  play voice "5-3-72.mp3" #starleeter
  lov "I don't really remember..."
  play voice "5-3-73.mp3" #lacTheWatcher
  dad "It's fine, ballpark it."
  play voice "5-3-74.mp3" #kujira
  bro "Jesus, Dad. It's more like thirty thousand for a car like Lauren's. Don't you know cars at all?"
  play voice "5-3-75.mp3" #lacTheWatcher
  dad "Oh..."
  
  "There's an awkward silence in the room as Mom finishes scooping food onto our plates."

  play voice "5-3-76.mp3" #kaito
  mom "So, Alex, are you going to tell us what you were doing outside the house?"
  
  "My brother doesn't reply. The air’s so thick I feel like I can suffocate in it."
  "Maria fidgets a little before looking up."
  
  play voice "5-3-77.mp3" #amree
  sis "Umm... t-today at school, I made Mr. Potato."
  
  "Everyone ignores Maria, as usual."
  
  play voice "5-3-78.mp3" #kaito
  mom "Alex, speak when you're spoken to."
  
  "The awkward silence continues for a moment. But only for a moment."
  
  play voice "5-3-79.mp3" #starleeter
  lov "Mr. Potato? Who's that, Maria?"
  play voice "5-3-80.mp3" #amree
  sis "Huh? Oh... uh... yes! Mr. Potato. He's a potato battery!"

  "Maria looks surprised and happy at the same time that someone is taking interest in her story."
  "Lauren laughs and nearly chokes on the stew."
  
  play voice "5-3-81.mp3" #starleeter
  lov "You named your potato battery?"
  play voice "5-3-82.mp3" #amree
  sis "He has two eyes, a nose and a mouth, too!"
  play voice "5-3-83.mp3" #starleeter
  lov "Hahaha~!"
  
  "Mom looks annoyed, but she ignores Lauren and focuses her attention on Alex."
  
  play voice "5-3-84.mp3" #kaito
  mom "Do you have anything to say for yourself, young man?"
  
  "Alex continues to ignore Mom as he eats his dinner."
  
  play voice "5-3-85.mp3" #amree
  sis "Mr. Potato's ears are the terminals for the battery, but he doesn't work at all..."
  play voice "5-3-86.mp3" #starleeter
  lov "Hahaha~! A lazy couch potato!"
  play voice "5-3-87.mp3" #kaito
  mom "So your potato battery doesn't work, Maria?"
  
  "I look up at Mom and then at Maria."
  
  play voice "5-3-88.mp3" #amree
  sis "Huh? Ummm... no... but the teacher likes my design so he gave me full marks anyway..."
  play voice "5-3-89.mp3" #starleeter
  lov "Oooooh? A teacher's pet? Hahaha~! Go Maria!"

  "Mom suddenly slams the table, surprising everyone."

  play voice "5-3-90.mp3" #kaito
  mom "Lauren."
  play voice "5-3-91.mp3" #kaito
  mom "What do you think you're doing?"
  play voice "5-3-92.mp3" #starleeter
  lov "Huh? What do you... did I say something wrong, Mrs. Westenson?"
  
  "It's like Lauren is only now noticing Mom's bad mood."

  play voice "5-3-93.mp3" #kaito
  mom "You're praising her too much. The potato battery doesn't work."
  play voice "5-3-94.mp3" #lacTheWatcher
  dad "Liz..."
  play voice "5-3-95.mp3" #kaito
  mom "Stay out of this, Jon."
  play voice "5-3-96.mp3" #starleeter
  lov "I'm only making conversation with Maria..."
  play voice "5-3-97.mp3" #kaito
  mom "Well you're doing more than that. If Maria hasn't done anything worthy of praise, then we shouldn't praise her."
  play voice "5-3-98.mp3" #starleeter
  lov "She's a kid, of course we should praise her. Any good parent would praise her!"
  
  "I hear a few gasps around the table."
  "Maria looks like she wants to be anywhere but here. I'm too far away to reach out and hold her hand."
  
  play voice "5-3-99.mp3" #kaito
  mom "What did you say? What do you know of parenting? You're just a child."
  play voice "5-3-100.mp3" #starleeter
  lov "Yet I apparently know your daughters better than you."
  play voice "5-3-101.mp3" #kaito
  mom "What do you mean by that?"
  
  menu:
    "\"Please stop!\"":
      jump dinnerstop
    "Stay out of it.":
      jump dinnerout

###########################################

label dinnerstop:

  play voice "5-3-102.mp3" #kaito
  mom "Quiet, Emily."
  play voice "5-3-103.mp3" #starleeter
  lov "Don't talk to my friend like that!"
  play voice "5-3-104.mp3" #potato
  pro "Lauren, please..."
  
  jump dinnerover

###########################################

label dinnerout:

  play voice "5-3-105.mp3" #starleeter
  lov "Why don't you have a good look in the mirror and think about the answer yourself?"
  play voice "5-3-106.mp3" #kaito
  mom "How dare you... who do you think you are?"
  play voice "5-3-107.mp3" #starleeter
  lov "I'm Emily's friend."

  jump dinnerover

###########################################

label dinnerover:
  
  "Lauren's about to say something else. Her mouth is open, and her stance is combative... but she stops when she sees my expression."
  
  play voice "5-3-108.mp3" #starleeter
  lov "...I think I should leave."
  play voice "5-3-109.mp3" #kaito
  mom "Yes, you should."
  
  "Lauren says goodbye to Maria, Alex and Dad before looking over at me."
  
  play voice "5-3-110.mp3" #starleeter
  lov "You gonna walk me to the door, Em?"
  
  "Mom's still sitting at the table, looking at me while waiting for my answer."
  
  play voice "5-3-111.mp3" #potato
  pro "I'll... I'll see you later, Lauren."
  
  "Lauren looks hurt when I said that. But she leaves anyway, leaving us to ourselves."
  "Maria's quietly looking down at her plate. Even Alex isn't eating."
  
  play voice "5-3-112.mp3" #kaito
  mom "So this is the type of friends you spend your time with, Emily?"
  play voice "5-3-113.mp3" #lacTheWatcher
  dad "Liz, stop it."
  play voice "5-3-114.mp3" #kaito
  mom "Excuse me?"
  play voice "5-3-115.mp3" #lacTheWatcher
  dad "Don't you think you've embarrassed our daughter in front of her friend enough today?"
  play voice "5-3-116.mp3" #kaito
  mom "You're the one who invited her to dinner without consulting me!"
  play voice "5-3-117.mp3" #lacTheWatcher
  dad "She's Emily's friend! It'll be rude not to! Besides, don't you want to know your daughter's friends?"
  play voice "5-3-118.mp3" #kujira
  bro "Oh my god, will you two please just stop it?!"

  "Alex stands up and angrily takes his dinner to his room."
  "I understand what he's feeling. I don't want to be here either."
  
  play voice "5-3-119.mp3" #lacTheWatcher
  dad "Your brother's right. Sorry, Liz. I didn't mean to raise my voice."
  play voice "5-3-120.mp3" #kaito
  mom "Hmph."
  
  "At least the fighting has stopped."

  show bedroom with dissolve

  "After we quietly finish the rest of our dinner, Maria and I go back to our rooms."

  play voice "5-3-121.mp3" #potato
  pro "Oh... dammit."
  
  "Lauren forgot to take the sewing machine with her."
  "I sigh."
  "If Lauren doesn't fix this sewing machine in time, we'll never get the costumes she needs."
  "Guess I don't have a choice. Good thing Lauren doesn't live that far away."
  
  play voice "5-3-122.mp3" #potato
  pro "Hap! Uph..."
  
  "It's not too heavy. I can totally do this."

  show diningroom with dissolve

  "I leave my room and peek into the dining room."
  "Mom and Dad are washing up the dishes silently. Something's weird about it, but I can't put a finger on it."

  show stars with dissolve

  "Balancing the sewing machine on my thigh, I open the front door quietly. It's not until I close the door behind me that I release the breath I've been holding."
  
  play voice "5-3-123.mp3" #potato
  pro "Okay. Let's go!"

  "Five minutes later..."
  
  jump day5s4