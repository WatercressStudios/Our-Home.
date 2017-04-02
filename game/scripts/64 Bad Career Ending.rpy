label badCareerEnding:

    scene bedroom dark with dissolve
    play sound alarm
    "{b}BEEP! BEEP! BEEP!{/b}"

    "Ugh, it's barely morning…"
    "Alright, up and at 'em. C'mon Em, today's another big day…" 

    scene bedroom with dissolve
    play sound curtains
    play music bgmneutralintro noloop
    queue music bgmneutralloop loop

    "Rising groggily from my bed, I stretch out all the aching bones in my body."
    "Blinking my eyes a few times, I stare across the room."

    scene sewingkit with dissolve

    "Grandma's old sewing machine. It's an antique, isn't it?"
    "...Wonder how much I could get for it if I found a collector to sell it to."
    "...Ach, am I really thinking about selling that? I mean, it has some sentimental value, but…"
    "It's not like I use it anymore. Who has the time?"
    "It's hard to catch a break these days. Working two dead-end jobs is altogether killing me a little too slowly…" 

    scene bedroom with dissolve
    play sound fabric

    "Shuffling out of bed, I reach for my uniform, carelessly strewn across the floor."
    "It's fine. They say I'm a great worker, so that's about all that matters to them. I'd be too much of a pain in the ass to replace."
    "So that's one small relief. The sooner I save enough money up for school, the sooner I can do something I actually care about."
    "Or something that brings in more money to the house for less work. I'm so tired of standing around all day. My feet are okay for now, but I know I'm gonna be sore later."
    "I guess that's the dream now. I'll have to get used to it. Sometimes you have to make personal sacrifices to get anywhere."

    play sound fabric

    "Slipping on my work shirt, I go over my schedule today. Handling the opening shift at the grocery, and then the closing shift at the coffee shop will get me some good hours."
    "All about the hours, baby…" 

    scene livingroom with dissolve

    "Packing my bag, I nearly head out the door, before something catches my eye."
    "Maria's drawing. Of all of us, together."
    
    show black with dissolve

    if family > 7:
        show mom happy2 with dissolve:
            align (0.1, 1.0)
        show dad smile2 with dissolve:
            align (0.3, 1.0)
        show bro smirk2 with dissolve:
            align (0.5, 1.0)
        show sis happy1 with dissolve:
            align (0.7, 1.0)
        "Mom, Dad, Alex, Maria, and me."
    else:
        show mom sad2 with dissolve:
            align (0.1, 1.0)
        show dad sad2 with dissolve:
            align (0.3, 1.0)
        show bro sad1 with dissolve:
            align (0.5, 1.0)
        show sis sad2 with dissolve:
            align (0.7, 1.0)
        "Mom's in the drawing, too. I wonder if Maria misses her."

    if love > 7:
        show lov happy1 with dissolve:
            align (0.9, 1.0)
        "And look, she added Lauren in a little after. She's basically part of the family now, isn't she…"

    "Yeah. I put this up here to remind myself of what's important. Why I'm putting myself through these trials."

    scene house with dissolve
    play sound slamdoor

    "It can be a personal hell just to drag myself out of day, crawl over to work to work hours cobbled together by a monkey using a dart board…"
    "...And having to deal with ungrateful shits with the fakest smile I can muster."
    if love > 7:
        "But I know it's worth it. Because at the end of the day, I can catch up with my family and Lauren. The ones I love the most."
    else:
        "But I know it's worth it. Because at the end of the day, I can catch up with my family. The ones I love the most."

    "It's not much, but… I'm gonna do my best. It's all I can offer, really."
    "This is my home, after all..."

    show black with Dissolve(2.0)

    jump composite_future2
