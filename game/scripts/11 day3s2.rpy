label day3s2:

    scene library
    with dissolve
#     play ambience crowd fadein 2.0

    "Finally made it. The library's a nice little home away from home."
    "I should try to find Lauren and get this work done and over pretty quickly. I still got some stuff to do at home. Maria's plushie could use some work…"
    "Oh, there she is. Already picked out a work-station, neat. She's waving me over."

    play music bgmlov fadeout 1.0 fadein 0.0
    show lov happyh
    with dissolve
    voice "3-2-1.mp3" #starleeter
    lov "Emily!~ Hi, what's up with you?"
    voice "3-2-2.mp3" #potato
    pro "You, uh, do realize we're in a library, right? Indoor voice."

    show lov angryb

    "I chided her with a slight wink. Her cheeks puffed up in slight annoyance."

    show lov confused2b

    voice "3-2-3.mp3" #starleeter
    lov "It's not like there's anyone else here…"

    show lov confused1b
    voice "3-2-4.mp3" #potato
    pro "Oh. True. I guess this early in the year, no one's bothering with the cramming part of their studies. Give it time, though…"

    show lov shy1bh
    "Out of the corner of my eye, I catch the librarian shooting us both a cold glance."


    show lov shy2bh
    voice "3-2-5.mp3" #potato
    pro "I guess conversing isn't school-appropriate behaviour."

    "I tilt my head in the librarian's direction, Lauren's eyes widening."

    show lov happy

    voice "3-2-6.mp3" #starleeter
    lov "...O-oh, yeah, let's get started! We got the computer right here…"
    voice "3-2-7.mp3" #potato
    pro "So you wanted, like, fifties fashion stuff, right?"
    voice "3-2-8.mp3" #potato
    pro "Doubt there'll be any old-timey magazines in a school library, but there might just be a reference book somewhere…"
    voice "3-2-9.mp3" #starleeter
    lov "W, well! worst-case scenario, we'll just Google some stuff and find something cute, right?"
    voice "3-2-10.mp3" #potato
    pro "...That, uh, works, I guess? Technically?"
    voice "3-2-11.mp3" #starleeter
    lov "Oh, good, heheh!"

    "Lauren's acting pretty odd. It is basically just the two of us, but… she doesn't usually stutter."
    "Whatever, let's get this done."

    voice "3-2-12.mp3" #potato
    pro "First thing we can do is look up some keywords and see what pops up in the library…"
    voice "3-2-13.mp3" #potato
    pro "Oh, a fashion sourcebook. Over 300 illustrations? probably good… want me to go find it?"
    voice "3-2-14.mp3" #starleeter
    lov "Sure! I'll wait for you."

    "It was on the second floor. Guess I got some running around to do."

    hide lov
    with dissolve
    #NEED BG
    #scene library2 with dissolve

    "I guess this is a convenient way to think about things. probably shouldn't be too long though."
    "I could pretend I don't know where I'm looking, but… nah, wouldn't work, she saw me figure out the searches pretty fast."
    "I'll just find the section quickly. It's not exactly difficult."
    "There's something a little weird about this meetup with Lauren, though."
    "If she thought she could just Google the outfits she liked, why'd she need me to come out for this job?"
    "She must have a billion other things to do with others. I don't really get her."
    "Which is weird, she's not exactly a recluse. Pretty open with basically everyone."
    "I guess we're friends, so I'm happy to help her out a bit, but… this seems like busywork more than anything."
    "Whatever. I think I found what I was looking for."

    show fashionbook
    with dissolve

    play sound paper
    "Thumbing through the pages, I browse its contents."
    play sound paper
    "Accessories, garments, sportswear, leisurewear… seemed pretty thorough."
    voice "3-2-15.mp3" #potato
    pro "Ugh, dusty thing. Reckon fifties fashion isn't a hot topic for go-getting youths today. {i}Oh God I sound so old...{/i}"
    play sound paper
    "Some cute stuff in here, too. Mostly sketches, though. Should be good for inspiration."

    hide fashionbook
    with dissolve

    "Alright, let's take this back to Lauren."

    scene library
    with dissolve

    show lov confused2
    with dissolve

    voice "3-2-16.mp3" #potato
    pro "Alright, I'm back, I found the book. How's your search down here?"

    show lov happy

    voice "3-2-17.mp3" #starleeter
    lov "These outfits are really cute! Come see, come see!"

    show lov happy2
    "She turned the screen towards me, beaming proudly."

    #think we can slot a comedic CG in here with some lewd outfits on the screen
    #fuck it just save it for an update -TUTTY

    show lov happy
    voice "3-2-18.mp3" #starleeter
    lov "Well, what about these?"
    voice "3-2-19.mp3" #potato
    pro "...What in the…?"
    "They look more at home at the Playboy Mansion than in a school play..."
    "But Lauren looks {i}so happy with herself{/i}...!"
    voice "3-2-20.mp3" #potato
    pro "I'm, uh, honestly impressed, like… where'd you even look to find those?"
    voice "3-2-21.mp3" #starleeter
    show lov happy2h
    lov "Oh, I've been pretty busy since you were away! You think these'd be good?"
    voice "3-2-22.mp3" #potato
    pro "W-well, I… there's nothing there. Is that even allowed in the dress code?"
    voice "3-2-23.mp3" #potato
    pro "It's practically a bikini!"
    voice "3-2-24.mp3" #starleeter

    show lov happy1h
    lov "Yeah, but I'd look good in it, right?"
    voice "3-2-25.mp3" #potato
    pro "Th-that's not the point! It's for a school play!"
    voice "3-2-26.mp3" #starleeter

    lov "I mean, I could get a Beach Boys thing going! {i}Babababa Barbara Ann!~{/i}"
    voice "3-2-27.mp3" #potato
    pro "That's from the sixties, Lauren…"

    hide lov
    with dissolve
    scene black
    with dissolve

    "... ... ..."

    scene library
    with dissolve
    show lov confused2h
    voice "3-2-28.mp3" #potato
    pro "I think you have some good styles picked out. Polka dots are always cute and go well with the era, uh…"
