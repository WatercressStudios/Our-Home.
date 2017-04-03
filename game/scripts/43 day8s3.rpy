label day8s3:

    #Probably doesn’t require a transition from 8.2

    play ambience nightsuburb fadein 3.0
    play music bgmdad fadeout 1.0 fadein 0.0

    "My phone rings from the pocket of my skirt."
    voice "8-3-1.mp3" #potato
    pro "Yeah, Dad?"
    voice "8-3-2.mp3" #lacTheWatcher
    dad "Hey, Emily. Where are you?"
    voice "8-3-3.mp3" #potato
    pro "Walking home. Lauren and I hung out to... get my mind off things."
    voice "8-3-4.mp3" #lacTheWatcher
    dad "...Right."
    "A brief silence hangs in the call."
    voice "8-3-5.mp3" #lacTheWatcher
    dad "The doctor called. Alex woke up fifteen minutes ago and he’s fine. He’s… fine."
    "Dad’s tearful relief is palpable in his voice."
    voice "8-3-6.mp3" #lacTheWatcher
    dad "She said we can visit him. But I’m busy with work and won’t be able to make it."
    voice "8-3-7.mp3" #lacTheWatcher
    dad "Visiting hours end at 9, can you go visit him?"
    voice "8-3-8.mp3" #lacTheWatcher
    dad "Maybe you could see if Mom is home? I’m sure she’d drive you."
    voice "8-3-9.mp3" #potato
    pro "...I can make it myself."
    voice "8-3-10.mp3" #potato
    pro "But I’ll be there. Do you know the bus schedule to make it over there?"
    "It’s a bit of a long way to the hospital. Since we were in another town when we found him, the place he’s staying is too far to reach by foot."
    voice "8-3-11.mp3" #lacTheWatcher
    dad "Let me look it up."
    voice "8-3-12.mp3" #lacTheWatcher
    dad "There’s a stop leaving near your school in 15 minutes, I’ll text you some directions in a little bit."
    voice "8-3-13.mp3" #lacTheWatcher
    dad "…Thank you, Emily."
    voice "8-3-14.mp3" #potato
    pro "…It’s not worth thanking me for, dad—"
    voice "8-3-15.mp3" #lacTheWatcher
    dad "He wouldn’t be here without you. You know that, right?"
    voice "8-3-16.mp3" #potato
    pro "But…"
    "Even so, I failed him. I should have done something long before then. So what if I found him?"
    voice "8-3-17.mp3" #lacTheWatcher
    dad "Thank you, Emily. It’s because of you that he didn’t have to be alone. I can thank you for that, can’t I?"
    voice "8-3-18.mp3" #potato
    pro "I guess you’re right, dad."
    voice "8-3-19.mp3" #lacTheWatcher
    dad "Thank you."
    voice "8-3-20.mp3" #lacTheWatcher
    dad "And—I’m sorry I couldn’t be there for all of you, either. I’ll…make certain to change that. I promise."
    voice "8-3-21.mp3" #potato
    pro "Later, dad."
    voice "8-3-22.mp3" #lacTheWatcher
    dad "Bye, Emily."

    #Transition to bus

    scene bus with dissolve

    "With nothing to do but wait until I make it to the next town, my mind begins to wander."
    "Lauren distracted me for a little while, but now that I’m alone I can’t help but dwell on all that’s happened."

    "Alex almost died last night. Alex almost died because I fucked up. He trusted me to get rid of the drugs, and I fucked up. Mom turned into a lunatic again..."

    #If player yelled at Alex in d7s1
    "And I even broke down and yelled at him, too."

    #If player didn’t yell at Alex in d7s1
    "But I didn’t do anything to help him."

    "He ran away and almost got himself killed, and I told myself it wouldn’t be a big deal."
    "I failed him. I wanted to ignore it. I avoided thinking about it because I didn’t want to care. I told myself whatever happened to him wouldn’t be a big deal. I justified abandoning him because it was too much of a hassle. I hurt him because I didn’t want to make an effort."
    "And worse, I’m not even strong enough to hate myself for it. Maybe if someone would, it wouldn’t be so painful. Maybe being scorned would let me forgive myself."

    if goodtalk:

        #TODO: Show flashback to d6s3 line where bro says "But thinking about it, I should shoot for something better than self-pity."
        "That’s right."
        "I’m not proud of all of the decisions I’ve made, but acting on good thoughts will do a lot more good than thinking about bad ones."
        "I manage to stay positive for the rest of the trip to the hospital."

    else:

        "I keep stewing on thoughts like these until I finally make it to the hospital."

    #Transition to hospital

    scene hospital dark with dissolve

    "A sprawling, twenty-story complex that feels like a cross between a toy store and a funeral, with pristine white walls and windows clear as an untouched ocean."
    "The woman at the front desk lets me know where Alex’s room is. Room 5-22, a solo room in the east wing."

    #Transition to hospital hallway

    scene hospitallobby with dissolve

    "A door stands ahead of me. When I knock, the inside rings hollow, yet the door barely shakes in response. It feels different from the cheap doors at school."
    voice "8-3-23.mp3" #potato
    pro "H-hello?"
    "This… says it’s the right place, right? The plate next to the door is correct, right?"
    "The handle on the door feels heavy. Even at the slightest of turns, heavy locks come tumbling and turning to allow passage, swerving into place until the door moves freely."
    #Creaking sound effect
    "I pull it open, creaking along the way until I make it through, releasing my hand as it seals once more."

    show hospitalroom with dissolve

    voice "8-3-24.mp3" #potato
    pro "…Alex?"
    "A heavy silence blankets the room. Even straining to listen, I can’t hear anything but my own breath."
    "All around, the brilliant white reflects the sunlight from the window into a blinding shimmer from every direction. My arms tremble at the weight of the air. My body shakes from the chilling sensation from every direction."
    "A bed rests in the middle of the room. With white, soothing blankets spread above them and a boy lying gently upon it."

    show bro sad1 with dissolve

    voice "8-3-25.mp3" #kujira
    bro "Hey, Emily."
    "Alex sits up from his bed and turns his head. His skin is pale – a flushed white color, with arms even thinner than before that might as well be skin and bones, and his hair is even more of a mess than usual."
    voice "8-3-26.mp3" #potato
    pro "H-how are you feeling? Does your head hurt? I can get a doctor if you need anything—"
    voice "8-3-27.mp3" #kujira
    bro "Please, there’s no need. They already did all the basics when I first woke up. I’m just waiting for my first meal, honest."
    voice "8-3-28.mp3" #potato
    pro "...Are you sure?"
    voice "8-3-29.mp3" #kujira
    bro "Yeah, I’m sure."

    "We spent the next half an hour going back and forth between awkward silences and petty talk."
    "At some point, we joked about how we didn’t actually know what hospital food was like, and when his dinner came around, we ended up making fun of how weird the pudding tasted."
    "We laughed and made goofy puns about how Dad used to act on vacation or whatever funny stories we had about our childhoods."
    "Somehow, we both avoided mentioning Maria. I don’t think he’s ready to talk about her."
    "…Even then, it’s been a long time since we’ve spent time like that together."

    voice "8-3-30.mp3" #potato
    pro "I’m sorry, Alex."
    voice "8-3-31.mp3" #kujira
    bro "E-eh? For what?"
    voice "8-3-32.mp3" #potato
    pro "I mean, I… I should have done a better job of things. I should have been able to keep something like this from happening to begin with."
    voice "8-3-33.mp3" #kujira
    bro "N-no, you don’t need to say something like that. Honest!"
    voice "8-3-34.mp3" #kujira
    bro "It’s just… what happened was my fault, Emily. I should have been stronger. I should have found a better way to deal with things."
    voice "8-3-35.mp3" #kujira
    bro "Do you know what it’s like to have friends, Emily?"
    voice "8-3-36.mp3" #potato
    pro "Hey, what’s that supposed to mean?"
    voice "8-3-37.mp3" #kujira
    bro "Sorry, I was just thinking. It feels a little bit different from home, somehow. It was strange when I first found it. It felt nice, but I was worried about how… alien it all felt. It made being at home a lot more painful."
    voice "8-3-38.mp3" #kujira
    bro "Like, I ended up going to this friend’s house once for homework – that short kid that hangs out with the rest of our group. I helped him out with math for a few hours, and his parents were so impressed they just up and pulled out a bucket of ice cream."
    voice "8-3-39.mp3" #kujira
    bro "It was strange and weird and just confusing and almost gave me a heart attack."
    voice "8-3-40.mp3" #potato
    pro "The ice cream?"
    voice "8-3-41.mp3" #kujira
    bro "Not that! It felt like I mattered somehow. It was better there than at home. Like no matter what crazy shit they would pull it felt like they were happy compared to everyone else."
    voice "8-3-42.mp3" #kujira
    bro "Then when I was laying around in my room, feeling scared to leave because something could happen between me and mom. I wanted to feel like I mattered again. Staying at home with everyone acting like they do made me hate myself. It was painful."
    voice "8-3-43.mp3" #kujira
    bro "I just… didn’t want to be alone anymore. Then I tried to figure out how to change that, and the drugs happened and someone gave me a bit of heroin and… Well, I fucked up."

    voice "8-3-44.mp3" #kujira
    bro "Every day it’s just inching closer and closer to some shit blowing up between us or between me and mom over the littlest things."
    voice "8-3-45.mp3" #kujira
    bro "It felt like I had to fight back in order to deal with it. Like I had to shout and scream…"
    voice "8-3-46.mp3" #kujira
    bro "...because standing there and taking it meant losing what little strength I had left."
    voice "8-3-47.mp3" #kujira
    bro "I couldn’t handle that and ended up making it worse for everyone."
    "We meet in a gentle embrace. A hug of some kind, I’d suppose. It’s been a long time since I've shared something like this with someone other than Maria."
    "It’s warm and close, yet it feels… faintly distant, somehow."
    voice "8-3-48.mp3" #kujira
    bro "I’m sorry, Emily. Thank you."
    voice "8-3-49.mp3" #potato
    pro "…I forgive you, Alex. Sorry that things turned out like this."
    voice "8-3-50.mp3" #potato
    pro "Someday things will be better for us, right?"
    voice "8-3-51.mp3" #kujira
    bro "Yeah. I’ll be looking forward to it."
    "We part the hug after a few more seconds. Another awkward silence ensues, but it’s over quickly."
    voice "8-3-52.mp3" #kujira
    bro "A-anyways! You can go ahead and leave, Emily. I don’t mind."
    voice "8-3-53.mp3" #potato
    pro "What do you mean!? I’ve been waiting all day for you to wake up and you’re telling me to go home already?"
    voice "8-3-54.mp3" #kujira
    bro "T-that’s not it! That’s not it at all!"
    voice "8-3-55.mp3" #kujira
    bro "I just…think a bit of time alone would be helpful for me right now. You can come back tomorrow and we can talk all you want."
    voice "8-3-56.mp3" #potato
    pro "Promise?"
    voice "8-3-57.mp3" #kujira
    bro "Yes. Promise."
    voice "8-3-58.mp3" #potato
    pro "…Alright, alright. You’ll be okay for the night then?"
    voice "8-3-59.mp3" #kujira
    bro "Y-yeah. I’ll be fine."
    voice "8-3-60.mp3" #potato
    pro "Later, Alex."
    voice "8-3-61.mp3" #kujira
    bro "Later."

    "But as I turn around and start walking, he stops me,"

    voice "8-3-62.mp3" #kujira
    bro "Emily...."
    voice "8-3-63.mp3" #kujira
    bro "Where’s Mom and Dad?"
    voice "8-3-64.mp3" #potato
    pro "Dad wants to see you but can’t get away from work. Mom… well she’ll turn up when she’s ready."
    voice "8-3-65.mp3" #kujira
    bro "And what about… what about..."

    "Alex can’t bring herself to say her name, but I know who he’s asking about."

    voice "8-3-66.mp3" #potato
    pro "Maria’s fine. She wants to see you, too. Should I bring her next time?"
    voice "8-3-67.mp3" #kujira
    bro "Don’t. Please."
    voice "8-3-68.mp3" #potato
    pro "Okay, I won’t. When you’re ready. I’ll go now, Alex."

    "He doesn’t reply, so I walk out into the hall and close Alex’s door behind me."
    "Apparently Dad texted me sometime while we were talking."

    scene hospitallobby with dissolve

    "‘How’s Alex doing? Did you get to see him?’"
    "I sit down on a nearby chair and start tapping out a response."
    "'Alex is doing fine – was just about to leave the hospital. He still looks a little bit sickly, but it feels like he’s improving at least. Maybe soon he’ll'"
    #maybe some sound effects? Something from the VAs?
    "I’m distracted by a barely audible sound from the other side of the door."
    "I probably shouldn’t, but my curiosity makes me press my ear against the door."
    "...Ah."
    "Crying."
    "He sounds softer than he used to be. I hope he’ll be home soon."

    jump day8s4
