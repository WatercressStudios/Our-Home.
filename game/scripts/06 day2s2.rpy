label day2s2:

    scene house with dissolve
    play ambience suburb fadein 2.0

    "I rock back and forth on my heels, rubbing my sides to keep warm in this chilly morning air."
    
    voice "2-2-1.mp3" #potato
    pro "Hurry up! You're going to be late!"

    play sound slamdoor
    "I yell into the house through the front door, hoping Maria will hurry her little ass up. The door slams as she rushes out, slinging her bag onto her back as she goes."

    play music bgmsis fadeout 1.0 fadein 0.0

    show sis worry1
    with dissolve 
    
    voice "2-2-2.mp3" #amree

    sis "S-sorry! Got distracted…"

    voice "2-2-3.mp3" #potato
    pro "Uhh, by what?"
    
    show sis worry2
    voice "2-2-4.mp3" #amree

    sis "Nothing in particular."

    voice "2-2-5.mp3" #potato
    pro "Suuure."

    scene siswalk with dissolve
    
    voice "2-2-6.mp3" #amree
    sis "So, are you excited for school?"

    voice "2-2-7.mp3" #potato
    pro "Are you?"

    show sis sad2
    voice "2-2-8.mp3" #amree
    sis "Not exactly…"

    voice "2-2-9.mp3" #potato
    pro "Yeah. I'm glad I'm almost done with it."

    "I'm lying, of course. I mean, I don't like school, but I don't like the prospect of what comes after it, either. To be frank, I'm not excited about any bit of anything right now."

    show sis happy1
    voice "2-2-10.mp3" #amree

    sis "Ahh, that's true. You're almost all grown up!"

    voice "2-2-11.mp3" #potato
    pro "You could say that, I guess."


    show sis happy2
    voice "2-2-12.mp3" #amree

    sis "Yeah! You're super old now."

    voice "2-2-13.mp3" #potato
    pro "Thanks?"


    show sis worry2b
    voice "2-2-14.mp3" #amree

    sis "I mean, no, uhh…"

    "She hides her face, failing to find the right words."


    show sis happy1b
    voice "2-2-15.mp3" #amree

    sis "You're a grownup now. Like Mom."

    "I stifle a cough."

    voice "2-2-16.mp3" #potato
    pro "I sure hope not."


    show sis worry1
    voice "2-2-17.mp3" #amree
    sis "I-I guess."


    voice "2-2-18.mp3" #amree
    sis "Hey... Emily?"

    voice "2-2-19.mp3" #potato
    pro "Yeah?"


    show sis worry2
    voice "2-2-20.mp3" #amree
    sis "Do you love Mom?"

    "Agh, Maria, why do you always have to ask the hard questions? First thing in the morning, too..."

    menu:
        "Of course I love her.":
            jump day2s2love

        "I-I think I do.":
            jump day2s2nolove

label day2s2love:
    voice "2-2-21.mp3" #potato
    pro "Yeah, I love her. She's not a perfect person, but no one is… I think."

    voice "2-2-22.mp3" #potato
    pro "She's human, and despite her flaws, she's our mother."


    show sis happy1
    voice "2-2-23.mp3" #amree

    sis "I-I think that makes sense…"
    jump day2s2movingon
    
label day2s2nolove:
    voice "2-2-24.mp3" #potato
    pro "I think? It's hard to say. She's not… she's not what I wish she'd be. I… I'm not sure."
    
    show sis sad2

    "Maria frowns, and doesn't respond. I'm not sure exactly what she was expecting. It's our mother. She's a terrible human being, even if she has some good parts to her. She's too far gone."
    jump day2s2movingon

label day2s2movingon:
        
    #SCENE CHANGE
    hide sis
    with dissolve 
    
    scene sisschool with dissolve

    "The rest of the walk is relatively uneventful, and I make my way to my own school after I've dropped Maria off."

    stop music fadeout 5.0

    scene siswalk2 with dissolve

    "I kinda like the walks I take. I have a set endpoint, and there's nothing interfering with me along the way. Sure, the anxiety of class isn't the best thing in the world, but it's like the calm before the storm."
    "I get some peace and quiet. Not much of my life's quiet nowadays, since I'm almost always surrounded by people. Most of the people aren't exactly star citizens, either."
    "While I do hate school with a passion, at least I have a friend there. One single friend, but a friend nonetheless."
    "Speaking of, I wonder if she'll make it to class today? She's been awfully busy with the play."
    "I guess I'll have to wait and see."  
    
    #SCENE CHANGE
    scene schoolhallway with dissolve

    play ambience crowd fadeout 1.0 fadein 1.0

    "I arrive at the school, moving quickly towards the senior lockers - Lauren'll be nearby, surely. We have a habit of meeting up before class, and it always brightens my day."
    "Okay. I need to wake up. I've practically been dragging myself through the motions this morning, and I'd rather not 'go through the motions' with Lauren. That'd be a disservice."
    "I move past the huddled masses, weaving through the waves of students that occupy this part of the school every morning."
    "I skip right by my locker, carrying everything I need with me."
    "In the distance, I see it."
    "The bright red hair, the slightly risque uniform, the bright blue eyes. She spots me and waives enthusiastically."
    
    play music bgmlov fadeout 1.0 fadein 0.0

    show lov happy
    with dissolve
    
    voice "2-2-25.mp3" #starleeter


    lov "Heya, Emily! How's it going?"

    "I wave back at her, cringing all the way. She always has to make a spectacle, and I'm forced try to avoid the glares that undoubtedly come my way."

    voice "2-2-26.mp3" #potato
    pro "Shh, Lauren, not so loud…"
    
    show lov shy2

    voice "2-2-27.mp3" #starleeter
    lov "Oh, you spoilsport."

    voice "2-2-28.mp3" #potato
    pro "So, are you having theater today?"
    
    show lov happyh

    voice "2-2-29.mp3" #starleeter
    lov "Yes! We're getting ready for our next play! So, uhh, I won't be in class today. Sorry!"

    voice "2-2-30.mp3" #potato
    pro "Eh, I expected it."
    
    show lov angry

    "She pouts, poking me in the cheek."

    voice "2-2-31.mp3" #potato
    pro "Hey-"
    
    show lov happy2h

    voice "2-2-32.mp3" #starleeter
    lov "Stop that. Class isn't that long anyways. Meet me after, promise?"

    voice "2-2-33.mp3" #potato
    pro "Yeah, yeah."
    
    show lov happy

    voice "2-2-34.mp3" #starleeter
    lov "Okay, sweet! I'll catch you after class then!"

    voice "2-2-35.mp3" #potato
    pro "Off so early?"

    voice "2-2-36.mp3" #starleeter
    lov "Ya know it! Gotta help set up before, of course. See ya!"

    voice "2-2-37.mp3" #potato
    pro "Alright, later."
    
    hide lov
    with dissolve

    stop music fadeout 2.0

    "As she scampers off, I linger a bit at her locker, leaning against it."
    "Agh, screw class. I'm not thrilled at all for this. It's been a crummy few days, and I feel like I'm in molasses."
    "Even my thoughts are slow, dragging on today."
    "...But I have to go anyways. I don't want to deal with the blowback of yet another absence. Mother would kill me."    
    "Well, that'd probably be preferable to the alternative."

    scene classroom with dissolve
    stop ambience fadeout 0.5

    "Oh well. I suck it up and make my way into the classroom, making sure to avoid any and all human interaction on the way. I'm not exactly the most popular person here."
    "Sitting down, I pull out my class supplies, including the books that weigh down my bag."
    "Shortly thereafter, the teacher walks in, and the lesson begins."

    jump day2s3
