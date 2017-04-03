label day8s2:
    # Bedroom

    scene bedroom night with dissolve
    "The walk didn’t end up doing much good."
    "When I got back I went up to my room, I just hid. I really wasn’t in the mood to talk to anyone."
    "Everything is just a mess."
    "Was this really worth all the effort?"
    "I sit up in my bed when my phone starts buzzing."
    "I check it and it’s Lauren trying to video call me."

    play music bgmlov2 fadeout 1.0 fadein 0.0

    "I sigh. I’m tempted not to answer but I know I should."
    "Lauren would just get worried if I didn’t and that’d just make things worse."
    "I accept the call."
    voice "8-2-1.mp3" #potato
    pro "Hey."
    voice "8-2-2.mp3" #starleeter
    lov "I heard what happened to your brother. Is he okay?"
    voice "8-2-3.mp3" #potato
    pro "He’s alive. I don’t know about okay."
    voice "8-2-4.mp3" #starleeter
    lov "I’m sorry. I wanted to call sooner but everything has just been so crazy at school."
    "She sighs and shakes her head."
    voice "8-2-5.mp3" #starleeter
    lov "Anyway, how are you doing? You okay?"
    voice "8-2-6.mp3" #potato
    pro "I’m fine, I guess."
    voice "8-2-7.mp3" #starleeter
    lov "Really?"
    voice "8-2-8.mp3" #potato
    pro "Fine… considering."
    "I sigh."
    voice "8-2-9.mp3" #potato
    pro "It’s bad, okay? Probably the worst thing that’s happened here, and that’s saying something."
    voice "8-2-10.mp3" #potato
    pro "I just… I guess I’m just numb."
    voice "8-2-11.mp3" #starleeter
    lov "You want to meet me for some coffee or something? Get out of the house and just have some company?"
    "I really don’t deserve a friend like Lauren. Who else would be willing to give up their time just to listen to me whine about how miserable my life is?"
    voice "8-2-12.mp3" #potato
    pro "Can we go right now?"
    voice "8-2-13.mp3" #starleeter
    lov "Uh… Sure, I guess?"
    voice "8-2-14.mp3" #potato
    pro "You know where to meet me, right?"
    voice "8-2-15.mp3" #starleeter
    lov "Same place your dad goes to?"
    "I grimace. Well Dad won’t be there, I guess."
    voice "8-2-16.mp3" #potato
    pro "Yeah, that’s the one."
    voice "8-2-17.mp3" #starleeter
    lov "I’ll see ya there!"
    "She hangs up and I get ready to go."

    scene hallway with dissolve

    "It’s quiet in the hallway again. I think Maria is with Dad, but I don’t really know."
    "She should be okay, though."
    "I walk out the door, not bothering to let Mom know where I’m going. I’ve got my phone, so she can get me if she needs me."
    # transition to coffee shop

    scene cafe sunset with dissolve
    play ambience crowd fadein 2.0

    "It’s pretty busy in the shop, but I spot Lauren near the back."

    show lov happy2 with dissolve

    "She’s managed to claim a table, although it’s a tiny one that’s barely big enough for both of us."
    "I shrug, make my order, and join her."
    voice "8-2-18.mp3" #starleeter

    show lov happy1 with dissolve

    lov "Hey!"
    voice "8-2-19.mp3" #potato
    pro "Hi…"
    voice "8-2-20.mp3" #starleeter
    lov "So how's your brother?"
    "Lauren always gets straight to the point, doesn’t she?"
    voice "8-2-21.mp3" #potato

    show lov confused1 with dissolve

    pro "Well, he's not in critical condition anymore, but… it was a pretty bad overdose."
    voice "8-2-22.mp3" #potato
    pro "The doctors are hopeful it won’t do permanent damage, but there’s no way of knowing with these things."
    voice "8-2-23.mp3" #potato
    pro "If he really got messed up, he could be a whole different person…"
    voice "8-2-24.mp3" #potato
    pro "He's such an…"
    "I want to add ‘idiot’ to the end of my sentence, but choose otherwise."
    "I’m still mad at Alex, but... wasn’t he trying to find a way out, like me?."
    "He just chose a less legal way of doing it."
    voice "8-2-25.mp3" #starleeter

    show lov shy2 with dissolve

    lov "I hope he’ll be okay."
    "I nod."
    "The Barista yells out our names."
    #voice "8-2-26.mp3" #starleeter
    lov "I’ll get it! You keep our seat!"
    "I nod again. I’m comfortable just letting Lauren do all the work right now."
    "Fortunately, I soon have a coffee in front of me."
    "The last thing Lauren needs is more energy, but she’s gulping that thing down like she just escaped a desert."
    voice "8-2-27.mp3" #starleeter
    lov "How is Maria taking it?"
    voice "8-2-28.mp3" #potato
    pro "Probably the best out of all of us."
    voice "8-2-29.mp3" #starleeter
    lov "What about your Dad and Mom?"
    "I pause, shaking my head."
    voice "8-2-30.mp3" #starleeter
    lov "Not well, huh?"
    "I nod."
    voice "8-2-31.mp3" #starleeter
    lov "I’m glad you came out to meet me."
    "She put her empty cup down."
    "...How is it already empty?!"
    voice "8-2-32.mp3" #starleeter
    lov "I was worried you wouldn’t come or answer my calls."
    voice "8-2-33.mp3" #potato
    pro "Why?"
    voice "8-2-34.mp3" #starleeter
    lov "Well I know you like to be alone when things aren’t going well."
    voice "8-2-35.mp3" #potato
    pro "I’m... trying to get over that."
    voice "8-2-36.mp3" #starleeter
    lov "So I’m really happy you’re here."
    "I can’t help but smile a little. Lauren’s cheerfulness can be so infectious."
    voice "8-2-37.mp3" #starleeter
    lov "Is there anything I can do to help?"
    menu:

        "Talk about my problems":
            jump listening

        "Ask Lauren about her day":
            $ love += 1
            jump laurentalk

