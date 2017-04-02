label day2s3:
    
    $ teaconcern = False

    scene classroom with dissolve

    #music used in this scene should be pretty chill, lowkey. Potentially use of percussion drums and bass guitar. Musicians can have fun with this one?

    voice "2-3-1.mp3" #skinimini
    tea "...Now that we are a few weeks into our required reading, I trust many of you have taken the requisite time to digest the chapters from our assigned readings."
    voice "2-3-2.mp3" #skinimini
    tea "While the choice of {i}Nineteen Eighty Four{/i} is a rather… interesting pick from the school board, I find many of you will come out of this inspired."
    voice "2-3-3.mp3" #skinimini
    tea "We're going to learn a lot from this round-table, I can feel it."

    "I slump further back in my chair. Round table is an absolute slog, and a waste of time for everyone involved." 
    "A shredded newspaper left on the bus would be more well-read than most of my classmates." 

    voice "2-3-4.mp3" #skinimini
    tea "Now, can anyone tell me something about Winston?"

#     voice "2-3-5.mp3" #all #probably not going to record this one
    all "..."
    voice "2-3-6.mp3" #skinimini
    tea "...Well don't all jump up at once, now."

    "We've done this same song and dance for a while now. Dead silence until someone decides to bite the bullet."
    "And it just drags everything out even longer. I just want to get out of here and go home…"

    "...Wait, fuck, do I really want to go back? This morning was a mess..."
    "Ugh, get up, head up. She's getting back to the lesson. Just gotta go through the motions."
    "It's the last class of the day, so of course it has to drag like this."

    voice "2-3-7.mp3" #skinimini
    tea "...Fine, I'll call someone's name. Emily, would you like to start us off?"
    voice "2-3-8.mp3" #potato
    pro "...Huh? Uh… right..."

    "Winston, he was the protagonist, right? He…"

    menu: 

        "He's terrified.":
            jump day2s3terrified

        "He's gloomy.":
            jump day2s3gloomy

        "He's relatable.": 
            jump day2s3relatable

label day2s3terrified: 
    voice "2-3-9.mp3" #potato
    pro "He's terrified of his surroundings, and really of the power of The Party."
    jump day2s3normal

label day2s3gloomy:
    voice "2-3-10.mp3" #potato
    pro "He's gloomy, because he doesn't think there's much of a future to look forward to."
    jump day2s3normal

label day2s3relatable:
    $ teaconcern = True
    voice "2-3-11.mp3" #potato
    pro "He's kind of relatable, in his thinking. I… guess a lot of people have a lot to be afraid of, lately. Hard to be optimistic."
    jump day2s3concern

label day2s3normal:
    voice "2-3-12.mp3" #skinimini
    tea "Yes, that's an apt start. Thank you, Emily."

    "I relax back in my seat as the teacher resumes her lesson. Somebody had to take one for the team, I guess that just had to be me."

    jump day2s3lecture

label day2s3concern:
    "I think I might've said a little too much. Or maybe it was something on my face?"
    "Either or, she gives me a momentary look of almost palpable pity."

    voice "2-3-13.mp3" #skinimini
    tea "...Mm, true enough. Politics as they are right now are, well, difficult, all things considered…" 

    "She turned her back and headed back to the front to continue her lecture."

    jump day2s3lecture

