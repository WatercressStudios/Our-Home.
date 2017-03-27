label day4s2:

  $ go_hospital = False
  $ bring_sis = False

  show classroom with dissolve

  # TODO: use whatever music track’s usually used for the classroom

  play voice "4-2-1.mp3" #skinimini
  tea "...and when you integrate an exponent to the power of three, you should divide it by..."

  ### TODO: Math Teacher named Reynolds, who was also the English teacher in Tutty’s scene. We’ll make it a joke.
  "I'm not really listening to Miss Reynolds, and I doubt anyone else in class is."

  play voice "4-2-2.mp3" #skinimini
  tea "...resulting a fraction of three quarters and... oh, someone's raising their hand. Yes, Miss Moodie?"
  play voice "4-2-3.mp3" #starleeter
  lov "Can we go back to the previous equation? Where did the minus sign..."

  "No one apart from Lauren, it seems. Despite barely having any time to herself, she gives her all to everything she does."
  "I don't know how she does it. Nor do I understand why."

  # TODO: sound phone beeping / text message
  "BEEP~ BEEP~"

  "I feel my cellphone vibrate and I quickly fish it out before the teacher hears it."

  # TODO: sound phone beep to indicate it being used
  "\"Alex in hospital. Mom.\""
  "My breath catches, and I freeze, chest tightening up."
  "This can't be happening..."

  # TODO: flashback to the previous scene where Emily says "you'll die of an overdose" to Alex. As in, literally copy & paste the words, BG and sprites from that scene, and apply a vignette & sepia filter over it for flashback feels.

  "No... what have I done..."
  "How could I say something like that to him? Fuck!"
  "I shake my head. My hands are trembling."
  "But... maybe he's fine. People overdose all the time, and they turn out fine. Maybe it isn't even an overdose."
  "I'm totally overreacting."

  # TODO: flashforward to the funeral CG? I.e. show a flash of the coffin in black and white or sepia filter.

  play voice "4-2-4.mp3" #skinimini
  tea "Miss Westenson, would you like to share what's on your phone with the class?"

  "I look up."
  "Everyone's staring at me. Lauren's staring at me."

  menu:
    "Pretend nothing's happening.":
      jump carryon
    "Go to the hospital.":
      jump hospital

###########################################

label hospital1:

  $ go_hospital = True
  
  # TODO: LOVE+ and FAMILY+ 

  "No! What am I thinking? I have to get to the hospital!"
  "I quickly push my chair back and stand up. I consider saying something to the teacher, but I don't."
  "Instead, I snatch my bag and dash out of the classroom."
  
  show hallway with dissolve

  "I can hear the teacher calling out to me, but I don't have time to deal with anything else right now."
  play voice "4-2-5.mp3" #starleeter
  lov "Emily!"

  "I hear footsteps in the hallway catching up to me."

  play voice "4-2-6.mp3" #starleeter
  lov "Emily, wait!"

  "Lauren grabs my hand to stop me from walking."

  play voice "4-2-7.mp3" #potato
  pro "Lauren? What are you doing here?"
  play voice "4-2-8.mp3" #starleeter
  lov "I should be the one asking you that. Are you okay? What's going on?"
  play voice "4-2-9.mp3" #potato
  pro "It's..."
  
  "I hesitate."
  "It occurs to me that Lauren's worried about me."
  "But what should I tell her? Does she really want to hear about my family problems?"
  "As if sensing my indecision, Lauren notices the phone in my hand and takes it."
  
  play voice "4-2-10.mp3" #starleeter
  lov "Can I read this?"
  play voice "4-2-11.mp3" #potato
  pro "Umm..."
  
  "I don't know what's going on with me, but it's like my brain has turned into mush."
  "Lauren must have assumed I said yes because she reads it anyway."

  play voice "4-2-12.mp3" #starleeter
  lov "Alex? Isn't he your brother?"
  
  "I nod."
  "Lauren hands my phone back to me and looks at me with a determined expression."
  
  play voice "4-2-13.mp3" #starleeter
  lov "Which way?"
  play voice "4-2-14.mp3" #potato
  pro "Huh?"
  play voice "4-2-15.mp3" #starleeter
  lov "Which hospital is it? I have a car, so I'll drive you there. It'll be quicker that way."
  play voice "4-2-16.mp3" #potato
  pro "Oh... you don't have to do that!"
  play voice "4-2-17.mp3" #starleeter
  lov "Just tell me where to go. Is there anyone we should pick up on the way?"
  
  "I immediately think about my little sister."
  "No, Maria's too young for this."
  "Yet, she's family. Doesn't she deserve to be there, even if it wrecks her?"
  "My little sister's the only good thing at home... I don't want to destroy her too."
  
  # TODO: show sky/clouds OR school carpark with dissolve

  play voice "4-2-18.mp3" #starleeter
  lov "Emily?"
  
  menu:
    "\"There's no one else.\"":
      jump day4s2nosister
    "\"We need to get Maria.\"":
      jump withsister
      
