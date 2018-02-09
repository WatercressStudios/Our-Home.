label day7s4:

    # TODO: hide background with dissolve

    scene black with dissolve

    "How did it all go so wrong?"
    "The choices we each have made... has it all led to this?"
    "Why?"

    scene hospitalhallway with dissolve
    voice "7-4-1.mp3" #skinimini
    doc "Alex's heart stopped on the way to the hospital. The paramedics were unable to revive him while in the ambulance."
    # TODO VA: SKINIMINI (also possible to crop the audio ourselves)
    voice "7-4-2.mp3" #skinimini
    doc "The hospital's ER team managed to revive and stabilize him, but he's still in critical condition."

    # TODO: hide background with dissolve
    "The beeping of heart monitors. The shuffling of feet as medical staff rush from one hallway to another."

    voice "7-4-3.mp3" #skinimini
    doc "His stomach was pumped and we've administered Naxolone to counter the effects of the overdose."
    voice "7-4-4.mp3" #lacTheWatcher
    show dad sad2
    dad "So he'll be fine?"
    voice "7-4-5.mp3" #skinimini
    doc "I'm sorry, but it's too early to tell. As I said earlier, he's in critical condition and his condition might change in the next twelve hours. And... Alex was deprived of oxygen for a long time."
    voice "7-4-6.mp3" #lacTheWatcher
    dad "Deprived of oxygen? What.. what does that mean?"
    voice "7-4-7.mp3" #skinimini
    doc "It means there's a possibility Alex has sustained some neurological damage."

    # TODO: hide background with dissolve
    "I wonder what Diane is doing. I really want to see her. Maybe I should see her."

    voice "7-4-8.mp3" #lacTheWatcher
    show dad angry3
    dad "What does that mean?! Can't you speak in English?? Liz! Say something to the doctor!"
#    voice "7-4-9.mp3" #kaito silence
    show dad angry2
    show mom sad1 with dissolve:
        align (0.25, 1.00)
    mom "..."
    voice "7-4-10.mp3" #lacTheWatcher
    show dad angry3
    dad "Liz? Liz!"
    voice "7-4-11.mp3" #skinimini
    show dad angry2
    doc "Please calm down, sir."
    voice "7-4-12.mp3" #lacTheWatcher
    show dad angry3
    dad "How can I calm down when no one would tell me what all this damn medical jargon means?!"
    voice "7-4-13.mp3" #skinimini
    show dad angry2
    doc "It's... you might know it as brain damage."
    voice "7-4-14.mp3" #lacTheWatcher
    show dad sad2
    dad "...A-Alex has brain damage?"
    voice "7-4-15.mp3" #skinimini
    doc "It's only a possibility. There's no way to know the extent of the damage, if any, until... {i}if{/i} he wakes up."
    voice "7-4-16.mp3" #lacTheWatcher
    show dad angry1
    dad "This... this must be a mistake! You have the wrong chart! Please check—"
    voice "7-4-17.mp3" #kaito
    show dad angry2
    show mom sad2
    mom "I want to see my son."
    voice "7-4-18.mp3" #lacTheWatcher
    show dad sad2
    dad "Liz?"
    voice "7-4-19.mp3" #kaito
    mom "Please let me see my son."
    voice "7-4-20.mp3" #skinimini
    doc "I'm sorry, Alex is in the ICU. The next twelve hours are critical."
    voice "7-4-21.mp3" #kaito
    show mom cry
    mom "Please. I'm begging you."
    voice "7-4-22.mp3" #skinimini
    doc "I'm really sorry..."
    scene black with dissolve
    hide mom
    hide dad

    # TODO: hide background with dissolve
    scene black with dissolve
    "I don't even remember when or how it happened, but at some point later, I'm in the car with Dad, Mom and Maria."
    "No one is speaking."
    "It's not until we get home when Dad says something."

    scene diningroom with dissolve
    voice "7-4-23.mp3" #lacTheWatcher
    show dad sad1 with dissolve:
        align (0.65, 1.00)
    dad "Sleep early, Maria. It's late... we'll talk tomorrow."
    voice "7-4-24.mp3" #amree
    show sis bandage at center
    sis "Okay Dad..."

    hide sis
    "Maria walks away sullenly."

    voice "7-4-25.mp3" #lacTheWatcher
    show dad sad2
    dad "Liz? Are you okay, honey?"
#    voice "7-4-26.mp3" #kaito silence
    show mom sad1 with dissolve:
        align (0.25, 1.00)
    mom "..."
    voice "7-4-27.mp3" #lacTheWatcher
    dad "Liz?"

    hide mom
    "Mom just steps away without a word. Her expression is unreadable."

    voice "7-4-28.mp3" #lacTheWatcher
    dad "Emily? Cookie?"

    scene bedroom night with dissolve
    "I don't reply either. I stumble away into my room and close my eyes."

    scene black with dissolve
    scene black

    stop music

    $ renpy.movie_cutscene("vfx/irltodream.mpg") # Loads the credit video

    scene black 
    jump dream8