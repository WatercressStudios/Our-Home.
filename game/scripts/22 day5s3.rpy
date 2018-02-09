label day5s3:

    $ carrot_cubes = False

    scene diningroom with dissolve

    "When I get home, Mom's already cooking in the kitchen. I head straight into my room and prepare grandma’s sewing machine for transport."
    "Once it’s boxed up, I consider carrying it to the front door, but I don’t want Mom asking too many questions."
    "So instead, I wait in the dining room, occasionally looking out into the street."
    "I can get the sewing machine from my room when Lauren gets here. She's arriving any minute now."
    "Quick. Easy. Efficient exchange."

    play sound vibrate
    "BEEP~ BEEP~"
    "{color=#FF69B4}\"oh noes~! got stuck @ rush hour traffic! sorryyyy Em!!! Be there in 10, promise <33333\"{/color}"
    "Aww, I was looking forward to seeing her. Now I have to wait for another ten minutes."
    
    voice "5-3-1.mp3" #kaito
    show mom angry2 with dissolve 
    mom "Emily, what are you doing over there?"
    play music bgmmomintro noloop fadeout 1.0
    queue music bgmmomloop loop
    voice "5-3-2.mp3" #potato
    pro "Huh? Oh, umm, nothing..."
    voice "5-3-3.mp3" #kaito
    show mom angry1 with dissolve
    mom "Instead of doing nothing, why don't you help me cut up some vegetables?"
    
    "I glance at the door before walking into the kitchen. I have a bit of time before Lauren gets here, so it should be fine."

    scene kitchen with dissolve
    voice "5-3-4.mp3" #kaito
    show mom surprise with dissolve 
    mom "Chop the carrots with this knife."
    hide mom with dissolve
    
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
    
    voice "5-3-5.mp3" #potato
    pro "Umm, Mom? About the carrots, how do I... umm..."
    voice "5-3-6.mp3" #kaito
    show mom sad3 with dissolve
    mom "Oh for crying out loud, cut them horizontally into dime-sized pieces. They should look like a bunch of coins when you're done."
    
    hide mom
    "I nod and move the knife towards the carrots..."

    jump carrots
    
###########################################
            
label carrotcubes:
    
    $ carrot_cubes = True

    jump carrots

###########################################

