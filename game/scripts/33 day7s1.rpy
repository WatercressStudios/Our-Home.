label day7s1:

    $ scoldalex = False
 
    #Protag’s Bedroom
    #It’s Saturday, so if any characters normally wear uniforms, they need casual clothes for days 7 and 8.

    play voice "7-1-1.mp3" #kaito
    mom "Alex Westenson! Get your ass over here this instant!"

    "Ugh. Even on Saturday, extra sleep is a rare luxury under this roof."

    "Wait. Alex?"

    "Shit. Can he even handle an argument with Mom right now?"

    "I shoot out of bed, throw on some clothes, and bolt towards Alex’s room."

    #Transition to Alex’s room, showing the whole family, except the dad.

    "I manage to show up just in time."

    #Cue Mom's theme

    "Or in other words, at the worst possible time."

    play voice "7-1-2.mp3" #kaito
    mom "Alex, what the hell is a syringe doing in your room?"

    "Oh God."

    play voice "7-1-3.mp3" #kujira
    bro "W-what? Why the hell were you snooping in here?!"

    play voice "7-1-4.mp3" #kaito
    mom "What else is a mother supposed to do when she cleans the bathroom and finds some powder she’s never seen before right next to the damn toilet?!"

    "Some... Powder?"

    "Oh."

    "Oh God."

    # TODO: Flashback to d6s4 where the protag rushes and spills the powder.

    "Did I...?"

    play voice "7-1-5.mp3" #amree
    sis "U-um, it wasn't drugs! That was my science project! I-I used water from the sink to make it and then some of the ingredients spilled and"

    play voice "7-1-6.mp3" #kaito
    mom "Be quiet, Maria!"

    play voice "7-1-7.mp3" #amree
    sis "Uu..."

    play voice "7-1-8.mp3" #kujira
    bro "Fine, you got me! I did some shit I wasn't supposed to, but I'm clean now! I quit!"

    play voice "7-1-9.mp3" #kaito
    mom "Don't give me that bullshit!"

    play voice "7-1-10.mp3" #kaito
    mom "Why the hell are you doing this?! How can a boy as smart as you grow up to be so stupid?!"

    play voice "7-1-11.mp3" #kaito
    mom "You would have had such a bright and successful future ahead of you! Don't you know you're throwing it all away?"

    play voice "7-1-12.mp3" #kaito
    mom "Don't you know there are people who care about what you do and get hurt when they see see you ruining yourself?"

    play voice "7-1-13.mp3" #kujira
    bro "I know that! I know all of that shit!"

    play voice "7-1-14.mp3" #kaito
    mom "Then why? What would make you even consider this?!"

    play voice "7-1-15.mp3" #kujira
    bro "...You wanna know why? You really wanna know why?!"

    play voice "7-1-16.mp3" #kujira
    bro "It's the only thing I can do to stop myself from suffocating under all of your bullshit!"

    play voice "7-1-17.mp3" #kaito
    mom "Don't make this my fault! It's about time you show some responsibility!"

    play voice "7-1-18.mp3" #kujira
    bro "No, I think it's about time you shut your mouth and let me talk!"

    play voice "7-1-19.mp3" #kujira
    bro "You always complain. You beat me down for every single fucking thing, and not once, not even <i>once</i> have you treated me like an adult."

    "We need to put a stop to this before it gets any worse, but I don’t know what to do. I can’t bring myself to say anything."

    play voice "7-1-20.mp3" #kujira
    bro "Yeah, I’m young, so I'll make mistakes every now and then, but Jesus Christ, would it it kill you to admit that I'm right <i>one fucking time?</i>"

    play voice "7-1-21.mp3" #kujira
    bro "You say you want me to have a successful future, but how am I supposed to believe that if the past and present have all been a living hell?"

    "Maria is fidgeting. She must feel even more powerless than I do."

    play voice "7-1-22.mp3" #kujira
    bro "So yeah, I'm a fucking deadbeat druggie, and if you don't want to believe that I quit, then you’re always right, so I guess that must be the truth!"

    play voice "7-1-23.mp3" #kujira
    bro "But hey, I'm nothing but a problem for all of you to solve, so who the hell cares what I thi-"

    #Music cuts out

    play voice "7-1-24.mp3" #amree
    sis "Stop it!"

    "Maria jumps at Alex and tries to hug him, but he catches her and"

    #Thudding sound effect

    hide sis

    "throws her into the wall!"

    play voice "7-1-25.mp3" #amree
    sis "Aah!"

    "She bounces off the wall and collapses. She’s not moving. I feel my heart stop at that moment."

    play voice "7-1-26.mp3" #kaito
    mom "Maria!"

    "We all run to her at once. Maria’s eyes are closed."

    play voice "7-1-27.mp3" #kaito
    mom "Maria, wake up!"

    play voice "7-1-28.mp3" #amree
    sis "Hnnng..."

    "Maria stirs a little, but her eyes are still closed."

    menu:

        "Alex, what the fuck?!":
            #Family +0
            $ scoldalex = True
            jump d7s1unforgiveable

        "Don’t say anything.":
            #Family +1
            $ family += 1
            jump d7s1unfortunate

    # # #

