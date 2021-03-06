label day6s3:
 
    $ goodtalk = False
 
    scene brodoor
    play music bgmbrointro noloop fadeout 1.0
    queue music bgmbroloop loop
    show lov angry with dissolve:
        align (0.75, 1.00)
    show sis worry with dissolve:
        align (0.25, 1.00)
    with dissolve
     
    "Every inch of my being crawled with apprehension."
     
    "We said we would talk to Alex, but now that his door is staring us in the face, the reality of it all is pushing down on me."
     
    show lov happy2 angry with dissolve:
        align (0.75, 1.00)
    with dissolve  
    voice "6-3-1.mp3" #starleeter
    lov "C’mon, Em. All we’re going to do is talk to him. It’ll be fine."
     
    show sis worry2 with dissolve:
        align (0.25, 1.00)
    with dissolve
    voice "6-3-2.mp3" #amree
    sis "We just want the best for Alex, so... everything will turn out okay."
     
    "I guess I couldn’t back down even if I tried."
     
    voice "6-3-3.mp3" #potato
    pro "You’re right. I’m ready."
     
    show sis worry with dissolve:
        align (0.25, 1.00)
    with dissolve
    "Slowly,"
     
    #Knocking Sound#####################################################################3
    "I knocked on the door."
     
    show sis worry2 with dissolve:
        align (0.25, 1.00)
    with dissolve
    voice "6-3-4.mp3" #potato
    pro "Hey, Alex?"
     
    voice "6-3-5.mp3" #kujira
    bro "Yeah?"
     
    voice "6-3-6.mp3" #potato
    pro "Maria, Lauren, and I want to talk to you. Is that alright?"
    
    show sis worry with dissolve:
        align (0.25, 1.00)
    show lov angryh angry with dissolve:
        align (0.75, 1.00)
    with dissolve
    "..."
     
    voice "6-3-7.mp3" #kujira
    bro "Fine. You can come in."
     
    #Creaking sound effect############################333333333333##################3
     
    scene broroom
    show lov happy2h with dissolve:
        align (0.85, 1.00)
    show sis worry with dissolve:
        align (0.15, 1.00)
    show bro angry at center
    with dissolve
     
    "As filthy as ever, but that’s not what we’re here for right now."
     
    show sis worry2 with dissolve:
        align (0.15, 1.00)
    "..."
    
    show bro angry2 at center with dissolve
    voice "6-3-8.mp3" #kujira
    bro "So? What do you want?"
     
    show lov angry2h angry with dissolve:
        align (0.85, 1.00)
    "Lauren elbowed me in the rib. Guess I’m not getting out of this one."
     
    show lov happy2h angry with dissolve:
        align (0.85, 1.00)
    voice "6-3-9.mp3" #potato
    pro "Well, to get straight to the point... we’re, uh, here about your drug habit."
    
    show bro smirk at center with dissolve
    voice "6-3-10.mp3" #kujira
    bro "Tch. Figures..."
    
    show sis worry with dissolve:
        align (0.15, 1.00)
    voice "6-3-11.mp3" #amree
    sis "W-we just want to help."
    
    show bro angry at center
    voice "6-3-12.mp3" #kujira
    bro "Yeah? So does Mom, and she hasn’t managed jack shit."
     
    voice "6-3-13.mp3" #potato
    pro "This isn’t about her."
     
    show bro angry2 at center
    show sis worry2 with dissolve:
        align (0.15, 1.00)
    show lov angry with dissolve:
        align (0.85, 1.00)
    with dissolve
    voice "6-3-14.mp3" #kujira
    bro "Like hell it isn’t. That shit is the only way I can stay sane with her always on my back."
     
    voice "6-3-15.mp3" #potato
    pro "Mom’s not exactly perfect, but is this really your only answer?"
     
    show bro smirk at center with dissolve
    voice "6-3-16.mp3" #kujira
    bro "Should I just lock myself in my room all day instead?"
     
    "Dammit Alex, don’t make this about me again."
     
    show lov angry2 with dissolve:
        align (0.85, 1.00)
    voice "6-3-17.mp3" #starleeter
    lov "I can’t really talk about your family situation, but do you really think all the harm you’re doing to yourself is worth it?"
     
    show sis worry with dissolve:
        align (0.15, 1.00)
    voice "6-3-18.mp3" #amree
    sis "A-and it’s not just you. We’re worried about you, so..."
     
    show bro angry at center with dissolve 
    voice "6-3-19.mp3" #kujira
    bro "None of you have any idea what it is you’re talking about."
     
    show lov confused with dissolve:
        align (0.85, 1.00)
    voice "6-3-20.mp3" #starleeter
    lov "Maybe we don’t, but can’t we talk about it? This isn’t something we can ignore."
     
    voice "6-3-21.mp3" #potato
    pro "Please. Maria and I have dealt with Mom, too. We can help!"
     
    show bro angry2 at center with dissolve
    voice "6-3-22.mp3" #kujira
    bro "How? She’s a bitch, through and through. You know that as well as I do. Talking about it isn’t going to do anything."
     
    voice "6-3-23.mp3" #kujira
    bro "You’re just here to wave your superiority around and set your deadbeat brother onto the path of righteousness, right?"
     
    show bro sad at center with dissolve 
    voice "6-3-24.mp3" #kujira
    bro "Just shut up and leave if you’re only going to tell me shit I already know."
     
    "Looks like this intervention is getting off on the wrong foot."
     
    "There’s no direction here. If we’re going to do anything for Alex, we need to give this conversation some kind of focus."
     
    voice "6-3-25.mp3" #potato
    pro "We can’t do that yet, Alex. There’s still one thing you need to understand."
    
    show bro angry at center with dissolve
    voice "6-3-26.mp3" #kujira
    bro "Really? Try me. I’m not nearly as stupid as you think I am."
     
    "I should really try to choose my words carefully, here."
     
     
    menu:
     
        "Drugs are bad for you.":
            jump d6s3elementaryschool
     
        "This affects more than just you.":
            jump d6s3ouch
     
        "You don’t need drugs to make it through this.":
            $ goodtalk = True
            $ family += 1
            $ love += 1
            $ career += 1
            jump d6s3sugary
     
     
