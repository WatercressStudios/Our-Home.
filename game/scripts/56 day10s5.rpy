label day10s5:

$ sappyalex = False
scene livingroom night

show bro smirk1 with dissolve:
    align (0.65, 1.0)
voice "10-5-0.mp3" #kujira
bro "Hey, Maria?"

"Alex sticks his head into the front door."

"No response. Is Maria asleep…?"
show bro sad1 with dissolve:
    align (0.65, 1.0)

"Alex really wants to see her, huh…"

menu:
    "See Maria":
        $ sappyalex = True
        jump reunion

    "Take Alex to his room":
        jump bedtime

label reunion:
    voice "10-5-1.mp3" #potato
    pro "Well… she's probably a little scared but… let's see if we can't coax her out…"

    scene black with dissolve

    "We ascend the staircase. Alex has a little more spring to his step than he did on the way in."

    scene brodoor dark with dissolve 

    "Stepping outside Maria's door, I notice something odd."

    "There's a little light streaming out from underneath the door. Was she still up?"

    voice "10-5-2.mp3" #potato
    pro "Maria? Are you awake?"
#    voice "10-5-3.mp3" #amree silence
    sis "..."

    "No response. I glance towards Alex, before taking another breath."

    voice "10-5-4.mp3" #potato
    pro "Alex is here. He was really hoping to see you. Could you come out?"

    "My voice was a little above a dulcet whisper."

    "A dreadful pause follows. Is she listening…?"

    "...Ah! I hear movement! She's getting up!"

    play sound opendoor
    "The door cracks open slowly… agonizingly slow."

    scene sisroom dark with dissolve
    show sis cry with dissolve:
        align (0.35, 1.0)
    "My posture is lowered to try and meet her eyes, so I was the first to notice."

    "She's crying. She raises her wrist to rub at her eyes."

    "Alex looks pained as well. It takes a lot for him to drop his guard like this."

    voice "10-5-5.mp3" #kujira
    bro "Maria? A-are you alright?"

    voice "10-5-6.mp3" #amree
    sis "*sniff* ...I-I'm fine. I… missed you."

    voice "10-5-7.mp3" #kujira
    bro "You missed me…?"

    voice "10-5-8.mp3" #amree
    sis "Y… yeah… I-I thought I'd never get to see you again, th-that they'd taken you away and-"

    voice "10-5-9.mp3" #kujira
    bro "Maria, Maria, it's… it's okay! I'm here, it's okay…" 

    show bro sad1 with dissolve:
        align (0.65, 1.0)
    
    "Alex kneels down to get a better look at Maria, raising a hand to her face to wipe away some of the tears."

    "She fidgets slightly with the contact, but settles down, her wet eyes looking up at his."

    "Silently, I step back, allowing them to make up lost time."

    voice "10-5-10.mp3" #kujira
    bro "...I-I guess some of the bruising is healing…"

    voice "10-5-11.mp3" #amree
    sis "...I'm sorry…"

    show bro sad2 with dissolve:
        align (0.65, 1.0)
    voice "10-5-12.mp3" #kujira
    bro "What? No, it's… it's I who should be apologizing to you, I…"

    show bro angry1 with dissolve:
        align (0.65, 1.0)
    voice "10-5-13.mp3" #kujira
    bro "...I feel… awful, about what happened, and…"

    voice "10-5-14.mp3" #kujira
    bro "I promise… I won't hurt you ever again."

    voice "10-5-15.mp3" #amree
    sis "But… but I only made things worse, didn't I?"

    show bro sad1 with dissolve:
        align (0.65, 1.0)
    voice "10-5-16.mp3" #amree
    sis "I-I didn't know what to do, and I…"

    voice "10-5-17.mp3" #kujira
    bro "It's… it's not your fault. Your big bro made some big mistakes, and…"

    show bro cry with dissolve:
        align (0.65, 1.0)
    voice "10-5-18.mp3" #kujira
    bro "He's gonna get better, okay? So you don't have to be afraid anymore."

    voice "10-5-19.mp3" #amree
    sis "...I missed you. So much."

    "Maria sobs, leaning forward into Alex's chest. He holds her tightly."

    "...It's then I notice that Maria is holding something. A piece of paper? It's scrunched up and damp with tears."

    voice "10-5-20.mp3" #potato
    pro "H-hey, Maria. What's that in your hand…?"

    show sis sad1 with dissolve:
        align (0.35, 1.0)
    voice "10-5-21.mp3" #amree
    sis "Ah? It's… I drew it for you."

    show sis sad2 with dissolve:
        align (0.35, 1.0)
    voice "10-5-22.mp3" #amree
    sis "A-and Alex. And… everyone."

    play sound paper
    "Standing up straight, she carefully unfolded the picture, holding it up for us to see."
    
    show drawing with dissolve

    "A hand drawn picture of our family. It's... adorable. Heartbreaking..."

    "The top's dated. She's been working on it for over a week…"

    voice "10-5-23.mp3" #amree
    sis "I-I've been drawing it every morning…"

    voice "10-5-24.mp3" #potato
    pro "This is why you've been late getting up recently."

    voice "10-5-25.mp3" #amree
    sis "Yeah… I'm sorry."

    voice "10-5-26.mp3" #kujira
    bro "It's… it's pretty good!"

    voice "10-5-27.mp3" #kujira
    bro "I mean, the shading could be touched up, and the colouring in the lines could be a bit cleaner, but…"

    voice "10-5-28.mp3" #potato
    pro "I love it. And Alex loves it too, right?"

    voice "10-5-29.mp3" #kujira
    bro "...Heh. Yeah. Figured the {i}artiste{/i} like some constructive critique, y'know…?"

    hide drawing with dissolve
    
    show sis happy1:
        align (0.35, 1.0)
    show bro smile2:
        align (0.65, 1.0)
    
    "Maria's finally smiling again. Even through her tears, her smile shines so radiantly."

    voice "10-5-30.mp3" #amree
    sis "Y, you guys are the… the best family I could ask for. A-and I wanted to give something back, so I…"

    voice "10-5-31.mp3" #potato
    pro "Oh sis… you've given us so much. How about we give something to you?"

    "I squeeze Alex's hand. He glances over to me, nodding affirmatively."

    show sis sad2 with dissolve:
        align (0.40, 1.0)
    show bro sad1 with dissolve:
        align (0.60, 1.0)
    
    "We both wrap Maria in a great big hug. Her small, trembling body, enveloped in warmth, is gently sandwiched between us."

    "This is the least we can give her. To the girl who believed in our family this whole time. Who still believes, with all her heart."

    "I don't want to break her heart. Alex must feel the same."

    voice "10-5-32.mp3" #amree
    sis "Are we a family again…?"

    show sis cry with dissolve:
        align (0.40, 1.0)
    voice "10-5-33.mp3" #potato
    pro "We're getting there… we have each other now."

    show bro cry with dissolve:
        align (0.60, 1.0)
    voice "10-5-34.mp3" #kujira
    bro "God, I missed you guys…"

    "For those quiet moments, we all hold each other. The three of us, united again."

    scene black with dissolve

    "I know I'm supposed to be strong for the family, but… I know I felt a few quiet tears roll down my cheeks."

    "I think Alex felt it too, himself. He'd never admit it, though."

    scene sisroom dark with dissolve

    show bro grin2 with dissolve:
        align (0.65, 1.0)
    voice "10-5-35.mp3" #kujira
    bro "Hey, Em. Maria and I got a lot to catch up on. How about you post her drawing up on the fridge for us?"

    show sis worry2 with dissolve:
        align (0.35, 1.0)
    voice "10-5-36.mp3" #amree
    sis "What!? The fridge!? But Mom only uses that space for important things."

    voice "10-5-37.mp3" #potato
    pro "I think it's very important, but…"

    voice "10-5-38.mp3" #potato
    pro "Alex, shouldn't you get some rest? And you too, Maria?"

    show bro grin1 with dissolve:
        align (0.65, 1.0)
    voice "10-5-39.mp3" #kujira
    bro "Em, look at it this way… our parents aren't home, and I just got out of several days of strictly regimented hospital life."

    show bro smile2 with dissolve:
        align (0.65, 1.0)
    voice "10-5-40.mp3" #kujira
    bro "Lemme have a bit with my lil sister, okay?"
    
    show sis happy2 with dissolve:
        align (0.35, 1.0)

    voice "10-5-41.mp3" #potato
    pro "...Okay. But don't stay up too late. I'm coming to check up on you two in a bit."

    show bro smirk2 with dissolve:
        align (0.65, 1.0)
    voice "10-5-42.mp3" #kujira
    bro "Ugh, you sound like Mom…"

    show sis happy1b with dissolve:
        align (0.35, 1.0)
    
    "Maria lets out a short giggle."

    "All of us with smiling faces again."
    
    
    play sound paper
    show drawing with dissolve
    
    "I unfold Maria's drawing, and look it over one more time."

    "This… this is what Maria dreams of, isn't it? The whole family back together?"

    "...No. This isn't just her dream."

    scene black with dissolve
    
    "It's our dream, too."

    jump day10s5continue

