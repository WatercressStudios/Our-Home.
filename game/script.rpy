# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#IF I PUSH THIS IT'S TO DEMO VOICE TAGS - ECHOFROST
define e = Character("Eileen", voice_tag="eileen")
define t = Character("Tristan", voice_tag="tristan")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    # Since we defined the filename format on config, there's no need
    # to indicate the folder. ~MatKrulli
    voice "runexploder2.mp3"
    e "We run and we explode! I'm gonna blow up!"

    voice "toomanyer.mp3"
    t "Master Skywalker, there's too many of them. What are we going to do?"

    # This ends the game.

    return