#    voice "3-2-29.mp3" #starleeter silence
    show lov confused1h
    lov "..."
    voice "3-2-30.mp3" #potato
    pro "Accessorizing might be hard, I don't think we have much at home, mm… oh?"
    "Lauren's giving me a really odd look. How long has she been staring at me like that?"
    "What do I say?"

    menu:

        "What's wrong?":
            jump day3s2wrong

        "You're staring at me.":
            $ love += 1
            jump day3s2stare

        "Pay attention.":
            jump day3s2rude

label day3s2wrong:
    voice "3-2-31.mp3" #potato
    pro "Is something wrong? You seem out of it."

    show lov shy2b

    voice "3-2-32.mp3" #starleeter
    lov "Ah!? Omigosh, was I spacing out?"
    voice "3-2-33.mp3" #potato
    pro "Uh… a little?"

    show lov shy1b

    voice "3-2-34.mp3" #starleeter
    lov "I-I'm so sorry, it's just…"
    jump day3s2bags

label day3s2stare:
    voice "3-2-35.mp3" #potato
    pro "You're staring at me. Is there something on my face?"
    show lov shy2bh
    voice "3-2-36.mp3" #starleeter
    lov "Eh? N-no, I mean… I didn't mean to..."
    show lov happy2bh
    voice "3-2-37.mp3" #starleeter
    lov "W-well, I guess there, ah, {i}is{/i} something on your face, technically, but…"
    voice "3-2-38.mp3" #potato
    pro "...Eh? Really?"
    "My hand reaches up to feel for something, but Lauren reaches out to grab my hand."
    show lov happy2b
    "Her hand was really soft. Gentle."

    voice "3-2-39.mp3" #potato
    pro "..."

    show lov shy1b

    "Oh God, now I was staring. I draw back my hand."

    voice "3-2-40.mp3" #potato
    pro "S-sorry, just… you're not making much sense, is all."
    show lov happy2b
    voice "3-2-41.mp3" #starleeter
    lov "Haha… I know. It's just…"
    jump day3s2bags

label day3s2rude:
    voice "3-2-42.mp3" #potato
    pro "Yo, snap out of it, okay? We're doing work right now."
    show lov shy1h
    voice "3-2-43.mp3" #starleeter
    lov "Ah, I...I know, sorry, it's just…"

    "Shit, did I snap at her? She looks concerned for me."
    "There's a pang in my stomach. Man, I regret snapping at her… like, almost immediately."

    show lov shy2h
    voice "3-2-44.mp3" #starleeter
    lov "It's about you though, just… I was looking, and…"
    jump day3s2bags

label day3s2bags:
    show lov shy2
    voice "3-2-45.mp3" #starleeter
    lov "Emily, you know you got, like, really bad bags under your eyes, right?"
    voice "3-2-46.mp3" #potato
    pro "...Oh? Yeah, I know. Hard to miss 'em in the morning…"
    show lov confused1
    voice "3-2-47.mp3" #starleeter
    lov "Are you getting enough sleep, though?"
    voice "3-2-48.mp3" #potato
    pro "'Course I am, I mean… wait, what about you?"
    voice "3-2-49.mp3" #starleeter
    show lov shy2
    lov "Mm? Well, I stay busy, but..."
    voice "3-2-50.mp3" #potato
    pro "Well, like, the other people in drama keep coming to you to help with all the drama stuff. Script reading, set building, rehearsals, and this…"
    "It's crazy to think, but…"

    menu:
        "Aren't you tired?":
            $ love += 1
            $ slumberparty = True
            jump day3s2tired

        "Don't you feel used?":
            jump day3s2used

        "I couldn't handle that.":
            jump day3s2handle

