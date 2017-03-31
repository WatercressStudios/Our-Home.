label goodFamilyEnding:

    "She looks at us for a long while, the taxi honking a second time."

    play voice "20-9-1.mp3" #kaito
    mom "I... I'm..."
    play voice "20-9-2.mp3" #potato
    pro "It won't be the same this time around."
    play voice "20-9-3.mp3" #potato
    pro "We've all changed, Mom. All of us. Things can work out this time. We just have to give it a shot."

    "Mom shakes her head no. But at least she isn't picking up her suitcase."

    play voice "20-9-4.mp3" #kaito
    mom "But, how? I'm still the same horrible person I was before. I'll still be unsatisfied with my life. I... I haven't changed."
    play voice "20-9-5.mp3" #potato
    pro "Then change something! Do something that will make you happy!"
    play voice "20-9-6.mp3" #kaito
    mom "No, that's not possible. I'm too busy with housework..."
    play voice "20-9-7.mp3" #amree
    sis "We'll h-help! We can fold the clothes, do the dishes..."
    play voice "20-9-8.mp3" #kujira
    bro "...take out the trash, do the washing..."

    "The taxi honks at us for the third time. Mom looks out the window indecisively, torn between choices."

    play voice "20-9-9.mp3" #lacTheWatcher
    dad "I'll do the cooking and mind the kids. I'll tell my boss to cut down on my hours. And..."
    play voice "20-9-10.mp3" #lacTheWatcher
    dad "...I'll go to counselling with you."
    play voice "20-9-11.mp3" #potato
    pro "We'll all go to counselling. As a family."

    "Maria and Alex nod in agreement."  
    "Mom looks at each one of us, one by one. Then, she does something I've never seen her do before..."

    # show mom's crying sprite. THIS IS THE ONLY TIME MOM CRYING SPRITE IS USED
    play voice "20-9-12.mp3" #kaito
    mom "...okay, I-I'll stay..."

    "She isn't the only one in tears. We all are. Even Dad."

    play voice "20-9-13.mp3" #kaito
    mom "A-And I'll do better this time... if not... I'll..."
    play voice "20-9-14.mp3" #lacTheWatcher
    dad "We'll do better, Liz. We'll all do better."

    "Mom is sobbing openly now. Maria runs over and hugs her. Laughing with tears in our eyes, the rest of us do the same."
    "The taxi honks angrily at us one last time and drives off, leaving our family intact in our home."

    jump composite_future1

    ###########################################

label goodFamilyEnding_future:

    if career < 8:
        "I walk in the front door and kick off my shoes. It's been a long day and I can't wait to relax a little."
    else:
        "The long awaited holiday is finally here, and I've come home to see my family."
        "My bedroom hasn't changed at all. I guess they kept it for me."

    "I can smell dinner wafting in from the kitchen."

    play voice "20-9-15.mp3" #potato
    pro "What are you cooking? It smells good."
    play voice "20-9-16.mp3" #lacTheWatcher
    dad "Uh, lamb stew, I think? It might become something else. We'll see. I'm getting better, so it might turn out to be lamb stew after all."
    play voice "20-9-17.mp3" #kujira
    bro "It's something else."

    "Alex said that in a matter-of-fact manner as he walks into the dining room with a Physics textbook in his hand."
    "Seeing the science-y book he's parading around, one might think he's most like our mom among the three of us."

    play voice "20-9-18.mp3" #kujira
    bro "Here you go, sis."
    play voice "20-9-19.mp3" #amree
    sis "T-Thanks, Alex."

    "Maria takes his textbook from him. Yes. Out of the three of us, Maria's the one who truly inherited Mom's brains."
    if love > 7:
        "Even Lauren was surprised when I told her, and she's the expert in rolling with things."

    play voice "20-9-20.mp3" #kujira
    bro "No problem. I won't need that in the College of Music and Arts in Chicago after all."
    play voice "20-9-21.mp3" #potato
    pro "Hah! You're assuming you'll get in."
    play voice "20-9-22.mp3" #kujira
    bro "Have you heard the jazz piece I arranged and performed?"

    "I laugh at that. Alex may only be seventeen, but he's right. The boy has talent. He plays more jazz instruments than I can count, and he's a brilliant composer."
    if career < 8:
        "After dropping off my bag in my room, I start setting the table while Dad scoops his stew into our bowls."
    else:
        "At Dad's request, I start setting the table while he scoops his stew into our bowls."

    if love < 8:
        "For some reason, I think about the time Lauren cooked dinner for us. She really knew how to cook."
    else:
        "It's too bad Lauren can't join us tonight. I miss her already."

    play voice "20-9-23.mp3" #potato
    pro "Maria, don't study at the dinner table."
    play voice "20-9-24.mp3" #amree
    sis "F-Five more minutes! This chapter on electromagnetism isn't very long..."
    play voice "20-9-25.mp3" #potato
    pro "You realize that book's like three years above your year level, right?"
    play voice "20-9-26.mp3" #amree
    sis "Miss Reynolds said I might get to skip another year..."
    play voice "20-9-27.mp3" #kujira
    bro "A-Another year? Maria, you'll finish highschool quicker than me at this rate!"

    "Feelings of pride fills me as I resist the urge to hug my genius little sister. Maria's grown out of it, even though she's still timid and shy most of the time."
    "I say most of the time because when she needs to, she'll speak up, and when she does, everyone listens."

    play voice "20-9-28.mp3" #potato
    pro "Where's Mom? Will she be home for dinner?"
    play voice "20-9-29.mp3" #lacTheWatcher
    dad "Yes, but she said she'll be a bit late. Emergency meeting with the university board about one of her students."
    play voice "20-9-30.mp3" #kujira
    bro "Sounds serious. What did they do?"
    play voice "20-9-31.mp3" #lacTheWatcher
    dad "Plagiarism or something."
    play voice "20-9-32.mp3" #potato
    pro "Hah, trying to pull one over Mom? Clearly they have no idea who they're dealing with."

    "The moment I said that, the front door swings open and in walks the Physics professor, kicking off her shoes."

    play voice "20-9-33.mp3" #amree
    sis "Mom! I have a question about Maxwell's equations in the integral form—"
    play voice "20-9-34.mp3" #kaito
    mom "Maria, give me a chance to breathe."
    play voice "20-9-35.mp3" #amree
    sis "But..."
    play voice "20-9-36.mp3" #kaito
    mom "I'll answer your questions after dinner, promise. But for now..."

    # show mom's smiling sprite
    play voice "20-9-37.mp3" #kaito
    mom "Hi kids. How's everyone? Tell me about your day..."

    jump composite_future3

    #### THE END