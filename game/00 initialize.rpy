###############################
# Dream Character Declaration #
###############################
define dn = Character(None, what_color="#FFFFFF", kind=nvl, what_size=32)
define dbro = Character('Brother', color="#800000", show_two_window=True)
define dmom = Character('Mother', color="#800000", show_two_window=True)
define ddad = Character('Father', color="#800000", show_two_window=True)
define dlov = Character('Diane', color="#800000", show_two_window=True)

#########################
# Character Declaration #
#########################
define n = Character(None, what_color="#FFFFFF", kind=nvl, what_size=32)
define pro = Character('Emily', color="#800000", show_two_window=True)
define lov = Character('Lauren', color="#800000", show_two_window=True)
define sis = Character('Maria', color="#800000", show_two_window=True)
define bro = Character('Alex', color="#800000", show_two_window=True)
define mom = Character('Elizabeth', color="#800000", show_two_window=True)
define dad = Character('Jonathan', color="#800000", show_two_window=True)
define tea = Character('Teacher', color="#800000", show_two_window=True)
define doc = Character('Doctor', color="#800000", show_two_window=True) #Make doctor and nurse the same color
define nur = Character('Nurse', color="#800000", show_two_window=True) #Make doctor and nurse the same color
define all = Character('All', color="#800000", show_two_window=True)
define cho = Character('Choreographer', color="#800000", show_two_window=True)
define hm = Character('Hall Monitor', color="#800000", show_two_window=True)


############################
# Dream Sprite Declaration #
############################


######################
# Sprite Declaration #
######################


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
    
    jump scene1