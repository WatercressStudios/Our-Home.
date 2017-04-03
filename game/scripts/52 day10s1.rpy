label day10s1:
    
    scene bedroom with dissolve 
    stop music fadeout .5
    #play sound bedalarm

    "*BEEP! BEEP! BEEP! BEEP!*"

    "I awake in my comfortable bed. It's time for school."
    "My eyes hurt… oh God, was I crying?"
    "Ugh, wake up, get up… there's a lot to do."
    "...What smells so good? Is someone cooking breakfast…?"
    voice "10-1-1.mp3" #potato
    pro "Mom…???"

    scene black with dissolve

    "Hurrying to get myself pulled together, dressed and ready, I scramble out of my room."
    "I know it's only been a few days since Mom wandered off, but… I want to see her. I have a lot to tell her!"

    scene kitchen with dissolve
    #CG with little sister making pancakes, maybe?

    play music bgmsis2 fadeout 1.0 fadein 0.0
    voice "10-1-2.mp3" #amree
    show sis happy2
    sis "Good moooooooorning, Emilyyy!~"
    voice "10-1-3.mp3" #potato
    pro "M-Maria…?"

    "What was she doing? Making breakfast for us?"
    "...W-well, yeah, sure looked like it, but… there were HUGE stacks of the stuff!"

    voice "10-1-4.mp3" #amree
    show sis worry1
    sis "I know it was hard yesterday, cuz mom usually makes breakfast, and she wasn't here, so…"
    voice "10-1-5.mp3" #amree
    show sis happy2
    sis "I made breakfast instead! Yeah, followed the boxes and everything!"
    voice "10-1-6.mp3" #potato
    pro "How, how many did you need to make, though…?"
    voice "10-1-7.mp3" #amree
    sis "I used the whole box!"
    voice "10-1-8.mp3" #potato
    show sis happy1
    pro "B-but that's good for forty-two pancakes! There are THREE of us!"
    voice "10-1-9.mp3" #amree
    show sis worry2
    sis "Uh, two, actually, Dad went for work early. B-but I asked him how to make coffee, and then he showed me, so now I can do that too!"
    voice "10-1-10.mp3" #potato
    show sis happy1
    pro "I… that's really great, sis, heheh…"
    voice "10-1-11.mp3" #amree
    show sis happy2
    sis "Are you hungry? I got some in a plate over there for you! And I'll make some for myself here..."
    voice "10-1-12.mp3" #potato
    show sis happy1
    pro "I-I'm so glad you went through all this effort, but… there's like sixteen pancakes here, I can't finish that many by myself." 
    voice "10-1-13.mp3" #amree
    show sis happy2b
    sis "...Oh. That is a lot, heheh…" 

    hide sis
    "Oh, what a mess this is, though… the sink was just filled with mixing tools. She was trying her best, but…" 
    "I'm gonna help her."

    voice "10-1-14.mp3" #potato
    pro "Hey, sis, how much pancake batter do you have left over?"
    voice "10-1-15.mp3" #amree
    show sis worry2
    sis "...Uhh… this much."

    show sis happy1
    "That is a lot of it, isn't it. Guess this morning is going to be more hectic than I had hoped."

    voice "10-1-16.mp3" #potato
    pro "Ahhh… cover that bowl up in plastic wrap, and we'll make more tomorrow."
    voice "10-1-17.mp3" #amree
    show sis worry1
    sis "Oh, um, okay. But I was gonna-"
    voice "10-1-18.mp3" #potato
    show sis happy1
    pro "Yeah, we'll split my pancakes, it'll be good for the both of us. And then I'll help you do the dishes and clean up, okay?"
    voice "10-1-19.mp3" #amree
    sis "...Mm…"
    voice "10-1-20.mp3" #amree
    show sis happy2
    sis "Okay! I'm really hungry!"

    hide sis
    "Breathing a sigh of relief, her boundless enthusiasm momentarily quelled, we sat the table to enjoy our meal together." 
    scene diningroom with dissolve
    "Cutting into mine, I take a piece and take a bite. It's good, though a little overcooked."
    "I notice, across the table, Maria was staring at me with great interest."
    show sis happy2
    "Hmmm… what should I say?"
    menu:

        "My compliments to the chef!":
            $ career += 1
            jump compliment

        "Needs more seasoning.":
            jump seasoning

label compliment:
    voice "10-1-21.mp3" #potato
    show sis happy2
    pro "My compliments to the chef! Best way to start the morning!"
    voice "10-1-22.mp3" #potato
    pro "The fluffiness of the pastry is complimented well by the slight crisp, all melting together under the care of the artificial maple syrup product."
    voice "10-1-23.mp3" #amree
    show sis happy2b
    sis "Yay! I'm glad you like it!"
    "We share a laugh, raising our glasses of orange juice in good cheer."
    jump pancakes

label seasoning:
    voice "10-1-24.mp3" #potato
    pro "Mm… could use a little extra spice. More zing."
    voice "10-1-25.mp3" #amree
    show sis happy1
    sis "Eh? Zing?"
    voice "10-1-26.mp3" #potato
    pro "Y'know, like, {i}pow{/i}. Have you tried cayenne pepper?"
    voice "10-1-27.mp3" #amree
    show sis worry2
    sis "Oh, on a pancake??"

    "Her eyes widen with some mixture of trepidation and intrigue. Oh goodness, she was actually considering it."

    voice "10-1-28.mp3" #potato
    pro "Yeah, uh, don't try it. It's awful."
    voice "10-1-29.mp3" #potato
    pro "These pancakes are really good though, great stuff."
    voice "10-1-30.mp3" #amree
    show sis happy1
    sis "Oh! Shoulda just said so in the first place!"
    voice "10-1-31.mp3" #potato
    pro "Teasing you is fun, though.~"
    jump pancakes