label day2s3lecture:

    voice "2-3-14.mp3" #skinimini
    tea "Winston as a character is, well, best described as a fatalist."
    voice "2-3-15.mp3" #skinimini
    tea "Fear encompasses all of his actions, fear borne from an environment of Orwellian social conditioning and psychological manipulation."
    voice "2-3-16.mp3" #skinimini
    tea "The world of {i}Nineteen Eighty Four{/i} is dark, and in the lens of our protagonist, it gets gloomier still…"

    "The lecture goes on. Ms. Reynolds talked big and knew her stuff, and it was better to take her view on things compared to the rest of the class."
    "I should probably be taking more notes, but… I already know this stuff. So long as I threw together reports, she didn't care."
    "Not like there were really any revelatory truths anyway. Shit sucks when fascists take power, what else is new?"

    scene black with dissolve

    "... ... ..."

    scene classroom with dissolve

    #play sound schoolbell

    "DOO DO DOO DO!"

    voice "2-3-17.mp3" #potato
    pro "Finally…" 

    "The anxious bodies in the classroom all rush to the door like the wildebeest."
    "I take my sweet time rising from my chair. I'm not exactly in any rush."

    voice "2-3-18.mp3" #skinimini
    tea "Oh, Emily, do you have a minute?"
    voice "2-3-19.mp3" #potato
    pro "Huhwhat?"
    voice "2-3-20.mp3" #skinimini
    tea "I got some notes for Lauren, could you deliver them to her?"
    voice "2-3-21.mp3" #potato
    pro "I, uh…"
    voice "2-3-22.mp3" #skinimini
    tea "You're friends with her, right? She can't make my lessons often, so I figured you could be of help here."

    voice "2-3-23.mp3" #potato
    pro "Oh. Sure, fine, whatever."
    voice "2-3-24.mp3" #skinimini
    tea "Thanks,  she's over with the drama department, as usual."

    "She pushes a folder towards me. It was heavier than I expected. Really packed it all in, didn't she…?"

    if teaconcern == True:
        voice "2-3-25.mp3" #skinimini
        tea "Oh yeah, and if you need to talk to someone, I'm a good listener."
        voice "2-3-26.mp3" #potato
        pro "...Thanks?"

    "I can't say I'm privy to being used as someone's gopher here, but it's not like I have much else to do right now."
    "I don't think I used the right tone with Reynolds either. Did I sound annoyed? I didn't want to give her attitude, but…"
    "Well, let's get going."

    ##SCENE CHANGE
    scene schoolhallway with dissolve
    
    "... ... ..."

    ##SCENE CHANGE
    scene drama with dissolve

    "There's a lot of energy in this room. The choreographer's running a group of maybe a dozen juniors through a series of motions."
    "They don't look in sync yet. It's a little exhausting to look at. Don't think I'd be cut out for that."

    voice "2-3-27.mp3" #potato
    pro "Alright, where is she in here…" 

    "There's a ton of moving bodies, scampering here and there. Some are messing with large sheets of wood in the back."
    "Others huddle up, highlighters aimed at bundles of pages. I guess they're scripts?"
    "The air hangs heavy with the smell of B.O. and paint."

#     show cg_LIdrama1 with dissolve
    #LI with a clipboard, talking with classmates
    show lov happy2 with dissolve

    "Oh, there she is. Her stark red hair's pretty hard to miss. Done up neatly in a ponytail."
    "Her uniform's pretty ruffled up too. Guess she's been at this for a while."
    "Still smiling, though. How does she get anything done with all these distractions??" 

#     show cg_LIdrama2 with dissolve 
    #same as above, but looking directly at reader and smiling
    show lov happyh with dissolve

<<<<<<< HEAD
#     voice "2-3-28.mp3" #starleeter
=======
#    voice "2-3-28.mp3" #starleeter silence
>>>>>>> 715d1fd704f25b0a15f5e9ee57ad9351cd1d6bfc
    lov "...?"

    "Oh, she saw me. What's that look she's giving me?"
    
    "...She's coming over…!"