label listening:
    "Do you mind just listening?"

    show lov happy1 with dissolve

    voice "8-2-38.mp3" #starleeter
    lov "Of course!"
    voice "8-2-39.mp3" #potato

    show lov happy2 with dissolve

    pro "I guess I’ll start with what you just said about... about always wanting to be alone."
    voice "8-2-40.mp3" #potato
    pro "I’m not proud of it."
    voice "8-2-41.mp3" #potato
    pro "I feel like I run away from my problems a lot. When things get tough, I just... hardly ever felt like I have the strength to deal with them."
    voice "8-2-42.mp3" #potato
    pro "And even when I did feel strong enough, sometimes I just didn’t want to deal with them, because I was tired or whatever."
    voice "8-2-43.mp3" #potato
    pro "But the crazy thing is that I thought that was fine! I’d tell myself that there’s no point in doing things if they just frustrate me, so it’s a better use of my time to just ignore them and be happy."
    voice "8-2-44.mp3" #potato
    pro "Like... If the real world was too hard, I could just imagine a better one."
    voice "8-2-45.mp3" #potato
    pro "Mom, Alex, school, life after high school... I was honestly happier just pretending things like that didn’t exist."
    voice "8-2-46.mp3" #potato
    pro "But I don’t think I want to be happy. I mean, I do, I really do want to be happy, but not like that, you know?"
    voice "8-2-47.mp3" #potato
    pro "When I looked at Alex, I saw what I was doing to myself. I don’t mean literally, just that he was just escaping in his own way."
    voice "8-2-48.mp3" #potato
    pro "He’s been going through the same shit as me. Same Mom, same... Well, okay, his siblings are way less moody,"
    voice "8-2-49.mp3" #starleeter
    lov "*cough*"
    voice "8-2-50.mp3" #potato
    pro "Hey!"
    voice "8-2-51.mp3" #starleeter
    lov "Just kidding, just kidding~!"
    voice "8-2-52.mp3" #potato
    pro "But anyways, I saw that he was just running away from his problems, too. I saw what that looks like from the outside. It’s not pretty."
    voice "8-2-53.mp3" #starleeter
    lov "Eh, I think you could pull off that look."
    "Huh?"
    voice "8-2-54.mp3" #starleeter
    lov "Kidding~!"
    voice "8-2-55.mp3" #potato
    pro "M-moving on. With everything that’s happened to Alex, I see that I’ve been doing something wrong."
    voice "8-2-56.mp3" #potato
    pro "I’ve never really been able to help him, and now look what’s happened. I know it’s not all my fault, but I definitely could have done something."
    voice "8-2-57.mp3" #potato
    pro "So I’m going to change."
    voice "8-2-58.mp3" #potato
    pro "I value the things that I’ll lose if I don’t face my problems, so I can’t afford to run away."

    #Transition to indicate the passage of time, have the scene get dark

    "When it was over, I didn’t even remember half the things I said."
    "Lauren just sat there and listened."
    "Sometimes she’d ask a question if she didn’t understand something I said, but for the most part she stayed quiet."
    "Honestly, I was grateful for it."
    voice "8-2-59.mp3" #starleeter
    lov "Wow, Em, I don’t know if I’ve ever heard you say this much in my life!"
    "She’s probably right."
    voice "8-2-60.mp3" #potato
    pro "I should probably head home."
    voice "8-2-61.mp3" #starleeter
    lov "Oh, okay."
    voice "8-2-62.mp3" #potato
    pro "Thanks for listening to me. I really appreciate it."
    voice "8-2-63.mp3" #starleeter
    lov "Of course! I was happy to."
    voice "8-2-64.mp3" #potato
    pro "Just don’t go talking about it to anyone else, alright?"
    voice "8-2-65.mp3" #starleeter
    lov "My lips are sealed."
    voice "8-2-66.mp3" #potato
    pro "Thanks, Lauren."
    voice "8-2-67.mp3" #starleeter
    lov "No problem."
    jump day8s2merge


