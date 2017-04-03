label day4s4:

  scene house dark with dissolve
  # TODO: hide background with dissolve

  "As I approach my front door, I catch my smiling face in the reflection of a window."
  "At first I'm confused. What am I so happy about? It must be because Alex is fine, I tell myself."
  "Yet, my mind wanders over to Lauren. I keep replaying the time we spent together in my head."
  
  scene black with dissolve
  "God, it's late. If I'm in my room, Mom won't suspect a thing."
  "Let's go let's go... ah, the stairs are right there!"

  
  # TODO: show mom's angry expression against the black background. Tint it grey if possible, since she's in the dark and I want her to look scary.
  voice "4-4-1.mp3" #kaito
  show mom angry2
  mom "Emily Westenson."
  
  "I freeze."
  "Mom's sitting in the dining room by herself in the dark. "
  
  # TODO: play clicking SFX of a lamp being turned on.
  # TODO: show diningroom background instantly

  scene diningroom dark with dissolve
  show mom angry2 with dissolve
  voice "4-4-2.mp3" #kaito
  mom "What do you think you're doing?"
  voice "4-4-3.mp3" #potato
  pro "M-Mom? W-What do you mean—"
  show mom angry1 with dissolve
  voice "4-4-4.mp3" #kaito
  mom "Don't be coy. You know exactly what this is about, Emily Westenson."

  "My heart's racing, thumping painfully in my chest."
  "Did Mom find out I was thinking about Lauren?"
  "I open my mouth and try to stammer out a denial, but Mom cuts me off again."
  
  voice "4-4-5.mp3" #kaito
  mom "What time do you think it is?"
  
  "I'm not sure if I'm supposed to speak, so I don't say anything."
  
  voice "4-4-6.mp3" #kaito
  show mom angry2 with dissolve
  mom "Speak when you're spoken to, Emily."
  
  "My eyes dart over to the wall clock in the kitchen."
  
  voice "4-4-7.mp3" #potato
  pro "Umm... it's nine o'clock..."
  voice "4-4-8.mp3" #kaito
  show mom angry1 with dissolve
  mom "Did I give you permission to be out so late?"
  voice "4-4-9.mp3" #potato
  pro "I-I sent you a text message about the drama club—"
  voice "4-4-10.mp3" #kaito
  show mom sad3 with dissolve
  mom "Drama club!"
  voice "4-4-11.mp3" #kaito
  mom "Do you even have any interest in acting? Why are you wasting your time doing pointless things?!"
  
  menu:
    "\"I'm helping a friend.\"":
      jump helplauren
    "Don't say anything.":
      jump keepsilent
  
###########################################

label helplauren:


  voice "4-4-12.mp3" #kaito
  show mom angry2 with dissolve
  mom "So you're not even there for yourself?"

  "I'm not sure what the right answer is, so I just nod a little. Unfortunately, that seems to make Mom angrier."
  
  voice "4-4-13.mp3" #kaito
  show mom sad1 with dissolve
  mom "All you're doing is helping someone else with {i}their{/i} dream?!"
  voice "4-4-14.mp3" #kaito
  mom "Have you no dream of your own?"
  voice "4-4-15.mp3" #potato
  pro "I-I do..."
  voice "4-4-16.mp3" #kaito
  show mom angry2 with dissolve
  mom "Could have fooled me."
  
  jump momcareer
  

###########################################

label keepsilent:

  voice "4-4-17.mp3" #kaito
  show mom angry1 with dissolve
  mom "You're not even going to deny it?"

  "I search my head for the right answer, but I come up with nothing. So I continue looking at my feet silently."


  show mom sad2 with dissolve
  voice "4-4-18.mp3" #kaito
  mom "You have no drive for success, girl."
  voice "4-4-19.mp3" #kaito
  mom "It's hard to believe you're my child."
  jump momcareer

###########################################

label momcareer:


  "Mom doesn't say anything else for about minute, so I tentatively glance up at her."
  
  voice "4-4-20.mp3" #potato
  pro "Umm, may I go to my room now?"
  show mom angry1 with dissolve
  voice "4-4-21.mp3" #kaito
  mom "I had to take care of your fool of a brother all day today."
  voice "4-4-22.mp3" #potato
  pro "Huh? Is Alex okay? Did something else happen?"
  voice "4-4-23.mp3" #kaito
  mom "You're supposed to be at home taking care of your siblings."
  voice "4-4-24.mp3" #kaito
  show mom sad3 with dissolve
  mom "Honestly, I take my eyes off for a minute and one of you manage to stab yourself in the foot."
  voice "4-4-25.mp3" #kaito
  show mom angry2 with dissolve
  mom "I don't have time to deal with all of your shenanigans, which is why you need to stop acting like a child and step up for once, Emily."
  voice "4-4-26.mp3" #kaito
  mom "Do I really have to explain to you that, as the eldest, you’re responsible for your siblings?"

  "Not this again..."
  "I keep my mouth shut and my eyes down."

  voice "4-4-27.mp3" #kaito
  show mom surprise with dissolve
  mom "I had to take care of my family at your age, and I still managed to seize the career that I wanted."
  show mom angry2 with dissolve
  voice "4-4-28.mp3" #kaito
  mom "And you? You're just lazing around without a purpose. You have no idea how lucky you are with all the opportunity just handed to you. And what do you do with these opportunities? You waste them!"

  scene black with dissolve
  "Mom continues her lecture for a few more minutes as I tune out everything around me."
  "By the time she finally finishes, it's already past nine thirty.."

  scene bedroom night with dissolve

  "I solemnly return to my room, having been thoroughly talked at but good."
  "Whatever good mood I had before is thoroughly rinsed away."

  voice "4-4-29.mp3" #potato
  pro "I still have a little time to do some sewing..."
  
  scene sewingkit with dissolve
  
  "Turning my attention to ye olde faithful sewing machine, I steel myself for the coming work session."
  "...There's only one problem."
  
  voice "4-4-30.mp3" #potato
  pro "Huh?"
  
  "It just stopped..."
  "I push my foot down on the pedal again and again but it refuses to work."
  "My sewing machine is dead. Of course it is."
  "I sigh."
  
  scene bedroom night with dissolve
  
  # sfx of some strange sounds next door (brother's going through a rough withdrawal)
  "TAP! TAP! TAP!"
  
  voice "4-4-31.mp3" #potato
  pro "What the...?"
  
  "That strange noise is coming from Alex's room. It sounds like he's impatiently tapping on his desk or something."
  "I walk up to the wall connecting our rooms and knock on it with my knuckles."
  
  voice "4-4-32.mp3" #potato
  pro "Alex, what's going on in there?"
  voice "4-4-33.mp3" #kujira
  bro "Go away!"
  
  "...whatever. I'm going to bed."
  
  scene black with dissolve
  
  "... ... ..."
  
  jump dream5

