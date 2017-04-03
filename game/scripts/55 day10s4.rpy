label day10s4:

    $ laurendrives = False

    scene siswalk2 with dissolve

    "Walking Maria home from school again. I think Maria's still worried about Mom, so it's a quiet walk so far…"

    # TODO cellphone
    # play sound cellphonechime

    "Oh, a text! Let's see who it's from…"
    "...Alex?"
    voice "10-4-1.mp3" #amree
    show sis happy1
    sis "Wh, who's that? Are you scared??"
    voice "10-4-2.mp3" #potato
    pro "N, no, it's just… it's from Alex."
    voice "10-4-3.mp3" #potato
    pro "He says he's getting discharged today…!"
    voice "10-4-4.mp3" #amree
    show sis worry2
    sis "What? No, they can't… they can't do that to him…!"
    voice "10-4-5.mp3" #potato
    pro "N, no, Maria, that's good! It means they're letting him come home."
    voice "10-4-6.mp3" #amree
    show sis happy1
    sis "Oh, really! I, it is good!"
    "But wait, who’s picking up Alex? Hmm, Mom was at the hospital yesterday..."
    voice "10-4-7.mp3" #potato
    pro "Lemme send a text to Mom to pick him up. Oh God, she'll be so relieved."
    voice "10-4-8.mp3" #amree
    sis "A-and then we'll all be together again?"
    voice "10-4-9.mp3" #potato
    pro "Yeah! Let's wait for him tonight. It'll be like a little party!"
    voice "10-4-10.mp3" #amree
    sis "...Okay! I'll wait for him..."
    "With the good news, our walk home is a lot chipper."

    scene black with dissolve
    "God, I can't wait to see him."
    "..."


    scene livingroom sunset with dissolve

    "Later that night, we sit across from one another in dreary silence."
    "Isn't Mom going to be home with Alex any minute? How much longer…?" 
    "Alex is supposed to be discharged from the hospital tonight. Why's it taking so long?"
    "Maria's quieter than usual, almost deathly still. On any other night, she'd be asking me question after question, but…" 
    "Let's get her attention." 

    voice "10-4-11.mp3" #potato
    pro "Hey, Maria. What's the matter?"
    voice "10-4-12.mp3" #amree
    show sis sad1
    sis "I… I haven't seen Big Brother since… y-y'know…"
    voice "10-4-13.mp3" #amree
    show sis sad2
    sis "I-I know I should be excited, and happy, but… I-I'm kind of scared of… what he'll think of me…"
    voice "10-4-14.mp3" #potato
    pro "Ah…"

    "Of course. That night."
    #flashback of moment in greyscale, probably with appropriate soundeffect

    "It's understandable. Maria must've had more time to think about it."
    "She hasn't seen her brother since that awful night. She probably blames herself, on some level."
    "She looks so uncomfortable. I should say something to her…" 

    menu:
        "Cheer up.":
            jump cheerup

        "It's okay to be scared.":
            jump scared

label cheerup:
    voice "10-4-15.mp3" #potato
    pro "Hey, you should cheer up a bit. Alex is coming home tonight."
    voice "10-4-16.mp3" #potato
    pro "I'm sure he'd be relieved to see you smiling again."
    voice "10-4-17.mp3" #amree
    show sis sad1
    sis "Nn…" 
    voice "10-4-18.mp3" #potato
    pro "...And I'm sure he misses you a lot as well."
    voice "10-4-19.mp3" #amree
    show sis sad2
    sis "It's hard, I… I'm scared, but… I have to try."
    "I frown slightly. She only feels worse now…" 
    jump upstairs

label scared:
    voice "10-4-20.mp3" #potato
    pro "It's okay to be scared, after everything that happened…" 
    voice "10-4-21.mp3" #potato
    pro "You don't have to see him if you don't want to."
    voice "10-4-22.mp3" #amree
    sis "B… but then I'd be a bad sister, wouldn't I?"
    voice "10-4-23.mp3" #potato
    pro "I…"
    "I don't know what to say to that. How can she blame herself for what happened?"
    jump upstairs