#     hide cg_LIdrama2 with dissolve
    
    show lov confusedh
    with dissolve 
    voice "2-3-29.mp3" #starleeter
    lov "Emily! What're you doing here?"
    show lov happyh
    voice "2-3-30.mp3" #starleeter
    lov "Oh, and happy birthday!~"
    voice "2-3-31.mp3" #potato
    pro "Whoa, Lauren, you remembered? Gee, thanks. How're you?"
    voice "2-3-32.mp3" #starleeter
    show lov happy
    lov "Pretty good, pretty good! I hope you weren't looking to audition, the casting calls were wrapped up a while ago."
    voice "2-3-33.mp3" #potato
    pro "Nah, not quite, acting isn't really for me. Ms. Reynolds wanted me to, uh, deliver some notes to you. For our English class?"

    "Raising the folder to my chest, I catch Lauren looking over the folder incredulous, before reaching forward to take it."
    "Opening it up, she began to thumb through it." 

    show lov shy
    lov  "Lesse… oh, hm…!"
    voice "2-3-34.mp3" #potato
    pro "You look concerned."
    
    show lov shy2
    voice "2-3-35.mp3" #starleeter
    lov "Oh, no, it's just, ah, extra credit. My attendance mark in that class is gonna hurt a lot, so… I asked if there was something else I could do."
    voice "2-3-36.mp3" #starleeter
    lov "It's just some extra lil' short stories, I'll be okay!"
    voice "2-3-37.mp3" #potato
    pro "What about the other assigned reading, though?"

    show lov confused2bh
    voice "2-3-38.mp3" #starleeter
    lov "Wh-what other assigned reading?"
    voice "2-3-39.mp3" #potato
    pro "...{i}Nineteen Eighty Four{/i}? There's class talks and everything."
    show lov shy2b
    voice "2-3-40.mp3" #starleeter
    lov "Ohhhh, I forgot! I've been really busy over here, I hadn't even opened it at all!"
    voice "2-3-41.mp3" #starleeter
    show lov shyb
    lov "I've been so busy with the show and the rehearsals and… I just got the script, I've been pouring over that!"
    voice "2-3-42.mp3" #potato
    pro "Yo, it's okay, you aren't missing much. Don't think anyone else read much does much in our class either."
    show lov happy2
    voice "2-3-43.mp3" #starleeter
    lov "Oh? I see..."
    show lov happy
    voice "2-3-44.mp3" #starleeter
    lov "Alright! Grading curve's gonna bail me out of this one!~"
    voice "2-3-45.mp3" #potato
    pro "...I guess that's one way to see it."

    "Poor Lauren. Horrendously overworked, as per usual, but she keeps her chin up, somehow."
    voice "2-3-46.mp3" #potato
    pro "So, uh… what are you doing in here? I guess you got a role?"
