label dreamEpilogue:

    scene dream3 with Dissolve(1.3)

    show emily with dissolve
    dpro "It's been awhile hasn't it?"

    "The world around me is bright, but not blindingly so. It's new, and it's refreshing."

    "I know that I'm dreaming. I've been here before, but it's different this time."

    voice "20-6-1.mp3" #potato
    pro "It's been years…"
    show emily happy
    dpro "That, it has."

    "In front of me stands, well, me."

    "It's odd. Have I always looked like this? I look better than I used to, back when these types of dreams were a staple of my life."

    voice "20-6-2.mp3" #potato
    pro "Why am I here?"
    show emily
    dpro "Because you've been wanting some finality. The dreams you used to have disappeared with little warning."
    show emily happy
    dpro "You wanted your story to wrap up, nice and tidy."

    "It's true, the dreams did fade away. Sometimes, I still miss them. Now, however? I don't need them. Sure, many aspects of my life didn't go exactly the way I had planned, but…"

    "At least I'm here, right?"

    dpro "I wanted to thank you."

    voice "20-6-3.mp3" #potato
    pro "Thank me?"
    show emily
    dpro "Yes. You made a decision, and that single decision brought you to this point. If you would have chosen wrong, you very well could have been in a much, much more tragic place."
    show emily happy
    dpro "You are here because you decided to make something of yourself. You chose the real world. You chose to go home."

    voice "20-6-4.mp3" #potato
    pro "I guess that's true. It's interesting, how a single decision could hold so much weight, especially given how many decisions one makes on a daily basis."
    show emily
    dpro "Many of them don't matter, but sometimes…"

    voice "20-6-5.mp3" #potato
    pro "You'll find yourself on a crossroads."

    dpro "You'll find yourself asking the {i}right questions{/i}."

    voice "20-6-6.mp3" #potato
    pro "And I made the right choice?"
    show emily happy
    dpro "That, you did."

    dpro "No matter how well or poorly your life is going so far, it's much better than the alternative."

    dpro "You chose to live, and you chose to start living - two things that are not necessarily the same thing."

    voice "20-6-7.mp3" #potato
    pro "But they aren't always mutually exclusive, either."
    show emily
    dpro "Right."

    voice "20-6-8.mp3" #potato
    pro "Yeah, you're right. I'm in a better place than I used to be."
    show emily happy
    dpro "And you did that all on your own."

    "She comes close, putting a hand on my shoulder."

    dpro "You chose our home."
    show emily
    dpro "And Emily?"

    voice "20-6-9.mp3" #potato
    pro "Yeah?"

    #Next line should occupy the middle of the screen if possible. Larger text, it should stand out. It's the last four words that the player will see each time they get an Act 2 ending.
    show emily happy
    dpro "I'm proud of you."
    
    scene dreamepilogue with Dissolve(3)
    pause

    #GAMEEND

    if family > 7 and love > 7 and career > 7:
        ".:. Super Good Ending (1/11)"
    elif family < 8 and love < 8 and career < 8:
        ".:. Super Bad Ending (2/11)"
    elif family > 7 and love > 7 and career < 8:
        ".:. Neutral+ Ending A (3/11)"
    elif family > 7 and love < 8 and career > 7:
        ".:. Neutral+ Ending B (4/11)"
    elif family < 8 and love > 7 and career > 7:
        ".:. Neutral+ Ending C (5/11)"
    elif family < 8 and love < 8 and career > 7:
        ".:. Neutral- Ending A (6/11)"
    elif family < 8 and love > 7 and career < 8:
        ".:. Neutral- Ending B (7/11)"
    elif family > 7 and love < 8 and career < 8:
        ".:. Neutral- Ending C (8/11)"
    return
