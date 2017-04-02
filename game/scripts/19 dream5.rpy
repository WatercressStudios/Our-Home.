label dream5:

    scene dlivingroom with dissolve

    play music bgmdream fadeout 1.0 fadein 0.0

    "I take a sip of the warm tea my brother likes so much."

    show dbro happy
    voice "d5-1-1.mp3" #kujira
    dbro "How is it?"
    show dbro smile
    voice "d5-1-2.mp3" #potato
    pro "It's... strangely leafy. And flowery."
    show dbro happy
    voice "d5-1-3.mp3" #kujira
    dbro "And warm and calming, right?"
    show dbro smile
    voice "d5-1-4.mp3" #potato
    pro "I suppose so."
    show dbro happy
    voice "d5-1-5.mp3" #kujira
    dbro "You should start drinking tea with your family from time to time."
    show dbro smile
    "I smile at Alex."

    voice "d5-1-6.mp3" #potato
    pro "Maybe."

    "Truthfully, tea isn't really my thing, but the rest of my family likes it."
    "Plus, my brother's right... it's calming."
    "I'm sure boiled, leafy water will grow on me eventually if I keep drinking it."
    
    show dbro happy
    voice "d5-1-7.mp3" #kujira
    dbro "So, what are you thinking, sis?"
    show dbro smile
    voice "d5-1-8.mp3" #potato
    pro "Hmm?"
    show dbro happy
    voice "d5-1-9.mp3" #kujira
    dbro "Something is on your mind."
    show dbro smile
    
    "I put the tea down and laugh a little."
    
    voice "d5-1-10.mp3" #potato
    pro "You sure know me, little brother."
    show dbro laugh
    voice "d5-1-11.mp3" #kujira
    dbro "Tell me. What is it?"
    show dbro worried
    "The tea calmed me a little, but there's still this stubborn and strange anxiety lingering in my chest. I don’t understand it. I have no reason to feel this way."
    "Alex must have noticed my confusion and puts on a serious expression."
    
    voice "d5-1-12.mp3" #potato
    pro "Alex, will you ever... go anywhere? Or disappear? Or... get hurt?"
    
    "My brother seems surprised by the question, but he smiles radiantly anyway."
    show dbro frown
    voice "d5-1-13.mp3" #kujira
    dbro "What are you talking about, sis?"
    voice "d5-1-14.mp3" #potato
    pro "Dunno. It's just that... I've been thinking about this."
    voice "d5-1-15.mp3" #kujira
    show dbro worried
    dbro "Well, it's unlikely I'll ever go anywhere. Why? Do you need me here for you, always?"
    
    menu:
        "\"Yes.\"":
            jump brostayyes
        "\"No.\"":
            jump brostayno

###########################################

label brostayyes:

    show dbro happy
    voice "d5-1-16.mp3" #kujira
    dbro "I understand. In that case, I'll always be here for you."
    show dbro smile
    "I smile in relief. Alex takes another sip of his tea, and I do the same. The tea's definitely growing on me."
    voice "d5-1-17.mp3" #potato
    pro "Thank you, Alex."
    
    hide dbro
    
    jump dream5lover

###########################################

label brostayno:

    $ career += 1

    show dbro frown
    voice "d5-1-18.mp3" #kujira
    dbro "No?"
    voice "d5-1-19.mp3" #potato
    pro "No. I mean, it'll be nice if you're always here for me, but you have a life too, and you should live it instead of being here with me all the time."
    show dbro smile
    "My brother nods, smiles, and takes another sip of his tea. I consider taking another sip too, but I stop when Alex says something strange."
    show dbro happy
    voice "d5-1-20.mp3" #kujira
    dbro "The same can be said about you too, sis."
    show dbro smile
    voice "d5-1-21.mp3" #potato
    pro "Hmm?"
    
    jump dream5lover

###########################################

label dream5lover:

    show dlov happy at left
    voice "d5-1-22.mp3" #vivi
    dlov "Oh, hey Emily."
    show dlov smile at left
    voice "d5-1-23.mp3" #potato
    pro "Diane! When did you get here?"

    "Diane smiles timidly and tucks her hair behind her ear."
    "Any anxiety I felt earlier is now gone."
    show dlov happy at left
    voice "d5-1-24.mp3" #vivi
    dlov "Your mom let me in. She's so nice. Oh, hey Alex."
    show dlov smile at left
    show dbro happy
    voice "d5-1-25.mp3" #kujira
    dbro "Hey Diane! Anyway, I'll leave you two alone. Bye!"
    hide dbro
    hide dlov
    show dlov smile
    
    "Alex winks at us and retreats the room while chuckling to himself."
    "I feel myself blushing a little."
    "That cheeky little boy."
    
    show dlov surprise
    voice "d5-1-26.mp3" #vivi
    dlov "So, is Alex going somewhere? I heard you say something like that."
    show dlov smile
    voice "d5-1-27.mp3" #potato
    pro "Oh, he's not. I just wondered what I would do if something happened to him, and then I got a bit worried. It's stupid."
    
    "Diane smiles at me, and I feel like the room is getting a little brighter."
    show dlov happy
    voice "d5-1-28.mp3" #vivi
    dlov "There's no point worrying over something we can't control. It's better to appreciate what we have in the moment, isn't it?"
    show dlov smile
    voice "d5-1-29.mp3" #potato
    pro "I suppose you're right. It's so unfair we don't have control over the things that affects us."
    show dlov surprise
    voice "d5-1-30.mp3" #vivi
    dlov "Why do you say that?"
    show dlov smile
    voice "d5-1-31.mp3" #potato
    pro "It makes me... feel a little {i}trapped{/i}, you know. I wish we could control everything in our lives."
    voice "d5-1-32.mp3" #vivi
    show dlov happy
    dlov "But, if we control everything, then nothing unexpected will happen to us anymore. Is it really living if we can't be surprised?"
    voice "d5-1-33.mp3" #vivi
    dlov "The anticipation of things to come. The discovery of something new. Even the unwanted events in our lives. There is beauty in these things, don't you think?"
    show dlov smile
    "I sit back and think about what Diane said. Something about it is making me feel uncomfortable. Unsettled."
    
    voice "d5-1-34.mp3" #potato
    pro "I don't know. What if... what if I can still be surprised even though I'm in control?"
    show dlov surprise
    voice "d5-1-35.mp3" #vivi
    dlov "How so?"
    show dlov smile
    voice "d5-1-36.mp3" #potato
    pro "What if... say... I don't realize I'm actually in control. But I am, so everything will always turn out the way I want, even though I’m unaware of it."
    
    "My heart starts to thump harder and louder. Why is this conversation making me feel strange?"
    show dlov sad2
    voice "d5-1-37.mp3" #vivi
    dlov "Let your subconscious take control."
    show dlov smile
    voice "d5-1-38.mp3" #potato
    pro "Yeah. I don't know. I guess?"
    voice "d5-1-39.mp3" #vivi
    show dlov happy
    dlov "That's an interesting thought. Don't you think it’s interesting, Emily?"
    voice "d5-1-40.mp3" #potato
    show dlov smile
    pro "Huh?"
    
    hide dlov with dissolve
    
    scene black with dissolve
    
    jump day5s1