#    voice "2-3-46_2.mp3" #starleeter recording
    lov "Oh, they gave me a huuuge role! We're doing {i}Bye Bye Birdie{/i} this year, and I got one of the lead roles!"

    hide lov
    with dissolve
    
    "Lauren bent over to lift the script she had left on the carpet, rustling the sheets as she did."
    "That was, uh… a big script. At least a hundred pages."

    show lov happy
    with dissolve
    voice "2-3-47.mp3" #starleeter
    lov "See, look, look! I'm Rose, the secretary! I have all my lines highlighted!"

    voice "2-3-48.mp3" #potato
    pro "Wow, that's uh… that's a lot of lines. Lots of highlighter too."
    voice "2-3-49.mp3" #starleeter
    lov "Mmhm! I'm using different colours to note the mood I'm going for! Happy, sad, mad… y'know!"

    "The highlighter stroked had bled through to the opposite side of the pages. She must've been really excited."
    "I'm getting overwhelmed just flipping through this script. She was out of her mind."

    voice "2-3-50.mp3" #potato
    pro "Must be a lot of work if it's something you have to miss class for, though…"
    
    show lov happy2
    voice "2-3-51.mp3" #starleeter
    lov "Ahhh, well, I wanna go into acting school after this, so I feel this'd be way better for me."
    
    show lov happy
    lov "There's never any shortage of things to do… oh, Em, could you help me rehearse a bit??"
    voice "2-3-52.mp3" #potato
    pro "Rehearse? What? I'm not an-"
    show lov happy2
    voice "2-3-53.mp3" #starleeter

    lov "I just need to try to remember my lines a bit. Can you be Albert?"
    voice "2-3-54.mp3" #potato
    pro "I, uh, hadn't thought of being a guy before, but… I'll give it a try."
    show lov happy2h
    voice "2-3-55.mp3" #starleeter

    lov "Just read his lines! Lemme flip tooooooo… ah, here we are!"
    
    hide lov
    with dissolve

    "I narrow my eyes to look at the passage she wants me to go over. Well, here goes nothing…"

    voice "2-3-56.mp3" #potato
    pro "'My pills, where are my pills. The little white ones I take when I'm overwrought.'"

    "In the corner of my eye, I see her lips pursing. Was I not putting my all into it? I said I wasn't much of an actor…"
    "In contrast to my stiff demeanor, her arm flows forward like a woven thread and… hangs it in front of me."

    show lov happy
    with dissolve 
    voice "2-3-57.mp3" #starleeter

    lov "'Here.~'"

    "Oh, am I supposed to take… 'it'? Sure, whatever."
    show lov happy2
    "...Wait, not quite."

    voice "2-3-58.mp3" #potato
    pro "'Not so much, break it in half.'"
    voice "2-3-59.mp3" #starleeter
    show lov angry2

    lov "'You're thirty-three years old, {i}Albert{/i}. You can take a whole aspirin, right?'"

    show lov happy2b
    "She winked as she spoke this. That wasn't in the script. She was already making her own flourishes. Wonder what the director would have to say about that."

    show lov happy2
    voice "2-3-60.mp3" #potato

    pro "'I'm not thirty-three. I'm a long way from thirty-three. I won't be turning thirty-three until tomorrow… u-uh, water?'"

    "I guess I should've shouted that, but I was feeling weird about this whole thing. Lauren was already at the ready with an invisible glass of water."

    voice "2-3-61.mp3" #potato
    pro "(What?)"
    show lov confused 
    voice "2-3-62.mp3" #starleeter
    lov "(It's a glass of water.)"
    voice "2-3-63.mp3" #potato
    pro "(I was, uh, a little thirsty, maybe you could...)"
    voice "2-3-64.mp3" #starleeter
    show lov shy2h
    lov "(Can't you just pretend a lil' bit longer for meee…?)"

    "Her pouty face's enough for me to crack up a bit. I take the pretend water glass, pretending to pound it back."
    "The pretend water, pretending to be refreshing, would have to do for now. I raise my pretend glass in pretend cheer."
    show lov happy2
    "More refreshing is the chuckle I got out of her from that pretend gesture."

    show lov angry
    voice "2-3-65.mp3" #starleeter

    lov "'It's no use, Albert, my mind's made up. I've been with Alme… Almater… Alma mater…?'"
    voice "2-3-66.mp3" #potato
    pro "...It's, uh, Almaelou."
    show lov shyh
    voice "2-3-67.mp3" #starleeter
    lov "Ahhh, shoot, I always bungle that one…" 
    show lov confused2h
    voice "2-3-68.mp3" #starleeter
    
    lov "...'F-for eight years now! A-and you well know, I've been a lot more than a secretary to you!'"
    voice "2-3-69.mp3" #potato
    pro "Little shaky on that last one, wanna go again?"
    
    voice "2-3-70.mp3" #other
    cho "Hey, Lauren, can I see you for a bit? Need to work on steps!"

    show lov confusedh
    voice "2-3-71.mp3" #starleeter

    lov "Oh, be right over Katie, just gimme a moment!"

    "Her eyes locked with mine. She must be in a rush."


    show lov shy
    voice "2-3-72.mp3" #starleeter

    lov "H-hey, Em, I just wanted to ask you for a big favour, could you help me out?"
    voice "2-3-73.mp3" #potato
    pro "Uh, sure, what's up?"

    show lov shy2
    voice "2-3-74.mp3" #starleeter

    lov "It's just, you make clothing right?"

    "Huh? That came out of left field…"

    menu: 

        "I'm pretty good, yeah.":
            jump day2s3ocelot

        "I'm pretty rusty.":
            jump day2s3rusty

        "Talk about Halloween plans.":
            jump day2s3halloween

label day2s3ocelot:
    voice "2-3-75.mp3" #potato
    pro "Yeah. Done it as a hobby for a while now, got a sewing machine at home. What'd, you need something…?"

    show lov happy
    voice "2-3-76.mp3" #starleeter

    lov "Yeah! You think you could help me?"
    jump day2s3favour

label day2s3rusty:
    voice "2-3-77.mp3" #potato
    pro "I dunno if I could help you much, I'm pretty rusty and, ah, out of practice…"
    show lov happy2
    voice "2-3-78.mp3" #starleeter

    lov "Oh, I think you'll do just fine! Here, lemme explain…"
    jump day2s3favour

label day2s3halloween:
    #Placeholder, want it to be funny
    $ halloween = True
    voice "2-3-79.mp3" #potato
    pro "Yeah, I was thinking about my Halloween costume. I was gonna go for a velociraptor."
    voice "2-3-80.mp3" #starleeter
    show lov confusedh

    lov "A velociraptor??"
    voice "2-3-81.mp3" #potato
    pro "A sexy velociraptor."
    show lov shy2bh
    voice "2-3-82.mp3" #starleeter

    lov "WOW, um… not… {i}quite{/i} what I had in mind, haha!"
    "Her cheeks lit up like Christmas decorations. It's fun to rile her up."
    jump day2s3favour


