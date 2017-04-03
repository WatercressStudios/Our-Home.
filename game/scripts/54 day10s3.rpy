label day10s3:

    scene cafeexterior with dissolve
    
    "Ahh, the cafe. This tends to be the go to place to meet my father, nowadays."

    "It's homey, comfortable, and a good place of compromise outside of our home. We aren't burdened here."

    scene cafe with dissolve
    
    "Dad puts away his laptop as I walk over, drink in hand. He too has a drink - black coffee, probably for the energy."

    voice "10-3-1.mp3" #potato
    pro "Hey Dad."

    voice "10-3-2.mp3" #lacTheWatcher
    show dad smile2
    dad "Hi sweetie. How's your day been?"

    voice "10-3-3.mp3" #potato
    show dad smile1
    pro "It's been pretty average so far."

    voice "10-3-4.mp3" #lacTheWatcher
    show dad smile2
    dad "Same here."

    voice "10-3-5.mp3" #potato
    show dad smile1
    pro "So..."

    "I cut right through the small talk."

    voice "10-3-6.mp3" #potato
    pro "As you know, stuff hasn't been so great lately."

    show dad neutral2
    "Dad opens his mouth to speak-"

    voice "10-3-7.mp3" #lacTheWatcher
    dad "Yeah, I kn-"

    "-and I interrupt him before he can continue."

    voice "10-3-8.mp3" #potato
    pro "Wait, I'm not done. We can't rely on excuses, and we can't continually blame ourselves. We have to think of solutions, not of symptoms."

    voice "10-3-9.mp3" #lacTheWatcher
    show dad sad1
    dad "That's true."

    "He stays quiet, respectfully awaiting my speech."

    voice "10-3-10.mp3" #potato
    pro "So, moving forward, what are we going to do? What happens if Mom never comes home, and what happens if she eventually... does?"

    "I pause to consider this myself. I truly wish I had the answer myself. It's just… some spectre of a possibility to me."
    "The idea looms over us like a great shadow. And I'm not sure if I have the strength to suffer either way."

    voice "10-3-11.mp3" #lacTheWatcher
    show dad sad2
    dad "Well, if she never comes home, I'll have to work less. You won't always be here, and your brother can't exactly hold the fort when I'm gone."

    voice "10-3-12.mp3" #lacTheWatcher
    dad "If she does come back, then I'll still take off from work more often, adjusting my schedule if possible. I can't help but feel that this is a result of my absence."

    voice "10-3-13.mp3" #potato
    pro "You being gone so often is a part of it of course, but you being home won't fix everything, Dad. Mom is a problem, even with you being more available."

    voice "10-3-14.mp3" #lacTheWatcher
    show dad sad1
    dad "She's… she's something, yes."

    voice "10-3-15.mp3" #potato
    pro "Do you really have nothing to say about it?"

    voice "10-3-16.mp3" #lacTheWatcher
    show dad sad2
    dad "I just… don't know what to do. She is who she is."

    voice "10-3-17.mp3" #potato
    pro "Dad, please, for the sake of the family, you need to stand up to her."

    voice "10-3-18.mp3" #potato
    pro "She's hurting our family, and you are just letting it happen. You can't just let her keep doing what she's been doing."

    voice "10-3-19.mp3" #potato
    pro "She's the reason my little brother - your son - is in the situation he's in. And no one has ever stood up to her."

    voice "10-3-20.mp3" #potato
    pro "You're her husband, right? It's your responsibility to deal with her. You chose her, we didn't."

    "My hands clench silently. I'm trying so hard to stay calm, but… I'm so frustrated."

    "I'm trying so hard to be an adult, and talk things out like an adult."

    "I've always tried so hard to limit the burden I put on others, and that's meant keeping quiet about everything around me. "

    "I can't do this any longer. I'm tired of standing around while my family falls apart. I'm tired of people I love getting hurt."

    "When Lauren went off on my mother way back when, it helped open my eyes, even if I might not have realized it then."

    "I've made the choice to be more proactive, even if it means I have to hurt people. This is so, so hard to do, but…"

    "I've simply got no other choice."

    voice "10-3-21.mp3" #lacTheWatcher
    show dad neutral2
    dad "No, you're right. I've been avoiding everything. I've been avoiding her. I've used my work as a crutch, as an excuse to stay away. I've sacrificed my family for my own selfishness."

    voice "10-3-22.mp3" #lacTheWatcher
    show dad angry2
    dad "I'll confront her. I'll try to help her see things our way. I'll open up a dialogue with her. We'll have a conversation, and we'll try to see things from each perspective. If that doesn't work, then…"

    "Unfortunately, he's right. If we can't make Mom see things our way, and if she refuses to let us see her's, then there's nothing we can do."

    "I don't expect it to go over well, given her track record, but we'll try."

    voice "10-3-23.mp3" #potato
    pro "Yeah."

    "I take a sip from my lukewarm coffee, ignoring the awkward silence."

    voice "10-3-24.mp3" #potato
    pro "Remember, we're here as well. I'll make sure to be a part of this conversation. We'll handle this together."

    "Like a neat little father-daughter bonding session."

    "Kinda."

    #Choice to alleviate dad’s stress by offering to get the siblings to do more at home (FAMILY+1), or keep quiet (FAMILY+0).
    menu:
        "I should elicit the help of my siblings, too.":
            $ family += 1
            jump bloodbonds

        "It's best if I help him on my own.":
            jump soloventures

