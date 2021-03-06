label day5s2:

    $ jotnotes = False
    stop music fadeout .5
    scene classroom with dissolve
    play ambience blackboard fadein 2.0
    voice "5-2-1.mp3" #skinimini
    tea "...To wrap up our lecture today, I would like to reflect briefly on the idea of psychological independence."
    voice "5-2-2.mp3" #skinimini
    tea "In our readings, you will have noted that, in {i}Nineteen Eighty-Four{/i}, the Party brings this equation to bear."
    "She writes 2 + 2 = 5 on the blackboard. We're going through this book really quickly, aren't we…" 
    "I should be taking notes for Lauren. She really doesn't have the time to be reading so much of this book at once. Even if she didn't have the show to worry about."
    "Wonder how thorough I should be. I can copy my notes over, but how..." 

    menu: 
        "Take short jotnotes.":
            $ jotnotes = True
            jump jot

        "Transcribe the whole lecture.":
            jump essay

label jot:
    "She doesn't need me to be thorough. I'll isolate the important bits."
    jump lecture1

label essay:
    "Let's give her as much as I can, and she can sift through it all laterish."
    jump lecture1

label lecture1: 
    voice "5-2-3.mp3" #skinimini
    tea "Of course, this is nonsense to us, but it's meant to be a challenge to the intellectual notions that we consider fundamental to reality as we see it." 
    voice "5-2-4.mp3" #skinimini
    tea "The Party is able to affect the perception of reality through challenging these intellectual notions, representing a kind of psychological manipulation."
    voice "5-2-5.mp3" #skinimini
    tea "The rejection that 2+2=4 opens a broad expanse that, if such ideas could be so broadly and fundamentally influenced…"
    voice "5-2-6.mp3" #skinimini
    tea "...Would suggest the ability to influence reality, as we see it, experience it, around us."
    voice "5-2-7.mp3" #skinimini
    tea "What else would we consider real? if forces could control what we perceive is real, what we think is real, what can we even call objective reality?"
    voice "5-2-8.mp3" #skinimini
    tea "Would it be possible to invent our own reality, if pushed to extreme circumstances? I'm sure many of you are familiar enough with that notion."
    voice "5-2-9.mp3" #skinimini
    tea "...None of you are actually paying attention, are you. This is interesting stuff, people!"

    "Miss Reynolds' passion and enthusiasm for the material is apparently lost on us troglodytes."

    play sound schoolbell

    "DOO DO DOO DO!"

    "Whew, free at last, free at last."

    "Let's find Lauren, I gotta get this stuff to her."

    "Miss Reynolds was eying the class, looking absolutely pitiable."

    voice "5-2-10.mp3" #skinimini
    tea "Anyone wanna talk about the book…? We can start a book club. It'll be fun!"

    "Trying not to make direct eye contact, I shuffle out of the class…" 
    stop ambience fadeout 2.0
    scene black with dissolve
    
    "..."
    play music bgmlov fadeout 1.0 fadein 0.0
    scene drama with dissolve 
    voice "5-2-11.mp3" #potato
    
    show lov confused2 with dissolve
    pro "Hey, Lauren?"
    voice "5-2-12.mp3" #starleeter
    show lov happy1 with dissolve
    lov "\"Mm?\" Oh, Emily!" 
    voice "5-2-13.mp3" #potato
    pro "Got English notes for you. Figured you wouldn't have time to keep up, so…" 
    voice "5-2-14.mp3" #starleeter
    show lov happy2 with dissolve
    lov "Oh, thank you! Lesse…"
    show lov happy2h with dissolve
    "Taking the papers from me, she rustles them scanning them…" 

    if jotnotes:
        voice "5-2-15.mp3" #starleeter
        show lov confused1h with dissolve
        lov "'2+2=5'? I'm not so good at math, but even I know better than that…"
        voice "5-2-16.mp3" #potato
        pro "Oh, it's, uh, a plot device thing. About psychological manipulation of objective fact and-"
        voice "5-2-17.mp3" #starleeter
        show lov shy1h with dissolve
        lov "'Is reality real?' I-I guess, I mean… of course it would be, right??"
        voice "5-2-18.mp3" #potato
        pro "Ooh boy…"
        "What else was I supposed to write? The entire lecture was like… rambling. Fanboyism? Fangirlism?"

    else:
        voice "5-2-19.mp3" #starleeter
        show lov confused2h with dissolve
        lov "'2+2=5' is meant to symbolize the end result of an alternate reality fabricated by the rejection of intellectual notions of objective reality."
        voice "5-2-20.mp3" #potato
        pro "Uh. Yeah."
        show lov happy1 with dissolve
        voice "5-2-21.mp3" #starleeter
        lov "Okay!"
        voice "5-2-22.mp3" #potato
        pro "Do you get it?"
        voice "5-2-23.mp3" #starleeter
        show lov shy2 with dissolve
        lov "Prooobably not!~"
        "Looking down at the sheet, it really just comes out to being a wall of text..."

    voice "5-2-24.mp3" #potato
    pro "Sorry, I don't think there really was a good way of capturing the, uh, intricacies of Miss Reynolds' lecture…"
    voice "5-2-25.mp3" #starleeter
    show lov happy2 with dissolve
    lov "Oh, it's okay! You tried your best, I'll figure it out from here!"
    voice "5-2-26.mp3" #potato
    pro "How're things going over here?" 
    voice "5-2-27.mp3" #starleeter
    show lov shy1 with dissolve
    lov "Oh, there's so much going on! They're trying to build set components in here! It's awful crowded now…" 

    "I look towards to the back of the room. Sure enough, there's a group of shop students trying to assemble the pieces to plywood buildings."

    voice "5-2-28.mp3" #potato
    pro "...Huh. Running out of space, I see."
    voice "5-2-29.mp3" #starleeter
    show lov confused1 with dissolve
    lov "We could take this outside if you want?"
    voice "5-2-30.mp3" #potato
    pro "Oh, no need, I was just visiting."
    voice "5-2-31.mp3" #starleeter
    show lov happy1 with dissolve
    lov "By the way, any progress on the dress? I'm really excited to see it!" 
    voice "5-2-32.mp3" #potato
    pro "Ahhh… about that…" 
    voice "5-2-33.mp3" #starleeter
    show lov happy2h with dissolve
    lov "Hm?"

    "She gives me a curious look. I don't know what to say, but I can't just make up an excuse."
    "It's probably bad to admit I couldn't do anything about it, but… I should be honest, she'd expect nothing less."
    "I take a breath."

    voice "5-2-34.mp3" #potato
    pro "I tried to get some work done last night, but the sewing machine, it's well… it broke."
    voice "5-2-35.mp3" #starleeter
    show lov shy1 with dissolve
    lov "Eh? Really?"
    voice "5-2-36.mp3" #potato
    pro "Yeah, I couldn't get it to work, something in it was jamming, I… can't really get it to work."

    show lov shy2h
    voice "5-2-37.mp3" #starleeter
    lov "Oh, it's okay Emily…"
    voice "5-2-38.mp3" #potato
    pro "I'm really sorry, I couldn't-"
    voice "5-2-39.mp3" #starleeter
    show lov happy1 with dissolve
    lov "I know a guy! He can repair it for us!"
    voice "5-2-40.mp3" #potato
    pro "...S-sorry, what?"

    "I gotta say, her reaction is much more chipper than I was expecting."
    "I mean, I was rehearsing this in my head for a bit, about how she'd be disappointed in me, and we'd go our separate ways, and she'd end up ordering something out from a catalogue, but…" 
    "This… I didn't expect this."

    show lov happy2 with dissolve
    voice "5-2-41.mp3" #starleeter
    lov "Mmhm! I can stop by later today to pick it up, and he'll take a looksy. That good with you, Em?"
    voice "5-2-42.mp3" #potato
    pro "Oh, wait, I mean… I-I'm grateful you'd volunteer, but… y-you don't have to go out of your way to do that."
    voice "5-2-43.mp3" #starleeter
    show lov happy1h with dissolve
    lov "Oh I insist! You've done so much to help me with all this planning, and the notes in class…"

    voice "5-2-44.mp3" #starleeter
    show lov happy2 with dissolve
    lov "I think I owe you a little something, right?"
    voice "5-2-45.mp3" #potato
    pro "Y-you don't have to say it like that!"
    voice "5-2-46.mp3" #starleeter
    show lov shy2b with dissolve
    lov "Huh? How'd I say it?"
    voice "5-2-47.mp3" #potato
    pro "N-nevermind. But… I could just as easily bring it over to your house, so… like, you don't have to go out of your way for me."
    voice "5-2-48.mp3" #starleeter
    show lov shy1 with dissolve
    lov "Ohhh… I guess it's true. I have ulterior motives…" 
    voice "5-2-49.mp3" #potato
    pro "...I, uh, don't think I was accusing you of anything."
    voice "5-2-50.mp3" #starleeter
    show lov happy1 with dissolve
    lov "I wanna see your house! And your family! I don't think I've gotten much of a chance to meet them!"
    voice "5-2-51.mp3" #starleeter
    show lov happy2 with dissolve
    lov "And we've known each other for, like, four years now, is it? Crazy to go that long!"
    voice "5-2-52.mp3" #potato
    pro "...That is true…" 

    "In her flighty, chipper manner of speaking, she was a mean negotiator."
    "I mean… the home situation is a shitshow right now, but… maybe if it's quick, she doesn't have to see Mom. Or Alex when he's… well, doing that stuff."

    voice "5-2-53.mp3" #potato
    pro "Alright. I'll see you tonight, then?"
    voice "5-2-54.mp3" #starleeter
    show lov happy1 with dissolve
    lov "Mmhm! I'll put it in my planner."
    voice "5-2-55.mp3" #potato
    show lov happy2 with dissolve
    pro "...You don't strike me as the sort to have a planner."
    show lov happy1h with dissolve
    voice "5-2-56.mp3" #starleeter
    lov "It's up here, silly!"

    "She pointed at the side of her head."

    voice "5-2-57.mp3" #potato
    pro "Ah. Yes. Memory of an elephant. What's the significance of 2+2=5?"
    voice "5-2-58.mp3" #starleeter
    show lov shy1bh with dissolve
    lov "Ah? It's, eh, hem… I-I'll write a memo..."

    "And just like that, we set a time to meet up and exchange the busted old sewing machine. Hopefully her guy's the real deal."
    "...Still, I'm scared that this could go badly."

    voice "5-2-59.mp3" #potato
    pro "I'm gonna head home and make sure everything's packed up for you, okay?"
    voice "5-2-60.mp3" #starleeter
    show lov happy1 with dissolve
    lov "Ah, sure! Bet you need to clean up before I arrive too, huh?~"
    voice "5-2-61.mp3" #potato
    pro "...Heh. Yeah."

    "In a sense, yeah. She isn't wrong..."
    stop music fadeout .5
    "... ... ..."
    jump day5s3