###########################################

label day4s2nosister:

  play voice "4-2-19.mp3" #starleeter
  lov "Understood. Don't worry, Emily. I'll get you there!"
  play voice "4-2-20.mp3" #potato
  pro "..."
  play voice "4-2-21.mp3" #potato
  pro "Thank you, Lauren."
  jump hospital2

###########################################

label withsister:

  $ bring_sis = True

  # TODO: CAREER+ 
  
  play voice "4-2-22.mp3" #starleeter
  lov "Maria's your sister, right?"
  play voice "4-2-23.mp3" #potato
  pro "Yes. She's in a different school, though, if that's—"
  play voice "4-2-24.mp3" #starleeter
  lov "That's not a problem. Just tell me the way."
  play voice "4-2-25.mp3" #potato
  pro "..."
  play voice "4-2-26.mp3" #potato
  pro "Thank you, Lauren."
  jump hospital2
  
###########################################

label hospital2:

  show hospital with dissolve

  if bring_sis:
    "As soon as we reach the hospital, Maria and I jump out of the car and run into the lobby."
  else:
    "As soon as we reach the hospital, I jump out of the car and run into the lobby."

  play voice "4-2-27.mp3" #potato
  pro "*huff* *huff*"
  play voice "4-2-28.mp3" #potato
  pro "Alex Westenson... which room is he in?"
  play voice "4-2-29.mp3" #skinimini
  nur "Please wait a moment, Miss."
  
  "The nurse isn't even looking for Alex's room. She's on the phone talking to her boyfriend or something."
  
  play voice "4-2-30.mp3" #potato
  pro "Hey! I'm talking to you! Where is Alex Westenson?!"
  play voice "4-2-31.mp3" #kaito
  mom "People are working hard in this hospital, Emily. Stop irritating the staff with your screaming."
  play voice "4-2-32.mp3" #potato
  pro "Mom? Where's Alex?"
  play voice "4-2-33.mp3" #kaito
  mom "What are you doing here? Why are you not in school?"
  if bring_sis:
    "And... you brought Maria with you?"
    play voice "4-2-34.mp3" #amree
    sis "..."
  play voice "4-2-35.mp3" #potato
  pro "Mom! Where the hell's Alex!"
  play voice "4-2-36.mp3" #kaito
  mom "Watch your tone with me, young lady. You're no longer a child."
  play voice "4-2-37.mp3" #kaito
  mom "Your brother's wound is being disinfected by a nurse in Ward C right now."
  play voice "4-2-38.mp3" #potato
  pro "Wounds? What are you talking about? What's happened to him?"  
  play voice "4-2-39.mp3" #kaito
  mom "Your brother, in his infinite wisdom, has stepped on a nail in a construction site near his school."
  play voice "4-2-40.mp3" #kaito
  mom "If the brightest of the three of you is this absent-minded, there's not much future for you."

  "Alex stepped on a nail?"
  "So, he's... fine?"
  "I feel like I've been holding my breath for hours, and I finally get to exhale right now."
  "Why the fuck did Mom send me a message like that?!"

  play voice "4-2-41.mp3" #starleeter
  lov "Emily!"
  
  "Lauren suddenly runs in from the elevator."
  
  play voice "4-2-42.mp3" #potato
  pro "Lauren, you didn't have to come in!"
  play voice "4-2-43.mp3" #starleeter
  lov "Nonsense, of course I had to. How's your brother doing?"
  play voice "4-2-44.mp3" #potato
  pro "Alex is fine. It's just a misunderstanding."
  
  "I tell Lauren what Mom just told me."
  
  play voice "4-2-45.mp3" #kaito
  mom "Hmph. I understand why your friend might think this is more serious than it is, but I don't see why you'd misunderstand, Emily. You know what your brother's like."
  play voice "4-2-46.mp3" #potato
  pro "Yes, I know, but I thought he..."

  "I stop myself just in time. I suddenly remember Mom doesn't know about the heroin."
  "Mom looks at me suspiciously. She notices my expression."
  
  play voice "4-2-47.mp3" #kaito
  mom "What were you about to say?"
  play voice "4-2-48.mp3" #potato
  pro "I-It's nothing."
  play voice "4-2-49.mp3" #kaito
  mom "...Hmph."
  
  "I can tell Mom doesn't believe me. She knows I'm hiding something."
  
  play voice "4-2-50.mp3" #kaito
  mom "Either way, shouldn't you be in class? Or are you planning to fail at high school? Don't use your brother as an excuse to laze around."

  "In an instant, Mom turns my mood from relief that Alex is safe, to annoyed."

  play voice "4-2-51.mp3" #potato
  pro "Fine. I'll go back to school. Lauren, would you mind?"
  play voice "4-2-52.mp3" #starleeter
  lov "Not at all."
  
  "Despite wasting Lauren's precious time for what turned out to be nothing, she seems to be in a much better mood than I am."

  if bring_sis:

    "Maria seems to be in a pretty good mood herself."

    play voice "4-2-53.mp3" #amree
    sis "I know Alex will be alright!"
    play voice "4-2-54.mp3" #amree
    sis "But even if he isn't, it'll still be fine, because we have each other, right?"
    
    "I smile at my little sister. She's incredibly strong for a girl her age."

  play voice "4-2-55.mp3" #starleeter
  lov "Emily, don't you want to talk to your brother before we leave?"
  
  "Do I?"
  "I'm not sure what I want, or how I'm feeling. My feelings are in a heap of mess."
  
  menu:
    "\"Yes, if you don't mind waiting.\"":
      jump talkbrother
    "\"No need. I'll see him at home.\"":
      jump nobrother