label upstairs:
    voice "10-4-24.mp3" #amree
    show sis worry1
    sis "Can I go upstairs? I… I was doing something."
    voice "10-4-25.mp3" #potato
    pro "...Okay. You shouldn't stay up late anyway…"
    voice "10-4-26.mp3" #potato
    pro "I'll see you tomorrow, Maria."
    hide sis
    "Quick as a bunny, she scampered up the stairs, stopping to send one last, pitiful look towards me before disappearing around a corner."
    "And then there was one. Just me."
    voice "10-4-27.mp3" #potato
    pro "Not much of a welcome home party, is it…" 
    "Dad's hammered by work. Maria's traumatized. Mom won't be happy about this."

    # TODO cellphone
    # play sound ringtone

    voice "10-4-28.mp3" #potato
    pro "!"
    "My phone! Who's calling?"
    "I check the ID."
    voice "10-4-29.mp3" #potato
    pro "...Alex???"
    "I pick it up quickly, the force of my sliding motion nearly toppling me from my chair."
    voice "10-4-30.mp3" #potato
    pro "H-hello!? Alex!?"
    voice "10-4-31.mp3" #kujira
    bro "Hey, hey, not so loud. My head's killing me, heh."
    voice "10-4-32.mp3" #potato
    pro "Oh my God, hi! You! You, ah, sound chipper!"
    voice "10-4-33.mp3" #kujira
    bro "I mean, I guess, in comparison, uh… where's the cavalry?"
    voice "10-4-34.mp3" #potato
    pro "Cavalry? What, Mom?"
    voice "10-4-35.mp3" #kujira
    bro "Yeah, I've been here for an hour, but I haven't seen her."
    voice "10-4-36.mp3" #kujira
    bro "I keep poking my head out every few minutes…" 
    voice "10-4-37.mp3" #potato
    pro "...Damn it…" 
    "I'm such an idiot. I texted Mom to pick him up, but… in that moment of stupidity, I forgot."
    "She's gone."
    "I was too caught up on all of us being together again, and I… I messed up."
    voice "10-4-38.mp3" #potato
    pro "Damn it... you're stranded right now, aren't you?"
    voice "10-4-39.mp3" #kujira
    bro "Crossed my mind. Mom's still MIA?"
    voice "10-4-40.mp3" #potato
    pro "Yeah… lemme think of something, and I'll shoot you a text. Sit tight, okay?"
    voice "10-4-41.mp3" #kujira
    bro "Sure. How's Maria holding up?"
    voice "10-4-42.mp3" #potato
    pro "She's… okay."
    voice "10-4-43.mp3" #kujira
    bro "Good, good… alright, get back to me when you can."
    voice "10-4-44.mp3" #potato
    pro "Roger."

    "I hang up the phone, slumping back into my chair."
    "What do I do now? I have to send someone…"
    "Where the Hell is Mom anyway? I open her name up on my contacts and start to peck out an angry message…"
    voice "10-4-45.mp3" #potato
    pro "...Agh...What's the point…" 
    "Mom's not gonna do anything about it. She's been gone for… what, three days now?"
    "If anyone's gonna get Alex home, I'll have to think of something else…"

    menu:
        #Choice to call LI (LOVE+1), or not (LOVE+0).
        "Ask Lauren for help":
            $ laurendrives = True
            $ love += 1
            jump carpool

        "Call a taxi":
            jump taxi

label taxi:
    "Looking up a taxi company, I arrange one to swing by the hospital to pick up Alex."
    "I quickly shoot him a text explaining the situation before leaning back in my chair."
    "It'll be a while before he gets here. Might as well relax…"
    scene black with dissolve
    "..." 
    jump brohome2

