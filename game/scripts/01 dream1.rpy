label dream1:

    play music bgmdream fadeout 1.0 fadein 3.0
    scene dream1 with Dissolve(3.0)

    "I always enjoy coming back to this place."
    "Opening the door into the living room, I’m hit with the enchanting fragrance of fresh pine."

    scene dlivingroom with dissolve

    "Dad loves working with pine, and there’s no shortage of evergreens around our house. It shows, as homemade pieces are scattered around the living room."
    "I look upon the upholstered club chair dominating the middle of the living room. It’s unoccupied, which piqued my curiosity."
    "Normally, Dad will be reading the paper in it and be ready with a greeting, followed shortly by an embarrassing quip. His absence, it seems, hangs in the air like a spectre."
    "I can feel the presence of others in this old house. Focusing my hearing, I can pick up dull murmuring coming from… the hallway?"
    "I can’t help grinning. They aren’t seriously gonna do that, are they?"

    voice "d1-1-1.mp3" #potato
    pro "Heh, alright, guess there's no avoiding it, you dorks."

    "Pacing over to the door, I brace myself for the inevitable…"

    scene dhallway with dissolve

    voice "d1-1-2.mp3" #all
    all "Happy birthday!"

    voice "d1-1-3.mp3" #potato
    pro "Aww, guys…"

    "They remember. It’s my birthday. Number eighteen."
    "I guess I'm technically an adult now? It feels weird, but… a good weird."
    "I definitely asked them not to make a big event out of it, but here they are. God, my cheeks are flushing..."

    scene dlivingroom with dissolve

    show dbro smile

    voice "d1-1-4.mp3" #kujira
    dbro "Sweet eighteen, sis! Took your sweet time gettin' here, huh?"

    voice "d1-1-5.mp3" #potato
    pro "Heh, you do know it's called a sweet sixteen, right?"

    #brother should have an expression of surprise

    voice "d1-1-6.mp3" #kujira
    dbro "Ah, right! Well, uh, regardless, I don't really get your point. Like, every birthday's supposed to be sweet, y'know?"

    voice "d1-1-7.mp3" #potato
    pro "Ah, yes, of course, you're right. My mistake.~"

    hide dbro

    "Smiling, I take my seat at the head of the table."
    "It’s weird, seeing Dad at the side instead of the head, but I get over that feeling quickly."

    show dmom smile with dissolve:
        align (0.25, 1.0)
    show ddad smile with dissolve:
        align (0.75, 1.0)

    voice "d1-1-8.mp3" #lacTheWatcher
    ddad "Happy birthday, sweetie. Hate to surprise you like this, but we all got a little ahead of ourselves this year…"

    #mom's mouth should open wide, indicate more excitement

    voice "d1-1-9.mp3" #kaito
    dmom "Old John getting excited for something, oh yes! You went to Samantha's and brought back the flour and sugar, right?"

    #close dad's eyes, indicate pensive thought, still smiling

    voice "d1-1-10.mp3" #lacTheWatcher
    ddad "Mm, yeah, I sure did. Did a hell of a job with the centerpiece, I gotta say."

    "Even in this festive atmosphere, Dad carries an air of gentle calm and dignity. I don't know how anyone can keep such a straight face with all of these gaudy streamers strung up."

    "Ah well. I'm having fun."

    hide dmom
    hide ddad
    show dbro smile

    voice "d1-1-11.mp3" #kujira
    dbro "Diane and I handled the decorations. Her idea, I just provided the muscle."

    "Wait, it’s {i}her{/i} idea? My eyes dart across the table in amazement."

    hide dbro
    show dlov smile

    "Sure enough, it’s Diane at the other end of the table, a silent observer, her expression glowing with a warm smile."
    "She’s looking right at me too. Our eyes meet."

    #close dream girl eyes for a moment, indicate a silent laugh

    "Oh gosh, we looked right into each other’s eyes! She quietly laughs as I sink a little into my chair."
    "God, she can read me like a book… I feel my cheeks flushing with redness."

    voice "d1-1-12.mp3" #potato
    pro "This is too much guys, really…"

    show dlov with dissolve:
        align (0.25, 1.0)
    show dbro happy with dissolve:
        align (0.75, 1.0)
    #pan dream girl to left before brother comes in

    voice "d1-1-13.mp3" #kujira
    dbro "Hey, no sweat! Just means you'll have to pay the family back later!"
    voice "d1-1-14.mp3" #kujira
    dbro "Mom 'n Pop's anniversary's coming up, right?"

    voice "d1-1-15.mp3" #potato
    pro "Ah, of course."

    hide dlov
    hide dbro
    show dmom smile with dissolve:
        align (0.25, 1.0)
    show ddad smile with dissolve:
        align (0.75, 1.0)

    "I nod. It’s true. Mom and Dad give each other knowing looks."

    hide dmom
    hide ddad
    show cake
    #can just be a sprite of a cake instead of a cg or w.e

    "I look down at the cake. It’s really impressive, it won’t be out of place at a metropolitan bakery!"

    "The icing forms a gentle, delicate curve as it wraps around the cake."

    "The candles are arranged in a perfect circle. Eighteen of them. I can feel the heat emanating from them."

    voice "d1-1-16.mp3" #kaito
    dmom "Do you know what you're going to wish for?"

    voice "d1-1-17.mp3" #kujira
    dbro "Don't pry it from her, Ma! It's gotta be a secret!"

    voice "d1-1-18.mp3" #lacTheWatcher
    ddad "Haha, that is true… you don't have to tell us if you don't want to."

    "I smirk at this exchange. My lil’ brother is always looking out for me, even over the silliest details."

    voice "d1-1-19.mp3" #potato
    pro "It's all right up in here."

    "I tap my forehead affirmatively, a wry grin spreading across my cheeks."

    "I haven’t really given it much thought, but… yeah, I ought to wish for something. Sweet eighteen, and all that."

    "What to wish for… I wish…"

    menu:

        "I wish for this moment to last.":
            jump dream1cake

        "I wish for a better tomorrow.":
            jump dream1cake

        "I wish for world peace.":
            jump dream1cake

label dream1cake:
    "I take a deep breath, and…"

    hide cake
    show black

    stop music fadeout 0.3
    play sound thud
    "{b}WHUMP!{/b}"

    scene black

    stop music

    $ renpy.movie_cutscene("vfx/dreamtoirl.mpg") # Loads the credit video
  
    
    scene black 

    jump day1s1
