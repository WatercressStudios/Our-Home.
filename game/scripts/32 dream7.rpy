label dream7:

    scene dream1 with dissolve

    dbro "Welcome back."

    show dbro smile
    "Here he is, my brother. Sitting across from me, as he has many times before. Difference is, however, that I now know that this isn't real. It's all a dream."

    voice "d7-1-1.mp3" #potato
    pro "Thank you… This is, uh, still new to me."
    show dbro happy
    voice "d7-1-2.mp3" #kujira
    dbro "Now that you understand just what this is, it's a completely different beast, isn't it?"
    show dbro smile
    "I fidget awkwardly. It's so weird. He's acting like nothing is different, but it's all incredibly different."

    voice "d7-1-3.mp3" #potato
    pro "Yeah. Very much so. It's so odd. Is this normal?"
    show dbro laugh
    voice "d7-1-4.mp3" #kujira
    dbro "Is your situation normal?"
    show dbro smile
    "Thinking about it, it isn't. How many people can really say that they've lived the life that I have? The broken home, the scraps left behind, the desperate attempt at an escape, it's all unique to me."

    voice "d7-1-5.mp3" #potato
    pro "I guess not."
    show dbro happy
    voice "d7-1-6.mp3" #kujira
    dbro "No, it's more normal than one would think, actually."
    show dbro smile
    voice "d7-1-7.mp3" #potato
    pro "Really?"

    "Bullshit."
    show dbro happy
    voice "d7-1-8.mp3" #kujira
    dbro "Humans are inherently flawed creatures."
    show dbro smile
    voice "d7-1-9.mp3" #potato
    pro "This flawed, though?"
    show dbro happy
    voice "d7-1-10.mp3" #kujira
    dbro "Yes."
    show dbro smile
    "No, I'm alone. Right? If I'm not alone, then this world is even worse than I originally thought."

    voice "d7-1-11.mp3" #potato
    pro "It's hard to imagine, knowing how much pain I've endured…"
    show dbro frown
    voice "d7-1-12.mp3" #kujira
    dbro "The world is a painful place. It's worsened by how terrible we all are at communication."

    "I can't really argue with that."

    voice "d7-1-13.mp3" #potato
    pro "That's true. We're really bad at being good to each other."

    show dbro happy
    voice "d7-1-14.mp3" #kujira
    dbro "No, that's not what I meant."

    show dbro smile
    voice "d7-1-15.mp3" #potato
    pro "Oh?"

    show dbro happy
    voice "d7-1-16.mp3" #kujira
    dbro "We're really bad at expressing what's wrong."
    show dbro smile
    "It doesn't matter, though. Idle chatter about the root of all evil doesn't solve a damn thing."

    voice "d7-1-17.mp3" #potato
    pro "Yeah, but talking about it isn't going to solve the issue."
    show dbro worried
    voice "d7-1-18.mp3" #kujira
    dbro "Which is?"

    voice "d7-1-19.mp3" #potato
    pro "The fact that we don't tell others what's wrong, like you said."
    show dbro happy
    voice "d7-1-20.mp3" #kujira
    dbro "Well…"
    show dbro smile
    voice "d7-1-21.mp3" #potato
    pro "Well?"

    "I'm not sure what he's asking. He's being cryptic, and it's frustrating me. Normally, dreams have the opposite effect, but this time around? It's different."
    show dbro happy
    voice "d7-1-22.mp3" #kujira
    dbro "What's your solution?"
    show dbro smile
    voice "d7-1-23.mp3" #potato
    pro "My solution?"
    show dbro happy
    voice "d7-1-24.mp3" #kujira
    dbro "Yes."
    show dbro smile
    voice "d7-1-25.mp3" #potato
    pro "I guess it'd be to be more open to others. As much as I wish I could, I can't exactly force others to do things the right way."

    voice "d7-1-26.mp3" #potato
    pro "But it just frustrates me to no end. I hate my mother, and I hate everything about my family. I can't even begin to comprehend just what it took to create that… monster."
    show dbro worried
    voice "d7-1-27.mp3" #kujira
    dbro "Wouldn't it do you some good to think about why she behaves the way she does? It serves no purpose to be blindly angry at someone. Think about the {i}why{/i}, not the what."

    voice "d7-1-28.mp3" #potato
    pro "That's it, though. I have no idea what could've happened. I'm lost, and every time I think about it, I just get angrier and angrier."
    show dbro happy
    voice "d7-1-29.mp3" #kujira
    dbro "Here's my last piece of advice, from you to you. Everyone has a reason for why they do what they do. Sometimes, it isn't as sinister, nor is it as hardwired as you think it is."

    voice "d7-1-30.mp3" #kujira
    dbro "Look into the past, look into the present. Everything happens for a reason, just not in a divine sense."

    voice "d7-1-31.mp3" #kujira
    dbro "Try to trust in people more. See the good in them, not just the bad. Do you think you can do that?"
    #decides to trust people more: FAMILY+1, if not: FAMILY+0.
    show dbro smile
    menu:

        "I can't trust anyone, not after what I've been through…":
            jump trust

        "It will be hard, but I can try.":
            $ family += 1
            jump trust

