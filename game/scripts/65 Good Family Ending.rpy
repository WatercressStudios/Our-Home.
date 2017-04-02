label goodFamilyEnding:

    show mom sad2 with dissolve
    play sound honk

    "She looks at us for a long while, the taxi honking a second time."

    play music bgmfin
    show mom sad2 with dissolve

    voice "20-9-1.mp3" #kaito
    mom "I... I'm..."
    voice "20-9-2.mp3" #potato
    pro "It won't be the same this time around."
    voice "20-9-3.mp3" #potato
    pro "We've all changed, Mom. All of us. Things can work out this time. We just have to give it a shot."

    show mom sad1 with dissolve

    "Mom shakes her head no. But at least she isn't picking up her suitcase."

    show mom sad2 with dissolve

    voice "20-9-4.mp3" #kaito
    mom "But, how? I'm still the same horrible person I was before. I'll still be unsatisfied with my life. I... I haven't changed."
    voice "20-9-5.mp3" #potato
    pro "Then change something! Do something that will make you happy!"

    show mom sad1 with dissolve

    voice "20-9-6.mp3" #kaito
    mom "No, that's not possible. I'm too busy with housework..."

    hide mom with dissolve
    show sis happy1 at left with dissolve

    voice "20-9-7.mp3" #amree
    sis "We'll h-help! We can fold the clothes, do the dishes..."

    show bro smile2 at right with dissolve

    voice "20-9-8.mp3" #kujira
    bro "...take out the trash, do the washing..."

    play sound honk

    hide sis with dissolve
    hide bro with dissolve
    show mom sad2 with dissolve

    "The taxi honks at us for the third time. Mom looks out the window indecisively, torn between choices."

    hide mom with dissolve
    show sis happy1 at left with dissolve
    show bro smile2 at right with dissolve
    show dad neutral1 with dissolve

    voice "20-9-9.mp3" #lacTheWatcher
    dad "I'll do the cooking and mind the kids. I'll tell my boss to cut down on my hours. And..."
    voice "20-9-10.mp3" #lacTheWatcher
    dad "...I'll go to counselling with you."
    voice "20-9-11.mp3" #potato
    pro "We'll all go to counselling. As a family."

    show sis happy2 at left with dissolve
    show bro smirk2 at right with dissolve

    "Maria and Alex nod in agreement."
    
    hide sis with dissolve    
    hide bro with dissolve    
    hide dad with dissolve    

    show mom sad2 with dissolve

    "Mom looks at each one of us, one by one. Then, she does something I've never seen her do before..."

    show mom cry with dissolve

    # show mom's crying sprite. THIS IS THE ONLY TIME MOM CRYING SPRITE IS USED
    voice "20-9-12.mp3" #kaito
    mom "...okay, I-I'll stay..."

    show dad cry with dissolve:
        align (0.8, 1.0)

    "She isn't the only one in tears. We all are. Even Dad."

    voice "20-9-13.mp3" #kaito
    mom "A-And I'll do better this time... if not... I'll..."
    voice "20-9-14.mp3" #lacTheWatcher
    dad "We'll do better, Liz. We'll all do better."

    show sis cry with dissolve:
        align (0.3, 1.0)
    show bro cry with dissolve:
        align (0.1, 1.0)

    "Mom is sobbing openly now. Maria runs over and hugs her. Laughing with tears in our eyes, the rest of us do the same."
    "The taxi honks angrily at us one last time and drives off, leaving our family intact in our home."

    stop music fadeout 5.0
    show black with Dissolve(5.0)

    jump composite_future1

    ###########################################

