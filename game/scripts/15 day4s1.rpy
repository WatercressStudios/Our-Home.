label day4s1:

    scene bedroom 
    with dissolve
    "Sunlight pierces my eyes."
    "My body chills and shivers as blood rushes through my veins, thrusting me into the world of the living once more."
    "…Do I really have to wake up now?"
    "The effort to keep my eyelids open almost feels like too much, if not for the sunlight that bleeds into my vision and scrapes at my pupils." 
    "I get up from my bed and loosely stand on my own two feet. My muscles strain and ache as I stretch away whatever ill-fated weights once locked my shoulders in place." 
    "I grab my uniform, get dressed and get ready for school – it’s like an average, regular day, except my fingers are numb with pain and my back is in desperate need of a spa day."
    "I go outside and knock on my sister’s door before opening it."
    scene sisroom
    with dissolve
    show sis sad1
    with dissolve
    voice "4-1-1.mp3" #potato
    pro "Morning, sis."
    show sis sad1
    "Maria yawns and stretches into the air. She rubs her eyes trying to wake up."
    voice "4-1-2.mp3" #potato
    pro "How are you today, Maria?"
    show sis worry1
    sis "I wanna go back to sleep."
    "Her hair's a mess, and her face seems to hang in its expression like it hasn’t woken up yet."
    voice "4-1-3.mp3" #potato
    pro "Hey, stay right there for a moment okay? I’m gonna go grab something."
    show sis worry2
    sis "E-eh?"
    hide sis with dissolve
    scene bedroom with dissolve
    "I run back to my room to grab the plushie – placed on top of a shelf so it could be a worthwhile surprise."

    if not plushie:
        show plushie damage with dissolve
        "Yep. Absolutely perfect. No chance of breaking or falling apart because you had to finish it with a bunch of tape. Absolutely no blemishes because someone waited until the last minute to finish it."
        "Is what I want to tell myself while my brain panics with anxiety and nearly blows a hole in my head. Jesus Christ, what is this!? The color looks all wrong and the cotton is flimsy and cheap and the horn isn’t even shaped right and aaaAAAAH."
        "...No, no I’m overreacting. I can do this, I can do this."
        hide plushie damage with dissolve
    else:
        show plushie with dissolve
        "It’s…relatively normal. The soft color of the skin gives off a peach-like hue, the fabric is soft to touch, and the horns give off this weighty, bouncy feeling when you walk around with it."
        "Is this enough? It’s not spectacular at all. It feels like something you’d buy in a bargain bin because it didn’t sell well enough. Shouldn’t I be refining it? Is this good enough to give to her?"
        "…No, no. It’s fine. I won’t get anywhere if I’m stressing over this."
        hide plushie with dissolve
    scene hallway with dissolve
    "I sneak my way out of the room, hiding the plushie behind my back."
    voice "4-1-4.mp3" #potato
    pro "Maariaaa~"
    voice "4-1-5.mp3" #amree
    show sis worry1 with dissolve
    sis "Emily, w-what are you doing?"
    "She looks at me with a face of confusion."
    voice "4-1-6.mp3" #potato
    pro "Close your eyes."
    show sis sad2 with dissolve
    voice "4-1-7.mp3" #amree
    sis "I’m scared."
    voice "4-1-8.mp3" #potato
    pro "You don’t need to be."
    voice "4-1-9.mp3" #amree
    sis "B-but…"
    "She lowers her head and looks down towards the floor."
    voice "4-1-10.mp3" #potato
    pro "It’s alright. I’m giving you a surprise. Hold out your hands."
    show sis sad1b with dissolve
    "She closes her eyes and holds out her hands."
    voice "4-1-11.mp3" #amree
    show sis sad2b with dissolve
    sis "Is it candy?"
    "I take the plushie and place it in her hands."
    voice "4-1-12.mp3" #amree
    show sis sad1b with dissolve
    sis "I-is it cotton candy!?"
    voice "4-1-13.mp3" #potato
    pro "Nope."
    show sis happy1 with dissolve
    "She opens her eyes and squeezes at it."
    voice "4-1-14.mp3" #amree
    show sis happy2 with dissolve
    sis "Did…did you buy this for me?"
    voice "4-1-15.mp3" #potato
    pro "I made it."
    voice "4-1-16.mp3" #amree
    sis "You… you did?"
    show sis happy2b with dissolve
    "Her face flushes a bright red as she processes how much work must’ve gone into it."
    sis "E-E-Emily, you d-didn’t really have to go through this! I-It’s too much, honest!"
    voice "4-1-17.mp3" #potato
    pro "It’s a present! There’s never too much for something like this, right?"
    show sis worry2b with dissolve
    voice "4-1-18.mp3" #amree
    sis "B-but…"
    voice "4-1-19.mp3" #potato
    pro "It’s yours. You don’t need to feel guilty over it."
    voice "4-1-20.mp3" #amree
    show sis happy1b with dissolve
    sis "…Thank you, Emily."
    "She finally calms down, and a smile comes across her face."
    "Right! Time for the day to begin in earnest!"
    hide sis with dissolve
    if not plushie:
        show plushie damage with dissolve
        voice "4-1-21.mp3" #amree
        sis "A-aah, Emily!"
        voice "4-1-22.mp3" #potato
        pro "Yes, Maria?"
        voice "4-1-23.mp3" #amree
        sis "T-the tape fell off! W-what do I dooo…"
        "Oh, shit."
        voice "4-1-24.mp3" #potato
        pro "S-Set it down and I’ll fix it when I real quick, okay?"
        voice "4-1-25.mp3" #amree
        sis "Okay…"
        hide plushie damage with dissolve
        scene bedroom with dissolve
        "Rushing to my room, I grab some more tape to fix it up. I reapply it, hoping that it will stick long enough for a more permanent fix later."
        "I come back over to her, handing it back."
        scene hallway with dissolve
        show sis worry2 with dissolve
        voice "4-1-26.mp3" #potato
        pro "Sorry, I ran out of materials… I'll be sure to give it a real good fix later."
        show sis happy1 with dissolve
        "She nods, smiling at me."
        voice "4-1-27.mp3" #amree
        sis "I love it, even if it isn't perfect…"
    voice "4-1-28.mp3" #kaito
    show sis sad2 with dissolve
    mom "Emily! Maria! Are you done over there!?"
    voice "4-1-29.mp3" #potato
    pro "Coming, mom!"
    hide sis with dissolve
    
    scene livingroom with dissolve
    show mom angry1 with dissolve:
        align (0.250, 1.0)
    show bro sad1 with dissolve:
        align (0.500, 1.0)
    show sis worry2 with dissolve:
        align (0.750, 1.0)
        
    "Maria and I come down to the living room, with her carrying the plushie in her hands."
    if not plushie:
        "...and trying to keep the tape stuck in place."
    
    voice "4-1-30.mp3" #kaito
    mom "Children – breakfast will be late today. Someone drank the last of the orange juice and put it back in the fridge. You know how much that irks me, don't you?"
    show bro sad2 with dissolve:
        align (0.500, 1.0)
    show sis sad1 with dissolve:
        align (0.750, 1.0)
    "An audible gasp escapes Maria’s mouth and she looks to the floor in embarrassment."
    "Mother gazes at each of us. We remember Maria finishing it last night, but it isn’t worth bringing up."
    voice "4-1-31.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.250, 1.0)
    mom "I'm going to the store. I’ll be back in five minutes – Emily, you’re responsible for getting them ready when I’m out."
    voice "4-1-32.mp3" #potato
    pro "Yes, Mom."
    hide mom with dissolve
    "She rushes out the door, and we’re left to our own."
    show bro sad1 with dissolve:
    show sis worry1 with dissolve:
        align (0.750, 1.0)
    "Five minutes. Five minutes until she gets home."
    voice "4-1-33.mp3" #potato
    pro "Better kick our asses into high gear…"
    hide sis with dissolve
    "Maria runs off to return her plushie to her room. Alex lays down on a nearby chair."
    "Barely dressed, his uniform worn like a toddler wears his dinner. A pair of socks lay abandoned on the floor."
    voice "4-1-34.mp3" #potato
    pro "Alex, could you put your shoes on? We’ve gotta get ready soon."
    
    show bro sad2 with dissolve
    voice "4-1-35.mp3" #kujira
    bro "Ugh, I'm exhausted, got a headache… could you turn your voice down just a little."

    voice "4-1-36.mp3" #potato
    pro "Hey, I'm not thrilled about this either, but if Mom catches you in that state, it's me she's gonna ream out."

    show bro smile2 with dissolve
    voice "4-1-37.mp3" #kujira
    bro "Five minutes is plenty of time. Relax."

    voice "4-1-38.mp3" #potato
    pro "That wasn't a request, though…" 

    show bro smile1 with dissolve
    voice "4-1-39.mp3" #kujira
    bro "Pfft, what? Who the hell made you the boss of me?"
    
    voice "4-1-40.mp3" #potato
    pro "Uhhh… Mom did, technically."

    show bro smirk2 with dissolve
    voice "4-1-41.mp3" #kujira
    bro "News to me…" 

    "He groans, rising to his feet, stretching himself out."

    show bro sad1 with dissolve
    voice "4-1-42.mp3" #kujira
    bro "Ugh, groggy as shit…"

    voice "4-1-43.mp3" #potato
    pro "How late were you up…?"

    show bro sad2 with dissolve
    voice "4-1-44.mp3" #kujira
    bro "I was doing important shit, alright? Burning midnight oil on a group project for school."

    voice "4-1-45.mp3" #potato
    pro "...Really."

    show bro smile1 with dissolve
    voice "4-1-46.mp3" #kujira
    bro "You could look a little less skeptical. Someone in the family has to give a shit about their grades."

    voice "4-1-47.mp3" #potato
    pro "You look like shit, though. How are you going to survive classes?"

    show bro smirk2 with dissolve
    voice "4-1-48.mp3" #kujira
    bro "Just gotta show up. I got it." 

    voice "4-1-49.mp3" #potato
    pro "If you got off that stupid shit you've been doing, it'd be easier to get through the day."

    show bro angry1 with dissolve
    voice "4-1-50.mp3" #kujira
    bro "Hey, screw off, alright? I already got Mom breathing down my neck about everything I do, and I don't need a second pair of eyes on me at all time, alright?"

    voice "4-1-51.mp3" #potato
    pro "...What?"

    "Why is Alex so angry now? He's been so agitated all of the time lately! What happened?"
    "...What a stupid question. Of course I know what happened."

    voice "4-1-52.mp3" #potato
    pro "This stuff is messing with your head, okay? We're just… worried."

    show bro smirk1 with dissolve
    voice "4-1-53.mp3" #kujira
    bro "Shut up. Just, shut up. You ever stop to think that maybe, just maybe, it's you dense idiots that's the problem?"

    voice "4-1-54.mp3" #potato
    pro "Wh, what'd I do...?"

    show bro angry2 with dissolve
    voice "4-1-55.mp3" #kujira
    bro "Ugh, you dense idiot, you're giving me that look again! You pity me, don't you!?"

    voice "4-1-56.mp3" #potato
    pro "No, that isn't it! You need to stop taking this stuff!"

    voice "4-1-57.mp3" #kujira
    bro "What the fuck are you talking about!? You only act like you care when you're trying to win an argument!"

    show bro smirk1 with dissolve
    voice "4-1-58.mp3" #kujira
    bro "You hole up in your room and abandon me while I have to deal with mom! Why the fuck do you get to run away when I'm getting fuckin' yelled at for it!?"

    show bro sad2 with dissolve
    voice "4-1-59.mp3" #kujira
    bro "You're a fuckin' hypocrite! Don't take the moral high ground just when it's convenient for you!"
    
    "As Alex continues to go full blast, Maria is poking her head out of her room. The look of terror on her face makes this all the more heart wrenching."

    voice "4-1-60.mp3" #amree
    sis "Guys, please don't fight…"
    show bro smirk 1 with dissolve
    voice "4-1-61.mp3" #kujira
    bro "Not now, Maria!"
    voice "4-1-62.mp3" #potato
    pro "Hey, don't yell at her, she's got nothing to do with this!"
    show bro angry1 with dissolve
    voice "4-1-63.mp3" #kujira
    bro "Then she should mind her own damn business! What's with this family!? Bunch of goddamn snoops…"

    hide sis with dissolve
    "Maria retreats back into her room."
    "That's it, I'm at the end of my patience with this prick today."

    voice "4-1-64.mp3" #potato
    show bro sad2 with dissolve
    pro "Fine! Do whatever! Do all the shit you want, have an overdose for all I care! It'd be one less thing I'd have to worry about!"
    voice "4-1-65.mp3" #kujira
    show bro grin1 with dissolve
    bro "Go hide in your cave, see if I care!"
    voice "4-1-66.mp3" #kaito
    show mom angry2 with dissolve: 
        align (0.250, 1.0)
    mom "What the hell is all this commotion!?"

    show bro sad2 with dissolve
    "All of us freeze in abject terror."
    "Five minutes. That's all we had."
    "She's scanning our expressions, glowering as she does."

    show mom angry1 with dissolve: 
        align (0.250, 1.0)
    voice "4-1-67.mp3" #kaito
    mom "...Did I not give you five minutes to be out the door?"

    "A stunned silence hangs over the house. Her mouth curls into a grimace."

    show mom angry2 with dissolve: 
        align (0.250, 1.0)
    voice "4-1-68.mp3" #kaito
    mom "...Well? Get out!"

    hide mom
    with dissolve
    hide bro
    with dissolve
    scene black
    with dissolve
    "As if hit by an electric shock, all three of us spring into motion."

    scene siswalk with dissolve
    
    "The air feels heavy as we begin our usual march towards schools. My brother breaks off quickly, not even bothering to say goodbye."
    "I remember that's not the usual route he's supposed to take, but I shake my head. I can't be bothered to deal with him right now."

    show sis sad1 with dissolve
    voice "4-1-69.mp3" #amree
    sis "Um… wh, what happened with you guys."
    voice "4-1-70.mp3" #potato
    pro "Not today, Maria. I really don't want to talk about it right now…" 
    voice "4-1-71.mp3" #amree
    show sis sad2 with dissolve
    sis "I… okay, sorry."
    voice "4-1-72.mp3" #potato
    pro "It's fine. I'm sorry too."

    "Our commutes were usually so pleasant and energetic."
    "Today, there's only the sound of footsteps. The sky above grey and overcast."
    "Dreary. Might rain. Yeah… feels about right."
    "...I feel awful. I can't even look Maria in the eye right now."

    jump day4s2