###########################################
      
label talkbrother:

  # TODO: FAMILY+ 
  play voice "4-2-56.mp3" #starleeter
  lov "Take your time, Emily. I'll wait here."
  if bring_sis:
    play voice "4-2-57.mp3" #starleeter
    lov "You going in, too, Maria?"
    
    "Maria looks up at me."
    
    play voice "4-2-58.mp3" #amree
    sis "Can I?"

    "I smile at her."

    play voice "4-2-59.mp3" #potato
    pro "Of course. Take my hand."

    "I nod at Lauren and we take off in our quest of finding our brother."
    "Purposefully avoiding Mom, we make our way over to Ward C."
   
  else:
    play voice "4-2-60.mp3" #potato
    pro "Thanks Lauren. I'll be quick."

    "I nod at my friend and take off in my quest of finding my brother."
    "Purposefully avoiding Mom, I make my way over to Ward C."

  show ward with dissolve

  "There he is, sitting on the edge of the bed with his right foot up."
  "The nurse is in the process of bandaging it."
  
  if bring_sis:
    play voice "4-2-61.mp3" #kujira
    bro "Emily? Maria? What are you two doing here?"
    play voice "4-2-62.mp3" #potato
    pro "We hear you've stepped on a nail."
  else:
    play voice "4-2-63.mp3" #kujira
    bro "Emily? What are you doing here?"
    play voice "4-2-64.mp3" #potato
    pro "I hear you've stepped on a nail."

  "Alex winces, though I'm not sure if it's from the memory, or from the bandaging."
  
  play voice "4-2-65.mp3" #kujira
  bro "Yeah. Not my finest moment. I had headphones on and wasn't paying attention."
  play voice "4-2-66.mp3" #potato
  pro "Mom doesn't seem too happy about what happened."
  play voice "4-2-67.mp3" #kujira
  bro "You have no idea. The entire ride over she keeps telling me how she has a busy day and how much I'm wasting her time."
  play voice "4-2-68.mp3" #kujira
  bro "It's not like I wanted to step on a nail, you know?"

  if bring_sis:
    play voice "4-2-69.mp3" #amree
    sis "I'm glad you're okay, Alex."
    play voice "4-2-70.mp3" #kujira
    bro "I'm glad I'm okay, too."
    play voice "4-2-71.mp3" #potato
    pro "Maria, you mind giving Alex and me a moment?"
    play voice "4-2-72.mp3" #amree
    sis "Sure!"

    "Like the good kid she is, Maria obediently steps out of the ward to give us some privacy."
  
  "I get quiet for a moment and Alex notices it."
  
  play voice "4-2-73.mp3" #kujira
  bro "What?"
  play voice "4-2-74.mp3" #potato
  pro "I'm just... glad you're alright."
  play voice "4-2-75.mp3" #kujira
  bro "Why wouldn't I be? It's just a bit of nail."
  pro "You know why."
  
  "Alex doesn't reply. From his expression, he knows I'm referring to the drugs he's been taking. The heroin."
  
  play voice "4-2-76.mp3" #potato
  pro "I'm sorry we got into a fight this morning. I didn't mean to get so angry."  
  play voice "4-2-77.mp3" #kujira
  bro "I'm sorry too."
  
  "For a short moment, we seem to understand each other."
  "But that moment passes quickly when Mom suddenly appears behind me."
  
  play voice "4-2-78.mp3" #kaito
  mom "Emily? What are you still doing here? I already said I'm not accepting this as an excuse for you to skip school!"
  play voice "4-2-79.mp3" #potato
  pro "I'm going, Mom. I just wanted to see Alex before I go."
  play voice "4-2-80.mp3" #kaito
  mom "You've seen him. Now go!"
  play voice "4-2-81.mp3" #potato
  pro "Okay!"
  
  if bring_sis:
    "I quickly leave the ward and grab my sister with me."
    
    play voice "4-2-82.mp3" #amree
    sis "Sorry, big sister, I didn't see Mom."
    play voice "4-2-83.mp3" #potato
    pro "It's not your fault, Maria."
    play voice "4-2-84.mp3" #amree
    sis "I'll do better next time."
    play voice "4-2-85.mp3" #potato
    pro "Don't worry about it."

  else:
    "I quickly leave the ward and make my way back to Lauren."
  
  "My friend's waiting by the elevators. She beams when she sees me. I can't help but smile a little back."
  
  play voice "4-2-86.mp3" #starleeter
  lov "How did it go?"
  play voice "4-2-87.mp3" #potato
  pro "As well as it can go."
  play voice "4-2-88.mp3" #starleeter
  lov "Ready to leave?"
  play voice "4-2-89.mp3" #potato
  pro "Yes. Let's head back to school."

  jump day4s3

