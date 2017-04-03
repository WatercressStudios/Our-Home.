label day6s6:

  scene park dark with dissolve
  
  "I'm whistling on my way home from the park."
  "Not even Mom's lectures can bring me down this time, so I'll—"
  
  scene black
   
  "Huh?"
  "Who's that dark figure crouching by my front door?"
  "It looks like they're doing something with the lock..."
  "Are they... {i}a burglar?!{/i}"
  "I look around to see if there's anyone to help me, but we're alone."
  
  menu:
    "Scream for help!":
      jump screamhelp
    "Try to knock them out!":
      jump knockout

###########################################

label screamhelp:
  
  "There's no choice. It's up to me to stop this. Maria and Alex are inside... I'm not letting anyone near them!"
  "I take a deep breath, and then.."
  
  voice "6-6-1.mp3" #potato
  pro "{i}AHHHH!!{/i}"
  voice "6-6-2.mp3" #lacTheWatcher
  dad "Gyaa!!"
  voice "6-6-3.mp3" #lacTheWatcher
  dad "E-Emily?! Why are you screaming??"
  
  jump day6s6dad

###########################################

label knockout:
  
  "There's no choice. It's up to me to stop this. Trembling a little, I pick up a small stick and tiptoe towards the dark figure by the front door."
  "Maria and Alex are inside... I'm not letting anyone near them!"
  
  voice "6-6-4.mp3" #potato
  pro "Hyaaa!"
  
  "WHAAAACK!"
  
  voice "6-6-5.mp3" #lacTheWatcher
  dad "YEOWCH!!"
  voice "6-6-6.mp3" #lacTheWatcher
  dad "E-Emily?! Why did you hit me with a stick??"
  
  jump day6s6dad

###########################################

label day6s6dad:
    
    scene house dark
    show dad sad2
    with dissolve
    play music bgmdad fadeout 1.0 fadein 0.0
    voice "6-6-7.mp3" #potato
    pro "Huh? Dad?"
    voice "6-6-8.mp3" #potato
    pro "Wha... What are you doing kneeling by our front door?!"
    show dad neutral with dissolve
    voice "6-6-9.mp3" #lacTheWatcher
    dad "Oh. Oh! This isn't what it looks like, cookie. I was just... it's just really dark and I can't see, you know, the lock."
    voice "6-6-10.mp3" #potato
    pro "Oh my god, Dad, use your phone to light it up! Nevermind, just, hang on."
  
    "I take out my phone and light up the lock."

    show dad smile2 with dissolve
    voice "6-6-11.mp3" #lacTheWatcher
    dad "Thanks, cookie."
  
    "Dad unlocks the front door and we enter the house."
    stop ambience fadeout 2.0
    scene diningroom dark
    show dad neutral2 with dissolve:
        align (0.75, 1.00)
    show mom angry2 with dissolve:
        align (0.25, 1.00)
    with dissolve
    play music bgmmomintro noloop fadeout 1.0
    queue music bgmmomloop loop
    voice "6-6-12.mp3" #kaito
    mom "Where were you?"
    
    "I resist sighing. Here we go again."
    "But... I'm fine. Just have to take it until she's satisfied. Nothing will bring me down today."
  
    voice "6-6-13.mp3" #lacTheWatcher
    dad "Take it easy, Liz, Emily was just—"
    show mom angry1 with dissolve:
        align (0.25, 1.00)
    with dissolve
    voice "6-6-14.mp3" #kaito
    mom "Not Emily, Jon. {i}You{/i}. Where were you?"
    
    "Huh?"
    
    show dad sad with dissolve:
        align (0.75, 1.00)
    with dissolve
    voice "6-6-15.mp3" #lacTheWatcher
    dad "I've been busy at work. You know that."
    voice "6-6-16.mp3" #kaito
    mom "You told me you'd be home with this week's groceries. Were you lying?"
    voice "6-6-17.mp3" #lacTheWatcher
    show dad neutral2 with dissolve:
        align (0.75, 1.00)
    with dissolve
    dad "No! It's just that my boss really needs the Farclay account closed."
    voice "6-6-18.mp3" #lacTheWatcher
    dad "In fact, I may need to spend more time at the office for the next week or two."
    show mom angry2 with dissolve:
        align (0.25, 1.00)
    with dissolve
    voice "6-6-19.mp3" #kaito
    mom "{i}More?{/i}"
    voice "6-6-20.mp3" #kaito
    show mom angry with dissolve:
        align (0.25, 1.00)
    with dissolve
    mom "Jon, you better be joking."
    voice "6-6-21.mp3" #lacTheWatcher
    dad "There's nothing I can do about it. I'm the one with the career here, Liz."
    voice "6-6-22.mp3" #kaito
    show mom angry3 with dissolve:
        align (0.25, 1.00)
    with dissolve
    mom "What... {i}what did you say?!{/i}"
    voice "6-6-23.mp3" #kaito
    mom "How dare you say that to my face!"

    scene bedroom dark with dissolve

    "I enter my room as the fight continues in the dining room."
    "What's going on?"
    "Are they fighting more often now?"
    stop music fadeout 1.0
    # sfx of some strange sounds next door (brother's going through a rough withdrawal)##############YEAH GO GET 'EM
    "TAP! TAP! TAP!"
  
    "It's that same strange noise coming from Alex's room. Only, this time I know what's going on with my brother."
    "I walk over to our connecting wall and gently knock on it."
  
    voice "6-6-24.mp3" #potato
    pro "Alex, hang in there. Let me know if you need me to hold your hand or something while you're in withdrawal."
    voice "6-6-25.mp3" #kujira
    bro "...thanks, sis. B-But I just really need to be alone."
    voice "6-6-26.mp3" #potato
    pro "Okay. I'm right here if you need me."

    if sleepinroom:
        "Someone knocks on my door at the moment. I go over and open it."

        show sis happy with dissolve

        voice "6-6-27.mp3" #potato
        pro "Hey Maria. You wanna sleep in my room again?"

        "She nods and walks into my room."
        "I lift the blanket for Maria to jump in before pulling the blanket over us."

        voice "6-6-28.mp3" #potato
        pro "Good night, sis."
        voice "6-6-29.mp3" #potato
        pro "Good night, Emi."
        
        scene black with dissolve

        jump dream7

    else:

        "There's nothing else I can do for Alex, so I walk over to my bed."
        "I lift the blanket and jump in."
        "I can't help but think about Lauren in the moonlight as I fall asleep."

        jump dream7

