label day4s3:

    #Might adjust this later for more 1984 talk, but it's really not a priority right now

    scene classroom with dissolve
    #REMEMBER TO UNCOMMENT THE SOUND ONCE WE HAVE IT!!
    play sound schoolbell

    "DOO DO DOO DO!"

    play ambience crowd fadein 2.0
    play music bgmbrointro noloop fadeout 1.0
    queue music bgmbroloop loop
    "Classes were finally over. What an exhausting day…"

    if go_hospital:
        "Lauren and I were able to make it back in time for our last class of the day."
        "Can't say geology is the most thrilling subject to end the otherwise high-energy day on."
        "Lauren even had to excuse herself partway through. She looked fidgety and restless the entire time."
        "She must've had a ton of other stuff to do when she left."
        "It was in that moment I rather envied her plethora of other commitments, because, well…"
        "...Let's be real, this class moves slower than the tectonic plates. I'd rather be anywhere but here."
        "...Wait, I didn't {i}learn something{/i}, did I??"
        "Anyway, that was then, this is now. Class is finally, mercifully over. Let's get on with our lives."

    else:
        # TODO: Play text message sound
        "I check my phone almost reflexively, cursing under my breath as I mess up my passcode entry twice in a row."
        "Fuck, what'd he get into… what? Another text from mom?"
        voice "4-3-1.mp3" #potato
        pro "'Your brother's out of the hospital. Mom.'"
        voice "4-3-2.mp3" #potato
        pro "...Huh?"
        "They threw him out that quickly? If it was an overdose, I thought they'd hold him for longer..."
        "I guess he's okay? ...I guess he is."
        "...I should be more worried than I am, but… I guess he ended up getting what he deserved."
        "At least he survived. He's fine now. Everything's fine."
        "Everything's fine."
        voice "4-3-3.mp3" #skinimini
        tea "Um, Emily? School's over. You can go home now."
        voice "4-3-4.mp3" #potato
        pro "...O-oh, right, uh… 'scuse me."
        "Why does it seem that Miss Reynolds teaches every class in this school??"
        "ANYWAY. Packing my shit, I vacate the premises as quickly as humanly possible."


    scene schoolhallway sunset with dissolve
    #play sound cellphonechime

    "My cell vibrates and chimes cheerily. Is that Lauren?"
    "Fishing it out of my pocket, I give it a read…"
    #texts can be in pink pls
    "{color=#FF69B4}\"hey em! pls com 2 drama, i rly need ur hALP PLS\"{/color}"
    "{color=#FF69B4}\"ops sry caps!! ^^;\"{/color}"
    #could draw this and accompany it with text reading but its so minor so we'll see
    "Attached to the text was a chibi bunny drawing thing. Was it, like, bowing to apologize?"
    voice "4-3-5.mp3" #potato
    pro "Well, it sounds pretty urgent, so… alright."
    "After packing my supplies back into my locker, I make a beeline towards the drama room."

    stop ambience fadeout 3.0
    scene black with dissolve

    "..."

    stop music fadeout 1.0

    scene drama with dissolve
    voice "4-3-6.mp3" #potato
    pro "Hey, Lauren? You wanted me to drop by?"

    play music bgmhijinksintro noloop fadeout 1.0
    queue music bgmhijinksloop loop

    voice "4-3-7.mp3" #potato
    pro "...Oh. Should I come back later?"

    #show cg stretching. Get Kieran's feedback

    #should ask kieran how hard an outfit change would be for the purposes of this scene. A sweater or a leotard would probably be preferred
    #also ask for a CG of doing stretches, probably something eyecandy
    
    show lov happy1h with dissolve
    voice "4-3-8.mp3" #starleeter
    lov "Oh! You sound hurt. You can join me in my stretches if you like!"
    voice "4-3-9.mp3" #potato
    pro "No, that's not it, it's just… I didn't think you could stretch that far."
    voice "4-3-10.mp3" #starleeter
    show lov happy2h with dissolve
    lov "You kiddin'? It's a musical, the actors gotta dance too! I'm just gettin' warmed up!~"
    voice "4-3-11.mp3" #potato
    pro "Yeah, but…"
    "I could feel blood rushing to my face. This was not what I was expecting to see!"
    voice "4-3-12.mp3" #starleeter
    show lov happy1 with dissolve
    lov "C'mon, you were sitting in a chair for an hour, gotta loosen up! Here, follow my moves!"
    voice "4-3-13.mp3" #starleeter
    
    scene black with dissolve
    
    lov "Alright, can you touch your toes! Just like this!"
    voice "4-3-14.mp3" #potato
    pro "...I-I'm not sure I can stretch that far, I… I could go down to the knees?"
    voice "4-3-15.mp3" #starleeter
    lov "No? Alright, leg up like thiiiis…"
    voice "4-3-16.mp3" #potato
    pro "How did you manage that? Isn't this a little excessive for a musical number??"
    voice "4-3-17.mp3" #starleeter
    lov "I take yoga on the weekends! I know all the poses! The reclining pigeon, the wild thing, the downward dog, the half lord of the fishes pose…"
    "Are these actual yoga poses, or something else entirely…?"
    voice "4-3-18.mp3" #potato
    pro "You made that last one up. No, all of those sound flagrantly false."
    voice "4-3-19.mp3" #starleeter
    lov "Would I lie to you?? I'm completely serious!"
    "It was then that I realized, yoga was a way weirder hobby than I thought."
    "And, I mean, it was already pretty weird."


    scene drama with dissolve
    show lov happy1 with dissolve
    voice "4-3-20.mp3" #starleeter
    lov "You should come with me! I have a discount for friends I can use if they come along!~"
    voice "4-3-21.mp3" #potato
    pro "I, uh… I'll pass."
    voice "4-3-22.mp3" #potato
    pro "So, uh, you didn't just call me here to do stretches with you, right?"
    voice "4-3-23.mp3" #starleeter
    show lov shy1h with dissolve
    lov "I, uh… maybe?"
    voice "4-3-24.mp3" #potato
    pro "...You didn't have anything for me to do this time? You made it sound so urgent."

    show lov shy2h with dissolve
    voice "4-3-25.mp3" #starleeter
    lov "I just wanted to see how you were doing, that was all."

    if not go_hospital:
        voice "4-3-26.mp3" #starleeter
        show lov shy1 with dissolve
        lov "The way you were looking at your phone during math class. It didn't sound okay…"
        voice "4-3-27.mp3" #starleeter
        show lov angry1 with dissolve
        lov "Are you {i}sure{/i} nothing's wrong?"
        voice "4-3-28.mp3" #potato
        pro "..."
        "I don't know what I should say. I didn't want to make a scene in class, but… she's smarter than she lets on."
        "Or maybe I'm just way too easy to read? She was always good at the 'emotional' part of people."
        "In a moment of weakness, I confess."
        voice "4-3-29.mp3" #potato
        pro "It's my brother. He was admitted to the hospital."
        show lov shy2h
        voice "4-3-30.mp3" #starleeter
        lov "What!?"
        #lauren should be gasping
        "Her face contorts in utter shock. I rise and try to calm her down."
        voice "4-3-31.mp3" #potato
        pro "I-it's okay, it's okay, he's home now!"
        voice "4-3-32.mp3" #starleeter
        show lov shy1h with dissolve
        lov "R-really? B-but, you should go see him, right??"
        "I can feel my mouth curl at that. She was absolutely right, and I hesitated."
        voice "4-3-33.mp3" #potato
        pro "I-I didn't want to cause a scene in class, or… or make you worry."
        voice "4-3-34.mp3" #starleeter
        show lov shy2 with dissolve
        lov "Hey, it's family we're talking about! I'll be fine!"

        show lov angryh
        voice "4-3-35.mp3" #starleeter
        show lov angry2 with dissolve
        lov "Seriously, you should go see him right now, or I'm gonna get really mad!"
        voice "4-3-36.mp3" #potato
        pro "I mean... I was thinking about it, until {i}someone{/i} asked me to rush over here to help with something…"
        voice "4-3-37.mp3" #starleeter
        show lov shy2b with dissolve
        lov "Ah? I, ah… I was thinking of you… you could've used a distraction." 
        "Oh God, she was an expert at eliciting sympathy. I couldn't stay mad even if I wanted to."
        voice "4-3-38.mp3" #potato
        pro "Hey, it was a joke, no big deal."

    else:
        voice "4-3-39.mp3" #potato
        pro "Don't worry. I'm fine, I'll survive. Today was a pretty crazy day, after all…"
        voice "4-3-40.mp3" #starleeter
        show lov shy1 with dissolve 
        lov "Yeah, no kidding… wow."
        voice "4-3-41.mp3" #starleeter
        show lov confused1 with dissolve
        lov "Especially the geology lecture."
        voice "4-3-42.mp3" #potato
        pro "What? You couldn't wait to get out of that."
        voice "4-3-43.mp3" #starleeter
        show lov happy2h
        lov "Yeah, I was on the edge of my seat the whole time.~"
        voice "4-3-44.mp3" #potato
        pro "Pfft. I think that was the first time I ever envied you and your extracurriculars."
        voice "4-3-45.mp3" #potato
        pro "Must make for a great Get Out Of Jail Free card."
        voice "4-3-46.mp3" #starleeter
        lov "Oh, it has its perks… the teacher wasn't as mad at me for chauffeuring you around. Miss Reynolds is used to it by now.~"

        if bring_sis:
            voice "4-3-47.mp3" #starleeter
            show lov happy1h with dissolve
            lov "And I even got to see little Maria again! She's really getting big!~"
            voice "4-3-48.mp3" #potato
            pro "Hey, you sound like a mom when you talk like that, heheh."
            voice "4-3-49.mp3" #starleeter
            show lov happy2h with dissolve
            lov "Heh. I always wanted to be a mom, but for now I can settle for being her cool big sis!"
            voice "4-3-50.mp3" #potato
            pro "W-wait, you can't… you can't do that, {i}I'm{/i} her cool big sister. Me, right here."
            voice "4-3-51.mp3" #starleeter
            show lov happy2 with dissolve
            lov "Oh, you're just a huge dork underneath all that edge and snark!"
            voice "4-3-52.mp3" #potato
            pro "D-dork…?"
            voice "4-3-53.mp3" #starleeter
            show lov happy1 with dissolve
            lov "See, there it is! You're blushinggg!"
            voice "4-3-54.mp3" #potato
            pro "I'm not… y-you just can't claim people as your own flesh and blood out of the blue!"
            voice "4-3-55.mp3" #starleeter
            show lov happy2 with dissolve
            lov "Pfft, of course not, I'm just gonna adopt her."
            voice "4-3-56.mp3" #potato
            pro "Back off, she's mine, you wicked harpy."
            voice "4-3-57.mp3" #starleeter
            show lov shy1h with dissolve
            lov "'Harpy'??? I'm hurt, Em!"
            voice "4-3-58.mp3" #potato
            pro "You can settle for being her crazy Aunt, okay?"
            show lov shy2h with dissolve
            voice "4-3-59.mp3" #starleeter
            lov "Whaaaat? I'm not crazy…"

        voice "4-3-60.mp3" #starleeter
        show lov shy1h with dissolve
        lov "But anyway… I'm just glad your brother was alright… boy was that an anti-climax…"
        voice "4-3-61.mp3" #potato
        pro "...Yeah… no kidding…"

    voice "4-3-62.mp3" #potato
    pro "I guess it's a relief though, but… it's gonna be an awful time, going home to see him."
    voice "4-3-63.mp3" #potato
    pro "Mom's the one who found out, and she's gonna blow a gasket."
    if not go_hospital:
        voice "4-3-64.mp3" #starleeter
        show lov confused1 with dissolve
        lov "It can't be that bad, right?? If he was let out the same day, I mean…" 
    voice "4-3-65.mp3" #potato
    pro "I'm worried, like… she's probably gonna throw him out of the house."
    voice "4-3-66.mp3" #starleeter
    show lov confused2 with dissolve
    lov "I dunno about that, like… he's family, right?"
    voice "4-3-67.mp3" #starleeter
    show lov happy2 with dissolve
    lov "A-and he seems like a nice guy. You told me he was gonna really smart too, right?"
    voice "4-3-68.mp3" #potato
    pro "...I did, didn't I?"
    "Wonder what happened. Since Alex got into the drugs, it's been one bone-headed decision after another."
    "I didn't have the heart to tell Lauren how worried I was about him. What I feared had come to pass the instant I saw that text."
    voice "4-3-69.mp3" #potato
    pro "I-I should go. I should see him. He's probably still in, mm, discomfort."
    voice "4-3-70.mp3" #starleeter
    show lov happy1 with dissolve
    lov "Ah, sure, don't let me keep you. Call me if you need anything, okay? I can always make time to talk."

    show lov happy2 with dissolve
    "Her smile is incredibly sweet. I take a mental snapshot of it and memorize it. I feel tonight's gonna be a rough night."
    "Sometimes it feels like she keeps me going, day by day."

    voice "4-3-71.mp3" #potato
    pro "...Y-yeah. Same. Thanks, s-see… see you later, okay?"
    voice "4-3-72.mp3" #starleeter
    show lov happy1 with dissolve
    lov "...Yeah! Sure. Anytime. I got a lot over here to do, so… good luck!"

    "She waves me off as I leave the drama room."
    scene schoolhallway with dissolve
    "I haven't really… told Lauren much about my family, have I? For four years now, it's kind of just been… my business."
    "But there was concern in her eyes. She's worried too, and… I think she's figuring it out."
    "God, I wish I wasn't such a coward about this. I know I should trust her, she's the sweetest thing in the school, but…"
    "It would burden her. I don't want to burden her with my problems, I guess. She has so much to take care of already."
    if not go_hospital:
        "I take a breath and head out. I should stop worrying about her for a bit, I know. Alex is probably getting an earful from Mom."
    else:
        "I take a breath and head out. I should stop worrying about her for a bit, I know. Alex is probably getting an earful from Mom, and we didn't get to talk much."
    "I miss him."
    
    scene black with dissolve
    "... ... ..."

    stop music fadeout 5.0

    jump day4s4
