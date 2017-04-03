label day10s2:

    $ detention = False
    
    scene schoolhallway with dissolve 

    "Finally made it! Hopefully I didn't miss too much of my classes." 
    "Scrambling to my locker, I sort out the stuff I need for morning classes." 

    voice "10-2-1.mp3" #other
    hm "HOLD IT!" 
    voice "10-2-2.mp3" #potato
    pro "Aw, shit…" 

    "A shrill voice hollers from down the hall. Am I gonna get arrested?"

    voice "10-2-3.mp3" #other
    hm "You there, what are you doing out here? Do you have a hall pass??"
    voice "10-2-4.mp3" #potato
    pro "Actually, no, I'm running late for class, and I'll be out of here if you just let me-"
    voice "10-2-5.mp3" #other
    hm "Oh, so you're playing hooky, is it? I'll have to write you up for detention."
    voice "10-2-6.mp3" #potato
    pro "Detention!? Listen, I've had a rough morning, and if you would just-"
    voice "10-2-7.mp3" #other
    hm "Sorry not sorry, rules are rules. We have to keep students in line and diligently attending their studies."
    voice "10-2-8.mp3" #other
    hm "Can't allow delinquent punks like you to get away with whatever they want."
    "This is outrageous. This self-righteous, power-crazed nutcase isn't letting me get a word in!"
    "And I'm getting written up for detention!? What gives!?"

    menu:
        "Get mad":
            $ career += 1
            jump mad

        "Take the write-up":
            $ detention = True
            jump writeup

label writeup:
    "I heave a sigh, extending my hand as he stuffs a yellow slip of paper into it."
    "I don't have time for this, so let's just cut the bullshit."
    voice "10-2-9.mp3" #other
    hm "And if you don't mind, I'll tag along with you to make sure you get back to your class."
    voice "10-2-10.mp3" #potato
    pro "Ugh…"
    scene black with dissolve
    jump runninglate

label mad:
    "Yeah, I'm not taking this shit from him. Not today. Not after the week I've been having."
    voice "10-2-11.mp3" #potato
    pro "Excuse me? 'Delinquent punk'? Excuse you!"
    voice "10-2-12.mp3" #potato
    pro "I'm running late because my little sister, bless her heart, tried to cook breakfast for the family!"
    voice "10-2-13.mp3" #potato
    pro "Y'know why? Because our mother ran out on us and hasn't been seen in {i}three days!{/i}"
    voice "10-2-14.mp3" #potato
    pro "My brother, idiot that he is, overdosed on heroin and nearly died, our entire family's falling apart, and I'm trying my damndest to hold everything together here!"
    voice "10-2-15.mp3" #potato
    pro "Where the {i}fuck{/i} do you come off, calling me a 'delinquent punk'!? After the shit I've been through the last week!?"
    voice "10-2-16.mp3" #other
    hm "Uh, ma'am, control your noise levels, I-"
    voice "10-2-17.mp3" #potato
    pro "FUCK YOUR NOISE LEVELS! Get out of my face or I swear to God I'm going to take that sash and strangle you with it!"
    voice "10-2-18.mp3" #other
    hm "Jesus- alright, alright, j-just get back to class!"

    "Turning rapidly, he unsteadily resumes his rounds around the hallways."
    "I take a deep breath, having a moment of quiet to myself once more."
    voice "10-2-19.mp3" #potato
    pro "...Jeez… I didn't think I was so angry…"
    voice "10-2-20.mp3" #potato
    pro "...Felt good, though. Heh."
    scene black with dissolve
    jump runninglate

label runninglate:
    scene classroom with dissolve

    voice "10-2-21.mp3" #potato
    pro "HiMissReynoldssorryimlate…!"
    #voice "10-2-22.mp3" #skinimini silence
    tea "...?" 

    "It occurs to me that this isn't the best way to arrive late to class."
    "...Glancing to the clock, class is almost over."
    "And now Miss Reynolds is looking at me like my head grew a third eye. Great."
    voice "10-2-23.mp3" #skinimini
    tea "...You may be seated, Emily."
    voice "10-2-24.mp3" #potato
    pro "...Thanks."

    "I head to my seat, trying to keep as low a profile as I could, which is difficult, considering the explosive entrance I just made." 

    voice "10-2-25.mp3" #skinimini
    tea "So, um, when you're writing your essays, I want you to consider important symbolism, and use those to support your literary analysis."
    voice "10-2-26.mp3" #skinimini
    tea "For example, you can explore themes of escapism by examining Winston's use of his diary, a device that offers him solace in day to day life."
    voice "10-2-27.mp3" #skinimini
    tea "You can also compare it to the use of the glass paperweight, an otherwise insignificant object that holds remarkable sentimental value."
    voice "10-2-28.mp3" #skinimini
    tea "The paperweight was primarily useful in providing an imagined environment of temporal stasis apart from the weight of the world."
    voice "10-2-29.mp3" #skinimini
    tea "You could even say it had more profound impact than the diary, more akin to unplugging a filled sink in the midst of a flood."
    voice "10-2-30.mp3" #skinimini
    tea "...oh darn, I just gave the lot of you a thesis, didn't I? Okay, argue what you like, but you can't use that, okay?"

    "I should probably be paying more attention to Miss Reynolds' lecture, but I'm still fuming over that snafu with the hallway monitor."
    "That wouldn't have happened if Mom hadn't bailed on us. What the fuck is she thinking…" 
    "It's been days, now. My brother's in the hospital, Dad's killing himself at a work desk, and she decides to just disappear?"
    "...Maybe she got into trouble. Maybe I should feel a bit more guilty, but… this is her fault."
    "If she didn't push Alex into a corner, he wouldn't have gotten into any seedy business, and we'd still be a family."
    voice "10-2-31.mp3" #potato
    pro "..."
    "Huffing, I pull out my phone. Time to text Dad."
    "'Hey Dad, it's Emily. Can we meet at the cafe this afternoon? 3:30ish?'"
    "Hiding my phone, I go back to taking notes. Lauren still needs this stuff."

    #play sound schoolbell

    "*DOO DO DOO DO!*"

    voice "10-2-32.mp3" #potato
    pro "...Or not."

    "Packing my shit up, I head out the door…" 
    scene schoolhallway with dissolve

    #play sound cellphonechime

    "Wait, hold up a sec. That was a quick response."
    "Lesse… 'Yeah. See you then. Love you.'"
    voice "10-2-33.mp3" #potato
    pro "...Love you too, Dad."

    "I guess I'll see him soon."

    if detention:
        "...After detention that is. Jackass hall monitor…" 

    scene black with dissolve
    
    jump day10s3