label d7s1unforgiveable:

    play voice "7-1-29.mp3" #potato
    pro "What the fuck is wrong with you?! She was just trying to help!"

    play voice "7-1-30.mp3" #kujira
    bro "I-I don’t need any help! And there’s nothing you can do to help me anyways! I just... Shut up!"

    jump d7s1merge

    # # #

label d7s1unfortunate:

    "It hurts, but I manage to control myself."

    "Alex is just angry.  What he did was wrong, but me blowing up at him is the last thing that he needs right now."

    jump d7s1merge

    # # #

label d7s1merge:

    play voice "7-1-31.mp3" #kaito
    mom "You little ingrate!"

    play voice "7-1-32.mp3" #kaito
    mom "How fucking DARE you lay a hand on her!"

    "In one stroke, Mom’s arm floats like the end of a whip tossed in the air."

    #Flash the screen black while cuing a smacking sound effect.
    #You’re the programmer, though, so feel free to do something else if you have a better idea.
    #I just want to distract from the fact that the static sprites are contradicting the text.

    "And then the whip’s cracked."

    play voice "7-1-33.mp3" #kujira
    bro "..."

    play voice "7-1-34.mp3" #potato
    pro "Alex, wait!"

    hide bro

    "The next moment, he’s sprinting out the door."

    #gimme that melancholic music
    #it’ll be great
    #Also, can we have sister sprite with bleeding forehead? Only need sad + crying expressions I believe

    "..."

    play voice "7-1-35.mp3" #kaito
    mom "Maria, honey, are you okay?"

    play voice "7-1-36.mp3" #amree
    sis "I’m sorry Mommy... Mom. But... can I talk to Emily please?"

    play voice "7-1-37.mp3" #amree
    sis "Alone?"

    play voice "7-1-38.mp3" #kaito
    mom "..."

    play voice "7-1-39.mp3" #kaito
    mom "That’s... that’s fine, honey."

    play voice "7-1-40.mp3" #kaito
    mom "I’ll leave. Mama will leave you alone."

    hide mom

    play voice "7-1-41.mp3" #amree
    sis "..."

    #There’s a crying sister sprite, right?
    #Of course there is.

    play voice "7-1-42.mp3" #amree
    sis "Emilyyyyyyyyy!"

    play voice "7-1-43.mp3" #amree
    sis "I’m sorry! Alex seemed so mad, and we said we’d be there for him, and I didn’t know how to do that, but then I thought a hug would work, except he hit me and made mom mad and... and..."

    "A hug might not have been such a great idea then, but now..."

    #Bring the sister sprite closer

    play voice "7-1-44.mp3" #potato
    pro "Ssh. It’s alright."

    "Well, no, this is the exact fucking opposite of alright, but that’s not important right now."

    play voice "7-1-45.mp3" #potato
    pro "You didn’t mean to cause any trouble, and I think he knows that."

    play voice "7-1-46.mp3" #potato
    pro "It wasn’t a good idea, but you didn’t know any better and your heart was in the right place. You don’t have anything to be ashamed of."

    play voice "7-1-47.mp3" #amree
    sis "R-really?"

    play voice "7-1-48.mp3" #potato
    pro "Yeah. In fact, maybe you should be proud. Nothing good was going to come of that conversation, and you knew that and did something about it."

    play voice "7-1-49.mp3" #potato
    pro "All I could bring myself to do was stand there and watch, so please don’t blame yourself for this. I think you were brave."

    #Little Sister can stop crying now, I guess.

    play voice "7-1-50.mp3" #amree
    sis "Okay, but only on one condition."

    play voice "7-1-51.mp3" #potato
    pro "Huh?"

    play voice "7-1-52.mp3" #amree
    sis "You... you spilled the, um, drugs, didn’t you? When you tried to get rid of them?"

    play voice "7-1-53.mp3" #potato
    pro "...Yeah. Yeah I did."

    play voice "7-1-54.mp3" #amree
    sis "So for my condition,"

    play voice "7-1-55.mp3" #amree
    sis "Please don’t blame yourself, either, okay?"

    play voice "7-1-56.mp3" #amree
    sis "It was just an accident."

    play voice "7-1-57.mp3" #potato
    pro "Yeah. It’s a deal."

    "I don’t know if I’m lying or not, but it’s important for Maria to hear me say that."

    "With that, I hug her a bit tighter and let her go. Mom returns with bandages and fusses over Maria. I go back to my room."

    jump day7s2