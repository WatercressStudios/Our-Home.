label day5s1:
 
    scene bedroom with dissolve
    stop music fadeout .5 
    "The morning sun’s assault on my retinas marks the start of a new day."
    "If today is anything like yesterday, I think I’ll pass."
    "Okay, okay, I know ‘five more minutes’ is cliche, but it’s a solid compromise."
    "...Fine, world. You win. I’ll get up."
    "..."
    "Slowly."
     
    scene kitchen with dissolve
    show bro sad1 with dissolve
     
    "The fact that there was only one person left at the breakfast table when I arrived told me that I was a bit {i}too{/i} slow."
    play music bgmbrointro noloop fadeout 1.0
    queue music bgmbroloop loop
    voice "5-1-1.mp3" #potato
    pro "Morning, sunshine."
     
    #My (extremely minimal) research on withdrawal symptoms shows that the only outward physical symptom is sweating. Some lightly sweating or generally exhausted sprites for bro could be put to good use here.
    
    voice "5-1-2.mp3" #kujira
    bro "..."
     
    voice "5-1-3.mp3" #potato
    pro "Yesterday scared the crap out of me, you know."
    
    show bro angry1 with dissolve
    
    voice "5-1-4.mp3" #kujira
    bro "Fuck off."
     
    "Jeez, what’s gotten into him?"
     
    #I apologize in advance for the mistakes I am probably making, o wondrous programmers
    #If I messed up and it’s not clear, I’m making the player choose the passive option twice to get the good outcome, but choosing angrily either time gets the bad outcome.
    #Thank you for all that you do
     
    menu:     
        "Brush it off":
            jump brushitoff
     
        "Fight back":
            jump d5s1bad
     
label brushitoff:
     
    "Seriously?"
    "I barely even said anything! I can’t just let him talk to me like that!"
     
    menu:
        "Let him have it.":
            jump d5s1bad
     
        "Just take a deep breath.":
            $ family += 1
            jump d5s1good
     
label d5s1bad:
     
    voice "5-1-5.mp3" #potato
    pro "It’s too damn early for me to put up with that shit, Alex."
     
    show bro sad2 with dissolve
    
    voice "5-1-6.mp3" #kujira
    bro "Then leave me alone."
     
    voice "5-1-7.mp3" #potato
    pro "Hey, what do you know. You actually had a good idea for once."
     
    show bro angry1 with dissolve
    
    "He gave me a glare and stopped talking."
     
    "Other than tasting a bit worse than usual, the rest of breakfast was uneventful."
     
    jump d5s1merged
     
label d5s1good:
     
    "This is fine. Nothing a bit of oxygen can’t fix."
     
    voice "5-1-8.mp3" #potato
    pro "Sorry, Alex. I’m just glad to see you’re okay, is all."
     
    show bro sad1 with dissolve
    
    voice "5-1-9.mp3" #kujira
    bro "...Right. Sorry I snapped, I just... I’m not feeling my best right now. If it’s alright, would you mind leaving me alone for a while?"
     
    voice "5-1-10.mp3" #potato
    pro "Is something wrong?"
     
    voice "5-1-11.mp3" #kujira
    bro "I don’t really want to talk about it."
     
    voice "5-1-12.mp3" #potato
    pro "Well, uh... alright, I guess."
     
    "Other than tasting a bit better than usual, the rest of breakfast was uneventful."
     
    jump d5s1merged
     
