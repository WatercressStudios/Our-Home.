label day10s1:
    
    scene bedroom with dissolve 
    #play sound bedalarm

    "{b}BEEP! BEEP! BEEP! BEEP!{/b}"

    "I awake in my comfortable bed. It's time for school."
    "My eyes hurt… oh God, was I crying?"
    "Ugh, wake up, get up… there's a lot to do."
    "...What smells so good? Is someone cooking breakfast…?"
    play voice "10-2-1.mp3" #potato
    pro "Mom…???"

    scene black with dissolve

    "Hurrying to get myself pulled together, dressed and ready, I scramble out of my room."
    "I know it's only been a few days since Mom wandered off, but… I want to see her. I have a lot to tell her!"

    scene kitchen with dissolve
    #CG with little sister making pancakes, maybe?


    play voice "10-2-2.mp3" #amree
    sis "Good moooooooorning, Emilyyy!~"
    play voice "10-2-3.mp3" #potato
    pro "M-Maria…?"

    "What was she doing? Making breakfast for us?"
    "...W-well, yeah, sure looked like it, but… there were HUGE stacks of the stuff!"

    play voice "10-2-4.mp3" #amree
    sis "I know it was hard yesterday, cuz mom usually makes breakfast, and she wasn't here, so…"
    play voice "10-2-5.mp3" #amree
    sis "I made breakfast instead! Yeah, followed the boxes and everything!"
    play voice "10-2-6.mp3" #potato
    pro "How, how many did you need to make, though…?"
    play voice "10-2-7.mp3" #amree
    sis "I used the whole box!"
    play voice "10-2-8.mp3" #potato
    pro "B-but that's good for forty-two pancakes! There are THREE of us!"
    play voice "10-2-9.mp3" #amree
    sis "Uh, two, actually, Dad went for work early. B-but I asked him how to make coffee, and then he showed me, so now I can do that too!"
    play voice "10-2-10.mp3" #potato
    pro "I… that's really great, sis, heheh…"
    play voice "10-2-11.mp3" #amree
    sis "Are you hungry? I got some in a plate over there for you! And I'll make some for myself here..."
    play voice "10-2-12.mp3" #potato
    pro "I-I'm so glad you went through all this effort, but… there's like sixteen pancakes here, I can't finish that many by myself." 
    play voice "10-2-13.mp3" #amree
    sis "...Oh. That is a lot, heheh…" 

    "Oh, what a mess this is, though… the sink was just filled with mixing tools. She was trying her best, but…" 
    "I'm gonna help her."

    play voice "10-2-14.mp3" #potato
    pro "Hey, sis, how much pancake batter do you have left over?"
    play voice "10-2-15.mp3" #amree
    sis "...Uhh… this much."

    "That is a lot of it, isn't it. Guess this morning is going to be more hectic than I had hoped."

    play voice "10-2-16.mp3" #potato
    pro "Ahhh… cover that bowl up in plastic wrap, and we'll make more tomorrow."
    play voice "10-2-17.mp3" #amree
    sis "Oh, um, okay. But I was gonna-"
    play voice "10-2-18.mp3" #potato
    pro "Yeah, we'll split my pancakes, it'll be good for the both of us. And then I'll help you do the dishes and clean up, okay?"
    play voice "10-2-19.mp3" #amree
    sis "...Mm…"
    play voice "10-2-20.mp3" #amree
    sis "Okay! I'm really hungry!"

    "Breathing a sigh of relief, her boundless enthusiasm momentarily quelled, we sat the table to enjoy our meal together." 
    "Cutting into mine, I take a piece and take a bite. It's good, though a little overcooked."
    "I notice, across the table, Maria was staring at me with great interest."
    "Hmmm… what should I say?"
    menu:

        "My compliments to the chef!":
            $ career += 1
            jump compliment

        "Needs more seasoning.":
            jump seasoning

label compliment:
    play voice "10-2-21.mp3" #potato
    pro "My compliments to the chef! Best way to start the morning!"
    play voice "10-2-22.mp3" #potato
    pro "The fluffiness of the pastry is complimented well by the slight crisp, all melting together under the care of the artificial maple syrup product."
    play voice "10-2-23.mp3" #amree
    sis "Yay! I'm glad you like it!"
    "We share a laugh, raising our glasses of orange juice in good cheer."
    jump pancakes

label seasoning:
    play voice "10-2-24.mp3" #potato
    pro "Mm… could use a little extra spice. More zing."
    play voice "10-2-25.mp3" #amree
    sis "Eh? Zing?"
    play voice "10-2-26.mp3" #potato
    pro "Y'know, like, {i}pow{/i}. Have you tried cayenne pepper?"
    play voice "10-2-27.mp3" #amree
    sis "O-On a pancake??"

    "Her eyes widen with some mixture of trepidation and intrigue. Oh goodness, she was actually considering it."

    play voice "10-2-28.mp3" #potato
    pro "Yeah, uh, don't try it. It's awful."
    play voice "10-2-29.mp3" #potato
    pro "These pancakes are really good though, great stuff."
    play voice "10-2-30.mp3" #amree
    sis "Oh! Shoulda just said so in the first place!"
    play voice "10-2-31.mp3" #potato
    pro "Teasing you is fun, though.~"
    jump pancakes