label bloodbonds:
    voice "10-3-25.mp3" #potato
    pro "I'll talk to the other two. They can help us. Despite their age, they can handle a lot, given the chance."

    voice "10-3-26.mp3" #potato
    pro "Be it directly or indirectly. Hell, keeping the house running would be enough. Alleviate the stress, so we can focus on the more hands on situation in front of us."

    "Dad nods with a defeated look on his face."

    voice "10-3-27.mp3" #lacTheWatcher
    show dad sad1
    dad "I hate to rely on you three, but it would be for the best."

    voice "10-3-28.mp3" #lacTheWatcher
    show dad neutral1
    dad "Thank you, Emily."

    voice "10-3-29.mp3" #potato
    pro "You don't need to thank me, remember? It's just part of my job. I've been absent, just like you, so this burden is, in reality, ours to share."

    "He shakes his head, but I cut him off."

    voice "10-3-30.mp3" #potato
    pro "It is."

    voice "10-3-31.mp3" #lacTheWatcher
    show dad neutral1
    dad "Okay. I trust you."

    "He grabs my hand in his, tears forming in his eyes."

    voice "10-3-32.mp3" #lacTheWatcher
    show dad cry
    dad "I trust you."

    "He releases my hand, shaking away his pain."

    voice "10-3-33.mp3" #lacTheWatcher
    dad "I'm a failure, but I won't let that be the end. I promise."

    jump atconversationsend

label soloventures:
    voice "10-3-34.mp3" #potato
    pro "We're doing this together, okay?"

    "He hesitates, defeated."

    voice "10-3-35.mp3" #lacTheWatcher
    show dad neutral1
    dad "Together."
    jump atconversationsend

label atconversationsend:
    "He tends to his coffee, loosening up his collar, and then continues on."

    voice "10-3-36.mp3" #lacTheWatcher
    show dad neutral1
    dad "At least I've been saving up vacation time. I wanted to take us all on a vacation, but things… got complicated."

    voice "10-3-37.mp3" #lacTheWatcher
    dad "I'll be sure to warn my boss that I might take it unexpectedly."

    voice "10-3-38.mp3" #potato
    pro "Oh? You thinking of using it if... or when Mom comes home?"

    voice "10-3-39.mp3" #lacTheWatcher
    show dad neutral2
    dad "It's the best situation I can use it for. We can't have a vacation without a family."

    voice "10-3-40.mp3" #potato
    pro "Yeah, yeah."

    "We trail off. I had hoped to end this conversation off on a happy note, but that's unfortunately not going to happen."

    voice "10-3-41.mp3" #lacTheWatcher
    show dad neutral1
    dad "It's rough, what I've put you through, but it will be alright, okay?"

    "He touches my hand again, hoping to calm my nerves."

    "I'm, uhh, not exactly sure how I should go about this. I don't know how to feel. Should I be sad, or happy about Mom being gone?"

    "Should I welcome Mom home with open arms?"

    "Should I get my hopes up… is it really all uphill from here?"

    "I don't know."

    "Dad lets go, accepting my silence."

    voice "10-3-42.mp3" #lacTheWatcher
    dad "It's time I go back to work, sweetie. See you soon, okay?"

    voice "10-3-43.mp3" #potato
    pro "See you."

    hide dad
    "I'm left alone with my thoughts."

    "Naturally, they turn to my siblings. I want to visit Alex today as well, but first, I need to make sure Maria doesn’t walk home alone."

    jump day10s4