label d5s1merged:
     
    scene livingroom with dissolve
    "Just as I was about to head for school, a tug on the back of my skirt reminded me of what I was missing."
    play music bgmsis fadeout 1.0 fadein 0.0 
    show sis worry2 with dissolve
     
    voice "5-1-13.mp3" #potato
    pro "Hey, I haven’t seen you all morning. What’s up?"
     
    "..."
     
    "Seems that nobody’s really in a talking mood today."
     
    "I walked out the door with Maria following silently behind me."
     
    #Transition to... well, whatever it is you do for "walking little sister to school" things. You guys are probably familiar with that.
    
    scene siswalk with dissolve
    play ambience suburb fadein 2.0 
    show sis worry1 with dissolve
    voice "5-1-14.mp3" #amree
    sis "Um..."
     
    voice "5-1-15.mp3" #amree
    sis "Is Alex mad at me?"
     
    voice "5-1-16.mp3" #potato
    pro "I’m pretty sure he’s mad at everything. What happened?"
     
    show sis sad1 with dissolve
    
    voice "5-1-17.mp3" #amree
    sis "He seemed tired, so I asked him if he was going to stay home from school, and he was in the hospital yesterday, so I asked if he needed to stay home from school, but, he, uh, yelled at me."
     
    voice "5-1-18.mp3" #potato
    pro "Seriously?"
     
    show sis worry2 with dissolve
    
    voice "5-1-19.mp3" #amree
    sis "I-it wasn’t very much! He just kind of snapped at me and I got scared and hid in my room."
     
    voice "5-1-20.mp3" #potato
    pro "Jeez... He snapped at me, too, this morning. I know he’s prickly, but this is just ridiculous."
     
    show sis happy1 with dissolve
    
    voice "5-1-21.mp3" #amree
    sis "So he’s not mad at me?"
     
    voice "5-1-22.mp3" #potato
    pro "Nah. Like I said, he’s just... mad."
     
    show sis happy2 with dissolve
    
    voice "5-1-23.mp3" #amree
    sis "Phew! He always seems so frustrated; I’d hate it if I made things even worse for him."
     
    voice "5-1-24.mp3" #potato
    pro "I don’t think you have to worry about that. But I do have to wonder what his problem is today."
     
    "Oh, who am I kidding."
     
    "It doesn’t take a genius to know he’s gotten himself involved in more drugs."
     
    "Apparently catching the disgust on my face, Maria changed the subject."
     
    show sis worry2 with dissolve
    
    voice "5-1-25.mp3" #amree
    sis "You know, I just remembered something that happened on a show I saw a few days ago!"
     
    voice "5-1-26.mp3" #potato
    pro "Oh, cool! Tell me all about it."
     
    "Anything to get my mind off of that asshat."
     
    show sis worry1 with dissolve
    
    voice "5-1-27.mp3" #amree
    sis "Well, it was kind of like a mystery episode."
     
    show sis happy1 with dissolve
    
    voice "5-1-28.mp3" #amree
    sis "The four girls all went on a camping trip, and they played in the woods, but when they got back to camp,"
     
    show sis happy2 with dissolve
    
    voice "5-1-29.mp3" #amree
    sis "One girl’s lunch was gone!"
     
    voice "5-1-30.mp3" #potato
    pro "That’s terrible!"
     
    "The stakes in kids’ shows sure are high."
     
    show sis happy1 with dissolve
    
    voice "5-1-31.mp3" #amree
    sis "They were on the land of the rich girl’s family, and she said that one of the four had to have stolen it."
     
    voice "5-1-32.mp3" #amree
    sis "They argued about it and realized that one girl left the group for a few minutes while they were playing and never said why."
     
    show sis worry2 with dissolve
    
    voice "5-1-33.mp3" #amree
    sis "The rich girl and the girl whose lunch was stolen got mad at her and said she would have to give up her own lunch so that everyone would get one, even though she said she was innocent."
     
    show sis happy2 with dissolve
    
    voice "5-1-34.mp3" #amree
    sis "But! The last girl, her sister couldn’t believe that one of her friends would do something like that and defended her."
     
    voice "5-1-35.mp3" #amree
    sis "She found some tracks, and everyone realized that the lunch wasn’t hidden well enough and an animal took it."
     
    voice "5-1-36.mp3" #potato
    pro "Should those girls really have been camping around wild animals like that?"
     
    show sis happy1 with dissolve
    
    voice "5-1-37.mp3" #amree
    sis "No, it’s okay. They have superpowers."
     
    voice "5-1-38.mp3" #potato
    pro "...Oh."
     
    "Freaking kids’ shows."
     
    voice "5-1-39.mp3" #amree
    sis "So anyways, they all gave parts of their lunches to the girl who lost hers, and everything turned out okay."
     
    voice "5-1-40.mp3" #potato
    pro "That’s good. So what made you think about that episode?"
     
    show sis worry1 with dissolve
    
    voice "5-1-41.mp3" #amree
    sis "Well, it kind of stood out because that show is normally about fighting bad guys,"
     
    show sis happy1 with dissolve
    
    voice "5-1-42.mp3" #amree
    sis "But I mostly liked something that the fourth girl said."
     
    voice "5-1-43.mp3" #amree
    sis "She said she had to believe the accused girl because they were family"
     
    voice "5-1-44.mp3" #potato
    pro "Really? That sounds a bit flimsy."
     
    "Was I really entertained by that kind of sappy stuff as a kid?"
     
    voice "5-1-45.mp3" #amree
    sis "I kind of thought so too, but.... it still made me happy to think about."
     
    voice "5-1-46.mp3" #potato
    pro "So would you believe me if I said I was an alien?"
     
    show sis worry2 with dissolve
    
    voice "5-1-47.mp3" #amree
    sis "Well... No, not really."
     
    scene sisschool with dissolve
    
    "I pitched a few more blatant lies at Maria before I dropped her off at school and went off on my own."
    stop ambience fadeout 2.0 
    "...But man, kids’ shows are sappy."
    
    scene black with dissolve
     
    "Way, way, way too sappy."
    "... ... ..."

    jump day5s2