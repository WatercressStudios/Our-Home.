label goodLoveEnding:

    scene bedroom with dissolve

    "After dinner is over, I sit in my room and think about the past."
    "I think about Lauren's theatre show in highschool."

    #TODO: FLASHBACK FILTER
#     scene drama with dissolve
    show black with dissolve
    play sound cheer

    "The audience roars with applause as Lauren's time on the center stage comes to an end."

    play ambience crowd fadein 2.0

    "The theater is filled to the brim. I'd say this was quite successful for her. Seeing her act on stage was super cute, especially knowing that I'd helped her with many of her lines."
    "She was probably very nervous, but she didn't let it show, not one bit."
    "She's good like that."
    "The applause finishes, and I go out to meet up with her after the performance."
    "Compared to her, I'm a nervous wreck."
    "Today's the day… the day I ask her out."
    "It took a lot of nerve, but eventually I was able to get the words out while Lauren was getting changed out of her costume."
    "I could hear her stop moving behind the sheet they put up to give people something to hide behind while changing."

    show lov shy1bh with dissolve

    voice "20-10-1.mp3" #starleeter
    lov "I’d love to!"
    voice "20-10-2.mp3" #potato
    pro "Uh… O-okay… C-cool."

    show lov happy2b with dissolve

    "Lauren came changing through the sheets and hugged me tight."
    "It made me blush, but... I didn’t exactly mind."
    "We just held each other for the longest time."
    "I guess we both wanted this, but neither of us was brave enough to ask."
    "When we pulled away, I noticed something I hadn’t noticed before."
    voice "20-10-3.mp3" #potato
    pro "Lauren…"

    show lov happy1b with dissolve

    voice "20-10-4.mp3" #starleeter
    lov "Uh-huh?"
    voice "20-10-5.mp3" #potato
    pro "Could you… uh... put some pants on?"
    "Lauren looked down."

    show lov shy1bh with dissolve

    voice "20-10-6.mp3" #starleeter
    lov "Gah! Sorry! I was too excited! I forgot I hadn’t finished changing!"
    
    show lov shy2bh with dissolve
    
    "She ducked away behind the sheet while laughing."
    voice "20-10-7.mp3" #potato
    pro "You were great out there, Lauren. I… I-I got you some roses."
    voice "20-10-8.mp3" #potato
    pro "I remember you saying your Dad would always come to your shows with roses…"

    show lov shy2b with dissolve

    voice "20-10-9.mp3" #starleeter
    lov "Ohmigosh, really? You're such a sweetheart!~"
    voice "20-10-10.mp3" #potato
    pro "Yeah… they reminded me of you."

    show lov happy2b with dissolve

    voice "20-10-11.mp3" #starleeter
    lov "Haha, because they're red, right??"
    voice "20-10-12.mp3" #potato
    pro "...Y, yeah, like your hair… *cough*"
    voice "20-10-13.mp3" #potato
    pro "W-well, it's… a little on the nose, but… th-the drama teacher said it's better to be big and boisterous, so…"

    show lov angry1bh with dissolve

    voice "20-10-14.mp3" #starleeter
    lov "You forgot flamboyant!~"
    voice "20-10-15.mp3" #potato
    pro "Ah, of course, how could I forget…"

    show lov angry1bh with dissolve

    "That... kind of set the tone for our relationship going forwards, but I wasn’t upset about it."
    "We dated and things just kept going from strength to strength!"
    
    if family > 7:
        "Honestly, I didn’t really expect things would go so well. Mom's changed for the better and Lauren's my girlfriend. Who knew things would turn out this way."
    else:
        "Honestly, I didn’t really expect it would go so well. After everything that had happened with Alex and with Mom, it was hard not to fall back into pessimism."

    if career > 7:
        show lov happy1bh with dissolve
        "Once we left school, we moved in together."
        show lov happy2b with dissolve
        "We’d sort of planned that already for college, but it ended up being for love too."
    else:
        show lov shy2bh with dissolve
        "Once we left school, Lauren went to college but I had to stay home."
        show lov happy2b with dissolve
        "We made it work, though. We'd visit each other often and we video chat every night."

    hide lov with dissolve
    stop ambience fadeout 2.0

    "It was wonderful, to say the least. I could never feel sad for long with her bubbliness in the air."
    "After a year of dating, Lauren said we should go to a café to celebrate."
    "I couldn’t say no to her when she put it like that."
    "That became our traditional celebration for our anniversary."

    #TODO: FLASHBACK FILTER ENDS

    scene cafe with Dissolve(2.0)
    play ambience crowd fadein 2.0

    show lov happy2 with dissolve

    voice "20-10-16.mp3" #starleeter
    lov "Happy Anniversary, Emily!"
    voice "20-10-17.mp3" #potato
    pro "Happy Anniversary, Lauren!"

    show lov happy1h with dissolve

    "We both giggle."
    voice "20-10-18.mp3" #potato
    pro "I know you like this place, but what are we going to do if it ever closes?"

    show lov confused1 with dissolve

    voice "20-10-19.mp3" #starleeter
    lov "We can always find another place. We don’t have to celebrate here."
    "I sigh."
    voice "20-10-20.mp3" #potato
    pro "If I knew that, I would have asked to go someplace else last year."

    show lov happy1h with dissolve

    "Lauren giggles."
    voice "20-10-21.mp3" #starleeter
    lov "You’re allowed to disagree with me, you know?"
    voice "20-10-22.mp3" #potato
    pro "I know, I know."
    "I reach out and take her hand."
    voice "20-10-23.mp3" #potato
    pro "I just like seeing how happy you get on days like this."

    show lov shy2b with dissolve

    voice "20-10-24.mp3" #starleeter
    lov "Aww!~"

    show lov happy1b with dissolve

    "I’m sure we’ve giving everyone else in here diabetes with our performance, but we can’t help it."
    "We get a bit silly when we’re together on dates like this."
    voice "20-10-25.mp3" #potato
    pro "To another year with the best girl in the world."

    show lov angry2h with dissolve

    voice "20-10-26.mp3" #starleeter
    lov "You’ve been cheating on me?!"
    "I roll my eyes."
    voice "20-10-27.mp3" #potato
    pro "Idiot."

    show lov happy1b with dissolve

    "Lauren laughs and squeezes my hand."

    show lov happy2b with dissolve

    voice "20-10-28.mp3" #starleeter
    lov "I love you."
    voice "20-10-29.mp3" #potato
    pro "I love you, too."

    if career < 8 and family < 8:
        show neutralminusending with Dissolve(2.0)
    else:
        show neutralplusending with Dissolve(2.0)
    # TODO: Credits

    stop ambience fadeout 2.0

    jump dreamEpilogue