label carrots:

    voice "5-3-7.mp3" #kaito
    show mom angry2 with dissolve
    mom "What do you think you're doing?! You have to peel them first!"
    voice "5-3-8.mp3" #potato
    pro "Oh, umm, okay."
    
    hide mom
    "I put down the knife and look around the kitchen for the peeler."
    "After about a minute, Mom taps on one of the drawers. I pull open that drawer and finally find the peeler."
    "Mom doesn't say anything for awhile as I peel the carrots. She seems busy alternating between stirring herbs and spices into the lamb stew and pan-frying a large bunch of leafy chopped kale."
    "When I'm nearly done with the carrots, Mom looks over at my work."
    
    if carrot_cubes:
        voice "5-3-9.mp3" #kaito
        show mom angry1 with dissolve
        mom "Why are you chopping them into cubes? They should've been dimes, Emily."
        voice "5-3-10.mp3" #potato
        pro "Oh... uh..."
        voice "5-3-11.mp3" #kaito
        show mom sad2 with dissolve
        mom "Forget it, it's too late to change it now."
        
        "It's strange. Mom doesn't look as angry as I thought she'd be."

    else:
        show mom angry2 with dissolve
        voice "5-3-12.mp3" #kaito
        mom "It looks a bit uneven, but it'll do."
        voice "5-3-13.mp3" #potato
        pro "Umm... thanks?"

        "It's strange. Mom isn't as judgemental as I thought she'd be."
    
    "From the kitchen, we see Dad and Maria walking into the dining room. I smile a little. It's good to see them talking... Dad's not home that often."
    
    voice "5-3-14.mp3" #kaito
    show mom happy1 with dissolve
    mom "Where did your sister get that plushie from?"
    voice "5-3-15.mp3" #potato
    pro "The plushie? I, uh, made it for her."
    voice "5-3-16.mp3" #kaito
    show mom angry2 with dissolve
    mom "I see."
    
    "Mom's strangely quiet today. I can't tell what she's thinking. Does she want me to throw away the plushie or something?"
    
    # TODO: show mom's neutral expression i.e. not angry
    voice "5-3-17.mp3" #kaito
    show mom sad2 with dissolve
    mom "Maria seems happier with it."
    
    scene diningroom with dissolve
    show dad neutral1 with dissolve:
        align (0.33, 1.0)
    show sis happy1 with dissolve:
        align (0.66, 1.0)
        
    "I look at Dad and Maria again. It's true my sister is smiling a lot more than usual, but it could be because she's talking to Dad, too."
    
    voice "5-3-18.mp3" #kaito
    mom "Although, isn't she too old for such childish things?"
    
    "Of course. It wouldn't be Mom if she didn't find something about us to criticize..."
    
    play sound knock
    show dad smile1 with dissolve:
        align (0.33, 1.0)
    show sis worry1 with dissolve:
        align (0.66, 1.0)

    "I look up from the unfinished carrots."
    "Lauren's here!"
    
    voice "5-3-19.mp3" #lacTheWatcher
    show dad smile2 with dissolve: 
        align (0.33, 1.0)
    dad "I'll get it."
    voice "5-3-20.mp3" #potato
    hide dad with dissolve 
    pro "N-No wait, I can get—"
    
    # TODO: sfx of a door opening
    scene black with dissolve
    "But it's too late. Dad opens the door, and sure enough, Lauren's beaming face is on the other side of it."
    play music bgmlov fadeout 1.0 fadein 0.0
    
    scene livingroom sunset with dissolve
    
    voice "5-3-21.mp3" #starleeter
    show dad smile1 with dissolve:
        align (0.66, 1.0)
    show lov happy1 with dissolve: 
        align (1.0, 1.0)
    lov "Hi Mister Westenson! How are you?"
    voice "5-3-22.mp3" #lacTheWatcher
    dad "Ah, you’re Emily’s friend from the cafe. Hello... ummm..."
    
    show dad sad2 with dissolve: 
        align (0.66, 1.0)
    show lov happy2h with dissolve: 
        align (1.0, 1.0)
    voice "5-3-23.mp3" #starleeter
    lov "Lauren! Don’t worry, I forget names all the time too... oh! Hey Em, sorry I'm late!~"
    
    "I can see Lauren waving at me enthusiastically from outside the door. I try to wave back, but I'm still holding the knife."
    
    voice "5-3-24.mp3" #lacTheWatcher
    show dad smile2 with dissolve:
        align (0.66, 1.0)
    dad "A friend of Emily's is a friend of the family. Come on in."
    voice "5-3-25.mp3" #starleeter
    show lov happy1 with dissolve:
        align (1.0, 1.0)
    lov "Thank you, Mr. Westenson!"
    voice "5-3-26.mp3" #lacTheWatcher
    show dad smile1 with dissolve:
        align (0.66, 1.0)
    dad "Please, Jonathan's fine."
    voice "5-3-27.mp3" #kaito
    show mom sad1 with dissolve:
        align (0.33, 1.0)
    mom "That wouldn't be appropriate, don't you think?"
    
    show sis worry1 with dissolve:
        align (0.0, 1.0)
    show dad smile2 with dissolve:
        align (0.66, 1.0)
    "Dad only laughs at Mom's remark. I look at her, expecting her to lecture Dad about it, but instead she ignores it."
    
    show dad smile1 with dissolve:
        align (0.66, 1.0)
    show mom surprise with dissolve:
        align (0.33, 1.0)
    voice "5-3-28.mp3" #kaito
    mom "I didn't realize Emily was expecting a guest. She'll be done in the kitchen in a moment."
    show lov shy1 with dissolve:
        align (1.0, 1.0)
    voice "5-3-29.mp3" #starleeter
    lov "Oh, no, no, don't worry about it, Mrs. Westenson! I don't mind waiting for Em."
    show mom sad3 with dissolve:
        align (0.33, 1.0)
    
    if go_hospital and bring_sis:
        voice "5-3-30.mp3" #starleeter
        show lov happy1h with dissolve:
            align (1.0, 1.0)
        lov "Good to see you again Maria~!"
    
        "Maria shyly smiles at Lauren."
    
        show sis happy2 with dissolve:
            align (0.0, 1.0)
        voice "5-3-31.mp3" #amree
        sis "Hi Laurie..."
        voice "5-3-32.mp3" #kaito
        show mom angry2 with dissolve:
            align (0.33, 1.0)
        mom "Her name's Lauren, Maria. Don't be rude."
        voice "5-3-33.mp3" #starleeter
        show lov confused1 with dissolve:
            align (1.0, 1.0)
        lov "Don't be silly! Of course you can call me Laurie!"
    else:
        voice "5-3-34.mp3" #starleeter
        show lov happy1h with dissolve:
            align (1.0, 1.0)
        lov "And who might this cute little girl be~?"
        
        show sis happy1b with dissolve:
            align (0.0, 1.0)
        "Maria shyly smiles at Lauren and clasps her hands behind her back."
        
        voice "5-3-35.mp3" #amree
        show sis happy2b with dissolve:
            align (0.0, 1.0)
        sis "M-Maria...."
        voice "5-3-36.mp3" #starleeter
        show lov happy2 with dissolve:
            align (0.0, 1.0)
        lov "Nice to meet you, Maria! You can call me Laurie if you want!"
        
    show lov happy1h with dissolve:
        align (1.0, 1.0)
    voice "5-3-37.mp3" #starleeter
    lov "By the way, something here smells amazing~"
    voice "5-3-38.mp3" #amree
    show sis happy1 with dissolve:
        align (0.0, 1.0)
    sis "Mom's cooking lamb stew..."
    voice "5-3-39.mp3" #starleeter
    show lov happy1bh with dissolve:
        align (1.0, 1.0)
    lov "Ahhh it's my favorite! No wonder it smells so great..."
    show dad smile2 with dissolve:
        align (0.66, 1.0)
    voice "5-3-40.mp3" #lacTheWatcher
    dad "Why don't you join us for dinner, Lauren?"
    
    "W-Wait, what? N... no!! I'm not comfortable with that! Stop!"
    
    show lov happy1 with dissolve:
        align (1.0, 1.0)
    voice "5-3-41.mp3" #starleeter
    lov "Oh my gosh, really?! I'd love to! Can I, really??"
    
    show mom angry1 with dissolve:
        align (0.33, 1.0)
    "I can see Mom's eyebrow tick upwards in annoyance."
    "For once, I understand how Mom feels... Dad just invited my friend to dinner without asking either of us!"
    "I glance at Mom, waiting for her to tell Dad off and uninvite Lauren."
    
    voice "5-3-42.mp3" #kaito
    show mom happy1 with dissolve:
        align (0.33, 1.0)
    mom "We're happy to have to you for dinner, Lauren. There's enough for everyone."
    voice "5-3-43.mp3" #starleeter
    lov "Thank you!!~"
    
    "I feel myself going a little faint. Is this really happening?"
    "Mom sweeps up my chopped carrots and tosses them into the stew." 

    voice "5-3-44.mp3" #kaito
    show mom surprise with dissolve:
        align (0.33, 1.0)
    mom "Go set the table for six, Emily."
    voice "5-3-45.mp3" #starleeter
    show lov happy2 with dissolve:
        align (1.0, 1.0)
    lov "I'll help you, Em~"
    
    scene kitchen with dissolve
    
    "Before any of us can stop Lauren, she strides into the kitchen and helps herself to a handful of cutlery from the open drawer."
    "My mind's still a little faint from the whole thing. What just happened?"
    "Is Lauren... really having dinner with my whole family?"
    "I gulp."
    
    voice "5-3-46.mp3" #starleeter
    lov "Come on, Em, bring the plates."
    voice "5-3-47.mp3" #potato
    pro "O-Okay."
    
    scene diningroom with dissolve
    show lov happy2 with dissolve
    "As Lauren and I are setting the dinner table together, I occasionally steal glances at her. She's whistling happily, as if this is the most exciting thing for her."
    
    voice "5-3-48.mp3" #potato
    pro "Umm, Lauren?"
    show lov confused1 with dissolve
    voice "5-3-49.mp3" #starleeter
    lov "Hmm?"
    voice "5-3-50.mp3" #potato
    pro "Are you sure you wanna do this? This dinner I mean. You really don't have to if you don't want to."
    show lov happy1 with dissolve
    voice "5-3-51.mp3" #starleeter
    lov "Of course I want to. I wanna know what your family's like after all~"
    
    show lov happy2 with dissolve
    "The feeling of discomfort is growing inside of me."
    
    voice "5-3-52.mp3" #potato
    pro "A-Are you sure? The sewing machine is in my room... we can get it and go if you want."

    show lov happy1h with dissolve
    "Lauren laughs good-naturedly."
    
    voice "5-3-53.mp3" #starleeter
    lov "Are you ashamed of me, Em? Don't worry, I won't embarrass you, promise~!"
    voice "5-3-54.mp3" #amree
    show sis worry2 with dissolve:
        align (0.66, 1.0)
    sis "Umm, Emi? Mom says to get Alex for dinner..."
    voice "5-3-55.mp3" #potato
    pro "Okay. I'll be right back— huh?"

    "My little sister is pulling at my sleeve."
    
    voice "5-3-56.mp3" #amree
    show sis worry1 with dissolve:
        align (0.66, 1.0)
    sis "I-I need to tell you something..."
    
    scene livingroom sunset
    show sis worry1 with dissolve
    
    "Maria gently pulls me out of the dining room, and out of earshot of the others. What is going on...?"
    
    voice "5-3-57.mp3" #amree
    show sis worry2 with dissolve
    sis "I already checked, Alex isn't home..."
    
    "Oh."
    "I glance over at Mom. I understand why Maria wants to keep this quiet."
    "What is Alex doing out? Isn’t his foot injured?"
    hide sis with dissolve
    "I pull out my phone and type out a quick text to him, asking him where he is."
    "He replies almost instantly."
    "{color=#568203}\"Front door. Can you let me in quietly?\"{/color}"
    "I glance over at Mom again. She's busy scooping up stir-fried kale onto a large platter. It's now or never."
    "As subtly as I can muster, I stride over to the front door..."
    
    show lov happy2 with dissolve:
        align (0.6, 1.0)
    show dad smile1 with dissolve:
        align (0.25, 1.0)
    
    voice "5-3-58.mp3" #lacTheWatcher
    dad "So, Lauren, how did you get here?"
    voice "5-3-59.mp3" #starleeter
    show lov shy1h with dissolve:
        align (0.6, 1.0)
    lov "I drove... if you count getting stuck in traffic driving."
    
    voice "5-3-60.mp3" #lacTheWatcher
    show dad smile2 with dissolve:
        align (0.25, 1.0)
    dad "Oh? You have a car already?"
    voice "5-3-61.mp3" #starleeter
    show lov happy2 with dissolve:
        align (0.6, 1.0)
    lov "Yup! It's the one parked just across the street~"
    voice "5-3-62.mp3" #lacTheWatcher
    show dad neutral2 with dissolve:
        align (0.25, 1.0)
    dad "I see, I see... uh cookie, what are you doing?"
    
    "I realize too late that Dad's talking to me as I quietly unlock the door and pull it open."
    show bro sad1 with dissolve:
        align (1.0, 1.0)
    "...Damn it."
    voice "5-3-63.mp3" #lacTheWatcher
    dad "Alex?"

    show bro sad2 with dissolve:
        align (1.0, 1.0)
    
    "Everyone's attention turns to my brother, standing just outside the door. Even Mom's staring at him."
    "My brother narrows his eyes at me unhappily."
    
    show bro angry1 with dissolve:
        align (1.0, 1.0)
    voice "5-3-64.mp3" #kujira
    bro "Really, sis?"
    
    show lov confused2 with dissolve:
        align (0.6, 1.0)
    show dad sad2 with dissolve:
        align (0.25, 1.0)
    "Before I have a chance to defend myself, Mom already has her sights on him."
    stop music fadeout 0.2
    voice "5-3-65.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.0, 1.0)
    mom "Don't you move, young man. Where were you?"
    voice "5-3-66.mp3" #kujira
    show bro smirk1 with dissolve:
        align (1.0, 1.0)
    bro "Nowhere, geez..."
    
    hide bro with dissolve
    
    show lov confused1h with dissolve:
        align (0.6, 1.0)
    show dad sad1 with dissolve:
        align (0.25, 1.0)
    "Alex rolls his eyes at Mom and squeezes past her into the dining room, limping as he does so."
    show mom angry1 with dissolve:
        align (0.0, 1.0)
    "The atmosphere is tense."
    "I can feel Mom about to explode at Alex... but she doesn't."
    hide mom with dissolve
    "Instead, she goes back to the kitchen and starts bringing out the dinner."
    "I don't understand it. Why hasn't Mom lectured Alex yet? She clearly wants to."
    play music bgmlov fadeout 1.0 fadein 0.0
    voice "5-3-67.mp3" #starleeter
    
    scene diningroom with dissolve
    
    show sis worry1 with dissolve:
        align (0.0, 1.0) 
    show dad neutral1 with dissolve:
        align (0.25, 1.0)
    show bro sad1 with dissolve:
        align (1.00, 1.0)
    show lov happy2 with dissolve:
        align (0.75, 1.0)
    
    lov "Hey Alex! Remember me? It's Lauren! I think you were only this high when I last saw you."
    voice "5-3-68.mp3" #kujira
    show bro sad2 with dissolve:
        align (1.0, 1.0)
    bro "...Hey?"

    show lov confused1 with dissolve:
        align (0.75, 1.0)
    "My brother's a little cold to Lauren, but I don't blame him. We can all feel that Mom's on a hair trigger, and we don't want to say or do anything to set her off."
    
    voice "5-3-69.mp3" #lacTheWatcher
    show dad smile1 with dissolve:
        align (0.25, 1.0)
    dad "So, Lauren, that's a pretty nice looking car. How much is it?"
    voice "5-3-70.mp3" #starleeter
    show lov happy2 with dissolve:
        align (0.75, 1.0)
    lov "Oh the cost isn't important. It's super comfy, that's what matters!"
    voice "5-3-71.mp3" #lacTheWatcher
    show dad neutral2 with dissolve:
        align (0.25, 1.0)
    dad "No, really. I'm thinking Emily might need her own car soon, so I should start looking. Is it five thousand? Six thousand?"
    voice "5-3-72.mp3" #starleeter
    show lov shy2 with dissolve:
        align (0.75, 1.0)
    lov "I don't really remember..."
    voice "5-3-73.mp3" #lacTheWatcher
    show dad smile1 with dissolve:
        align (0.25, 1.0)
    dad "It's fine, ballpark it."
    voice "5-3-74.mp3" #kujira
    show bro smirk1 with dissolve:
        align (1.0, 1.0)
    bro "Jesus, Dad. It's more like thirty thousand for a car like Lauren's. Don't you know cars at all?"
    voice "5-3-75.mp3" #lacTheWatcher
    show dad sad1 with dissolve:
        align (0.25, 1.0)
    dad "Oh..."
    play music bgmmomintro noloop fadeout 1.0
    queue music bgmmomloop loop
    show lov confused1 with dissolve:
        align (0.75, 1.0)
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    "There's an awkward silence in the room as Mom finishes scooping food onto our plates."

    
    show mom angry2 with dissolve:
        align (0.5, 1.0)
    voice "5-3-76.mp3" #kaito
    mom "So, Alex, are you going to tell us what you were doing outside the house?"
    
    show bro sad2 with dissolve:
        align (1.0, 1.0)
    show lov confused2 with dissolve:
        align (0.75, 1.0)
    show dad neutral1 with dissolve:
        align (0.25, 1.0)
    "My brother doesn't reply. The air’s so thick I feel like I can suffocate in it."
    show sis worry2 with dissolve:
        align (0.0, 1.0)
    "Maria fidgets a little before looking up."
    
    voice "5-3-77.mp3" #amree
    sis "Umm... t-today at school, I made Mr. Potato."
    
    show lov shy1 with dissolve:
        align (0.75, 1.0)
    "Everyone ignores Maria, as usual."
    
    show mom sad3 with dissolve:
        align (0.5, 1.0)
    voice "5-3-78.mp3" #kaito
    mom "Alex, speak when you're spoken to."
    
    "The awkward silence continues for a moment. But only for a moment."
    
    show lov happy2 with dissolve:
        align (0.75, 1.0)
    voice "5-3-79.mp3" #starleeter
    lov "Mr. Potato? Who's that, Maria?"
    show sis happy1 with dissolve:
        align (0.00, 1.0)
    voice "5-3-80.mp3" #amree
    sis "Huh? Oh... uh... yes! Mr. Potato. He's a potato battery!"

    show lov happy2b with dissolve:
        align (0.75, 1.0)
    "Maria looks surprised and happy at the same time that someone is taking interest in her story."
    "Lauren laughs and nearly chokes on the stew."
    
    show dad smile1 with dissolve:
        align (0.25, 1.0)
    show bro smile2 with dissolve:
        align (1.0, 1.0)
    voice "5-3-81.mp3" #starleeter
    lov "You named your potato battery?"
    voice "5-3-82.mp3" #amree
    show sis happy2 with dissolve:
        align (0.00, 1.0)
    sis "He has two eyes, a nose and a mouth, too!"
    voice "5-3-83.mp3" #starleeter
    show lov happy1bh with dissolve:
        align (0.75, 1.0)
    lov "Hahaha~!"
    
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    "Mom looks annoyed, but she ignores Lauren and focuses her attention on Alex."
    
    show lov confused1 with dissolve:
        align (0.75, 1.0)
    show sis happy1 with dissolve:
        align (0.0, 1.0)
    voice "5-3-84.mp3" #kaito
    mom "Do you have anything to say for yourself, young man?"
    
    show bro angry1 with dissolve:
        align (1.0, 1.0)
    "Alex continues to ignore Mom as he eats his dinner."
    
    voice "5-3-85.mp3" #amree
    show sis worry1 with dissolve:
        align (0.0, 1.0)
    sis "Mr. Potato's ears are the terminals for the battery, but he doesn't work at all..."
    voice "5-3-86.mp3" #starleeter
    show bro sad2 with dissolve:
        align (1.0, 1.0)
    show lov happy1 with dissolve:
        align (0.75, 1.0)
    lov "Hahaha~! A lazy couch potato!"
    show dad smile2 with dissolve:
        align (0.25, 1.0)
    show mom sad3 with dissolve:
        align (0.5, 1.0)
    voice "5-3-87.mp3" #kaito
    mom "So your potato battery doesn't work, Maria?"
    
    "I look up at Mom and then at Maria."
    
    show sis happy1b with dissolve:
        align (0.0, 1.0)
    voice "5-3-88.mp3" #amree
    sis "Huh? Ummm... no... but the teacher likes my design so he gave me full marks anyway..."
    voice "5-3-89.mp3" #starleeter
    show lov happy2h with dissolve:
        align (0.75, 1.0)
    show bro smile2 with dissolve:
        align (1.0, 1.0)
    lov "Oooooh? A teacher's pet? Hahaha~! Go Maria!"

    show mom angry1 with dissolve:
        align (0.5, 1.0) 
    show dad neutral2 with dissolve:
        align (0.25, 1.0)
    show sis sad1 with dissolve:
        align (0.0, 1.0)
    show lov shy1 with dissolve:
        align (0.75, 1.0)
    show bro sad2 with dissolve:
        align (1.0, 1.0)
        
    "Mom suddenly slams the table, surprising everyone."

    voice "5-3-90.mp3" #kaito
    mom "Lauren."
    voice "5-3-91.mp3" #kaito
    mom "What do you think you're doing?"
    voice "5-3-92.mp3" #starleeter
    show lov shy2 with dissolve:
        align (0.75, 1.0)
    lov "Huh? What do you... did I say something wrong, Mrs. Westenson?"
    
    show dad sad1 with dissolve:
        align (0.25, 1.0)
    show sis sad2 with dissolve:
        align (0.0, 1.0)
    show bro sad1 with dissolve:
        align (1.0, 1.0)
    
    "It's like Lauren is only now noticing Mom's bad mood."
    
    voice "5-3-93.mp3" #kaito
    mom "You're praising her too much. The potato battery doesn't work."
    voice "5-3-94.mp3" #lacTheWatcher
    
    show sis worry1 with dissolve:
        align (0.0, 1.0)
    show dad sad2 with dissolve:
        align (0.25, 1.0)
    dad "Liz..."
    voice "5-3-95.mp3" #kaito
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    mom "Stay out of this, Jon."
    voice "5-3-96.mp3" #starleeter
    show lov angry1 with dissolve:
        align (0.75, 1.0)
    lov "I'm only making conversation with Maria..."
    voice "5-3-97.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.5, 1.0)
    mom "Well you're doing more than that. If Maria hasn't done anything worthy of praise, then we shouldn't praise her."
    voice "5-3-98.mp3" #starleeter
    show lov angry2 with dissolve:
        align (0.75, 1.0)
    lov "She's a kid, of course we should praise her. Any good parent would praise her!"
    
    show lov angry1 with dissolve:
        align (0.75, 1.0)
    show dad neutral2 with dissolve:
        align (0.25, 1.0)
    show sis sad2 with dissolve:
        align (0.0, 1.0)
    show bro sad2 with dissolve:
        align (1.0, 1.0)
    show mom surprise with dissolve:
        align (0.5, 1.0)
    
    "I hear a few gasps around the table."
    "Maria looks like she wants to be anywhere but here. I'm too far away to reach out and hold her hand."
    
    voice "5-3-99.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.5, 1.0)
    mom "What did you say? What do you know of parenting? You're just a child."
    voice "5-3-100.mp3" #starleeter
    show lov angry2h with dissolve:
        align (0.75, 1.0)
    lov "Yet I apparently know your daughters better than you."
    voice "5-3-101.mp3" #kaito
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    mom "What do you mean by that?"
    
    menu:
        "\"Please stop!\"":
            jump dinnerstop
        "Stay out of it.":
            jump dinnerout

