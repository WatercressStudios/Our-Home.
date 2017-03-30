label day6s4:
    
    scene sewing room with dissolve 

    #REVISIT THE SHIT OUT OF THIS LATER FOR TRANSITIONS. I NEED TO KNOW HOW INTERVENTION scene GETS WRITTEN

    "Working in my bedroom has always been a good opportunity to clear my head. I think it's doing me better today than it used to."
    "The repeated motions of the sewing machine has something of a therapeutic quality to it. Calming, relaxing..."
    "After today's intervention, I definitely need something a little quieter, slower paced to wind down."
    "Another busy day in the Westenson household… I guess it's better to stay busy."
    
    #MAKE SURE TO UNCOMMENT ALL LOGIC STUFF YOU FUCK!!
    if goodtalk:
        "I think today went really well. Lauren was a big help in all of this."

        #if little sis helps, set a flag during research and bring it back here
        "And Maria… she's growing up so fast. Surprisingly mature. I'm glad we were all able to talk it out a bit."


    else:
        "The intervention could've gone a bit better on my part, but… it was a good attempt."
        "Alex agreed to cut the habit, so as long as I support him through it, it'll all be okay."

        #if little sis helps, set a flag during research and bring it back here
        "And Maria will help too. Bless her heart…"

    "We didn't have to get mom involved, which is fine by me. She would've probably made things a lot worse anyway."
    "I'll just have to help Alex through this." 
    "And on an even better note, I'm making some really solid progress on this outfit for lauren. Think she's gonna love the polka dot patterns…"
    "Heh. Think I'm smiling. I never smile. I think everything's gonna be okay." 

    #play sound franticdoorknock
    play voice "6-4-1.mp3" #potato
    pro "Huh? What?"
    play voice "6-4-2.mp3" #kujira
    bro "It's me. Need to talk."
    play voice "6-4-3.mp3" #potato
    pro "Uh… w-what's the matter?"
    play voice "6-4-4.mp3" #kujira
    bro "Get the door. Please."

    "He's being really terse. Is it about the intervention we just had...?"
    "Rising from my chair, I get the door. What's he need?"

    #play sound dooropen

    play voice "6-4-5.mp3" #kujira
    bro "Yo. We need to talk."
    play voice "6-4-6.mp3" #potato
    pro "S-sure, what'd you need."

    "He shoots a glance down the hallway, both ways, before looking me dead in the eye."

    play voice "6-4-7.mp3" #kujira
    bro "I'm coming in."
    play voice "6-4-8.mp3" #potato
    pro "W-wait a second, you can't just-"

    "Without asking for any sort of permission, he shoved me back into my room, shutting the door behind him."

    play voice "6-4-9.mp3" #kujira
    bro "I can't do it."
    play voice "6-4-10.mp3" #potato
    pro "W-what do you mean you can't-"
    play voice "6-4-11.mp3" #kujira
    bro "{b}I can't do it, okay!?{/b}"

    "Wincing, he recoils, putting some distance between us. The room's a little cramped, so his back merely presses to the door."
    "Words are failing me right now, seeing him in this desperate state."
    "I have to tell him something, though…"

    menu:
        "You can't give up!":
            jump give

        "You aren't alone.":
            jump alone

        "Why are you doing this!?":
            jump outrage

label give:
    play voice "6-4-12.mp3" #potato
    pro "You can't just give up like this! You're better than this! Smarter than this!"
    play voice "6-4-13.mp3" #kujira
    bro "No. I'm weak and desperate, and I have a… a craving." 
    play voice "6-4-14.mp3" #kujira
    bro "I can't do it. I need you to do something for me."
    jump disposal

label alone:
    play voice "6-4-15.mp3" #potato
    pro "Alex, it's okay. You don't have to do this alone. We talked about this."
    play voice "6-4-16.mp3" #potato
    pro "You have me, and Maria, and Lauren. Please, talk to me."
    play voice "6-4-17.mp3" #kujira
    bro "...Thanks. I came to do just that. I need your help."
    play voice "6-4-18.mp3" #potato
    pro "What is it?"
    jump disposal

label outrage:
    play voice "6-4-19.mp3" #potato
    pro "Why are you doing this, Alex!? We agreed to get over this together!"
    play voice "6-4-20.mp3" #potato
    pro "You can't give up now! What would Maria think of you!? You're her brother!"
    play voice "6-4-21.mp3" #kujira
    bro "Ugh. You sound like mom. It's not like that."
    play voice "6-4-22.mp3" #potato
    pro "I can't help you if you just give up like this!"
    play voice "6-4-23.mp3" #kujira
    bro "I'm {i}not{/i}. We're not debating this. Just listen. I need you to do something for me."
    jump disposal