label pancakes:
    play voice "10-2-32.mp3" #amree
    sis "I… think I overcooked them a little, honestly. But I'm a little new to all this, so…"
    play voice "10-2-33.mp3" #potato
    pro "You did pretty good on your own, but… why'd you do all this?" 
    play voice "10-2-34.mp3" #amree
    sis "I… well, Mom isn't here, and we dunno when she's coming back, so…"
    play voice "10-2-35.mp3" #amree
    sis "Everyone else is working really hard, so I should help out too. And all I had to do was follow the instructions on the box, so…"

    "I see. She was just trying to help…" 

    menu:
        "\"Thanks Maria.\"":
#             $ career += 1
            jump praise

        "\"Be careful when cooking.\"":
            jump stopusinglectureasalabel

label praise:
    play voice "10-2-36.mp3" #potato
    pro "I think you did a really good thing, today. It was good of you to show initiative, and I appreciate a good meal."
    play voice "10-2-37.mp3" #amree
    sis "You think so??"
    play voice "10-2-38.mp3" #potato
    pro "Yup! Just… ask one of us for help next time. I'm sure Dad would've been able to stay behind a bit." 
    play voice "10-2-39.mp3" #amree
    sis "Oh, sure. Of course!"
    "Maria is really maturing. She's probably being the strongest of all of us right now, and she's putting her best foot forward every day."
    "I couldn't wish for a better sister."
    jump hotcakes

label stopusinglectureasalabel:
    play voice "10-2-40.mp3" #potato
    pro "It's dangerous to be working around the stove alone, Maria. I'm glad you came out of it okay, but…"
    play voice "10-2-41.mp3" #amree
    sis "It's not a big deal, right? I was fine, and I've watched Mom do it before, and I followed the instructions, so it worked out!"
    play voice "10-2-42.mp3" #potato
    pro "Yeah, but… you should really… get Mom to show you how to do it next time."
    play voice "10-2-43.mp3" #amree
    sis "...But Mom isn't here right now…" 
    "Her head droops, as does mine. Mom isn't here. She's walked out on us, and we have no idea when she's getting back."
    "I wish she was here right now… I bet Maria feels the same way."
    jump hotcakes

label hotcakes:
    play voice "10-2-44.mp3" #amree
    sis "Mom isn't here right now, so I figured… m-maybe I could be, like, a replacement mother."
    play voice "10-2-45.mp3" #amree
    sis "I know I'm not as good at it as she is, but…"
    play voice "10-2-46.mp3" #potato
    pro "It's okay. You're still learning. You're gonna be a great mom." 
    play voice "10-2-47.mp3" #amree
    sis "...I know I can be."

    "Her eyes lit up with optimism. She's able to say that with such strength and conviction."
    "Maria really was incredible. I hope the others come to see that."

    play voice "10-2-48.mp3" #potato
    pro "Do you wanna be a mom when you grow up?"
    play voice "10-2-49.mp3" #amree
    sis "Y-yeah! I'm gonna get married and have a family of fifty!"

    "I nearly choke on the pancake piece I was chewing. What on Earth?"

    play voice "10-2-50.mp3" #potato
    pro "W-wow, that's, uh, a lot."
    play voice "10-2-51.mp3" #amree
    sis "You'll be part of my family too, right?"

    "Her offer's so genuine, too. She really put her heart into everything she did."
    "I hope to God I don't cry again this morning. Twice is too many times to tear up at the start of the day."

    play voice "10-2-52.mp3" #potato
    pro "...Silly goose, we're already family. We always will be."
    play voice "10-2-53.mp3" #amree
    sis "...Even if Mom's gone?"
    play voice "10-2-54.mp3" #potato
    pro "...Of course."
    play voice "10-2-55.mp3" #amree
    sis "...She's really upset, and she's made a lot of mistakes, but I believe in her."
    play voice "10-2-56.mp3" #amree
    sis "You're probably really mad at her, but… please don't shout at her when she gets back, okay?"
    play voice "10-2-57.mp3" #potato
    pro "...I… I won't Maria. We have enough shouting matches in this household…" 

    "We quietly finish our meals, enjoying each others company."
    "It's at this moment, cleaning our plates, I realize I'm going to miss my first class entirely, and probably a hefty chunk of my second class as well, just by cleaning the dishes and taking Maria to school!"
    "Maria says she can get to school on her own, so I shouldn't be late for mine, but… is that okay?" 
    "...No. I should trust Maria. She's a smart girl, and can handle herself. And I know she wants to at least try going to school on her own."
    scene black with dissolve

    "We part ways. This fast-paced morning isn't about to slow down anytime soon. I better book it…" 

    jump day10s2