label bedtime:
    voice "10-5-43.mp3" #potato
    pro "C'mon Alex. Let's go to bed."

    voice "10-5-44.mp3" #kujira
    bro "...Okay."

    "A look of disappointment flashes across his face, but it gives way to exhaustion quickly. I should hurry…"

    scene black with dissolve

    "..."

    scene broroom dark with dissolve

    show bro sad1 with dissolve
    
    voice "10-5-45.mp3" #potato
    pro "You going to be okay in here, Alex?"
    
    show bro happy2 with dissolve
    
    voice "10-5-46.mp3" #kujira
    bro "Yeah, yeah. You dote on me too much."

    voice "10-5-47.mp3" #potato
    pro "I know. It's just… we almost lost you, okay? I don't want to lose you for real this time."

    show bro grin2 with dissolve
    
    voice "10-5-48.mp3" #kujira
    bro "If anything, I wouldn't die alone in this room, would I? I'm out of the hospital for a reason. I'm cleared to be alone, now. I won't leave you guys this time."

    "I sigh, leaning against the doorframe to his bedroom. In front of me, Alex is preparing for sleep. He still looks like shit, and he's still sluggish, but he's better than he was in the hospital."

    "I still have issues trying to forget seeing him that way… I don't want to ever find him like that again."

    voice "10-5-49.mp3" #potato
    pro "You promise?"

    show bro smirk2 with dissolve
    voice "10-5-50.mp3" #kujira
    bro "Of course. Now let me get some sleep, God."

    "At least he hasn't changed all too much. Rolling my eyes, I back out of his room and close his door."
    stop music fadeout 1.0
    
    scene black with dissolve
    "Okay, time to check up on one last person before I go to sleep myself."
    
    scene brodoor dark with dissolve

    "Before heading to bed, I notice there's a bit of light trickling from underneath Maria's door."

    "Does she have a light on…? What could she be doing at this hour?"

    "I knock on Maria's door before entering."
    play music bgmsis fadeout 1.0 fadein 0.0
    voice "10-5-51.mp3" #potato
    pro "Heya, are you awake?"

    voice "10-5-52.mp3" #amree
    sis "Yeah…"

    play sound opendoor
    scene sisroom dark with dissolve
    show sis cry with dissolve
    
    "She's sitting on her bed with a piece of paper in her hands."

    voice "10-5-53.mp3" #amree
    sis "I couldn't sleep. I wanted to see Alex so bad, but when he came home…"

    voice "10-5-54.mp3" #amree
    sis "I was too nervous, and stayed here instead."

    "Tears well up in her eyes. She cries out, covering her face, her tears getting onto her paper."

    "I rush over to her, holding her close to me."

    "She rests her head against my chest."

    voice "10-5-55.mp3" #amree
    sis "I-I wanted to see him again when he was in the hospital…"

    voice "10-5-56.mp3" #amree
    sis "But then he came h-home and I was too afraid."

    voice "10-5-57.mp3" #amree
    sis "I'm a bad sister aren't I?"

    "Her words come out a blubbery mess, her face squished up."

    "I stop myself from crying with her. Gotta be strong..."

    voice "10-5-58.mp3" #potato
    pro "Of course not, Maria. Of course not. He understands, he really does."

    "I keep her close, even if she's soaking my top."

    voice "10-5-59.mp3" #potato
    pro "He missed you too. He just needs a bit of time to rest up, now that he's home. He'll be around tomorrow."

    show sis sad1 with dissolve
    
    voice "10-5-60.mp3" #amree
    sis "But I don't know that! He almost left us once, he could do it again."

    "I pull her into a bearhug, rocking her back and forth."

    show sis cry with dissolve
    voice "10-5-61.mp3" #potato
    pro "He won't. He won't ever leave us, not again. He's better, now. We're better now."

    "We are. Mom might not be home right now, but the rest of us finally are."

    "I release her, and tuck her into bed."

    voice "10-5-62.mp3" #potato
    pro "Oh, you got your paper all wet…"
    
    voice "10-5-63.mp3" #amree
    sis "O-oh…"

    "She continues to bawl her eyes out."

    voice "10-5-64.mp3" #amree
    sis "T-that was for you…"

    "I grab it from her hands, unwrinkling it."
    ###HOLDING OUT FOR DRAWING CG##
    
    "...It's a picture."

    "A hand drawn picture of our family. It's surprisingly good, given her age. Well done."

    "The top's dated. She's been working on it for over a week…"

    voice "10-5-65.mp3" #amree
    sis "I-I've been drawing it every morning…"

    voice "10-5-66.mp3" #potato
    pro "This is why you've been late getting up recently."

    voice "10-5-67.mp3" #amree
    sis "Yeah… I'm sorry."

    voice "10-5-68.mp3" #potato
    pro "No need to be. I love it."

    "Truth be told, it's not the best picture in the world, but it's hers. She made it for me, because she saw how tired I was."

    "She's truly an empath."

    "She wanted to brighten my day, so she worked her little heart out on this… just for me."

    voice "10-5-69.mp3" #potato
    pro "It's perfect just the way it is."

    "No matter the flaws, it's beautiful in my eyes."

    show sis happy2b with dissolve
    "I kiss her on her forehead, pulling her plushie close to her."

    voice "10-5-70.mp3" #potato
    pro "You're the best sister I ever could have asked for, Maria."

    voice "10-5-71.mp3" #potato
    pro "I love you, okay?"

    voice "10-5-72.mp3" #amree
    sis "I love y-you too, Emily…"

    voice "10-5-73.mp3" #potato
    pro "I'm going to go put this in a frame in my room. Get some good sleep, okay? I'll see you tomorrow."

    show sis happy1b with dissolve
    voice "10-5-74.mp3" #amree
    sis "Night…"

    voice "10-5-75.mp3" #potato
    pro "Goodnight."

    scene black with dissolve
    
    "I turn off her lamp, giving her one last look before backing out."

    if not laurendrives:

        "It's best if I get to bed now. It's been a long day, and I have to be ready for whatever comes my way tomorrow."

    else:
        scene livingroom night with dissolve
        show lov happy2 with dissolve
        "I head back to the living room, where Lauren sits quietly."
        play music bgmlov2 fadeout 1.0 fadein 0.0
        voice "10-5-76.mp3" #potato
        pro "...Weren't you gonna head home?"

        show lov happy2h with dissolve
        voice "10-5-77.mp3" #starleeter
        lov "Ohhh, I snuck in. I didn't wanna miss the happy reunion. How're they doing?"

        voice "10-5-78.mp3" #potato
        pro "Ah… Alex is the same as always. He's better, now, and we have an understanding that we didn't really have before."

        voice "10-5-79.mp3" #potato
        pro "Maria is really, really happy to see that Alex is back home."

        show drawing with dissolve
        "I sit next to her, showing her the picture Maria drew for me"

        voice "10-5-80.mp3" #potato
        pro "There's also this. Apparently Maria's been working on this for the past week. She's been really worried about me, and she wanted to cheer me up…"

        voice "10-5-81.mp3" #starleeter
        lov "D'awwww~ That's super nice of her! The drawing is suuuuper cute, too."

        voice "10-5-82.mp3" #starleeter
        lov "Your family all standing together. I love it!"

        voice "10-5-83.mp3" #potato
        pro "Yeah, I'm going to frame it in my room. It's something really small, but it's from her, which makes it the world to me."

        hide drawing with dissolve
        
        show lov happy1b with dissolve
        voice "10-5-84.mp3" #starleeter
        lov "It's like a photo a mom would put on a fridge. We're like parents now!"

        "She pulls me close for a hug, shaking me up and down. She's as hyper as ever."

        voice "10-5-85.mp3" #potato
        pro "Yeah, right? If she hadn't given it to me as a special gift, I really would have put it on the fridge."

        show lov happy2 with dissolve
        voice "10-5-86.mp3" #starleeter
        lov "Maybe you can when you get a fridge of your own~"

        voice "10-5-87.mp3" #potato
        pro "You think so?"

        voice "10-5-88.mp3" #starleeter
        lov "Yeah, sure thing!"

        "Chuckling, I stand back up."

        voice "10-5-89.mp3" #potato
        pro "Well, one day. In the meantime, it's dark and you need to get to sleep young ma'am!"

        show lov shy2 with dissolve 
        voice "10-5-90.mp3" #starleeter
        lov "Awwww, I wanted to spend more quallliiity time with my bestest friend in the whole world!"

        voice "10-5-91.mp3" #potato
        pro "Your pouting won't get to me, missy. Go get some sleep!"

        show lov shy1b with dissolve
        voice "10-5-92.mp3" #starleeter
        lov "Fiiiiine, yes ma'am."

        "She gives an exaggerated flourish as she turns to the door."

        show lov happy2 with dissolve
        voice "10-5-93.mp3" #starleeter
        lov "Be seein' ya soon!"

        voice "10-5-94.mp3" #potato
        pro "See ya."

        hide lov with dissolve
        "Now that she's gone, I should really be taking my own advice."

        "It's best if I get to bed now. It's been a long day, and I have to be ready for whatever comes my way tomorrow."

        scene black with dissolve
        play sound paper
        "I go back to my room, putting the picture in a frame large enough to fit it. I rest it center stage of my desk, serving as a reminder as to just why I'm here."

    jump day10s5continue

label day10s5continue:

    "The pieces are finally coming back together. This fragmented home still has hope yet."
    stop music fadeout 1.0

    jump day11s1