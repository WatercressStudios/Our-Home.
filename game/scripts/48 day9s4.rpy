label day9s4:
    scene house with dissolve
    show lov happy2bh
    "Lauren is hanging around outside by the time I get back from the hospital."
    "Honestly, I didn’t expect her to get here so fast."
    play music bgmlov2 fadeout 1.0 fadein 0.0
    voice "9-4-1.mp3" #starleeter
    lov "Hey! I was starting to worry the neighbours would call the police."
    "I shake my head and let her in."
    scene livingroom with dissolve
    voice "9-4-2.mp3" #starleeter
    lov "Wow, it really is quiet now."
    voice "9-4-3.mp3" #potato
    pro "Maria? Are you in here?"
    "I hear some movement down the corridor and a door opening."
    voice "9-4-4.mp3" #amree
    show sis worry2 at right
    hide lov happy2bh
    show lov happy2 at left
    sis "Emily?"
    voice "9-4-5.mp3" #potato
    pro "It’s me and Lauren. Are you okay?"
    voice "9-4-6.mp3" #amree
    sis "Yeah… How’s Alex?"
    voice "9-4-7.mp3" #potato
    pro "He’s getting better. Much better than yesterday."
    voice "9-4-8.mp3" #amree
    sis "C-Can I visit Alex, too, next time?"
    "Alex isn’t ready to see Maria yet, but I don’t want to say that to her."
    voice "9-4-9.mp3" #potato
    pro "There’s no need for that. They’ll probably let him out soon."
    voice "9-4-10.mp3" #amree
    hide sis worry2 at right
    show sis happy2 at right
    sis "Oh… okay!"
    "I walk inside with Lauren in tow."
    "Maria is standing at her door. She’s looking happier."
    "I gesture for Lauren to go into my room to set up while I talk to Maria."
    hide lov happy2 at left
    "Once we’re alone, I take Maria back into her room."
    scene sisroom with dissolve
    show sis happy1
    voice "9-4-11.mp3" #potato
    pro "You okay?"
    "She nods."
    "I give her a quick hug."
    voice "9-4-12.mp3" #potato
    pro "I’ve got some homework to do with Lauren. You okay on your own until dinner?"
    "Maria nodded."
    voice "9-4-13.mp3" #potato
    pro "Just call me if you need me."
    "She nodded again."
    scene bedroom with dissolve
    "I left Maria’s room and went into mine."
    show lov confused1bh
    voice "9-4-14.mp3" #starleeter
    lov "Is Maria okay?"
    voice "9-4-15.mp3" #potato
    pro "She’s fine. I think she’s doing better than all of us."
    voice "9-4-16.mp3" #starleeter
    lov "They say kids cope better than adults."
    voice "9-4-17.mp3" #potato
    pro "I guess."
    "I sigh."
    voice "9-4-18.mp3" #potato
    pro "So what do we need to do?"
    voice "9-4-19.mp3" #starleeter
    hide lov confused1bh
    show lov happy2
    lov "I’m still working on memorising my lines, and you’ve got costumes to finish."
    "I nod."
    voice "9-4-20.mp3" #potato
    pro "Alright. I’ll make a start on the costumes."
    voice "9-4-21.mp3" #potato
    pro "Do you mind if I use you to check they’ll stay on?"
    hide lov happy2
    show lov happy1bh
    "Lauren giggles."
    voice "9-4-22.mp3" #starleeter
    lov "Sure. So long as you don’t expect me to take my clothes off first."
    voice "9-4-23.mp3" #potato
    pro "Ah… n-no."
    "She giggles again."
    voice "9-4-24.mp3" #starleeter
    lov "Just kidding!"
    voice "9-4-25.mp3" #potato
    pro "Y-yeah…"
    "I sit myself down in front of my sewing machine and start getting to work."
    voice "9-4-26.mp3" #potato
    pro "I’m so behind."
    voice "9-4-27.mp3" #starleeter
    lov "At least you have an excuse. What’s mine?"
    voice "9-4-28.mp3" #potato
    pro "What do you mean?"
    voice "9-4-29.mp3" #starleeter
    lov "I kinda have a confession to make…"
    voice "9-4-30.mp3" #potato
    pro "What?"
    voice "9-4-31.mp3" #starleeter
    hide lov happy1bh
    show lov happy2
    lov "I’ve barely learned any more lines since we last practiced together…"
    voice "9-4-32.mp3" #potato
    pro "What?! Why?"
    "She laughs awkwardly."
    hide lov happy2
    show lov happy1bh
    voice "9-4-33.mp3" #starleeter
    lov "I guess my brain just doesn’t work like yours. I find it so hard to remember things if I’m working alone!"
    voice "9-4-34.mp3" #potato
    pro "We can work on it some more if you like, but you have to help me make costumes after."
    voice "9-4-35.mp3" #starleeter
    hide lov happy1bh
    show lov happy2
    lov "Sure!"
    "I take the script from her and we start going over her lines again."
    hide lov happy2
    "Almost an hour later and we’ve barely got another scene done."
    "Honestly, I don’t know how Lauren isn’t able to remember these things."
    "Maybe she just hasn’t figured out a good way to do it. I don’t know."
    "Lauren sighs."
    show lov angry1
    voice "9-4-36.mp3" #starleeter
    lov "Ugh this is taking forever."
    voice "9-4-37.mp3" #starleeter
    lov "What are people going to think when I can’t even remember my lines."
    "She flops onto my bed and sighs."
    voice "9-4-38.mp3" #starleeter
    lov "Ugh!"
    voice "9-4-39.mp3" #starleeter
    lov "Maybe I should ask to be made the understudy for the role. Maybe this is too much for me."

    menu:

        "Don’t say that! You can do it.":
            $ love += 1
            $ career += 1
            "Lauren sat up."
            voice "9-4-40.mp3" #starleeter
            lov "Do you really think so?"
            voice "9-4-41.mp3" #potato
            pro "I do."
            voice "9-4-42.mp3" #starleeter
            lov "It’s just taking so long, though."
            voice "9-4-43.mp3" #potato
            pro "We still have time. There’s not much left to do."
            voice "9-4-44.mp3" #starleeter
            lov "I guess…"
            voice "9-4-45.mp3" #potato
            pro "Let’s take a break and work on the costumes. After dinner we can do more, okay?"
            hide lov angry1
            show lov happy2
            voice "9-4-46.mp3" #starleeter
            lov "I guess, but I can’t stay too much longer."

        "...":
            voice "9-4-47.mp3" #starleeter
            lov "What do you think?"
            voice "9-4-48.mp3" #potato
            pro "I guess you should do what you think is best."
            voice "9-4-49.mp3" #potato
            pro "I think you’re way too hard on yourself, but it’s up to you."
            voice "9-4-50.mp3" #starleeter
            lov "I guess I can try a little more before giving up."
            "I nod."
            voice "9-4-51.mp3" #potato
            pro "Do you mind if we work on the costumes before dinner time?"
            hide lov angry1
            show lov happy2
            voice "9-4-52.mp3" #starleeter
            lov "Sure."

    # Menu statement ends here.
    "Lauren cuts some fabric up for me so I can sew it using the machine."
    voice "9-4-53.mp3" #starleeter
    lov "I’m starting to wonder if I’m taking on too much with this show."
    voice "9-4-54.mp3" #potato
    pro "You’re only thinking that now?"
    show lov happy1bh
    "She laughed."
    voice "9-4-55.mp3" #starleeter
    lov "Yeah, I know. You told me before."
    voice "9-4-56.mp3" #starleeter
    hide lov happy1bh
    show lov confused2b
    lov "It’s just… Everyone in my family is so smart and able to do so much. I feel so dumb compared to them."
    voice "9-4-57.mp3" #starleeter
    lov "I guess I’m just trying to prove myself wrong. Prove I’m not dumb."
    voice "9-4-58.mp3" #potato
    pro "You’re not dumb, Lauren. I’m amazed at all the stuff you can do."
    voice "9-4-59.mp3" #potato
    pro "You just need to figure out how you remember stuff. Everyone does it differently."
    voice "9-4-60.mp3" #potato
    pro "Maybe if you find time, you should look up techniques."
    voice "9-4-61.mp3" #starleeter
    hide lov confused2b
    show lov happy2
    lov "That might be good… I’ll try that."
    voice "9-4-62.mp3" #potato
    pro "You also need to learn how to say ‘no’ to people."
    hide lov happy2
    show lov happy1bh
    "Lauren giggles."
    voice "9-4-63.mp3" #starleeter
    lov "I say no all the time."
    voice "9-4-64.mp3" #potato
    pro "Name one time."
    voice "9-4-65.mp3" #starleeter
    lov "Um..."
    "..."
    voice "9-4-66.mp3" #starleeter
    lov "No."
    voice "9-4-67.mp3" #potato
    pro "Haha. Now just say it to people other than me."
    voice "9-4-68.mp3" #starleeter
    hide lov happy1bh
    show lov happy2b
    lov "I guess. It’s just hard. I hate letting people down."
    voice "9-4-69.mp3" #potato
    pro "Sometimes you need to look after yourself, you know?"
    voice "9-4-70.mp3" #starleeter
    lov "I know…"
    "I held up a skirt."
    voice "9-4-71.mp3" #potato
    pro "Can you try this on?"
    voice "9-4-72.mp3" #starleeter
    hide lov happy2b
    show lov shy2h
    lov "Do you want me to just put it on over my clothes?"
    voice "9-4-73.mp3" #potato
    pro "Y-yes... "
    voice "9-4-74.mp3" #starleeter
    lov "Okay."
    "She put the skirt on."
    voice "9-4-75.mp3" #starleeter
    hide lov shy2h
    show lov happy2b
    lov "Ooh fits like a charm. Good job!"
    "I nod."
    voice "9-4-76.mp3" #potato
    pro "Great. Only a million or so left to make."
    hide lov happy2b
    show lov happy1bh
    "Lauren giggles."
    voice "9-4-77.mp3" #starleeter
    lov "I guess we’d better get sewing."
    hide lov happy1bh
    "We both sigh and get back to work."
    jump day9s5
