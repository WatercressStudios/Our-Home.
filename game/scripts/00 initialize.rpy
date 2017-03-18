###############################
# Dream Character Declaration #
###############################
define dn = Character(None, what_color="#FFFFFF", kind=nvl, what_size=32)
define dbro = Character('Brother', color="#800000")
define dmom = Character('Mother', color="#800000")
define ddad = Character('Father', color="#800000")
define dlov = Character('Diane', color="#800000")


#########################
# Character Declaration #
#########################
define n = Character(None, what_color="#FFFFFF", kind=nvl, what_size=32)
define pro = Character('Emily', color="#800000")
define lov = Character('Lauren', color="#800000")
define sis = Character('Maria', color="#800000")
define bro = Character('Alex', color="#800000")
define mom = Character('Elizabeth', color="#800000")
define dad = Character('Jonathan', color="#800000")
define tea = Character('Miss Reynolds', color="#800000")
define doc = Character('Dr. Harriet', color="#800000") #Make doctor and nurse the same color
define nur = Character('Nurse', color="#800000") #Make doctor and nurse the same color
define all = Character('All', color="#800000")
define cho = Character('Choreographer', color="#800000")
define hm = Character('Hall Monitor', color="#800000")


############################
# Dream Sprite Declaration #
############################
image diane_angry = "sprites/diane/Angry1.png"
image diane_angry_speaking = "sprites/diane/Angry Speaking.png"
image diane_determined_mischievous = "sprites/diane/Determined Mischievous.png"
image diane_frown = "sprites/diane/Frown.png"
image diane_happy_speaking = "sprites/diane/Happy- Speaking.png"
image diane_smile = "sprites/diane/Smile.png"
image diane_speaking = "sprites/diane/Speaking.png"
image diane_worried = "sprites/diane/Worried 1.png"
image diane_worried_smile_speaking = "sprites/diane/Worried Smile- Speaking.png"
image diane_worried_smile = "sprites/diane/Worried Smile.png"
image diane_worried_speaking = "sprites/diane/Worried- Speaking.png"
image brother_angry = "sprites/brother/Angry.png"
image brother_frown = "sprites/brother/Frown.png"
image brother_happy_speaking = "sprites/brother/Happy Speaking.png"
image brother_neutral_smile = "sprites/brother/Neutral Smile.png"
image brother_worried_speaking = "sprites/brother/Worried Speaking.png"
image brother_worried = "sprites/brother/Worried.png"
image father_happy_speaking = "sprites/father/Happy Speaking.png"
image father_slight_frown = "sprites/father/Slight Frown.png"
image father_smirk = "sprites/father/Smirk.png"
image mother_eyes_closed_smile = "sprites/mother/Eyes Closed Smile.png"
image mother_eyes_closed_speaking = "sprites/mother/Eyes Closed Speaking.png"
image mother_eyes_closed_worried_smile = "sprites/mother/Eyes Closed Worried Smile.png"
image mother_neutral_smile = "sprites/mother/Neutral Smile.png"
image mother_neutral_speaking = "sprites/mother/Neutral Speaking.png"
image mother_neutral = "sprites/mother/Neutral.png"
image mother_worried_smile = "sprites/mother/Worried Smile.png"
image mother_worried = "sprites/mother/Worried.png"


######################
# Sprite Declaration #
######################
image emily = "sprites/emily/mclines.png" #We may never reference this but just in case :p
image lauren_angry = "sprites/lauren/l1angry.png"
image lauren_angry2 = "sprites/lauren/l1angry2.png"
image lauren_angry2b = "sprites/lauren/l1angry2b.png"
image lauren_angryb = "sprites/lauren/l1angryb.png"
image lauren_confused = "sprites/lauren/l1confused.png"
image lauren_confused2 = "sprites/lauren/l1confused2.png"
image lauren_confused2b = "sprites/lauren/l1confused2b.png"
image lauren_confusedb = "sprites/lauren/l1confusedb.png"
image lauren_happy = "sprites/lauren/l1happy.png"
image lauren_happy2 = "sprites/lauren/l1happy2.png"
image lauren_happy2b = "sprites/lauren/l1happy2b.png"
image lauren_happyb = "sprites/lauren/l1happyb.png"
image lauren_shy = "sprites/lauren/l1shy.png"
image lauren_shy2 = "sprites/lauren/l1shy2.png"
image lauren_shy2b = "sprites/lauren/l1shy2b.png"
image lauren_shyb = "sprites/lauren/l1shyb.png"
image lauren_angryh = "sprites/lauren/l2angry.png"
image lauren_angry2h = "sprites/lauren/l2angry2.png"
image lauren_angry2bh = "sprites/lauren/l2angry2b.png"
image lauren_angrybh = "sprites/lauren/l2angryb.png"
image lauren_confusedh = "sprites/lauren/l2confused.png"
image lauren_confused2h = "sprites/lauren/l2confused2.png"
image lauren_confused2bh = "sprites/lauren/l2confused2b.png"
image lauren_confusedbh = "sprites/lauren/l2confusedb.png"
image lauren_happyh = "sprites/lauren/l2happy.png"
image lauren_happy2h = "sprites/lauren/l2happy2.png"
image lauren_happy2bh = "sprites/lauren/l2happy2b.png"
image lauren_happybh = "sprites/lauren/l2happyb.png"
image lauren_shyh = "sprites/lauren/l2shy.png"
image lauren_shy2h = "sprites/lauren/l2shy2.png"
image lauren_shy2bh = "sprites/lauren/l2shy2b.png"
image lauren_shybh = "sprites/lauren/l2shyb.png"
image maria_happy1 = "sprites/maria/sishappy1.png"
image maria_happy1b = "sprites/maria/sishappy1b.png"
image maria_happy2 = "sprites/maria/sishappy2.png"
image maria_happy2b = "sprites/maria/sishappy2b.png"
image maria_sad1 = "sprites/maria/sissad1.png"
image maria_sad1b = "sprites/maria/sissad1b.png"
image maria_sad2 = "sprites/maria/sissad2.png"
image maria_sad2b = "sprites/maria/sissad2b.png"
image maria_worry1 = "sprites/maria/sisworry1.png"
image maria_worry1b = "sprites/maria/sisworry1b.png"
image maria_worry2 = "sprites/maria/sisworry2.png"
image maria_worry2b = "sprites/maria/sisworry2b.png"


########################
# Dream BG Declaration #
########################



##################
# BG Declaration #
##################



#######
# CGs #
#######



#######
# VFX #
#######
image watercress = "vfx/splashscreen.png"


# Flash the splash screen on launch
label splashscreen:
    scene black 
    with Pause(1)

    show watercress with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

# Applies transitions to all characters
init python:
    def callback_transition(event, interact=True, **kwargs):
        if event == "begin":
            renpy.transition(dissolve, layer="master")
        
    config.all_character_callbacks = [callback_transition] 

# This jumps us to the first scene
label start:
    
    jump dream1