label disposal:
    "He rummaged in his pockets, fishing for something."
    "His movements… they were shaking. He was trembling."
    "Withdrawal symptoms. He must have it really bad…" 

    play voice "6-4-24.mp3" #potato
    pro "I'm sorry, I… I didn't know."
    play voice "6-4-25.mp3" #kujira
    bro "Not important. I never actually got rid of this shit."

    show drugs
    #show a tin box with various drug components
    "He pulls out that awful box I encountered only a few days ago."
    "Inside are… satchels of white powder, syringes, some weird tool that looks like a razor."
    "The color drains from my face. This is the reality we're facing."
    "It's easy to turn a blind eye to it and pretend it's out of sight, out of mind, but… when this stuff is in front of you, it's scary."
    "I can feel the colour drain from my face, before I swallow my apprehension."
    play voice "6-4-26.mp3" #potato
    pro "Alex… why didn't you get rid of this? You said you dropped the habit."
    play voice "6-4-27.mp3" #kujira
    bro "{i}I just told you why not{/i}, because I couldn't alright!? That's why I need you!"
    "...Yeah. That's right. He couldn't bring it upon himself to do it, so he's asking me to?"
    play voice "6-4-28.mp3" #potato
    pro "...Ugh. I don't really want anything to do with this stuff, y'know."
    play voice "6-4-29.mp3" #kujira
    bro "I know. I wish I didn't have to."
    play voice "6-4-30.mp3" #kujira
    bro "But I can't trust myself to actually act on it. I need you to do it. I've tried and failed, and now I'm back to square one."
    play voice "6-4-31.mp3" #kujira
    bro "I know it's asking a lot, but… can I trust you to get rid of this shit?"
    play voice "6-4-32.mp3" #potato
    pro "...You're not giving me much choice here."
    play voice "6-4-33.mp3" #potato
    pro "Alright. I'll do it. But you owe me, alright?"
    play voice "6-4-34.mp3" #kujira
    bro "You name it, I got it. probably. Usually."
    play voice "6-4-35.mp3" #kujira
    bro "Just… don't let mom find it, okay?"
    play voice "6-4-36.mp3" #potato
    pro "Yeah, sure. I'll get on it."
    play voice "6-4-37.mp3" #kujira
    bro "Thanks. Really, {i}really{/i} appreciate it."
    play voice "6-4-38.mp3" #kujira
    bro "I'm gonna get some water… and then rest. Got some demons to fight."
    play voice "6-4-39.mp3" #potato
    pro "Yeah, sure, no problem. I'll let you go."

    #play sound dooropenandclose
    "Alex lumbered out the door, leaving me alone with his illicit contraband."
    "He has some nerve leaving me with this stuff, but… I could see the logic. He could relapse anytime if he still had access to this stuff."
    "I don't know how I'm supposed to get rid of the tools, though. Maybe I could bring it into the police? Throw it in the dump?"
    "It'd take a trip, and it's getting late to do it… I'll hide it under my bed, and deal with it in the morning."
    "...Oh, before I do…"
    play voice "6-4-40.mp3" #potato
    pro "Agh, be careful, there's a needle in there…"
    "It is {i}really{/i} dangerous to mess with this thing. I'm just… gonna grab the drugs for now."
    "So this is heroin? It's pressed into a little white… pill thing. And they're all in a little ziplock back as well."
    "Reminds me of the chewable pills I had when I was a kid."
    "Agh, stop it. I've seen enough TV shows to know what you're supposed to do with these."
    "So that's what the razor in there is for…"
    play voice "6-4-41.mp3" #potato
    pro "Alright. To the bathroom."

    scene bathroom with dissolve 
    #play sound footsteps

    "I make my way over to the bathroom, just across from me. This shouldn't be too hard."
    "Just gotta flush this shit and forget. Quickly, before someone sees…"
    "Just need to dump and flush…" 

    #play sound cellphonering
    "{b}DOODLE DOODLE DOODLE DOO DOOT DOOT!{/b}"

    #play sound whump

    "Jesus Christ that sound! Nearly jumped out of my fucking skin…" 

    play voice "6-4-42.mp3" #kaito
    mom "EMILY! What's that racket you're making!"
    play voice "6-4-43.mp3" #potato
    pro "N-nothing, mom! Just slipped!"

    "Was that a convincing lie? Hopefully. Who's calling me at a time like this?"
    "...Lauren?"

    #play sound click

    play voice "6-4-44.mp3" #starleeter
    lov "Hey, Em!!!" 
    play voice "6-4-45.mp3" #potato
    pro "Heyyyyy, Lauren…"
    play voice "6-4-46.mp3" #starleeter
    lov "Today was pretty exciting right? Think we made a lot of progress! I'm really proud of you guys."
    play voice "6-4-47.mp3" #potato
    pro "Hahaha, thanks! Um, why are you calling, it's really late…"
    play voice "6-4-48.mp3" #starleeter
    lov "OH! Yeah, I wanted to ask, are you free tonight?"
    play voice "6-4-49.mp3" #potato
    pro "...Free? Like, right now? It's, uh, almost ten."
    play voice "6-4-50.mp3" #starleeter
    lov "Yeah, exactly! You wanna meet me in the park in like, ah, 10 minutes? You know, Amethyst Park?"
    play voice "6-4-51.mp3" #potato
    pro "Huh? What for?"
    play voice "6-4-52.mp3" #starleeter
    lov "The night sky! It's really clear, and full of stars! I sent you a picture!"
    play voice "6-4-53.mp3" #potato
    pro "You did… I didn't get any picture-"
    #play sound cellphone chime
    play voice "6-4-54.mp3" #potato
    pro "...Oh, there it is."

    #show cg starry sky

    play voice "6-4-55.mp3" #potato
    pro "Wow, you weren't kidding, it's really nice out!"
    play voice "6-4-56.mp3" #starleeter
    lov "Yeah, right? Anyway, I'm out here right now, so come and join me!"
    play voice "6-4-57.mp3" #potato
    pro "Yeah, definitely! See you then!"

    "I hang up the phone, realizing I have an empty, overturned ziplock bag. Huh."
    "I look in the toilet bowl. Guess the deed's done?"
    "...Wait, I might've spilled some. Lemme look around…"
    "I don't see any on the floor. Guess they all made it into the toilet. Time to flush our troubles away."
    "I pull the lever, watching the pellets swirl and vanish into the plumbing."

    play voice "6-4-58.mp3" #potato
    pro "Good riddance."

    "Alright, let's get ready to see Lauren. I have a lot to say to her tonight, and I really don't want to keep her waiting!"

    jump day6s5

