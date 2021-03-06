﻿label day1s1:

    play sound loudknock
    "{b}BANG BANG BANG!{/b}"
    play sound loudknock
    "{b}BANG BANG BANG!{/b}"
    ##SFX, Large amount of screen shake.  Door banging SFX should begin quietly late into Dream 1 and increase greatly in volume once the scene shifts officially.  Scene should have no BGM early on to contrast with the cheery dream before it.
    ##I’ll be referring to these as a harsh cut – little to no transition time, combined with an SFX and varying degrees of screen shake.  Requires a change in either onscreen sprites or BG.  Used usually with the mother or when a character demands the attention of those around them.
    scene bedroom sunset with dissolve

    "A rattling bang stirs me from my sleep. The ground shakes, and the lamp above me sways from side to side. I try to hide under my blankets before realizing it’s still safe."
    "The tremor of my room stops, if only for a few faint seconds."
    voice "1-1-1.mp3" #kaito
    mom "Emily! Dinner’s ready, it’s time to get up!"
    "She walks away and leaves me to my business."
    "A stack of books lay next to my bed. Some, Alex and I have had since we were kids, which he hasn't bothered to touch since then. Others, I've others I've received from Lauren for my studies."
    "Warm orange beams of sunshine cut through the blinds as the sun begins to dip toward the horizon."

    play sound fabric

    "I stretch and yawn as I wake from my nap. There are still going to be a few long hours ahead of me."
    "…"
    "Worst birthday ever. And we haven’t even started dinner yet."
    scene hallway sunset with dissolve
    scene livingroom sunset with dissolve
    play music bgmdad fadeout 1.0 fadein 0.0
    ##maybe some soothing/calming BGM around here.

    ##SCENE CHANGE
    ##some sort of consistent/repeating dinner sounding/clackering utensils sound.  Show character sprites as they’re mentioned.
    "The five of us sit around the table."

    show mom sad3 at center
    with dissolve
    show dad neutral2 with dissolve:
        align (0.25, 1.0)
    show sis happy1 with dissolve:
        align (0.75, 1.0)

    "Mom sits at the head of the table, opposite of me. Father sits to her right, texting someone, and has a particularly worried look on his face. Alex sits to my right poking at his food with his fork."
    "Maria, my little sister, sits to my right, practically bouncing in her chair."

    voice "1-1-2.mp3" #amree
    hide mom
    with dissolve
    hide dad
    with dissolve
    hide sis
    with dissolve
    hide bro
    with dissolve
    show sis happy2
    sis "Emily! How was your trip with Lauren?"
    show sis happy1
    voice "1-1-3.mp3" #potato
    pro "Oh, yeah – it went well, sis."
    "Maria seems so full of energy, barely able to contain herself. Watching her hyperactive ventures is always very entertaining - I choke on my water trying to keep myself from laughing at her."
    voice "1-1-4.mp3" #amree
    show sis worry1b
    sis "Hey!  What’s so funny?"
    voice "1-1-5.mp3" #potato
    pro "It’s nothing, Maria. Just thinking about something she said earlier."
    show sis worry2
    "…"
    hide sis
    with dissolve
    "It’s a normal day. It’s not as good as it could have been, but we’re all getting along just fine. I really can't complain with how things are going so far."
    "Maybe…"
    "I was wrong to be afraid. It’s just a family dinner, after all."
    "Yeah, I’m just thinking too much about everything. It’s nothing to worry about, nothing at all."
    "I pick up my fork and take a bite of the small steak-kind of thing Mom made. It's actually pretty good. If anything, that’s at least a sign that things are improving."

    voice "1-1-6.mp3" #kujira
    show bro grin1
    with dissolve
    bro "Emily? I’m having a bit of trouble with this biology sheet. Could you help me study for the test next week?"
    voice "1-1-7.mp3" #potato
    show bro grin2
    pro "Jesus Christ, Alex.  I was hoping I’d never have to deal with Mr. Karbunkle again.  Just look up the material on the internet. Some of the sites out there do a better job explaining it than him."
    show bro sad2
    "In all honesty, people's' first impression of him is often that he doesn't even care about school."
    ##phone ringing sfx
    hide bro
    with dissolve
    "The phone rings from behind me."
    voice "1-1-8.mp3" #potato
    pro "Ah, I’ll get—"

    show mom sad3
    with dissolve

    voice "1-1-9.mp3" #kaito
    mom "I’ve got it."

    show mom angry1
    "Mom gets up from the table and picks up the phone."

    show mom angry2
    voice "1-1-10.mp3" #kaito
    mom "Hello?"