label carpool:
    "Lauren has a car. I hate to bug her like this, but… it's an emergency."
    "I dial her number quickly."
    voice "10-4-46.mp3" #potato
    pro "Hey, Lauren? It's Emily. Listen, I have a {i}huge{/i} favour I need to ask of you…"
    scene black with dissolve
    "..."
    scene car with dissolve
    voice "10-4-47.mp3" #starleeter
    show lov confused1
    lov "...So your brother was left at the hospital for {i}how long{/i}??"
    voice "10-4-48.mp3" #potato
    pro "Few hours… I completely forgot about the thing with my mother…"
    voice "10-4-49.mp3" #starleeter
    show lov happy1h
    lov "Ah well! Not to fear, cavalry's here! Dun dun DAAAAA!~"
    voice "10-4-50.mp3" #potato
    show lov happy2h
    pro "Haha, it's so late, Lauren, how do you maintain this much pep at this hour…?"
    voice "10-4-51.mp3" #starleeter
    show lov happy1h
    lov "That's for me to know and for you to find out."
    "I hope she didn't, like, pound back an entire cappuccino…" 
    voice "10-4-52.mp3" #potato
    show lov happy2
    pro "I really appreciate you doing this for me, Lauren."
    voice "10-4-53.mp3" #starleeter
    show lov happy1
    lov "Hey, if I was at the hospital, I'd want to get out of there as quickly as possible too!"
    voice "10-4-54.mp3" #potato
    show lov happy2
    pro "Y-yeah, but... I don't want it to be like I'm using you as a personal chauffeur or anything…" 
    voice "10-4-55.mp3" #starleeter
    show lov confused2h
    lov "Huh? I didn't think of that."
    voice "10-4-56.mp3" #starleeter
    show lov happy1h
    lov "...Though now that you mention it, I guess it'd be okay if I got a cute little black suit…" 
    voice "10-4-57.mp3" #potato
    pro "!"
    voice "10-4-58.mp3" #starleeter
    show lov happy1bh
    lov "You'll figure that out, right Miss Fashion Designer?~"
    "I'm speechless, my cheeks flushing right up."
    "Lauren catches this, and lets out a cheery giggle."
    voice "10-4-59.mp3" #starleeter
    show lov happy1
    lov "It's fine, it's fine! It's an emergency, right?"
    voice "10-4-60.mp3" #starleeter
    show lov shy2
    lov "And... I guess I have some ulterior motives. I wanted to see your brother again."
    voice "10-4-61.mp3" #potato
    pro "...Really?"
    voice "10-4-62.mp3" #starleeter
    lov "Well, yeah, I don't think I've seen him since the intervention the first time…"
    voice "10-4-63.mp3" #starleeter
    show lov shy1
    lov "Maybe it was… presumptuous of me to assume everything would be sunshine and rainbows after that peptalk…" 
    voice "10-4-64.mp3" #potato
    pro "No, Lauren, it was a big help. You don't have to beat yourself up about it."
    voice "10-4-65.mp3" #starleeter
    show lov shy2
    lov "...Mm… well, he's all better now, right?"
    voice "10-4-66.mp3" #potato
    pro "...Dunno. He still sounded out of it over the phone, but…"
    voice "10-4-67.mp3" #potato
    pro "It's okay. We'll work through this, together."
    voice "10-4-68.mp3" #starleeter
    show lov happy2
    lov "Right!"
    voice "10-4-69.mp3" #starleeter
    lov "...Oh! Next turn, almost there…" 
    scene hospital dark with dissolve
    "We pull to the front of the hospital. Lit windows dot the frontward face of the building in neat rows."
    "I squint, trying to catch a familiar face."
    voice "10-4-70.mp3" #potato
    pro "I think I see him! Just inside! Can you pull over here?"
    "He seems to notice us. He waves, slowly making his way close to the car."
    "Swinging the door open, I bounce out of the passenger seat, heading for him."
    voice "10-4-71.mp3" #potato
    pro "Alex!"
    voice "10-4-72.mp3" #kujira
    show bro grin1 
    bro "Hey, Emily…" 
    "I pull him tight into a hug. His arms slowly raise to wrap around my waist."
    voice "10-4-73.mp3" #potato
    pro "It's so good to see you out of bed! ...Ah, you're okay, right??"
    voice "10-4-74.mp3" #kujira
    bro "I-I dunno, I just hope you didn't crack a rib."
    voice "10-4-75.mp3" #starleeter
    show lov happy1 at Position(xpos = 0.25)
    lov "Hey, his sense of humor's still intact!"
    voice "10-4-76.mp3" #kujira
    show lov happy2
    show bro sad1
    bro "...Uh, what's she doing here?"
    voice "10-4-77.mp3" #potato
    pro "Oh, uh, Lauren's here to pick you up. Mom still has the car, and I couldn't reach her."
    voice "10-4-78.mp3" #kujira
    show bro sad2
    bro "Ah. Figures. She was really out of it when I saw her the other day…" 
    voice "10-4-79.mp3" #potato
    pro "H-here, take the passenger seat, I'll sit in the back."
    voice "10-4-80.mp3" #starleeter
    show lov happy1
    lov "Yeah, Emily kept it warm for you."
    voice "10-4-81.mp3" #kujira
    show bro smile2
    bro "You guys spoil me, y'know…" 
    "Alex seems to be in high enough spirits, though there's definite exhaustion and weariness hanging on his every word."
    "That's so like him. He doesn't like people worrying about him, even if he's still struggling."
    voice "10-4-82.mp3" #potato
    pro "C'mon. Let's get you home."
    scene black with dissolve
    "We hit the open road once more as the close approaches midnight…" 
    scene car with dissolve 
    voice "10-4-83.mp3" #starleeter
    show lov happy1 at Position(xpos = 0.25)
    lov "...So! Alex, how's treatment going?" 
    voice "10-4-84.mp3" #kujira
    show lov happy2
    show bro sad1 at Position(xpos = 0.75)
    bro "Ah, well… the worst of the detox is over, but the doc says I should stay home another week."
    voice "10-4-85.mp3" #starleeter
    show lov happy1
    lov "Well hey, that's something! You look great, by the way!"
    voice "10-4-86.mp3" #kujira
    show lov happy2
    show bro smirk1
    bro "Pfft. You're bullshitting me, right? I'm on the hangover of a lifetime here…"
    voice "10-4-87.mp3" #starleeter
    show bro smirk2
    show lov shy1
    lov "Mmmm… I mean, it's better than the last time I saw you."
    voice "10-4-88.mp3" #kujira
    show bro sad2
    bro "Oh, don't remind me… don't even wanna remember that whole mess." 
    voice "10-4-89.mp3" #potato
    pro "We can probably put on a nice hot bath for you when you're home…"
    voice "10-4-90.mp3" #kujira
    show bro smile2
    bro "Nah, I think I'm good. I just wanna see Maria. I’m ready to face her now."
    voice "10-4-91.mp3" #potato
    pro "Mm…"
    voice "10-4-92.mp3" #starleeter
    show lov happy1
    lov "Ah, yeah! I'm sure she missed you a lot!"
    voice "10-4-93.mp3" #kujira
    show lov happy2
    show bro sad1
    bro "...I wonder…"
    voice "10-4-94.mp3" #starleeter
    show lov confused1
    lov "...Mm? What's the matter…?"
    "Her head turns slightly towards me. She's asking me, it seems."
    voice "10-4-95.mp3" #potato
    pro "I'll tell you later..."
    voice "10-4-96.mp3" #kujira
    show bro smile2
    bro "Yeah, I appreciate you taking me home and all, but… I just need to think about what I'm gonna say to her."
    voice "10-4-97.mp3" #starleeter
    show lov happy2
    lov "Ah… well, I'm sure it'll be okay in the end."
    voice "10-4-98.mp3" #starleeter
    show lov happy1
    lov "She really looks up to you, y'know."
    voice "10-4-99.mp3" #kujira
    show bro grin1
    bro "Heh. That's funny."
    voice "10-4-100.mp3" #starleeter
    show bro smile2
    show lov angry2
    lov "I'm serious! I'm always deadly serious.~"
    voice "10-4-101.mp3" #starleeter
    show lov confused2
    lov "Everyone makes mistakes, Alex. It's not worth beating yourself up over."
    voice "10-4-102.mp3" #kujira
    show bro grin1
    bro "Thanks for the tip."
    # TODO kick
    # play sound kick
    voice "10-4-103.mp3" #kujira
    show lov happy2
    show bro smirk1
    bro "Whoa! I-I mean, I'll treasure your advice forever."
    voice "10-4-104.mp3" #potato
    show bro smirk2
    pro "Better."
    voice "10-4-105.mp3" #kujira
    show bro smirk1
    bro "Ugh, kicking the back of my seat? Low blow, Em."
    voice "10-4-106.mp3" #potato
    show bro smirk2
    pro "Just like we were kids, right?"
    voice "10-4-107.mp3" #starleeter
    show lov shy2
    lov "Please be gentle though, it's an expensive model…" 
    voice "10-4-108.mp3" #kujira
    show bro grin2
    bro "Sometimes it feels like we're still kids…" 
    jump brohome1

