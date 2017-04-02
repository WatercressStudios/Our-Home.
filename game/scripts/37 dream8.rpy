label dream8:

    $ homecoming = False

    scene dream2 with dissolve
    play music bgmdream2 fadeout 1.0 fadein 0.0
#    voice "d8-1-0.mp3" #vivi recording
    dlov "What's your answer?"

    "The words linger in the stagnant air. I don't know how she can be so calm at a time like this. How could she expect an answer after today?"

    "What does she want me to say?"

    "Dreams are just that - dreams. Visions of a better time. Something that, under normal circumstances, are unobtainable."

    "However, I have a choice. A choice she's given me.  A choice I've given myself. Her question echoes in my head, bouncing around, forcing its way to the top."

    show dlov worried
    "She wants an answer. I want an answer. Can I force myself to give it, or am I going to cower forever? I have to move. I can't sit still anymore. I have to decide if this world is worth living for… worth living in. Right?"

    "Which do I choose? What should I say?"

    "Diane stands quietly, waiting. She shows no emotion. She's perfectly still, unnaturally so, just like the air around me. A staple of this world lately."

    voice "d8-1-1.mp3" #potato
    pro "I don't know how you can ask that, still."
    show dlov happy
    voice "d8-1-2.mp3" #vivi
    dlov "I don't want to… I have to."
    show dlov smile
    voice "d8-1-3.mp3" #potato
    pro "Now?"
    show dlov happy
    voice "d8-1-4.mp3" #vivi
    dlov "Yes."

    voice "d8-1-5.mp3" #vivi
    dlov "I'm sorry. I wish I didn't have to, but…"

    voice "d8-1-6.mp3" #vivi
    dlov "You're making yourself choose."
    show dlov smile
    voice "d8-1-7.mp3" #potato
    pro "But how? How do I choose?"
    show dlov happy
    voice "d8-1-8.mp3" #vivi
    dlov "Think about everything that's happened up to this point."
    show dlov smile
    voice "d8-1-9.mp3" #potato
    pro "The pain, the hurt…"
    show dlov happy
    voice "d8-1-10.mp3" #vivi
    dlov "And the happiness in between."
    show dlov worried
    voice "d8-1-11.mp3" #potato
    pro "My brother just overdosed. Why would I ever want to return to a world where I'm doomed to live a shitty life?"
    show dlov sad2
    voice "d8-1-12.mp3" #vivi
    dlov "That's up to you to decide, but the choice is solely yours."

    voice "d8-1-13.mp3" #vivi
    dlov "Is life in the real world worth living in, if it causes you so much pain?"
    show dlov sad1
    menu:
        "My brother once told me… that pain is a part of life.":
            jump prehomecoming

        "Some people just aren't destined for a happy life. There's no reason to force it.":
            jump homeless

label prehomecoming:
#    POINTCHECK -> Love Point Check and Career Point Check
#    IF: < 3 for at least one, THEN: jump forcedreamend
#    IF: =/> 3 for both, THEN: jump homecoming

    if love < 4 or career < 4:
        jump forcedreamending
    else:
        jump homecoming

label homecoming:

    $ homecoming = True

    "That's just it, though. Throughout each and every one of these dreams, I've had the opportunity to think through what's always troubling me."

    "I've designed this world for that very specific purpose, even if it took me this long to realize."

    "This is my escape. This is my reprieve."

    "But, what's that saying again?"

    "This too, shall pass."

    "Yeah, that's it."

    "With pain comes happiness. With sorrow comes fulfillment."

    "It's just the way things are, in the real world. Some people aren't designed to work in a world so decisive."

    "Those people have a choice. A very complex one, and a very important one."

    "Do they want to grow? Or do they want to fail? Evolve, or fall?"

    "Do they want to try, or do they want to give up?"

    "Do they want to accept the world as it is, or do they want to run from it?"

    "If you would have asked me these questions a week ago, I'm sure I would have told you that those who aren't designed for this world shouldn't fight it. I would have said that perhaps those people shouldn't force themselves to adapt."

    "Now? I'm different. I'm still broken, I'm still in the same shitty situation that I've always been in, but my eyes have been opened."

    "I've come to a powerful realization."
    show dlov smile
    "{i}I'm not alone.{/i}"

    "I never had to be."

    "This is our home."

    "We are all human. We are all broken. Some more broken than others, yes, but that is not the point in life."

    "We shouldn't look at others and wish we could have what they have."

    "We should look at others and ask ourselves a simple question."

    "Do they have enough?"

    "We are all broken, damaged, fragmented. That's how we, as humans, are."

    "We are still people."

    "I am me, and you are you."

    "And I can accept that."

    voice "d8-1-14.mp3" #potato
    pro "Yes. Despite it all, yes."

    voice "d8-1-15.mp3" #potato
    pro "I can't give up now."

    "Pulling me into a close embrace, Diane whispers into my ear."
    show dlov happy
    voice "d8-1-16.mp3" #vivi
    dlov "You've grown so much, you know that?"
    show dlov smile
    "It's an odd feeling, being complimented. It feels…"

    "It feels good. I feel good. Even if the world around me is falling apart, I know that, in the end, It'll all work out. There will always be a chance at change."

    "Most importantly, I still have a family. I still have a friend. I still have something to hold onto, in the darkest of nights and the brightest of dawns."

    "That's just how it will be, from hereon out."

    "I'm sure of it."

    jump familypointcheck

label familypointcheck:

#    POINTCHECK -> Family Point Check 
#    IF: < 3, THEN: jump funeralend
#    IF: =/> 3, THEN: jump day8s1
    if family < 4:
        jump funeralending
    else:
        jump day8s1
    

label homeless:
    "Why would I want to go back to that place?"

    "It's fucked. I'm fucked. I hate it all."

    "A worthless father, an abusive mother, and a brother who's going to die. That's what I have. That's the hand that I've been dealt."

    "That's not the home that I want to return to. I'd rather be here… or nowhere at all."

    "I've given myself the choice, and I'm choosing the right one. Maybe not the right one for everyone, but it's the right one for me."

    "It's a valid one. I don't care if I'll be called weak. I don't care if people will say I abandoned them."

    "This is for their good just as much as it is for my own. I'm worthless, just like my mother used to tell me."

    "So, why bother? Why remain dead weight to them?"

    "I don't need to be a burden on them any longer. It's torture for everyone involved."

    "Yes, that's the decision I'm going to make."

    voice "d8-1-17.mp3" #potato
    pro "It's not worth it, not at all. The real world is a bad place, and no one is going to force me to stay there. As you said, it's my decision to make."
    show dlov sad2
    voice "d8-1-18.mp3" #vivi
    dlov "Yes, it is."
    hide dlov with Dissolve(1.2)
    "With that, she dissipates."

    "She's gone, for now. I'm left with one last question: What now?"
    
    scene black with Dissolve(2.0)

#    POINTCHECK -> Love Point Check and Career Point Check
#    IF: < 3 IN AT LEAST ONE, THEN:
#    menu:
#        "None of this matters anyways.":
#            jump suicideending
#
#    IF: =/> 3 IN BOTH VALUES, THEN: Where do I go from here?
#    menu:
#        "I go home.":
#            jump familypointcheck
#
#        "This is my home.":
#            jump dreamend
    if love < 4 or career < 4:
        menu:
            "None of this matters anyways.":
                jump suicideending
    else:
        menu:
            "I go home.":
                jump familypointcheck

            "This is my home.":
                jump dreamending