#    voice "1-1-11.mp3" #kaito silence
    mom "..."
    show mom happy1
    voice "1-1-12.mp3" #kaito
    mom "Yes, this is Elizabeth."
    show mom
    voice "1-1-13.mp3" #kaito
    show mom angry2
    mom "..."
    voice "1-1-14.mp3" #kaito
    show mom angry1
    mom "…Yes.  I understand."
    "Mom hangs up the phone."
    voice "1-1-15.mp3" #kaito
    show mom angry2
    with dissolve
    mom "Come here, Alex."
    voice "1-1-16.mp3" #kujira
    bro "Ah, can't I finish my food first? I—"

    ##harsh cut, BGM stops
    stop music fadeout 0.3

    voice "1-1-17.mp3" #kaito
    mom "Come here, Alex."
    hide mom
    with dissolve
    "Dinner stops. Whatever we had going here before has died. Plain and simple, like always."
    voice "1-1-18.mp3" #kaito
    mom "I don’t have all day. Get up, and come here or there’s going to be consequences."

    ## Fight starts about here, music should start right after the voice plays?
    play music bgmmomintro noloop
    queue music bgmmomloop loop

    show dad sad2 with dissolve:
        align (0.25, 1.0)
    show sis sad1 with dissolve:
        align (0.75, 1.0)

    "Father stares down at his food without the strength to do anything. Maria looks like she doesn’t want to be in the room anymore."
    "Alex gets up from his seat to meet Mom."
    hide dad
    with dissolve
    hide sis
    with dissolve
    show mom angry2 with dissolve:
        align (0.25, 1.0)
    show bro sad2 with dissolve:
        align (0.75, 1.0)
    voice "1-1-19.mp3" #kaito
    mom "That was your school. They told me you never showed up for your Sunday detention."
    voice "1-1-20.mp3" #kujira
    show bro sad1 with dissolve:
        align (0.75, 1.0)
    bro "…I tripped and twisted my ankle on my way there. I had to come back home to put ice on it."
    voice "1-1-21.mp3" #kaito
    mom "You had an obligation to hold up to!  If you can’t be responsible for these things now, how will you ever be responsible as an adult?"
    voice "1-1-22.mp3" #kujira
    show bro smirk1 with dissolve:
        align (0.75, 1.0)
    bro "I tried to! You were the one who said not to bother you – Emily was already out with Lauren and Dad was busy with work! That makes this your fault doesn’t it!?"
    ##harsh cut
    voice "1-1-23.mp3" #kaito
    show mom angry1 with dissolve:
        align (0.25, 1.0)
    mom "Don't you take that tone with me young man!"
    ##slow transition here to compare the two
    show bro sad2 with dissolve:
        align (0.75, 1.0)
    voice "1-1-24.mp3" #kujira
    bro "…Sorry."
    ##sad or depressed looking expression, not a standoffish one.
    show mom angry2 with dissolve:
        align (0.25, 1.0)
    voice "1-1-25.mp3" #kaito
    mom "You've been spending too much time with those friends of yours, and don't think I don't know there are drugs involved."
    voice "1-1-26.mp3" #kujira
    show bro smirk1 with dissolve:
        align (0.75, 1.0)
    bro "Why is that important right now!?"
    voice "1-1-27.mp3" #kaito
    show mom angry1 with dissolve:
        align (0.25, 1.0)
    mom "Why is that important!? They're a bad influence! When you hang around with them, you might as well be throwing away your future! This behavior of yours is clearly a sign that they've rubbed off on you."
    voice "1-1-28.mp3" #kujira
    bro "My future is mine!   What the fuck do you think you’re doing telling me how to live!?"
    voice "1-1-29.mp3" #kaito
    show mom angry2 with dissolve:
        align (0.25, 1.0)
    mom "Yes, your future is yours, but while you live under my roof you will listen. You will be responsible. You will show some Goddamn respect. But if you don't want to do that, you could always go and live on the streets. "
    voice "1-1-30.mp3" #kujira
    show bro angry2
    bro "For all I know, that would be better than being stuck here with you bitching at me all the time."
    voice "1-1-31.mp3" #kaito
    show mom angry1 with dissolve:
        align (0.25, 1.0)
    mom "I've had enough of this. Go to your room - now!"
    voice "1-1-32.mp3" #kujira
    show bro angry1 with dissolve:
        align (0.75, 1.0)
    bro "Fine.  I’m just as tired of this shit as you are."
    ##doorslam SFX?
    hide bro
    with dissolve
    play sound slamdoor
    "Alex stomps off to his room and slams the door, shaking the light fixture hanging over the table."
    voice "1-1-33.mp3" #kaito
    show mom sad1 with dissolve:
        align (0.25, 1.0)    
    mom "Sometimes I think he'll never learn."
    voice "1-1-34.mp3" #potato
    pro "He’s still a kid, Mom. And nobody's perfect."
    "I feel like I barely have the strength to speak right now. Maria and Dad don’t seem to want to involve themselves in the conversation."
    voice "1-1-35.mp3" #kaito
    hide mom
    with dissolve
    show mom angry1
    mom "Most people don’t fall asleep high or go missing for a day. You can’t expect a person like that to fix themselves on their own."
    voice "1-1-36.mp3" #potato
    pro "So he needs help."
    voice "1-1-37.mp3" #kaito
    mom "What do you do you think all that was about? I was trying to help him! And you know you have to help him too, since your dad’s always off with some work meeting or whatever."
    voice "1-1-38.mp3" #potato
    pro "It’s just…"
    show mom angry2
    voice "1-1-39.mp3" #kaito
    mom "Just what?"

    ##Fake choice. Agree with the mother’s treatment during the fight or say she shouldn’t have gone that hard on him. If disagree, pressure leads to protagonist saying she agrees anyway.  Has no effect on points, used to show lack of agency in protagonist’s life.
    #I think you were too hard on him.

    voice "1-1-40.mp3" #potato
    pro "Well…he had a twisted ankle, right? I’d probably have a hard time walking up the hill if that happened to me."

    voice "1-1-41.mp3" #kaito
    show mom sad1
    mom "It doesn't matter. He needs to start growing up. He's getting older and has responsibilities, but he still acts as if he doesn't."

    voice "1-1-42.mp3" #potato
    pro "But even so, someone should have helped him—"
    voice "1-1-43.mp3" #kaito
    show mom angry1
    mom "That's not how things work in the real world, Emily. When you don’t have someone to help you, you get up and get shit done. That’s all there is to it. Unless there’s something else you’re trying to say?"
    voice "1-1-44.mp3" #potato
    pro "…"
    voice "1-1-45.mp3" #potato
    pro "No. Not really. I guess you were right to be harsh."
    voice "1-1-46.mp3" #kaito
    show mom sad3
    mom "I have to be able to lay down the law sometimes. Otherwise, our family isn’t going to be able to function. I’ve told you since you were a kid, right?"
    voice "1-1-47.mp3" #potato
    pro "…Yeah, right."
    "I take the last bite of my food. I get up from the table and wash my plate in the sink."
    voice "1-1-48.mp3" #potato
    pro "I’m done with my food, so I’m going back to my room. Goodnight."
    voice "1-1-49.mp3" #kaito
    show mom sad2
    mom "Goodnight, Emily. See you in the morning."
    hide mom
    with dissolve

    jump day1s2
