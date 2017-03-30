label day5s5:

  $ sleepinroom = False

  scene stars with dissolve
  # cricket ambience sound?
  "As I fish out my keys by my front door, I hesitate. What if Mom's waiting for me inside again? It was dark in the house last night, too."
  "I sigh."
  "What am I gonna do? Spend all night outside?"
  "If mom's awake I'll just deal with it like I usually do."

  # TODO: hide background with dissolve
  "Hmm... looks like Mom's not here this—"
  
  # TODO: play clicking SFX of a lamp being turned on.
  # TODO: show diningroom background instantly

  play voice "5-5-1.mp3" #potato
  pro "Eek!"
  
  # show dad's surprised expression
  play voice "5-5-2.mp3" #lacTheWatcher
  dad "Emily?"
  play voice "5-5-3.mp3" #potato
  pro "Dad! You scared me."
  play voice "5-5-4.mp3" #lacTheWatcher
  dad "I'm just getting some water. What are you doing out so late?"
  play voice "5-5-5.mp3" #potato
  pro "Umm, Lauren forgot the sewing machine. I was just bringing it to her."
  play voice "5-5-6.mp3" #lacTheWatcher
  dad "Does your mother know about this?"
  
  "I don't answer his question but dad seems to get it anyway."
  
  play voice "5-5-7.mp3" #lacTheWatcher
  dad "Shhh. Take off your shoes and come in quietly. Your mother's about to finish up her bath."
  
  "Grateful, I nod silently and do as Dad says."
  "However, before I can take off my other shoe, I hear footsteps coming towards us."
  
  # show mom's angry expression
  play voice "5-5-8.mp3" #kaito
  mom "What's this? What's going on here?"
  play voice "5-5-9.mp3" #kaito
  mom "Have you been out late again, Emily?"
  
  "Dammit, so close. I choose not to reply and wait for her lecture."
  
  play voice "5-5-10.mp3" #lacTheWatcher
  dad "Take it easy on her, Liz. Emily was just helping a friend, that's all. It's not like she does this regularly."
  play voice "5-5-11.mp3" #kaito
  mom "Excuse me?"
  play voice "5-5-12.mp3" #kaito
  mom "What do you know about your daughter?"
  play voice "5-5-13.mp3" #kaito
  mom "If you're home more often you'd know that Emily was out late last night too!"
  play voice "5-5-14.mp3" #lacTheWatcher
  dad "I'm sure she has a reason for that too..."
  play voice "5-5-15.mp3" #kaito
  mom "Can you act like a real father for once?"
  play voice "5-5-16.mp3" #kaito
  mom "You're not the cool uncle they see sometimes... you're supposed to be the father!"
  play voice "5-5-17.mp3" #lacTheWatcher
  dad "I'm trying to be home more, but my job needs me there..."
  play voice "5-5-18.mp3" #kaito
  mom "Stop making excuses!"
  
  "The argument between them is getting worse, and it's like they don't even remember I'm there."
  "Not wanting to be a part of it, I sneak away and go into my room."
  
  scene bedroom with dissolve
  
  # sfx of some strange sounds next door (brother's going through a rough withdrawal)
  "TAP! TAP! TAP!"
  
  play voice "5-5-19.mp3" #potato
  pro "Huh?"
  
  "It's that same strange noise from last night coming from Alex's room."
  "I walk up to the wall connecting our rooms and knock on it with my knuckles."
  
  play voice "5-5-20.mp3" #potato
  pro "Alex, seriously, what's going on over there?"

  "Unlike yesterday, he doesn't answer this time, not even to tell me to go away."
  "Just before I can knock on the wall again, someone knocks on my door."
  "I stride over and pull the door open."
  
  play voice "5-5-21.mp3" #potato
  pro "Alex, what's going—"

  # show sis' surprised expression
  play voice "5-5-22.mp3" #potato
  pro "Oh, Maria."
  play voice "5-5-23.mp3" #amree
  sis "I-I'm sorry, it's just me..."
  play voice "5-5-24.mp3" #potato
  pro "What? No, don't be sorry. I'm happy to see you. What is it?"
  play voice "5-5-25.mp3" #amree
  sis "Umm..."
  
  "Maria's shuffling her feet uncertainly. She glances over at the sounds of our parents' argument."
  
  menu:
    "\"Do you wanna sleep in my room?\"":
      jump sleepinroom
    "\"Don't worry about the fighting.\"":
      jump dontworry

###########################################

label sleepinroom:

  $ sleepinroom = True

  "Maria nods quickly and enthusiastically as a look of relief washes over her face."
  "The fight between our parents must be affecting her more than she let on."
  
  play voice "5-5-26.mp3" #potato
  pro "Okay, come on in. Please try not to snore this time."
  play voice "5-5-27.mp3" #amree
  sis "I-I don't snore!"
  play voice "5-5-28.mp3" #potato
  pro "Oh yes you do. You may be tiny, but you snore super loudly."
  play voice "5-5-29.mp3" #amree
  sis "I don't!"
  play voice "5-5-30.mp3" #potato
  pro "Yes you do. Also, come here for a minute."
  play voice "5-5-31.mp3" #amree
  sis "Umm okay."
  play voice "5-5-32.mp3" #potato
  pro "Hyaaaa!~"
  
  "Maria giggles and begs for me to stop as I tickle her mercilessly."
  "I'm not sure what's happening to me. I feel like Lauren's playfulness is rubbing off on me."
  "It's like right now I'm Lauren, and Maria's me."

  play voice "5-5-33.mp3" #potato
  pro "Okay, okay, I'll stop, promise."
  play voice "5-5-34.mp3" #potato
  pro "We both need to sleep now anyway. It's getting late."
  play voice "5-5-35.mp3" #amree
  sis "Oh, okay. Good night, Emi."
  play voice "5-5-36.mp3" #potato
  pro "Good night, Maria."
  
  "I pull the blanket over us and close my eyes."
  jump dream6

###########################################

label dontworry:

  "Maria doesn't say anything at first. She flinches when Mom screams at Dad about something in the kitchen."
  
  play voice "5-5-37.mp3" #potato
  pro "Just ignore it. Pretend that it's not happening. Think about something else and go to sleep."

  "The fight between our parents must be affecting her more than she let on."
  
  play voice "5-5-38.mp3" #amree
  sis "O-Okay..."
  play voice "5-5-39.mp3" #potato
  pro "You can do it, Maria. I believe in you."
  
  "She seems to perk up a little at that."
  
  play voice "5-5-40.mp3" #amree
  sis "Okay!"
  play voice "5-5-41.mp3" #potato
  pro "Go on, go to sleep. I'll see you tomorrow morning."
  play voice "5-5-42.mp3" #amree
  sis "Good night, Emi."
  play voice "5-5-43.mp3" #potato
  pro "Good night, Maria."
  
  "I close the door, get into bed, and close my eyes. It's been a long day."
  jump dream6