label brohome1:
    scene black with dissolve
    "We banter like this through most of the drive home."
    "Alex keeps insisting he's tired, but… I think he's just as excited to be back as the rest of us are."
    "Some things never change with this cantankerous loser…" 
    scene house dark with dissolve
    voice "10-4-109.mp3" #starleeter
    show bro smile2 at Position(xpos = 0.75)
    show lov happy1 at Position(xpos = 0.25)
    lov "Here we are!" 
    voice "10-4-110.mp3" #potato
    show lov happy2
    pro "You sure you don't wanna come in? I could get you a drink."
    voice "10-4-111.mp3" #starleeter
    show lov happy1h
    lov "Girl, it's past midnight! I got stuff to do at home!"
    voice "10-4-112.mp3" #starleeter
    lov "And you got some teary-eyed family reunions to get to, right?"
    voice "10-4-113.mp3" #kujira
    show lov happy2
    show bro grin2
    bro "Heh. I'm not a fan of the sappy stuff. Emily's a big cry baby, though, didn't you know?"
    voice "10-4-114.mp3" #potato
    show bro smile2
    pro "Haha, Alex, what's all that about?"
    voice "10-4-115.mp3" #kujira
    show bro grin2
    bro "Oh yeah, one time she skinned her knee, and the whole block got to hear about it."
    voice "10-4-116.mp3" #starleeter
    show lov happy1h
    lov "If you're trying to embarrass your sister, I'm afraid I'm already familiar with her most unfortunate childhood memories."
    voice "10-4-117.mp3" #potato
    pro "Why do you guys have to gang up on me like this…?"
    "I could hardly believe it. Alex and Lauren seemed to… oddly click together?"
    "I didn't think his wry wit would go well with her… Laurenisms, but…"
    "I didn't hate it!"
    voice "10-4-118.mp3" #potato
    show lov happy2
    show bro smile2
    pro "Alright Alex, it's late, let's get you inside."
    voice "10-4-119.mp3" #kujira
    show bro grin1
    bro "Definitely. Frickin' freezing out here…" 
    hide lov
    "Lauren waved us off from the car as we both staggered towards the front door."
    jump day10s5