label goodFamilyEnding_future:

    scene livingroom with Dissolve(2.0)    
    if career < 8:
        "I walk in the front door and kick off my shoes. It's been a long day and I can't wait to relax a little."
        play sound slamdoor
    else:
        "The long awaited holiday is finally here, and I've come home to see my family."
        scene bedroom with dissolve   
        "My bedroom hasn't changed at all. I guess they kept it for me."

    "I can smell dinner wafting in from the kitchen."

    scene kitchen with dissolve   

    voice "20-9-15.mp3" #potato
    pro "What are you cooking? It smells good."

    show dad angry2 with dissolve

    voice "20-9-16.mp3" #lacTheWatcher
    dad "Uh, lamb stew, I think? It might become something else. We'll see. I'm getting better, so it might turn out to be lamb stew after all."

    scene livingroom with dissolve   
    show bro grin1 with dissolve

    voice "20-9-17.mp3" #kujira
    bro "It's something else."

    "Alex said that in a matter-of-fact manner as he walks into the dining room with a Physics textbook in his hand."
    "Seeing the science-y book he's parading around, one might think he's most like our mom among the three of us."

    show bro smirk1 with dissolve

    voice "20-9-18.mp3" #kujira
    bro "Here you go, sis."
    
    show bro smirk1 with dissolve:
        align (0.65, 1.0)
    show sis happy2 with dissolve:
        align (0.35, 1.0)
    
    voice "20-9-19.mp3" #amree
    sis "T-Thanks, Alex."

    show sis happy1 with dissolve

    "Maria takes his textbook from him. Yes. Out of the three of us, Maria's the one who truly inherited Mom's brains."
    if love > 7:
        "Even Lauren was surprised when I told her, and she's the expert in rolling with things."

    voice "20-9-20.mp3" #kujira

    show bro smirk2 with dissolve

    bro "No problem. I won't need that in the College of Music and Arts in Chicago after all."
    voice "20-9-21.mp3" #potato
    pro "Hah! You're assuming you'll get in."

    show bro grin2 with dissolve:

    voice "20-9-22.mp3" #kujira
    bro "Have you heard the jazz piece I arranged and performed?"

    "I laugh at that. Alex may only be seventeen, but he's right. The boy has talent. He plays more jazz instruments than I can count, and he's a brilliant composer."

    scene kitchen with dissolve   

    if career < 8:
        play sound fabric
        "After dropping off my bag in my room, I start setting the table while Dad scoops his stew into our bowls."
    else:
        "At Dad's request, I start setting the table while he scoops his stew into our bowls."

    if love < 8:
        "For some reason, I think about the time Lauren cooked dinner for us. She really knew how to cook."
    else:
        "It's too bad Lauren can't join us tonight. I miss her already."

    scene livingroom with dissolve   

    voice "20-9-23.mp3" #potato
    pro "Maria, don't study at the dinner table."

    show sis worry2 with dissolve
    play sound paper

    voice "20-9-24.mp3" #amree
    sis "F-Five more minutes! This chapter on electromagnetism isn't very long..."

    show sis worry1 with dissolve

    voice "20-9-25.mp3" #potato
    pro "You realize that book's like three years above your year level, right?"

    show sis happy1 with dissolve

    voice "20-9-26.mp3" #amree
    sis "Miss Reynolds said I might get to skip another year..."

    show bro angry2 with dissolve:
        align (0.8, 1.0)

    voice "20-9-27.mp3" #kujira
    bro "A-Another year? Maria, you'll finish highschool quicker than me at this rate!"

    hide bro with dissolve
    hide sis with dissolve

    "Feelings of pride fills me as I resist the urge to hug my genius little sister. Maria's grown out of it, even though she's still timid and shy most of the time."
    "I say most of the time because when she needs to, she'll speak up, and when she does, everyone listens."

    voice "20-9-28.mp3" #potato
    pro "Where's Mom? Will she be home for dinner?"
    
    show dad smile1 with dissolve
    
    voice "20-9-29.mp3" #lacTheWatcher
    dad "Yes, but she said she'll be a bit late. Emergency meeting with the university board about one of her students."

    hide dad with dissolve
    show bro angry1 with dissolve

    voice "20-9-30.mp3" #kujira
    bro "Sounds serious. What did they do?"

    hide bro with dissolve
    show dad smile2 with dissolve

    voice "20-9-31.mp3" #lacTheWatcher
    dad "Plagiarism or something."
    voice "20-9-32.mp3" #potato
    pro "Hah, trying to pull one over Mom? Clearly they have no idea who they're dealing with."

    play sound opendoor
    hide dad with dissolve
    show mom sad3 with dissolve

    "The moment I said that, the front door swings open and in walks the Physics professor, kicking off her shoes."

    hide mom with dissolve
    show sis happy2 with dissolve

    voice "20-9-33.mp3" #amree
    sis "Mom! I have a question about Maxwell's equations in the integral form—"

    hide sis with dissolve
    show mom sad3 with dissolve

    voice "20-9-34.mp3" #kaito
    mom "Maria, give me a chance to breathe."

    hide mom with dissolve
    show sis worry2 with dissolve

    voice "20-9-35.mp3" #amree
    sis "But..."

    hide sis with dissolve
    show mom sad3 with dissolve

    voice "20-9-36.mp3" #kaito
    mom "I'll answer your questions after dinner, promise. But for now..."

    # show mom's smiling sprite
    show mom happy2 with dissolve

    voice "20-9-37.mp3" #kaito
    mom "Hi kids. How's everyone? Tell me about your day..."

    show black with Dissolve(2.0)
    jump composite_future3

    #### THE END