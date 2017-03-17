label day10s2:

    scene hallway with dissolve 

    "Finally made it! Hopefully I didn't miss too much of my classes." 
    "Scrambling to my locker, I sort out the stuff I need for morning classes." 

    play voice "10-3-1.mp3" #other
    hm "HOLD IT!" 
    play voice "10-3-2.mp3" #potato
    pro "Aw, shit…" 

    "A shrill voice hollers from down the hall. Am I gonna get arrested?"

    play voice "10-3-3.mp3" #other
    hm "You there, what are you doing out here? Do you have a hall pass??"
    play voice "10-3-4.mp3" #potato
    pro "Actually, no, I'm running late for class, and I'll be out of here if you just let me-"
    play voice "10-3-5.mp3" #other
    hm "Oh, so you're playing hooky, is it? I'll have to write you up for detention."
    play voice "10-3-6.mp3" #potato
    pro "Detention!? Listen, I've had a rough morning, and if you would just-"
    play voice "10-3-7.mp3" #other
    hm "Sorry not sorry, rules are rules. We have to keep students in line and diligently attending their studies."
    play voice "10-3-8.mp3" #other
    hm "Can't allow delinquent punks like you to get away with whatever they want."
    "This is outrageous. This self-righteous, power-crazed nutcase isn't letting me get a word in!"
    "And I'm getting written up for detention!? What gives!?"

    menu:
        "Get mad":
            #$ career+=1
            jump mad

        "Take the write-up":
            #$ detention = True
            jump writeup

    label writeup:
    "I heave a sigh, extending my hand as he stuffs a yellow slip of paper into it."
    "I don't have time for this, so let's just cut the bullshit."
    play voice "10-3-9.mp3" #other
    hm "And if you don't mind, I'll tag along with you to make sure you get back to your class."
    play voice "10-3-10.mp3" #potato
    pro "Ugh…"
    scene black with dissolve
    jump runninglate

    label mad:
    "Yeah, I'm not taking this shit from him. Not today. Not after the week I've been having."
    play voice "10-3-11.mp3" #potato
    pro "Excuse me? 'Delinquent punk'? Excuse you!"
    play voice "10-3-12.mp3" #potato
    pro "I'm running late because my little sister, bless her heart, tried to cook breakfast for the family!"
    play voice "10-3-13.mp3" #potato
    pro "Y'know why? Because our mother ran out on us and hasn't been seen in <i>three days</i>!"
    play voice "10-3-14.mp3" #potato
    pro "My brother, idiot that he is, overdosed on heroin and nearly died, our entire family's falling apart, and I'm trying my damndest to hold everything together here!"
    play voice "10-3-15.mp3" #potato
    pro "Where the <i>fuck</i> do you come off, calling me a 'delinquent punk'!? After the shit I've been through the last week!?"
    play voice "10-3-16.mp3" #other
    hm "Uh, ma'am, control your noise levels, I-"
    play voice "10-3-17.mp3" #potato
    pro "FUCK YOUR NOISE LEVELS! Get out of my face or I swear to God I'm going to take that sash and strangle you with it!"
    play voice "10-3-18.mp3" #other
    hm "Jesus- alright, alright, j-just get back to class!"

    "Turning rapidly, he unsteadily resumes his rounds around the hallways."
    "I take a deep breath, having a moment of quiet to myself once more."
    play voice "10-3-19.mp3" #potato
    pro "...Jeez… I didn't think I was so angry…"
    play voice "10-3-20.mp3" #potato
    pro "...Felt good, though. Heh."
    scene black with dissolve
    jump runninglate

    label runninglate:
    scene classroom with dissolve

    play voice "10-3-21.mp3" #potato
    pro "HiMissReynoldssorryimlate…!"
    play voice "10-3-22.mp3" #skinimini
    tea "...?" 

    "It occurs to me that this isn't the best way to arrive late to class."
    "...Glancing to the clock, class is almost over."
    "And now Miss Reynolds is looking at me like my head grew a third eye. Great."
    play voice "10-3-23.mp3" #skinimini
    tea "...You may be seated, Emily."
    play voice "10-3-24.mp3" #potato
    pro "...Thanks."

    "I head to my seat, trying to keep as low a profile as I could, which is difficult, considering the explosive entrance I just made." 

    play voice "10-3-25.mp3" #skinimini
    tea "So, mm, when you're writing your essays, I want you to consider important symbolism, and use those to support your literary analysis."
    play voice "10-3-26.mp3" #skinimini
    tea "For example, you can explore themes of escapism by examining Winston's use of his diary, a device that offers him little solace in day to day life."
    play voice "10-3-27.mp3" #skinimini
    tea "You can also compare it to the use of the glass paperweight, an otherwise insignificant object that holds remarkable sentimental value."
    play voice "10-3-28.mp3" #skinimini
    tea "The paperweight was primarily useful in providing an imagined environment of temporal stasis apart from the weight of the world."
    play voice "10-3-29.mp3" #skinimini
    tea "You could even say it had more profound impact than the diary, more akin to unplugging a filled sink in the midst of a flood."
    play voice "10-3-30.mp3" #skinimini
    tea "...oh darn, I just gave the lot of you a thesis, didn't I? Okay, argue what you like, but you can't use that, okay?"

    "I should probably be paying more attention to Miss Reynold's lecture, but I'm still fuming over that snafu with the hallway monitor."
    "That wouldn't have happened if mom hadn't bailed on us. What the fuck is she thinking…" 
    "It's been days, now. My brother's in the hospital, dad's killing himself at a work desk, and she decides to just disappear?"
    "...Maybe she got into trouble. Maybe I should feel a bit more guilty, but… this is her fault."
    "If she didn't push Alex into a corner, he wouldn't have gotten into any seedy business, and we'd still be a family."
    play voice "10-3-31.mp3" #potato
    pro "..."
    "Huffing, I pull out my phone. Time to text Dad."
    "'Hey Dad, it's Emily. Can we meet at the cafe this afternoon? 3:30ish?'"
    "Hiding my phone, I go back to taking notes. Lauren still needs this stuff."

    #play sound schoolbell

    "DOO DO DOO DO!"

    play voice "10-3-32.mp3" #potato
    pro "...Or not."

    "Packing my shit up, I head out the door…" 

    #play sound cellphonechime

    "Wait, hold up a sec. That was a quick response."
    "Lesse… 'Yeah. See you then. Love you.'"
    play voice "10-3-33.mp3" #potato
    pro "...Love you too, Dad."

    "I guess I'll see him soon."

    #if detention = True:
    "...After detention that is. Jackass hall monitor…" 

    jump day10s3