label brohome2:
    scene black with dissolve
    "Time passes as I wait for the taxi to make its rounds…"
    "Watching, I grind my teeth, hoping the taxi will come in at any moment."
    "There's a credit card I nervously flip around in my right hand. It's kept for emergencies and… this was an emergency."
    "Maria's probably asleep by now… I don't feel it appropriate to grab her now, after the previous exchange."
    "My eyes widen as headlights illuminate the front of our house."
    "He's here! I scramble forward to the passenger door."
    scene carexterior dark with dissolve
    voice "10-4-120.mp3" #potato
    pro "Alex…!"
    voice "10-4-121.mp3" #kujira
    # Unsure about Alex's mood, he's happy for now
    show bro grin1
    bro "Hey, Emily. Sorry I'm late…" 
    voice "10-4-122.mp3" #potato
    show bro smile2
    pro "I-it's not your fault! How've you been?"
    voice "10-4-123.mp3" #kujira
    show bro grin2
    bro "...Been better. Been a hell of a lot worse, but… can't complain."
    voice "10-4-124.mp3" #kujira
    show bro sad1
    bro "...I'm sorry Em, but I was thinking a lot over this trip, and… I have things I need to tell Maria."
    voice "10-4-125.mp3" #kujira
    show bro smile2
    bro "We'll catch up later, okay?"
    voice "10-4-126.mp3" #potato
    pro "Ah, of course. It's late, you're exhausted… I'm exhausted."
    voice "10-4-127.mp3" #kujira
    show bro grin2
    bro "God, right, you must've been worried sick… I'm sorry, I'm back now."
    voice "10-4-128.mp3" #potato
    pro "...Yeah. Welcome home, brother."
    voice "10-4-129.mp3" #kujira
    show bro smile2
    bro "Good to be back."

    hide bro
    "Alex staggers past me towards the front door."
    "I look back at the cab, to find the impatient look of a middle-aged man staring me down."
    voice "10-4-130.mp3" #potato
    pro "...U-um… right, that."
    "Nearly tripping over myself, I fumbled around with the emergency credit card until the payment is made."
    voice "10-4-131.mp3" #potato
    pro "My, that's a lot of mileage for one cab ride… or was it for both ways? ...Ah..."
    jump day10s5