###########################################

label nobrother:

  if bring_sis:
    play voice "4-2-90.mp3" #starleeter
    lov "Okay then. Let's go. Ready, everyone?"
    play voice "4-2-91.mp3" #amree
    sis "Ready!"
  else:
    play voice "4-2-92.mp3" #starleeter
    lov "Okay then. Let's go. Ready, Emily?"

  play voice "4-2-93.mp3" #potato
  pro "Yes. Let's head back to school."

  jump day4s3
  
###########################################

label carryon:

  "I quickly put my phone away before the teacher decides to confiscate it."
  
  play voice "4-2-94.mp3" #potato
  pro "Sorry, Miss Reynolds."
  
  "The teacher glares at me briefly before returning to her lesson."
  "Luckily, Miss Reynolds is pretty lenient, despite having a strict demeanor."
  ### TODO: Lauren sitting next to or behind Emily in class?
  "As we return to our lesson, however, I feel Lauren tapping on my shoulder."
  
  play voice "4-2-95.mp3" #starleeter
  lov "What's wrong?"
  play voice "4-2-96.mp3" #potato
  pro "Nothing. Nothing's wrong."
  play voice "4-2-97.mp3" #starleeter
  lov "Are you sure?"
  
  "Lauren glances at where I put my cellphone. It's clear she knows that something's up."
  
  play voice "4-2-98.mp3" #potato
  pro "Nothing's wrong."

  "What's the saying?"  
  "If I say something enough times, it'll become true. Is that right?"
  "Yes, that sounds right."
  "Nothing's wrong."
  "Nothing's wrong."
  "Nothing's wrong..."

  # TODO: Fade to a short dream scene at home... foreshadow the bad dream end.
  show dhome with dissolve

  play voice "4-2-99.mp3" #kujira
  dbro "Hey sis, what are you doing?"
  play voice "4-2-100.mp3" #potato
  pro "Nothing. Just daydreaming."
  play voice "4-2-101.mp3" #kujira
  dbro "Is it a good dream?"
  play voice "4-2-102.mp3" #potato
  pro "..."
  play voice "4-2-103.mp3" #potato
  pro "No, it isn't."

  show classroom with dissolve

  # TODO: School bell!!
  
  "Before I know it, class is over."
  "I can tell from Miss Reynolds’ expression that she wants to talk to me."
  "So, I gather my things and leave before she has a chance to stop me."

  jump day4s3

###########################################

##label day4s3:

  #### JUMP TO DAY 4 SCENE 3, CLAIMED BY TUTTY

