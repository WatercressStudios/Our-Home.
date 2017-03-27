label day6s1:

    Pro "Hey, sis, time to go. I need to be at school at a reasonable time this morning, so open up."

    play voice "6-1-1.mp3" #amree
    Sis "J-just one second, just one more sock…"

    "Have you ever tried to hear someone whisper through a door? Yeah, that's what this is like, but it's my sister so it's even more difficult than that."

    "Thankfully, I'm used to this whole charade by now, so even if I misunderstood her exact words, I can put the puzzle together with relative ease."

    play voice "6-1-2.mp3" #potato
    Pro "Oof!"

    "Maria opens the door and runs right into me - she was probably expecting me to wait outside this time."

    play voice "6-1-3.mp3" #amree
    Sis "S-sorry!"

    "I don't blame her one bit. For some reason, I wanted to keep her a bit close to me this time around."

    play voice "6-1-4.mp3" #potato
    Pro "Ah, don't worry about it. I assume you're ready?"

    Si "Yeah…"

    play voice "6-1-5.mp3" #potato
    Pro "Alright, good."

    "Grabbing her hand in mine, we make our way towards her school, as we've done the last hundred times."

    "Her hand gets a little sweaty, which isn't the norm for her. She's nervous, but not in the manner she usually is."

    "Something's on her mind."

    play voice "6-1-6.mp3" #potato
    Pro "Hey, Maria?"

    play voice "6-1-7.mp3" #amree
    Sis "Yeah?"

    play voice "6-1-8.mp3" #potato
    Pro "What's wrong?"

    play voice "6-1-9.mp3" #amree
    Sis "Well…"

    "She kicks a rock, watching it soar off the side of the road. She fidgets, looking away and avoiding the question."

    play voice "6-1-10.mp3" #potato
    Pro "C'mon, I won't bite"

    play voice "6-1-11.mp3" #amree
    Sis "I'm… I'm worried about Alex."

    play voice "6-1-12.mp3" #potato
    Pro "Alex?"

    play voice "6-1-13.mp3" #amree
    Sis "Yeah. He's been acting really funny, and I don't like it. It's weird and not like him and kinda scary."

    "Symptoms of drug use. I've been noticing the same exact thing. If Maria's noticed it, then I'm almost positive the rest of the family has."

    "Harkening back to my late night conversation, Lauren recommended an intervention."

    "I wonder… would it help to have Maria join us?"

    "Is she old enough to even handle such a thing? Would she be able to keep it together, and would she be able to add anything to the conversation?"

    #Choice: involve her CAREER+1, don't involve her CAREER+0.

    menu:
        "We shouldn't subject her to what it could entail.":
            jump nosister

        "It's her brother, too. It's only fair.":
            $ yessister = True
            jump yessister

label nosister:

    "I elect not to say a thing. She's just not ready yet, and I'm not going to be held responsible for what could have happened if we included her."
    jump aftersister

label yessister:
    "It doesn't matter what I think. She's Alex's sister just as much as I am. We both care for him, and this is a family matter, for the family that matters."

    play voice "6-1-14.mp3" #potato
    pro "Truth be told, I'm worried too. Lauren noticed it as well. She recommended we hold an intervention - a little heart to heart session with him - so that we can try to help him get better."

    play voice "6-1-15.mp3" #potato
    pro "If you want to, you're invited. We're doing the research on it today."

    play voice "6-1-16.mp3" #amree
    sis "Oh! I'd love to."

    "That was easier than I thought it would be. She jumped at the occasion immediately, which isn't like her. She's normally much more shy and slower on the uptake than that."

    play voice "6-1-17.mp3" #potato
    pro "That settles it then! I'll make sure to pick you up when we're ready."

    play voice "6-1-18.mp3" #amree
    sis "Thank you… it means a lot. I really want to help him, even if I can't do too much…"

    play voice "6-1-19.mp3" #potato
    pro "Of course."
    jump aftersister

label aftersister:

    "Moving forward, we share some more idle chatter on our way to her school."

    "It's wonderful, really, to have her school be so close, and on the way to mine. It's one of the few conveniences I'm afforded in this life. It lets me keep a close eye on Maria, as well."

    "The path's lined with trees, the road quiet, the wind still. It's straight out of a picture. It's a good feeling, being in the now. Just quieting down, and listening to what's around you. Observing from the outside."

    "Sometimes I feel that acting upon the world around me might be better, but I don't think about that often. Generally, in my experience, it's best not to. Maybe I should, though? Especially with what's happened."

    "I guess this intervention is my way of breaking out into the world, even if it wasn't exactly my idea."

    "I'll just have to wait and see."

    jump day6s2