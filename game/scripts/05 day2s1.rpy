label day2s1:

    $ tendollar = False

    #Emily’s room, but... darker (and edgier?!)
    #Knocking

    play voice "2-1-1.mp3" #kujira
    bro "Hey, uh... Emily?"

    #protag is still half asleep

    play voice "2-1-2.mp3" #potato
    pro "Mm... What is it, Diane?"

    play voice "2-1-3.mp3" #kujira
    bro "Who’s Diane?"

    "..."

    "Shit."

    play voice "2-1-4.mp3" #potato
    pro "Nobody."

    "I look at the clock. Five forty-seven."

    "Dammit, that was a {i}really good dream{/i}, too."

    play voice "2-1-5.mp3" #potato
    pro "This had better be good, Alex."

    play voice "2-1-6.mp3" #kujira
    bro "Well, uh..."

    play voice "2-1-7.mp3" #kujira
    bro "Remember that biology test I asked for your help with? When I said it was next week, I actually meant that it’s, uh, today."

    play voice "2-1-8.mp3" #kujira
    bro "If I hadn’t, Mom would have been on my ass about it all night, you know?"

    play voice "2-1-9.mp3" #kujira
    bro "But since she {i}wasn’t{/i} on my ass, I... kind of... didn’t study. At all."

    play voice "2-1-10.mp3" #kujira
    bro "So since you took the class already, I was wondering if you might be willing to, uh, help me?"

    "Are you kidding me?"

    "I thought he was supposed to be smart!"

    "Why does he need help?!"

    "At five forty-seven?!"

    "It’s technically five forty-eight now, and I don’t think I’m going to fall asleep again, but... ugh."

    # # #

    menu:

        "You dug this hole for yourself. Don’t drag me in with you.":
            jump d2s1no

        "Fine, but you owe me.":
            $ family += 1
            $ tendollar = True
            jump d2s1yes

    # # #

label d2s1no:

    "You dug this hole for yourself. Don’t drag me in with you."

    play voice "2-1-11.mp3" #kujira
    bro "Ugh. Screw you."

    "I really don’t know what he expected."

    play voice "2-1-12.mp3" #potato
    pro "Five forty-eight. Sleep time. Don’t care."

    "Now Diane, where were we...?"

    #Time pass transition to Emily’s room with normal lighting.

    "I never fell back asleep. This is a cruel, cruel world we live in."

    "I somberly get ready for another day at school."

    #Transition to kitchen with mom and bro

    "It looks like Alex tried to work on it without me."

    play voice "2-1-13.mp3" #kaito
    mom "Alex, what are you doing?"

    jump d2s1merge

    # # #

label d2s1yes:

    "Fine, but you owe me."

    play voice "2-1-14.mp3" #kujira
    bro "Fine, sure, whatever. Five dollars sound good?"

    play voice "2-1-15.mp3" #potato
    pro "Ten."

    play voice "2-1-16.mp3" #kujira
    bro "For one test?!"

    play voice "2-1-17.mp3" #potato
    pro "We charge extra outside of normal operating hours."

    play voice "2-1-18.mp3" #kujira
    bro "Fine! Just help me, okay?"

    "Well, at least I’m turning a profit off this."

    #Transition to kitchen, with bro

    play voice "2-1-19.mp3" #potato
    pro "Alright, this’d better be quick."

    play voice "2-1-20.mp3" #kujira
    bro "Well..."

    "He hands me the study guide."

    #A paper sound effect might be appropriate here

    "He hasn’t written on it at all, and I don’t remember any of this. I sigh"

    play voice "2-1-21.mp3" #potato
    pro "Do you have notes?"

    play voice "2-1-22.mp3" #kujira
    bro "Nah. I’m smart. I don’t need ‘em."

    "{i}Obviously you do.{/i}"

    play voice "2-1-23.mp3" #potato
    pro "Alright. A textbook, then?"

    play voice "2-1-24.mp3" #kujira
    bro "Yeah. I’ve had trouble navigating this thing, but you’re welcome to try."

    play voice "2-1-25.mp3" #potato
    pro "I’ve spent the past three years of my life wrestling with these. Let me show you how it’s done."

    #Transition to indicate passage of time

    "In that half hour, I learned more about the Golgi apparatus than I ever thought possible."

    play voice "2-1-26.mp3" #kujira
    bro "Alright, I think I understand it all now."

    "Well, if he managed to cram it all that fast, he might be smart after all."

    "I extend my hand."

    play voice "2-1-27.mp3" #kujira
    bro "Eh?"

    play voice "2-1-28.mp3" #potato
    pro "Ten bucks."

    play voice "2-1-29.mp3" #kujira
    bro "Uhhh..."

    play voice "2-1-30.mp3" #kujira
    bro "About that."

    play voice "2-1-31.mp3" #potato
    pro "Are you kidding me?"

    play voice "2-1-32.mp3" #kujira
    bro "I can pay it, I swear! Just... not now."

    "I take it back. He’s a moron, through and through."

    play voice "2-1-33.mp3" #potato
    pro "Why didn’t you tell me that?!"

    play voice "2-1-34.mp3" #kujira
    bro "You wouldn’t have helped me!"

    play voice "2-1-35.mp3" #potato
    pro "Exactly!"

    play voice "2-1-36.mp3" #potato
    pro "You can at least give me the five you offered, right?"

    play voice "2-1-37.mp3" #kujira
    bro "Well, there was a quarter that fell behind my desk the other day..."

    play voice "2-1-38.mp3" #potato
    pro "You mean you offered it without... Fine. Whatever."

    play voice "2-1-39.mp3" #potato
    pro "Just... give me the ten dollars when you have it, okay?"

    play voice "2-1-40.mp3" #potato
    pro "Immediately."

    play voice "2-1-41.mp3" #kujira
    bro "Yeah, sure! You know I’m good for it."

    "Ah."

    "It seems that I’ve finally come to realize the bitter truth."

    "There is absolutely no chance that I am ever getting those ten dollars."

    show mom

    play voice "2-1-42.mp3" #kaito
    mom "What are you two doing up already?"

    jump d2s1merge

    # # #

label d2s1merge:

    play voice "2-1-43.mp3" #kujira
    bro "Well, I have a biology test today, so..."

    play voice "2-1-44.mp3" #kaito
    mom "What?! You said it was later this week!"

    play voice "2-1-45.mp3" #kujira
    bro "Well, actually, I said it was this week, and Monday {i}technically{/i}-"

    play voice "2-1-46.mp3" #kaito
    mom "Westensons don’t blow things off to the last minute! Don’t ever let me catch you doing this again!"

    "If you say that, won’t he just not study at all so he never gets caught doing it late?"

    play voice "2-1-47.mp3" #kaito
    mom "And you!"

    "Crap."

    play voice "2-1-48.mp3" #kaito
    mom "Don’t think I forgot that Alex asked you for help with this yesterday! If you’d helped him then, he wouldn’t be in this mess!"

    play voice "2-1-49.mp3" #potato
    pro "That’s not-"

    play voice "2-1-50.mp3" #kaito
    mom "Show some responsibility, will you?"

    "I have more than enough responsibility taking care of {i}myself{/i}, thank you very much. Of course, there’s no way in hell I’m actually going to say that."

    play voice "2-1-51.mp3" #potato
    pro "...Yes, Mom."

    "With that, she calms down and the rest of the morning proceeds in silence."

    "As soon as we’re finished with our morning rituals, I step out the front door, but Maria’s goes back to her room for some reason."

    jump day2s2