###########################################

label dinnerstop:

    voice "5-3-102.mp3" #kaito
    mom "Quiet, Emily."
    voice "5-3-103.mp3" #starleeter
    lov "Don't talk to my friend like that!"
    voice "5-3-104.mp3" #potato
    pro "Lauren, please..."
    
    jump dinnerover

###########################################

label dinnerout:

    voice "5-3-105.mp3" #starleeter
    lov "Why don't you have a good look in the mirror and think about the answer yourself?"
    voice "5-3-106.mp3" #kaito
    mom "How dare you... who do you think you are?"
    voice "5-3-107.mp3" #starleeter
    lov "I'm Emily's friend."

    jump dinnerover

###########################################

label dinnerover:
    
    "Lauren's about to say something else. Her mouth is open, and her stance is combative..."
    show lov shy2b with dissolve:
        align (0.75, 1.0)
    "...But she stops when she sees my expression."
    
    show lov shy1b with dissolve:
        align (0.75, 1.0)
    voice "5-3-108.mp3" #starleeter
    lov "...I think I should leave."
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    voice "5-3-109.mp3" #kaito
    mom "Yes, you should."
    
    show dad sad2 with dissolve:
        align (0.25, 1.0)
    show sis sad2 with dissolve:
        align (0.0, 1.0)
    show bro sad1 with dissolve:
        align (1.0, 1.0)
    "Lauren says goodbye to Maria, Alex and Dad before looking over at me."
    
    show lov angry1 with dissolve:
        align (0.75, 1.0)
    voice "5-3-110.mp3" #starleeter
    lov "You gonna walk me to the door, Em?"
    
    "Mom's still sitting at the table, looking at me while waiting for my answer."
    
    voice "5-3-111.mp3" #potato
    pro "I'll... I'll see you later, Lauren."
    
    show lov shy2 with dissolve:
        align (0.75, 1.0)
    "Lauren looks hurt when I said that. But she leaves anyway, leaving us to ourselves."
    
    hide lov with dissolve
    
    show sis sad1 with dissolve:
        align (0.0, 1.0)
    
    "Maria's quietly looking down at her plate. Even Alex isn't eating."
    
    voice "5-3-112.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.5, 1.0)
    mom "So this is the type of friends you spend your time with, Emily?"
    voice "5-3-113.mp3" #lacTheWatcher
    show dad angry2 with dissolve:
        align (0.25, 1.0)
    dad "Liz, stop it."
    voice "5-3-114.mp3" #kaito
    show mom surprise with dissolve:
        align (0.5, 1.0)
    mom "Excuse me?"
    voice "5-3-115.mp3" #lacTheWatcher
    dad "Don't you think you've embarrassed our daughter in front of her friend enough today?"
    show bro angry2 with dissolve:
        align (1.0, 1.0)
    show mom angry1 with dissolve:
        align (0.5, 1.0)
    voice "5-3-116.mp3" #kaito
    mom "You're the one who invited her to dinner without consulting me!"
    voice "5-3-117.mp3" #lacTheWatcher
    show dad angry1 with dissolve:
        align (0.25, 1.0)
    dad "She's Emily's friend! It'll be rude not to! Besides, don't you want to know your daughter's friends?"
    voice "5-3-118.mp3" #kujira
    show bro angry2 with dissolve:
        align (1.0, 1.0)
    bro "Oh my god, will you two please just stop it?!"

    hide bro with dissolve
    show sis sad2 with dissolve:
        align (0.0, 1.0)
    show mom sad1 with dissolve:
        align (0.5, 1.0)
    show dad sad1 with dissolve:
        align (0.25, 1.0)
    "Alex stands up and angrily takes his dinner to his room."
    "I understand what he's feeling. I don't want to be here either."
    
    voice "5-3-119.mp3" #lacTheWatcher
    
    show dad sad2 with dissolve:
        align (0.25, 1.0)
    dad "Your brother's right. Sorry, Liz. I didn't mean to raise my voice."
    voice "5-3-120.mp3" #kaito
    show mom sad2 with dissolve:
        align (0.5, 1.0)
    mom "Hmph."
    stop music fadeout .5    
    "At least the fighting has stopped."

    scene bedroom night with dissolve

    "After we quietly finish the rest of our dinner, Maria and I go back to our rooms."

    voice "5-3-121.mp3" #potato
    pro "Oh... dammit."
    
    "Lauren forgot to take the sewing machine with her."
    "I sigh."
    "If Lauren doesn't fix this sewing machine in time, we'll never get the costumes she needs."
    "Guess I don't have a choice. Good thing Lauren doesn't live that far away."
    
    voice "5-3-122.mp3" #potato
    pro "Hap! Uph..."
    
    "It's not too heavy. I can totally do this."

    scene diningroom with dissolve

    show mom sad2 with dissolve:
        align (0.350, 1.0)
    show dad sad2 with dissolve:
        align (0.650, 1.0)
    "I leave my room and peek into the dining room."
    "Mom and Dad are washing up the dishes silently. Something's weird about it, but I can't put a finger on it."

    scene house dark with dissolve

    "Balancing the sewing machine on my thigh, I open the front door quietly. It's not until I close the door behind me that I release the breath I've been holding."
    
    voice "5-3-123.mp3" #potato
    pro "Okay. Let's go!"

    scene black with dissolve
    "15 minutes later..."
    
    jump day5s4