label pancakes:
    voice "10-1-32.mp3" #amree
    show sis happy1
    sis "I… think I overcooked them a little, honestly. But I'm a little new to all this, so…"
    voice "10-1-33.mp3" #potato
    pro "You did pretty good on your own, but… why'd you do all this?" 
    voice "10-1-34.mp3" #amree
    show sis sad2
    sis "I… well, Mom isn't here, and we dunno when she's coming back, so…"
    voice "10-1-35.mp3" #amree
    show sis sad1
    sis "Everyone else is working really hard, so I should help out too. And all I had to do was follow the instructions on the box, so…"

    "I see. She was just trying to help…" 

    menu:
        "\"Thanks Maria.\"":
#             $ career += 1
            jump praise

        "\"Be careful when cooking.\"":
            jump stopusinglectureasalabel

label praise:
    voice "10-1-36.mp3" #potato
    pro "I think you did a really good thing, today. It was good of you to show initiative, and I appreciate a good meal."
    voice "10-1-37.mp3" #amree
    show sis happy2
    sis "You think so??"
    voice "10-1-38.mp3" #potato
    show sis happy1
    pro "Yup! Just… ask one of us for help next time. I'm sure Dad would've been able to stay behind a bit." 
    voice "10-1-39.mp3" #amree
    show sis happy2
    sis "Oh, sure. Of course!"
    "Maria is really maturing. She's probably being the strongest of all of us right now, and she's putting her best foot forward every day."
    "I couldn't wish for a better sister."
    jump hotcakes

label stopusinglectureasalabel:
    voice "10-1-40.mp3" #potato
    pro "It's dangerous to be working around the stove alone, Maria. I'm glad you came out of it okay, but…"
    voice "10-1-41.mp3" #amree
    show sis worry2
    sis "It's not a big deal, right? I was fine, and I've watched Mom do it before, and I followed the instructions, so it worked out!"
    voice "10-1-42.mp3" #potato
    show sis sad1
    pro "Yeah, but… you should really… get Mom to show you how to do it next time."
    voice "10-1-43.mp3" #amree
    show sis sad2
    sis "...But Mom isn't here right now…" 
    "Her head droops, as does mine. Mom isn't here. She's walked out on us, and we have no idea when she's getting back."
    "I wish she was here right now… I bet Maria feels the same way."
    jump hotcakes

label hotcakes:
    voice "10-1-44.mp3" #amree
    show sis worry1
    sis "Mom isn't here right now, so I figured… m-maybe I could be, like, a replacement mother."
    voice "10-1-45.mp3" #amree
    show sis worry2
    sis "I know I'm not as good at it as she is, but…"
    voice "10-1-46.mp3" #potato
    pro "It's okay. You're still learning. You're gonna be a great mom." 
    voice "10-1-47.mp3" #amree
    show sis happy1
    sis "...I know I can be."

    "Her eyes lit up with optimism. She's able to say that with such strength and conviction."
    "Maria really was incredible. I hope the others come to see that."

    voice "10-1-48.mp3" #potato
    pro "Do you wanna be a mom when you grow up?"
    voice "10-1-49.mp3" #amree
    show sis happy2b
    sis "Y-yeah! I'm gonna get married and have a family of fifty!"

    "I nearly choke on the pancake piece I was chewing. What on Earth?"

    voice "10-1-50.mp3" #potato
    pro "W-wow, that's, uh, a lot."
    voice "10-1-51.mp3" #amree
    sis "You'll be part of my family too, right?"

    "Her offer's so genuine, too. She really put her heart into everything she did."
    "I hope to God I don't cry again this morning. Twice is too many times to tear up at the start of the day."

    voice "10-1-52.mp3" #potato
    show sis happy1b
    pro "...Silly goose, we're already family. We always will be."
    voice "10-1-53.mp3" #amree
    show sis sad1
    sis "...Even if Mom's gone?"
    voice "10-1-54.mp3" #potato
    pro "...Of course."
    voice "10-1-55.mp3" #amree
    show sis happy1
    sis "...She's really upset, and she's made a lot of mistakes, but I believe in her."
    voice "10-1-56.mp3" #amree
    show sis sad1
    sis "You're probably really mad at her, but… please don't shout at her when she gets back, okay?"
    voice "10-1-57.mp3" #potato
    show sis happy1
    pro "...I… I won't Maria. We have enough shouting matches in this household…" 

    hide sis
    "We quietly finish our meals, enjoying each others company."
    "It's at this moment, cleaning our plates, I realize I'm going to miss my first class entirely, and probably a hefty chunk of my second class as well, just by cleaning the dishes and taking Maria to school!"
    "Maria says she can get to school on her own, so I shouldn't be late for mine, but… is that okay?" 
    "...No. I should trust Maria. She's a smart girl, and can handle herself. And I know she wants to at least try going to school on her own."
    scene black with dissolve
    stop music fadeout 1.0
    "We part ways. This fast-paced morning isn't about to slow down anytime soon. I better book it…" 

    jump day10s2

