label day9s1:

    scene bedroom with dissolve
    
    "Nothing, apparently. I'll dream about nothing."

    "It's a little disconcerting, but I guess there's a legitimate reasoning behind it."

    "This was my choice. Time to live with it."

    "It's time to wake up, get ready, and get Maria to school. Everything has to seem okay, even if it's not."

    scene hallway with dissolve
    
    "I go through the motions, dressing up and knocking on Maria's door as I pass by."

    scene livingroom with dissolve
    
    "Once again, the house is lonely. I rest my back against the couch, resisting my drowsiness without much success."

    "Mentally, I'm exhausted. Physically, however, I feel better than I have in a very long time."

    "The quality of my sleep has improved, at least for today. Something about REM sleep, I'm not sure."

    "Poke poke poke…"

    "Something taps my head lightly. Something small and delicate, but oddly capable."

    show sis happy2 with dissolve
    
    voice "9-1-1.mp3" #amree
    sis "I'm hungry…"

    voice "9-1-2.mp3" #potato
    pro "...SHIT."

    "I didn't make any food, and Mom isn't home to make anything either. Fuck me, I totally didn't think about that. So much for making things seem normal…"

    voice "9-1-3.mp3" #potato
    pro "Well, fuck, I totally forgot. We don't really have time to get food on the way to school either… I'm sorry."

    show sis sad1 with dissolve
    
    "She nods with a pout, offering me a hand to stand up from the couch."

    "I accept it, putting most of my weight on the couch so I don't destroy her poor little arms."

    voice "9-1-4.mp3" #amree
    sis "It's okay. I'll eat at school anyways."

    voice "9-1-5.mp3" #potato
    pro "You have enough money for that?"

    voice "9-1-6.mp3" #amree
    sis "Yeah, Dad gave me some."

    voice "9-1-7.mp3" #potato
    pro "Hmm, that was good of him."

    voice "9-1-8.mp3" #amree
    sis "It was…"

    voice "9-1-9.mp3" #potato
    pro "Okay! So, off to school then?"

    voice "9-1-10.mp3" #amree
    sis "Yep."

    scene siswalk with dissolve
    
    "With that, we're off. The trip starts off awfully quiet, my sister avoiding eye contact and being her normal shy self."

    "It wouldn't be out of the ordinary, if she weren't holding my hand with the strength of a hydraulic press."

    voice "9-1-11.mp3" #potato
    pro "Hey, sis, is everything okay?"

    show sis worry2 with dissolve
    
    voice "9-1-12.mp3" #amree
    sis "Is Mom ever coming home?"

    "Jesuuus."

    voice "9-1-13.mp3" #potato
    pro "That's… that's a complicated question. I hope so."

    voice "9-1-14.mp3" #amree
    sis "You do?"

    voice "9-1-15.mp3" #potato
    pro "I mean, she's made a lot of mistakes, but she's still part of the family, you know?"

    voice "9-1-16.mp3" #amree
    sis "D-don't you think things are... better without her?"

    voice "9-1-17.mp3" #potato
    pro "I don't think so… at least, not in the way I would want."

    voice "9-1-18.mp3" #potato
    pro "Sure, arguments happen less, and she's not around to talk our ears off about how we’re useless wastes of space, but…"

    "But? I'm not making the best argument here."

    voice "9-1-19.mp3" #potato
    pro "But she might be able to change, get better, if we try hard enough."

    voice "9-1-20.mp3" #amree
    sis "Yeah… I miss her. I wish she'd let us know when she's coming back home…"

    voice "9-1-21.mp3" #potato
    pro "I could ask her?"

    "She looks over to me with a jerk of her head."

    voice "9-1-22.mp3" #amree
    sis "You could?"

    voice "9-1-23.mp3" #potato
    pro "Why not?"

    "Pulling out my phone with my free hand, I dial her number."

    "The look on my sister's face is nothing short of sheer terror. She's not ready for this, and odds are, neither am I." 

    "Perhaps I shouldn't have done this so suddenly, without thoughts of the consequences."

    "We sit in suspense."

    "The phone rings, and rings, and rings…"

    "And goes to voicemail."

    voice "9-1-24.mp3" #potato
    pro "Well, at least we tried."

    voice "9-1-25.mp3" #amree
    sis "Could you text her? Maybe then…"

    #Choice to send text message to mom (FAMILY+1) or not (FAMILY+0).

    #Decision here
    "Should I  text her?"

    #Choices
    menu:
        "No, she needs time to recover.":
            jump recover
        "Yes, she needs to know we care.":
            $ family += 1
            jump showcare

