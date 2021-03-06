label badLoveEnding:

    scene bedroom with dissolve

    "After dinner is over, I sit in my room and think about the past."
    "I think about Lauren's theatre show in highschool."

    #TODO: FLASHBACK FILTER
    scene theatre with dissolve
    play sound cheer

    "The audience roars with applause as Lauren's time on the center stage comes to an end."

    play ambience crowd fadein 2.0
    
    "The theater is filled to the brim. I'd say this was quite successful for her. Seeing her act on stage was super cute, especially knowing that I'd helped her with many of her lines."
    "She was probably very nervous, but she didn't let it show, not one bit."
    "She's good like that."
    "The applause finishes, and I go out to meet up with her backstage after the performance."
    "Compared to her, I'm a nervous wreck."
    scene black with dissolve
    "Today's the day… the day I ask her out."
    "I've had these feelings for a while now, but I only recently realized just what the feelings were."
    "I love her. I love Lauren, from the bottom of my heart."
    "But… I don't know if I can actually follow through."

    scene changingroom with dissolve
    show lov happy1h

    voice "20-4-1.mp3" #starleeter
    lov "Hey Emily! I'm so happy you came! Wasn't I great?"

    "She walks up and gives me a hug, and I pray she doesn't notice my shaking."

    voice "20-4-2.mp3" #potato
    pro "Y-yeah, it was great! You're doing great, yes!"

    "My voices is a little shaky, and I'm sure she's noticed by now."

    show lov happy2 with dissolve

    voice "20-4-3.mp3" #starleeter
    lov "Yep! How're you, Em?"

    voice "20-4-4.mp3" #potato
    pro "Uh, me? Why do you ask?"

    show lov happy1 with dissolve

    voice "20-4-5.mp3" #starleeter
    lov "You just seem a bit more jittery than usual."

    show lov happy2 with dissolve

    "Fuck, she's got me."

    voice "20-4-6.mp3" #potato
    pro "Hmm? Nah, nothing. I'm just happy to see all of your work come to fruition."

    show lov happy1bh with dissolve

    voice "20-4-7.mp3" #starleeter
    lov "Awww, you're so sweet! This is why I love ya~"

    "My skin turns several shades more red, and I wave her off."

    voice "20-4-8.mp3" #potato
    pro "Nah, it's just my job as a friend, yeah?"

    show lov confused2b with dissolve

    voice "20-4-9.mp3" #starleeter
    lov "As a friend… yeah. Why not?"

    "She looks away with a small smile."
    
    scene black with dissolve
    stop ambience fadeout 2.0

    "Maybe it's better if I wait. I'll get around to it eventually…"
    "I really don't want to ruin her good day. If I were to put her in the position where she'd have to say no…"
    "Not today. I will get to it eventually."

    scene sky with Dissolve(2.0)
    "That was a long time ago, and of course…"
    "I didn't."
    "I never got around to it."
    "Shortly after, she was asked out by one of her other friends."
    "I still remember the day. She even came to me and asked if it was okay."
    "Of course it wasn't, but I wasn't about to say that."
    "I couldn't."    
    "I just wanted her to be happy. Sometimes I wonder if she would have been happier with me, but that's just selfish."
    "Maybe, when she asked me, she was trying to tell me something. Either way, nothing came of it. Nothing came of my love."
    "Eventually, Alex and Maria noticed me moping around and I had to make up an excuse."

    if family > 7:
        "Even Mom looked at me sadly and cooked my favorite meals for a week."
        "I think she always knew how I felt about Lauren."
    else:
        "I don't think I was very convincing, though."
    
    scene mallcafeteria with dissolve
    play ambience crowd fadein 2.0
    "And here I am, today, sitting across the mall, watching Lauren and her girlfriend have their romantic date."
    "And I'm alone."
    "Every once in awhile, I hear Lauren giggle, in the same way she used to around me…"
    "And it hurts so, so much. I miss her. I haven't been able to hang out with her lately."
    "I keep telling myself it's because I don't want to remain a burden on her, or that I want to give her more space for her girlfriend, but in reality I just can't stand it."
    "I can't stand the feelings that I still hold for her, and I can't take knowing that I could have been with her, but my own cowardice ruined it."
    "True love was right in front of me, and I fucked it all up."
    "Lauren and her girlfriend stand up from their seats, passing me as they go. I pretend to work on my laptop, hoping they don't notice me."

    show lov happy1 with dissolve

    voice "20-4-10.mp3" #starleeter
    lov "Emily! Hey, I didn't expect to see you around!"

    "..."

    "I lower my laptop lid, facing them with a smile on my face."

    voice "20-4-11.mp3" #potato
    pro "I didn't realize you were here, either. How're things?"

    show lov happy2 with dissolve

    voice "20-4-12.mp3" #starleeter
    lov "Things are great! Just out on a date."

    "She wraps a hand around her lover, hugging her tight."

    voice "20-4-13.mp3" #potato
    pro "That's awesome."

    show lov happy2h with dissolve

    voice "20-4-14.mp3" #starleeter
    lov "Yeah, it is. I haven't seen you around in aaages. What's up with that?"

    voice "20-4-15.mp3" #potato
    pro "I've just been busy is all, I'll have to make time to visit."

    show lov happy1 with dissolve

    voice "20-4-16.mp3" #starleeter
    lov "You really should! It'll be fun, just like old times!"

    voice "20-4-17.mp3" #potato
    pro "Ehh, I sure hope not…"

    show lov happy1h with dissolve

    voice "20-4-18.mp3" #starleeter
    lov "Oh, hehe, right. Well, you know where to find me!"

    voice "20-4-19.mp3" #potato
    pro "Yeah, see ya Lauren."

    show lov happy2 with dissolve

    voice "20-4-20.mp3" #starleeter
    lov "See ya later!"

    "With that, they leave. I couldn't help but notice her significant other was awkwardly quiet the entire time."
    
    stop ambience fadeout 2.0
    
    "I really can't follow through with my promise. I'm sorry Lauren, but I can't do it."
    "It's best if we just… never see each other again."
    if career > 7:
        scene sewingkit with dissolve
        "I'll pour all my energy into up-coming fashion show. I'll be too busy for anything else then."
    else:
        scene kmartexterior with dissolve
        "I'll even pick up a third dead-end job. I'll be too busy for anything else then."
    "Maybe then I could move on from you."
    "Maybe then I could forget you."

    if career > 7 and family > 7:
        scene neutralplusending with Dissolve(3.0)
    else:
        scene neutralminusending with Dissolve(3.0)
    pause


    # TODO: Credits
    jump dreamEpilogue