label day3s2tired:
    voice "3-2-51.mp3" #potato
    pro "Aren't you tired? All this running around, it has to be terribly exhausting."

    show lov shy2
    voice "3-2-52.mp3" #starleeter
    lov "Mm… to tell you the truth, it gets pretty rough, sometimes."

    show lov happy2
    voice "3-2-53.mp3" #starleeter
    lov "Wanna know a secret? My mom taught me a lot of makeup tricks, so…"
    show lov shy1
    voice "3-2-54.mp3" #starleeter
    lov "...if I look really miserable, I just fix myself up, and I'm ready for the day. No problem."
    voice "3-2-55.mp3" #potato
    pro "But… that's not fixing the problem, is it?"
    show lov happy2h
    voice "3-2-56.mp3" #starleeter
    lov "I dunno. I feel a lot better afterwards, myself."
    show lov happy1h
    voice "3-2-57.mp3" #starleeter
    lov "It means I hold my head a little higher when I have to face the day. I think that's good enough for me."

    "She's so optimistic and chipper all of the time. The sparkle in her eyes… she really believed what she was saying."
    "I don't believe she's fabricating that story. I always assumed she had her own struggles, it just… feels weird for her to open up about them like that."
    "She was really strong."
    jump day3s2future

label day3s2used:
    voice "3-2-58.mp3" #potato
    pro "Don't you feel used? Maybe some of these people are leaning on you too hard and-"

    voice "3-2-59.mp3" #starleeter
    show lov angry2
    lov "Stop. No. Don't talk about my friends like that."
    voice "3-2-60.mp3" #potato
    pro "Agh. Sorry, I…"

    "I winced sharply, right there. Never seen her take on that tone with me before.It's forceful and… unlike her."

    show lov angry1

    voice "3-2-61.mp3" #starleeter
    lov "I'm not being tricked into doing anything, Emily… I'm doing this because I want to."
    voice "3-2-62.mp3" #starleeter
    lov "And everyone needs me at my best, right? It's the least I could do."
    voice "3-2-63.mp3" #potato
    pro "Sorry, Lauren. I was presumptuous. I shouldn't really pry into your business like that."

    show lov happy2

    voice "3-2-64.mp3" #starleeter
    lov "It's okay… we're friends, I know you're worried. But I'm fine, okay?"
    jump day3s2future

label day3s2handle:
    voice "3-2-65.mp3" #potato
    pro "I don't think I could handle everything so well like… like you've been handling it all. It's really impressive and…"
    voice "3-2-66.mp3" #starleeter
    show lov happy1b
    lov "Oh, I'm not that strong, or cool! I'm just doing the least I can do."
    voice "3-2-67.mp3" #potato
    pro "Heh, I mean, you have way more friends around the school than I do. I'd say you're pretty damn cool."

    show lov shy1
    voice "3-2-68.mp3" #starleeter
    lov "Whaaaaat? Not as cool as you. You got the whole… aloof, mysterious stranger thing going."
    show lov happy2
    voice "3-2-69.mp3" #starleeter
    lov "Everyone wants to get inside that head of yours and delve into, ah, your poetic thoughts."
    voice "3-2-70.mp3" #potato
    pro "Heh… hahaha… thanks Lauren."
    show lov happy1h
    voice "3-2-71.mp3" #starleeter
    lov "Anytime!~"

    "It's a little too obvious she's trying to make me feel better, but the effort's appreciated."

    jump day3s2future