label recover:

    voice "9-1-26.mp3" #potato
    pro "I don't think that would be the best plan, honestly. She needs some time to recover. Shit's been… a mess lately."

    "Pardon my french, but I can't sugarcoat it any longer."

    "She's aware of how messy the situation is, Maria, so I shouldn't hide it from her. She's mature enough, these days."

    "She nods in half agreement, and doesn't push the discussion any further."

    jump day9s1continue

label showcare:

    voice "9-1-27.mp3" #potato
    pro "Yeah, that's a good idea. Even if she doesn't answer, at least she'll know we want her around, yeah?"

    "I text her something simple, 'I hope things are okay. We need you back home soon.'"

    "I put my phone away, not expecting any response."

    voice "9-1-28.mp3" #amree
    sis "Thank you… I'm worried about her."

    voice "9-1-29.mp3" #potato
    pro "I am too, I am too."

    jump day9s1continue

label day9s1continue:

    "A painful silence hangs over the both of us. Neither of us are really trying to open up."

    "I keep glancing over to Maria, her eyes glued to the sidewalk. Her mouth curls."

    show sis worry1 with dissolve
    
    "Maria stops along the sidewalk, unmoving. Her head tilts forward. I can't see her face."

    voice "9-1-30.mp3" #amree
    sis "Emily… are we still a family?"

    voice "9-1-31.mp3" #amree
    sis "Mom… isn't here. I-I don't know when she's coming back."

    voice "9-1-32.mp3" #amree
    sis "And Big Bro… A-Alex is gone too…"

    voice "9-1-33.mp3" #potato
    pro "...I don't know what's going to happen, Maria, but…"

    voice "9-1-34.mp3" #potato
    pro "We're still a family. You'll always have me, okay?"

    show sis cry with dissolve
    
    "I hear her fighting back tears… she was sobbing."

    voice "9-1-35.mp3" #amree
    sis "Alex… hates me, doesn't he…?"

    voice "9-1-36.mp3" #potato
    pro "No, no, of course he doesn't…! He couldn't hate you! He's just… he's in a lot of pain."

    "I had to think of something. Who knows what the Hell's been crossing his mind lately…" 

    voice "9-1-37.mp3" #amree
    sis "Mommy told me not to cry in public…!"

    voice "9-1-38.mp3" #potato
    pro "No, no, Maria, come here…!"

    "I hold her tightly to my chest. Oh God, now I'm gonna start crying soon."

    voice "9-1-39.mp3" #potato
    pro "Maria, it's okay, I'm here… we can go home, do you want to go home!?"

    "Maria rubs her head into my chest. I think she.. she's shaking her head."

    voice "9-1-40.mp3" #amree
    sis "*sniff* I… I miss Alex… I miss Mom, and Dad, and…"

    voice "9-1-41.mp3" #amree
    sis "I want my family back!"

    voice "9-1-42.mp3" #potato
    pro "It's okay… it's okay…"

    "Maria was being so strong for so long. She didn't think much of yesterday…"

    "But now the reality's hitting her. A poor, innocent girl like her… it's too much to bear."

    "I gently hold her head, kneeling down so our eyes meet."

    voice "9-1-43.mp3" #potato
    pro "Maria… I'm gonna see Alex at the hospital today, alright? I'll ask him if I can bring you next time."

    voice "9-1-44.mp3" #amree
    sis "O… okay… I miss him…"

    voice "9-1-45.mp3" #potato
    pro "I know… it's so hard, and you're being so strong. I want you to be strong for a little bit longer, okay?"

    voice "9-1-46.mp3" #potato
    pro "I won't abandon you. I'll see you at home. So no more tears, okay?"

    voice "9-1-47.mp3" #amree
    sis "...I… I know you won't leave me, sis…"

    "We hold each other for a little while longer…" 

    jump day9s2