label d6s3elementaryschool:
     
    show bro angry3 at center with dissolve 
    voice "6-3-27.mp3" #kujira
    bro "Are you fucking kidding me?"
     
    voice "6-3-28.mp3" #kujira
    bro "You get this whole mob together, barge in here, and {i}that’s{/i} what you want me to know? That {i}drugs are bad?{/i}"
     
    voice "6-3-29.mp3" #kujira
    bro "They teach you that in elementary school for God’s sake! Do you think I’m a complete fucking moron?!"
     
    show bro sad at center with dissolve
    jump d6s3salty
     
     
label d6s3ouch:
     
    show bro sad at center with dissolve
    voice "6-3-30.mp3" #kujira
    bro "Do you seriously think I don’t know that?"
     
    voice "6-3-31.mp3" #kujira
    bro "I’d have to be an idiot to think I was only hurting myself."
     
    voice "6-3-32.mp3" #kujira
    bro "Hell, maybe I am an idiot, but not the one you’re making me out to be."
     
    jump d6s3salty
     
label d6s3salty:
     
    show bro sad2 at center with dissolve 
    voice "6-3-33.mp3" #kujira
    bro "I’m not this way because I want to be! It’s just... it’s just the only way I’ve been able to keep myself sane, okay?"
     
    show bro smirk at center with dissolve 
    voice "6-3-34.mp3" #kujira
    bro "Saying crap that I already know... that already makes me feel like shit... how is that supposed to do anything but make me feel worse?"
     
    voice "6-3-35.mp3" #potato
    pro "I-I’m sorry Alex. I didn’t think-"
     
    voice "6-3-36.mp3" #kujira
    bro "No, you didn’t."
    
    show bro sad at center with dissolve
    voice "6-3-37.mp3" #kujira
    bro "But since you’re apparently so worried, maybe you’ll be glad to know that I’m already quitting."
     
    voice "6-3-38.mp3" #potato
    pro "Really?!"
    
    show lov angry2 with dissolve:
        align (0.85, 1.00)
    voice "6-3-39.mp3" #starleeter
    lov "Why didn’t you just say that in the first place?!"
     
    voice "6-3-40.mp3" #kujira
    bro "Idunno. You just kinda came at me in a big group like that, and I haven’t really committed to it yet, anyways."
     
    voice "6-3-41.mp3" #kujira
    bro "And I felt like I deserved to get yelled at."
     
    jump d6s3merge2
     
     