label day3s2future:

    voice "3-2-72.mp3" #starleeter
    show lov angry1h
    lov "Anyway! This isn't about me, it's about you, Em."
    show lov shy1h
    voice "3-2-73.mp3" #starleeter
    lov "Seriously, you look ill a lot of the time… you sure you're okay?"
    voice "3-2-74.mp3" #potato
    pro "Yeah, I'm fine. I get by just fine, you don't have to worry about me."

    show lov shy2

    voice "3-2-75.mp3" #starleeter
    lov "But I am worried! You look so tired all the time! And you just want to be so… aloof now."

    show lov happy2

    voice "3-2-76.mp3" #starleeter
    lov "Remember how we met?"
    voice "3-2-77.mp3" #potato
    pro "Uhhh… the class work? We pushed our desks together and… did the work?"
    show lov happy1
    voice "3-2-78.mp3" #starleeter
    lov "Mmhm! You were really smart and helpful, and I…"

    voice "3-2-79.mp3" #starleeter
    show lov confused2
    lov "...Well, I didn't really… get the work, at all. Heheh, I was pretty useless, huh."
    voice "3-2-80.mp3" #potato
    pro "Mm. I kind of did most of it, didn't I… b-but you still helped! A lot! A bit."

    show lov happy2b
    voice "3-2-81.mp3" #starleeter
    lov "Nah, you don't have to try make me feel better. I'm not practically perfect in every way, I get it."

    show lov confused1
    voice "3-2-82.mp3" #starleeter
    lov "In English class, you kind of have to just… sit there, read it all to yourself, and… I get bored, I can't take it."


    show lov happy2
    voice "3-2-83.mp3" #starleeter
    lov "So I'm just glad you were there to help me out in a pinch.~"
    voice "3-2-84.mp3" #potato
    pro "It, it was nothing, really…"

    show lov happy1

    voice "3-2-85.mp3" #starleeter
    lov "A-and you're still taking notes for me when I'm off doing drama stuff!"
    voice "3-2-86.mp3" #starleeter
    lov "C'mon, admit it, you're a big sweety when you wanna be, don't try to hide it.~"
    voice "3-2-87.mp3" #potato
    pro "I, I plead the fifth. You'd do the same for me, right?"
    voice "3-2-88.mp3" #starleeter
    show lov shy2bh
    lov "...Mm… I dunno if you'd get much out of my notes thooough… I'd probably just doodle."
    voice "3-2-89.mp3" #potato
    pro "Haha, true, true."
    show lov happy1
    voice "3-2-90.mp3" #starleeter
    lov "Hehe!~"
    show lov happy2
    voice "3-2-91.mp3" #starleeter
    lov "I'm not really good with memorization either, so… thanks for being patient with me."
    voice "3-2-92.mp3" #potato
    pro "It's not a big d- ...waaait, it, uh, kind of is?"
    show lov confused2h
    voice "3-2-93.mp3" #starleeter
    lov "Eh?"
    voice "3-2-94.mp3" #potato
    pro "Don't you have to, like, memorize your script and stuff?"
    voice "3-2-95.mp3" #starleeter
    show lov confused1h
    lov "...Huh… That's true."
    voice "3-2-96.mp3" #potato
    pro "H-hey, don't space out like that! It's part of the gig to know it by heart, right?"
    voice "3-2-97.mp3" #starleeter
    show lov happy2
    lov "Oh, absolutely. But I have friends in drama that are supporting me there too."
    voice "3-2-98.mp3" #starleeter
    show lov happy1
    lov "We read everything a dozen times as an exercise!~"
    voice "3-2-99.mp3" #potato
    pro "...Crazy..."
    show lov happy2
    voice "3-2-100.mp3" #starleeter
    lov "I really wanna be an actress, Em. And every bit of experience is good experience, right?"
    voice "3-2-101.mp3" #potato
    pro "Y, yeah, definitely, just… just don't throw your back out overworking yourself. I, ah... worry, about you."
    show lov big smile
    voice "3-2-102.mp3" #starleeter
    show lov happy1
    lov "Huh. Funny. I was thinking the same thing!~"
    voice "3-2-103.mp3" #potato
    pro "...Haha… true."

    if slumberparty:
        show lov happy1h
        voice "3-2-107.mp3" #starleeter
        lov "I was thinking we should have a slumber party one day, and I'll finally get to teach you all my makeup tricks from theatre!~"
        voice "3-2-108.mp3" #potato
        pro "Slumber party!? Lauren, we're 18, I think we're a little old for-"
        show lov angry1b
        voice "3-2-109.mp3" #starleeter
        lov "It's professional stuff, y'know! I should charge you for lessons, but…"
        show lov happy2b
        voice "3-2-110.mp3" #starleeter
        lov "For a friend, I don't mind. But that's beside the point!"

    show lov confused2

    voice "3-2-111.mp3" #starleeter
    lov "Hoo! I'm bushed!"
    voice "3-2-112.mp3" #potato
    pro "We, uh, didn't really do all that much, did we…?"
#    I think this was removed, so I'm adding it commented, but I'll leave it here 'till I confirm it. ~MatKrulli
#    voice "3-2-113.mp3" #starleeter
#    lov "Oh pish posh, you were a big help! You gave me a lot to think about today!"

    "Lauren leans back in her chair, reclining almost to the point of no return. My hand hovers out, stretched to catch her if she falls, as she is wont to do."
    "Is she already losing speed on this homework project!? Oy... time to double down…"

    hide lov
    with dissolve
    scene black
    with dissolve

    "... ... ..."
    jump day3s3