label laurentalk:

    voice "8-2-68.mp3" #potato
    pro "Actually… I wanted to hear more about what's new with you."
    voice "8-2-69.mp3" #starleeter
    lov "Huh? Why??"
    voice "8-2-70.mp3" #potato
    pro "I mean… I don't really get to listen to you talk much."
    voice "8-2-71.mp3" #potato
    pro "We talk, but not… {i}talk{/i} talk, y'know?"
    voice "8-2-72.mp3" #potato
    pro "So… please? What's up?"
    voice "8-2-73.mp3" #starleeter
    lov "...Aww, Em…"

    show lov happy2 with dissolve

    "She smiles warmly for a moment, before nodding her head."

    show lov happy1 with dissolve

    voice "8-2-74.mp3" #starleeter
    lov "Alright! Ah… gosh, I need to think, um…"
    voice "8-2-75.mp3" #starleeter
    lov "Well… mm, I already talk enough about the show…"
    voice "8-2-76.mp3" #starleeter
    lov "Ah, but this one guy, Mike, was trying way too hard to impress a girl when we were doing our stretches?"
    voice "8-2-77.mp3" #starleeter
    lov "And he must've pulled something…"
    voice "8-2-78.mp3" #starleeter
    lov "It was really funny… I shouldn't've laughed, but… heh!"
    voice "8-2-79.mp3" #starleeter
    lov "...Wonder if he'll be okay…"
    voice "8-2-80.mp3" #potato
    pro "Boys will be boys."
    voice "8-2-81.mp3" #starleeter
    lov "Ha, true!"
    voice "8-2-82.mp3" #starleeter
    lov "...Mm… I wish I got to spend more time with my dad, though…"
    voice "8-2-83.mp3" #starleeter
    lov "It's kind of funny, he's able to make time for me, and I… can't, really."
    voice "8-2-84.mp3" #starleeter
    lov "He's been super supportive… like, I used to go to drama camp, right?"
    voice "8-2-85.mp3" #starleeter
    lov "He'd always get me a rose for every little thing. Even rehearsals…"
    voice "8-2-86.mp3" #starleeter
    lov "It was super embarrassing… but he's kind of mushy like that."
    voice "8-2-87.mp3" #starleeter
    lov "Everyone teases me for it too, haha…"
    voice "8-2-88.mp3" #potato
    pro "Ah, that's silly. I thought seeing your family in the audience was every actor's dream."
    voice "8-2-89.mp3" #starleeter
    lov "It is!"
    voice "8-2-90.mp3" #starleeter
    lov "You're gonna be there too, right?"
    voice "8-2-91.mp3" #potato
    pro "Wouldn't miss it for the world, Lauren."

    voice "8-2-92.mp3" #starleeter
    lov "Huh? Why?"
    voice "8-2-93.mp3" #potato
    pro "Please?"
    voice "8-2-94.mp3" #starleeter
    lov "Well… sure… I guess."
    "Lauren started talking about school today and everything else I might have possibly missed."
    "She then went onto the show, which was still dominating pretty much her entire life outside of school and speaking to me."
    "It reminded me I still had a lot to do for that too. Lauren insisted I shouldn’t worry about it. She’d take care of it."
    "I wasn’t so sure though, so I promised that I would help out when I could."
    "She seemed to really appreciate that."
    "It was dark by the time she finally ran out of things to tell me."
    "Seriously, I knew Lauren could talk but even she took me by surprise tonight."
    "She was a little embarrassed when she realised the time, but I was happy with it."
    "It was nice to hear about someone else’s life rather than always talking about my own."
    "I think Lauren appreciated it too, although I can’t be sure."
    voice "8-2-95.mp3" #starleeter
    lov "We should probably go home now."
    voice "8-2-96.mp3" #potato
    pro "Yeah…"
    voice "8-2-97.mp3" #starleeter
    lov "Thanks for listening to all that."
    voice "8-2-98.mp3" #starleeter
    lov "Sorry I said so much…"
    voice "8-2-99.mp3" #potato
    pro "Don’t be sorry. I wanted you to tell me about your day."
    voice "8-2-100.mp3" #potato
    pro "I guess you just had a really full day."
    "Lauren giggled awkwardly."
    voice "8-2-101.mp3" #starleeter
    lov "I guess so."
    jump day8s2merge

label day8s2merge:
    #Merge

    scene cafeexterior with dissolve

    "We walk outside and say our goodbyes."
    "My walk back doesn’t feel as depressing as I expected."
    "Lauren really helped me out today. I hope I can make it up to her."

    stop music fadeout 2.0
    stop ambience fadeout 1.5

    jump day8s3