label d6s3sugary:
    
    show bro sad at center with dissolve
    voice "6-3-42.mp3" #kujira
    bro "Do you really mean it, or are you just saying that?"
     
    voice "6-3-43.mp3" #potato
    pro "I mean it."
     
    voice "6-3-44.mp3" #potato
    pro "I know things can get out of hand, and sometimes it feels like the world can’t offer enough to make it worth it."
    
    show sis happy with dissolve:
        align (0.15, 1.00)
    show lov happy2 with dissolve:
        align (0.85, 1.00)
    with dissolve
    voice "6-3-45.mp3" #potato
    pro "But I think maybe there are things worth searching for that you won’t find if you hide behind the easy answers."
     
    voice "6-3-46.mp3" #potato
    pro "And to be honest, I don’t know where they are. But we have to look, because... because if we don’t, then what’s even the point?"
     
    voice "6-3-47.mp3" #potato
    pro "So please, Alex. Please start looking. You deserve better than this."
     
    voice "6-3-48.mp3" #kujira
    bro "I deserve it, huh?"
     
    show bro smirk at center with dissolve 
    voice "6-3-49.mp3" #kujira
    bro "That’s a little vague, but I think I see what you mean."
     
    show bro sad2 at center with dissolve 
    voice "6-3-50.mp3" #kujira
    bro "To be honest, I’ve already tried to start quitting. I felt like I should have told you earlier, but I sort of wanted that lecture so I could feel bad for myself."
    
    show bro sad at center with dissolve
    voice "6-3-51.mp3" #kujira
    bro "But thinking about it, I should shoot for something better than self-pity."
     
    jump d6s3merge2
     

label d6s3merge2:
    
    show sis happy2 with dissolve:
        align (0.15, 1.00)
    voice "6-3-52.mp3" #amree
    sis "S-so it’s over? Everything is okay now?"
     
    voice "6-3-53.mp3" #kujira
    bro "Well, I hope so."
    
    show bro angry at center with dissolve
    voice "6-3-54.mp3" #kujira
    bro "But shit like this doesn’t just go away when you tell it to."
     
    voice "6-3-55.mp3" #kujira
    bro "I don’t really know if I can handle it. It’s hard enough already, and it might only take one outburst from Mom for me to crack."
    
    show lov happy2h with dissolve:
        align (0.85, 1.00)
    voice "6-3-56.mp3" #starleeter
    lov "That’s no problem! You’ve already finished the hardest step, and you’ve got two adorable sisters who’ll love to support you!"
     
    voice "6-3-57.mp3" #amree
    sis "I-if you ever want someone to talk to, I’ll listen!"
     
    "This definitely isn’t over, but it looks like we finally have a spot of hope."
     
    "...Hey, wait, what’s that about {i}two{/i} adorable sisters?"

# NOTE: removed following lines due to clash
#     voice "6-3-58.mp3" #kujira
#     bro "Actually, there is something you could help me with."
#      
#     voice "6-3-59.mp3" #kujira
#     bro "I still have some, uh, materials left over, but..."
# 
#     bro" I don’t think I can trust myself to throw them away."
#      
#     voice "6-3-60.mp3" #kujira
#     bro "If it’s not too much trouble, Emily, could you...?"
#      
#     voice "6-3-61.mp3" #potato
#     pro "Consider it done."
     
    voice "6-3-62.mp3" #starleeter
    lov "Woohoo! I’m sure everything’ll turn out okay for you guys."

    "After we settled down and exchanged our goodbyes, everyone went their separate ways."
    stop music fadeout 1.0
    scene black with dissolve
    
    jump day6s4

    