label trust:
    
    hide dbro
    
    "With that, my brother, or more accurately, the shard of me that takes the form of my brother, vanishes."

    "I'm not quite done yet, though. There's still one more person to talk to here."

    "With a simple thought, she appears in front of me."

    show dlov happy
    voice "d7-1-32.mp3" #vivi
    dlov "Hey, Emily. It's good to see you again."
    show dlov smile
    "She gives me her sweet smile, something I've become accustomed to after so many dreams"

    voice "d7-1-33.mp3" #potato
    pro "Yeah, it's good to see you too."
    show dlov happy
    voice "d7-1-34.mp3" #vivi
    dlov "So. Have you thought about my question?"
    show dlov smile
    voice "d7-1-35.mp3" #potato
    pro "I have, but I'm not sure I'm ready to answer it yet. I'm not sure if I can trust myself with the answer, let alone trust anyone else."
    show dlov laugh
    voice "d7-1-36.mp3" #vivi
    dlov "Honey, there are plenty of people that you can trust. You just have to think about it! Sometimes, they are right in front of you."
    show dlov smile
    voice "d7-1-37.mp3" #potato
    pro "You're here, I guess, but isn't that just me trusting myself?"
    show dlov laugh
    voice "d7-1-38.mp3" #vivi
    dlov "I wasn't talking about me, silly."
    show dlov smile
    voice "d7-1-39.mp3" #potato
    pro "Then wh- oh. Lauren…"
    show dlov happy
    voice "d7-1-40.mp3" #vivi
    dlov "You've grown very close to her. I daresay you might even love her."
    show dlov smile
    voice "d7-1-41.mp3" #potato
    pro "I-uhh, I dunno."
    show dlov surprise
    voice "d7-1-42.mp3" #vivi
    dlov "Emily, who do you want to be with?"
    show dlov smile
    voice "d7-1-43.mp3" #potato
    pro "What do you mean?"
    show dlov surprise
    voice "d7-1-44.mp3" #vivi
    dlov "Her in the real world, or me, in here?"

    #Choice: Who do you want to be with?  The me here, or the her in the other world? Love Interest LOVE+1, You LOVE+0.
    show dlov worried
    menu:

        "...I have to trust you more. I'm the only one that I can rely on.":
            jump me

        "Her. She's done so much for me. How could I not?":
            $ love += 1
            jump her

label me:
    show dlov worried
    voice "d7-1-45.mp3" #potato
    pro "There's only one person in this world that I can trust. That's me."
    show dlov sad2
    voice "d7-1-46.mp3" #vivi
    dlov "I see."
    show dlov sad1
    voice "d7-1-47.mp3" #potato
    pro "So, in the end, I have to choose you, right?"

    "It's the only right answer. I'm the only one that truly knows what it's like to be me, and I'm the only one I can be certain of."

    "I know my own motives. I can't be sure about the motives of everyone else, can I?"

    "Diane holds her hands together with a pained expression on her face."
    jump trustfalls

label her:
    voice "d7-1-48.mp3" #potato
    pro "Of course it's her. We've been together for so long, and she's always there for me - without fail."

    voice "d7-1-49.mp3" #potato
    pro "I owe her my life."
    show dlov smile
    "Diane smiles, nodding to my words."
    show dlov happy
    voice "d7-1-50.mp3" #vivi
    dlov "I love it when you say things like that. You really care about her, don't you?"
    show dlov smile
    voice "d7-1-51.mp3" #potato
    pro "Yeah, I do."
    jump trustfalls

label trustfalls:
    "I couldn't have chosen wrong, could I?"

    "I can't think too hard about it. I have to move on. My decisions are final, and I can't spend my life regretting them."

    "We fall quiet, the still air completely silent, unnatural."

    voice "d7-1-52.mp3" #potato
    pro "I am afraid of one thing, however."
    show dlov laugh
    voice "d7-1-53.mp3" #vivi
    dlov "Yes?"
    show dlov worried
    voice "d7-1-54.mp3" #potato
    pro "I'm afraid of losing you. I've become so close to Lauren, and to Maria, I feel like I'm neglecting you. Even if you are just a part of me, a piece of the puzzle that is Emily, I still don't want to lose you."

    voice "d7-1-55.mp3" #potato
    pro "...It's lonely without you."
    show dlov surprise
    voice "d7-1-56.mp3" #vivi
    dlov "Do you think that's a good thing? Do you think this newfound distance is okay, a step in the right direction?"

    menu:

        "I guess it is.":
            $ career += 1
#             $ love += 1
            jump realworld

        "I don't want to lose you.":
            jump dreamworld

label realworld:
    show dlov worried
    voice "d7-1-57.mp3" #potato
    pro "I have to move on sometime, don't I? I don't want to leave you, but if it's you or her…"
    show dlov laugh
    voice "d7-1-58.mp3" #vivi
    dlov "I understand, don't worry."
    show dlov smile
    "Approaching me, I feel the warmth of her hand against my face."

    "Gently, she strokes my hair, my face, my lips… Her smile is happy, and yet sad at the same time."
    show dlov happy
    voice "d7-1-59.mp3" #vivi
    dlov "I'm not the real one, am I?"
    show dlov smile
    "I didn't know I could cry in a dream, but I guess I can. My vision blurs as I stare back at her."

    voice "d7-1-60.mp3" #potato
    pro "I don't think so…"
    jump endofafantasy

label dreamworld:
    show dlov worried
    voice "d7-1-61.mp3" #potato
    pro "I can't bring myself to do it. I can't let you go."
    show dlov laugh
    voice "d7-1-62.mp3" #vivi
    dlov "I understand, don't worry."
    show dlov smile
    "Approaching me, I feel the warmth of her hand against my face."

    "Gently, she strokes my hair, my face, my lips… Her smile is happy, and yet sad at the same time."
    show dlov happy
    voice "d7-1-63.mp3" #vivi
    dlov "I'm not the real one, though, am I?"
    show dlov smile
    "I didn't know I could cry in a dream, but I guess I can. My vision blurs as I stare back at her."

    voice "d7-1-64.mp3" #potato
    pro "I don't know..."
    jump endofafantasy

label endofafantasy:
    "She pats my head, her fingers pushing into my messy hair, her other hand cupping my face. She brings herself in for a long, gentle kiss…"

    scene black with Dissolve(2.0)

    "And then I wake up."

    jump day7s1