label day2s3favour:
    voice "2-3-83.mp3" #starleeter
    show lov confused2h

    lov "I was hoping you could help me a bit with the costume design for the show, um..."
    voice "2-3-84.mp3" #starleeter
    lov "We need a series of, like, fifties inspired costumes, and I think you'd have a better eye for costume design for me.."
    show lov happy2
    voice "2-3-85.mp3" #starleeter

    lov "So, ah, could we meet up in the library sometime this week! I wanna do some research and get some of your opinions!"
    voice "2-3-86.mp3" #potato
    pro "Wait, you're overseeing costumes too?"
    voice "2-3-87.mp3" #starleeter
    show lov happy

    lov "Haha, I, well, seem to be seeing over a lot of things… everyone's relying on me, so I can't let them down. You'll help me out, right?"

    show lov happy2
    "I feel a bit conflicted, honestly. She's putting herself in a bad spot here, and dragging me with her, but…"
    "I can't really leave her to do this alone, can I?"

    menu: 

        "Accept with grace":
            $ love += 1
            $ career += 1
            jump day2s3grace

        "Decline":
            jump day2s3decline

label day2s3grace:
    voice "2-3-88.mp3" #potato
    pro "Yeah, sure, anytime. Text me if you need me. I could even make an outfit, if you needed me to."

    show lov happy
    voice "2-3-89.mp3" #starleeter

    lov "Omigosh, thank you {i}so much,{/i} Emily! That'd be a huge help! I knew I could count on you!~"
    jump day2s3accept

label day2s3decline:
    voice "2-3-90.mp3" #potato
    pro "I mean, it looks like a nice bunch of people, but I… I'm not sure I can…"

    show lov shy2
    voice "2-3-91.mp3" #starleeter

    lov "...?"
    voice "2-3-92.mp3" #potato
    pro "..."
    "...Curse Lauren. She's giving me that damn pouty face again. I know she's not actually heartbroken, but it's like dealing with a puppy."
    lov "...Alright, I'll do it… I guess you'd need an outfit too, right?"

    voice "2-3-93.mp3" #starleeter
    show lov happy

    lov "YAAAAY!~ Thank you!!~~~"
    "I couldn't say no. I couldn't. Ugh, what'd I get myself into…"
    jump day2s3accept

label day2s3accept:
    voice "2-3-94.mp3" #starleeter
    lov "I'll call you later with more details, okay? They need me over with the dancers right now."

    voice "2-3-95.mp3" #starleeter
    show lov happy2
    lov "Thanks again for bringing me my notes too!"
    "She wrapped her arms around me and gave me a tight squeeze. I could feel the life getting squeezed out of my diaphragm!"
    voice "2-3-96.mp3" #potato
    pro "OH! Ah, n-no problem, Lauren. J-just text me to talk when you're free."

    show lov happy
    voice "2-3-97.mp3" #starleeter

    lov "Mmhm! See ya later!~"

    hide lov
    with dissolve
    
    "We part ways, she bouncing over to the rest of the energetic, rowdy crowd, and myself towards the door."
    
    #SCENE CHANGE
    scene schoolhallway with dissolve
    
    "I'm getting mixed feelings about this whole thing. She might've dragged me into this, somewhat, I guess, but… she's nice to be around. It won't be all bad."
    "I reach into my pocket, grabbing my phone. Kind of a reflexive tic when I'm alone, I guess."
    "Let's check our messages, uh… oh."

    voice "2-3-98.mp3" #potato
    pro "'Family dinner tonight. Don't be late getting home.' To the point as always, mom…"

    "I pocket the phone, letting out an exhausted sigh. Why a family dinner today of all days?"
    "Is this about my birthday? The text's from maybe an hour ago."
    "Did she {i}just{/i} realize it? She'll probably act like she said, 'Happy birthday!' this morning, as if she remembered."
    "Ugh... the best birthday gift they could've given me is to leave me the hell alone. Thinking about this shit is already putting me in a bad mood..."

    scene black with dissolve

    jump day2s4
