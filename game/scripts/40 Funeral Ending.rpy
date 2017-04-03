label funeralending:

    #Don’t change the screen or music from Dream 8 just yet.

    # # #

    if homecoming:
        "None of my suffering matters in the grand scheme of things. I have the power to look past it and focus on the things that will make it all worth it."
    else:
        "But I can’t just leave."
        "The world is shit, but it’s better than playing make-believe all day."
        "Even if I can only trust myself, that’s still someone. I’ll fight for a life that’s better than this."

    "I’ll be happy that way."
    
    stop music
    scene black
    play sound slamdoor

    "..."

    "Right?"
    
    play ambience waterfall fadein 2.0
    scene funeralending with Dissolve(2.0)

    "The funeral is going about as you’d expect."

    "Maria probably hasn’t thought about death before, so she’s a mess right now."

    "Oh well."

    "She had to learn about mortality eventually. Plus, she’s still young, so she has plenty of time to get over it."

    "It’ll be hard, since the last time she ever saw him was when he slammed her against a wall, but in the end, time heals all wounds."

    "Mom and Dad aren’t so lucky, though."

    "As usual, Dad isn’t letting his emotions show very much. His eyes are watering up, though, so I think he’s still torn up about it."

    "He’s probably not as sad as anyone else, though."

    "For one, he’s a hard-working adult. It only makes sense that he’d approach this rationally and stay calm."

    "Plus, he’s at work so often that all things considered, he really never knew Alex that well."

    "If I had to guess, I’d say he’s just guilty."

    "It’s almost certain that he thinks he could have prevented this if he had been able to spend more time at home."

    "He probably won’t recover from that guilt. You can’t teach an old dog new tricks, you know?"

    "But at least he’s better off than Mom, who’s been sobbing the whole time."

    "Unlike Dad, Mom actually spent a lot of time with Alex. I’ve never understood it before, but now I think she really does love us. She just shows it poorly because life has her so frustrated."

    "She can’t look past the world’s flaws like I can, so she lashed out. It’s sad, really, and it’s even worse when I look at how guilty she must feel."

    "First, she yelled at her son and smacked him. Second, he killed himself. An objective look at the sequence of events will immediately tell you this is her fault."

    "If Mom can face that truth, she might be able to clean up her act and be a good mother to Maria, but..."

    "I personally doubt it. Mom’s never struck me as that strong of a person."

    "Thank God I’m eighteen so I can get off this sinking ship. I feel bad for Maria, but there’s nothing I can do about it. She’ll just have to learn to survive like I did."

    "Of course, I recognize that some of this is my fault."

    "I’ve been horrible to Alex. He’s snapped at me a few times when he wasn’t thinking straight, but at the end of the day, he really just needed my help."

    "If I had just given him the time of day, I’m sure I could have saved him, somehow."

    #Skip the next line if the player took the "unfortunate" route in d7s3. (i.e. if they didn’t yell at him)
    if scoldalex:
        "Plus, the last time I saw him before he died, I completely blew up at him. In a sense, I’m no better than Mom."

    "But that’s all in the past. There’s no point worrying about what-ifs and might-have-beens. This is the path I’ve chosen. There are flaws, but I can’t let them burden me."

    "I’m going to move on from this crappy life I’ve been given and dig through the mud until I find the life that I really want."

    "But... now that I actually start to think about it..."

    scene black
    stop music
    play sound slamdoor

    "Just what exactly {i}is{/i} the life that I really want?"
    
    #TODO: Credits
    scene funeralending with Dissolve(3.0)
    pause
    
    ".:. Funeral Ending (10/11)"
    return