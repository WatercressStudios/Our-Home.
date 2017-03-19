label day4s4:

  # TODO: hide background with dissolve

  "As I approach my front door, I catch my smiling face in the reflection of a window."
  "At first I'm confused. What am I so happy about? It must be because Alex is fine, I tell myself."
  "Yet, my mind wanders over to Lauren and I replay the time we spent together in my head."
  
  # TODO: show mom's angry expression against the black background. Tint it grey if possible, since she's in the dark and I want her to look scary.
  play voice "4-4-1.mp3" #kaito
  mom "Emily Westenson."
  
  "I freeze."
  "Mom's sitting in the dining room by herself in the dark. "
  
  # TODO: play clicking SFX of a lamp being turned on.
  # TODO: show diningroom background instantly

  play voice "4-4-2.mp3" #kaito
  mom "What do you think you're doing?"
  play voice "4-4-3.mp3" #potato
  pro "M-Mom? W-What do you mean—"
  play voice "4-4-4.mp3" #kaito
  mom "Don't be coy. You know exactly what this is about, Emily Westenson."

  "My heart's racing, thumping painfully in my chest."
  "Did Mom find out I was thinking about Lauren?"
  "I open my mouth and try to stammer out a denial, but Mom cuts me off again."
  
  play voice "4-4-5.mp3" #kaito
  mom "What time do you think it is?"
  
  "I'm not sure if I'm supposed to speak, so I don't say anything."
  
  play voice "4-4-6.mp3" #kaito
  mom "Speak when you're spoken to, Emily."
  
  "My eyes dart over to the wall clock in the kitchen."
  
  play voice "4-4-7.mp3" #potato
  pro "Umm... it's nine o'clock..."
  play voice "4-4-8.mp3" #kaito
  mom "Did I give you permission to be out so late?"
  play voice "4-4-9.mp3" #potato
  pro "I-I sent you a text message about the drama club—"
  play voice "4-4-10.mp3" #kaito
  mom "Drama club!"
  play voice "4-4-11.mp3" #kaito
  mom "Do you even have any interest in acting? Why are you wasting your time doing pointless things?!"
  
  menu:
    "\"I'm helping a friend.\"":
      jump helplauren
    "Don't say anything.":
      jump keepsilent
  
###########################################

label helplauren:

  play voice "4-4-12.mp3" #kaito
  mom "So you're not even there for yourself?"

  "I'm not sure what the right answer is, so I just nod a little. Unfortunately, that seems to make Mom angrier."
  
  play voice "4-4-13.mp3" #kaito
  mom "All you're doing is helping someone else with {i}their{/i} dream?!"
  play voice "4-4-14.mp3" #kaito
  mom "Have you no dream of your own?"
  play voice "4-4-15.mp3" #potato
  pro "I-I do..."
  play voice "4-4-16.mp3" #kaito
  mom "Could have fooled me."
  
  jump momcareer
  
###########################################

label keepsilent:

  play voice "4-4-17.mp3" #kaito
  mom "You're not even going to deny it?"

  "I search my head for the right answer, but I come up with nothing. So I continue looking at my feet silently."

  play voice "4-4-18.mp3" #kaito
  mom "You have no drive for success, girl."
  play voice "4-4-19.mp3" #kaito
  mom "It's hard to believe you're my child."

  jump momcareer

###########################################

label momcareer:

  "Mom doesn't say anything else for about minute, so I tentatively glance up at her."
  
  play voice "4-4-20.mp3" #potato
  pro "Umm, may I go to my room now?"
  play voice "4-4-21.mp3" #kaito
  mom "I had to take care of your fool of a brother all day today."
  play voice "4-4-22.mp3" #potato
  pro "Huh? Is Alex okay? Did something else happen?"
  play voice "4-4-23.mp3" #kaito
  mom "You're supposed to be at home taking care of your siblings."
  play voice "4-4-24.mp3" #kaito
  mom "Honestly, I take my eyes off for a minute and one of you manage to stab yourself in the foot."
  play voice "4-4-25.mp3" #kaito
  mom "I don't have time to deal with all of your shenanigans, which is why you need to stop acting like a child and step up for once, Emily."
  play voice "4-4-26.mp3" #kaito
  mom "Do I really have to explain to you that, as the eldest, you’re responsible for your siblings?"

  "Not this again..."
  "I keep my mouth shut and my eyes down."

  play voice "4-4-27.mp3" #kaito
  mom "I had to take care of my family at your age, and I still managed to seize the career that I wanted."
  play voice "4-4-28.mp3" #kaito
  mom "And you? You're just lazing around without a purpose. You have no idea how lucky you are with all the opportunity just handed to you. And what do you do with these opportunities? You waste them!"

  # TODO: hide background with dissolve
  "Mom continues her lecture for a few more minutes as I tune out everything around me."

  # TODO: hide mom
  "By the time she finally finishes, it's already past nine thirty.."

  show bedroom with dissolve

  "Whatever good mood I had before is thoroughly rinsed away."

  play voice "4-4-29.mp3" #potato
  pro "I still have a little time to do some sewing..."
  play voice "4-4-30.mp3" #potato
  pro "Huh?"
  
  "My sewing machine is broken. Of course it is."
  "I sigh."
  
  # sfx of some strange sounds next door (brother's going through a rough withdrawal)
  "TAP! TAP! TAP!"
  
  play voice "4-4-31.mp3" #potato
  pro "What the...?"
  
  "That strange noise is coming from Alex's room. It sounds like he's impatiently tapping on his desk or something."
  "I walk up to the wall connecting our rooms and knock on it with my knuckles."
  
  play voice "4-4-32.mp3" #potato
  pro "Alex, what's going on in there?"
  play voice "4-4-33.mp3" #kujira
  bro "Go away!"
  
  "...whatever. I'm going to bed."
  
  jump dream5

