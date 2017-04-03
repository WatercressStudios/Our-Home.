label day11s3:
    scene schoolcafeteria with dissolve

    play music bgmsad1intro noloop
    queue music bgmsad1loop loop

    "There! There she is."
    "Already feeling better, I walk over and join her at her lunch table."
    
    show lov confused1h with dissolve
    
    "I can feel Lauren staring as I unpack yet more pancakes for lunch."
    voice "11-3-1.mp3" #potato
    pro "Yes?"

    show lov confused1 with dissolve

    voice "11-3-2.mp3" #starleeter
    lov "Do you really like pancakes now or something?"
    "I shake my head."
    voice "11-3-3.mp3" #potato
    pro "Maria made an entire packet’s worth of them. We’re eating them so they don’t spoil."

    show lov happy2 with dissolve

    voice "11-3-4.mp3" #starleeter
    lov "She did that all by herself? That’s pretty impressive!"
    voice "11-3-5.mp3" #potato
    pro "Turns out she’s really good at following instructions."
    voice "11-3-6.mp3" #potato
    pro "Just... not so good at portion sizes."

    show lov happy1bh with dissolve

    "Lauren giggles."
    voice "11-3-7.mp3" #starleeter

    show lov happy2bh with dissolve

    lov "Well I guess that’s something. Maybe her future family will be grateful for how good she is at cooking."
    voice "11-3-8.mp3" #potato
    pro "Maybe."
    "I sigh and start eating."

    show lov confused1 with dissolve

    voice "11-3-9.mp3" #starleeter
    lov "So is your Mom still away?"
    "I shook my head."
    voice "11-3-10.mp3" #potato
    pro "No, Dad texted me during class. She came home a little bit ago."

    show lov angry2b with dissolve

    voice "11-3-11.mp3" #starleeter
    lov "And you didn’t go home!? Come on, Em, this is way more important than corresponding angles or whatever!"
    voice "11-3-12.mp3" #potato
    pro "I… I didn’t know what I’d find."

    show lov angry1 with dissolve

    voice "11-3-13.mp3" #starleeter
    lov "It’s your Mom!"
    voice "11-3-14.mp3" #potato
    pro "I know. Truth be told, I’m scared. She was gone all that time with barely a word and now she’s home."
    voice "11-3-15.mp3" #potato
    pro "Dad hasn’t texted me since she got back. They might’ve been fighting this whole time."
    voice "11-3-16.mp3" #potato
    pro "I’m sick of seeing that. I know I’m just blowing this off, but..."

    show lov confused2 with dissolve

    "Lauren grabs my hand."

    show lov confused1b with dissolve

    voice "11-3-17.mp3" #starleeter
    lov "You’ll be alright, Emily. I know it."
    "I look away."
    voice "11-3-18.mp3" #potato
    pro "What about everyone else?"

    show lov happy1b with dissolve

    voice "11-3-19.mp3" #starleeter
    lov "It’ll be okay."
    "She squeezes my hand."

    show lov happy2b with dissolve

    voice "11-3-20.mp3" #starleeter
    lov "I have an idea, actually!"
    voice "11-3-21.mp3" #potato
    pro "What?"

    show lov happy2bh with dissolve

    voice "11-3-22.mp3" #starleeter
    lov "Try texting your Mom and see if she replies to you."

    show lov happy2h with dissolve

    voice "11-3-23.mp3" #starleeter
    lov "She’ll text you if everything is okay, right?"
    voice "11-3-24.mp3" #potato
    pro "Maybe… I guess."
    "I take out my phone and send a quick text to Mom to see how she is."
    "I get a reply almost right away. I guess she mustn’t be fighting with Dad if she’s looking at her phone."

    show lov confused1h with dissolve

    voice "11-3-25.mp3" #starleeter
    lov "What does it say?"
    voice "11-3-26.mp3" #potato
    pro "‘Everything is going to be okay. I’m going to make it right.’"

    show lov happy1 with dissolve

    voice "11-3-27.mp3" #starleeter
    lov "See? Everything’s fine!"
    voice "11-3-28.mp3" #potato
    pro "No, she’s not. She never talks like this. Hang on, Alex is home. I’ll text him."
    "My brother replies almost instantly as well."

    show lov confused1 with dissolve

    voice "11-3-29.mp3" #starleeter
    lov "And?"
    voice "11-3-30.mp3" #potato
    pro "‘He won’t say. He’s asking if I can come home now. Dammit, I knew something was wrong!"

    show lov angry1 with dissolve

    voice "11-3-31.mp3" #starleeter
    lov "If you think so, then you should go home."
    voice "11-3-32.mp3" #potato
    pro "Now? But what about Maria?"

    show lov angry2 with dissolve

    voice "11-3-33.mp3" #starleeter
    lov "Just take her with you!"
    "I take a moment to think about it. Lauren’s right. I can’t have Maria walking home by herself again, and she deserves to be home too if something’s going on with..."
    "...with our family."

    show lov shy2b with dissolve

    "Lauren suddenly pulls me into a hug and tears start to leak from my eyes."
    voice "11-3-34.mp3" #starleeter
    lov "I know it’s been hard, Emily."
    voice "11-3-35.mp3" #starleeter
    lov "I know you’re scared. Everything’s a mess."

    show lov shy1b with dissolve

    voice "11-3-36.mp3" #starleeter
    lov "But! You’re the smartest girl I know. You can work it out. I know you will."
    "She squeezes me and I squeeze back."
    voice "11-3-37.mp3" #starleeter
    lov "You’ll be okay, right?"
    "I nod, trying to hide my tears."

    show lov confused1 with dissolve

    "Lauren releases me and I wipe my eyes."
    voice "11-3-38.mp3" #starleeter
    lov "You feeling a little better?"
    "I nod again."
    "This girl does way too much for me. I should really say something to her."
    "Does she even realise how much I appreciate it?"
    menu:

        "Play it cool":
            voice "11-3-39.mp3" #potato
            pro "Thanks."

            show lov happy2 with dissolve

            voice "11-3-40.mp3" #starleeter
            lov "Of course. That’s what friends are for, right?"
            "I nod."
            voice "11-3-41.mp3" #potato
            pro "Yeah…"

        "If there’s any time to be cheesy, it’s now.":
            stop ambience fadeout 4.0
            play music bgmlov2 fadeout 2.0
            $ love += 1

            voice "11-3-42.mp3" #potato
            pro "Thank you so much for everything. I couldn’t do half of what I do without you."

            show lov happy1bh with dissolve

            "Lauren giggles awkwardly, trying to hide her cheeks."
            voice "11-3-43.mp3" #starleeter
            lov "Oh… wow… You just came out with that, huh?"
            voice "11-3-44.mp3" #starleeter
            lov "I… uh… I’m really glad I’m your friend, Emily."
            voice "11-3-45.mp3" #starleeter

            show lov happy2bh with dissolve

            lov "You do a lot for me too. I just try so hard because I want to pay you back, okay?"
            "I nod."
            voice "11-3-46.mp3" #starleeter
            lov "Thanks, though. I… I’m happy to know I’m so important to you."

    # End menu statement
    
    scene schoolcafeteria with fade
    
    "We finish up our lunches before I get up to leave."
    "I might get some hassle from the school for leaving after lunch, but Lauren’s right. I need to get Maria, and then head home."

    show lov happy2 with dissolve

    voice "11-3-47.mp3" #starleeter
    lov "Not to worry! I’ll cover for you."
    voice "11-3-48.mp3" #potato
    pro "Thanks, Lauren."
    
    scene sky with dissolve
    play ambience suburb fadeout 1.0 fadein 1.0

    "I start making my way out of school."
    jump day11s4
