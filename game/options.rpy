## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Our Home.")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.
## Fuck version control

define config.version = "1.0"


## Text that is placed on the game's about screen. To insert a blank line
## between paragraphs, write \n\n.

define gui.about = _("")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "OurHome"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.
## I'do like to implement these later, don't forget!

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
## I'd like to implement this later, don't forget!

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve

## A transition that is used when entering the yes/no prompt screen.

define config.enter_yesno_transition = dissolve

## A transition that is used when exiting the yes/no prompt screen.

define config.exit_yesno_transition = dissolve

## The transition used when entering the game menu from the main menu, as is done
## when clicking "Load Game" or "Preferences."

define config.main_game_transition = dissolve

## The transition that is used to display the main menu after the end of the
## splashscreen.

define config.end_splash_transition = dissolve

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 90


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 10

## This sets the default value of the fullscreen preference. This should be True
## or False. If None, this is ignored, allowing other code to set the default 
## value. (It's usually set to False in options.rpy.)

default preferences.fullscreen = True

## The default value of the voice sustain preference. If this is True, the voice
## will continue past the next interaction. If false, voice will stop when the
## next interaction begins.

define config.default_voice_sustain = False

## The default value of the wait for voice preference. This determines if Ren'Py
## should wait for voice to finish before auto-forward takes place.

define config.default_wait_for_voice = True

## The default volume of the music mixer, which is used for the music and movie
## audio channels. This should be a number between 0.0 and 1.0, with 1.0 being
## full volume.

default preferences.music_volume = 0.9

## The default volume of the sfx mixer, which is used for the sound audio channel.
## This should be a number between 0.0 and 1.0, with 1.0 being full volume.

default preferences.sfx_volume = 0.9

## The default volume of the voice mixer, which is used for the voice audio channel
## (And hence the voice statement, auto-voice, etc.). This should be a number
## between 0.0 and 1.0, with 1.0 being full volume.

default preferences.voice_volume = 1.0


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "OurHome-1488760097"

## The number of slots used by autosaves.

define config.autosave_slots = 10

## The number of slots used by quicksaves.

define config.quicksave_slots = 10

## If true, the game will autosave. If false, no autosaving will occur.

define config.has_autosave = True

## Roughly, the number of interactions that will occur before an autosave occurs.
## To disable autosaving, set config.has_autosave to False, don't change this
## variable.

define config.autosave_frequency = 200

## If true, Ren'Py will autosave upon encountering an in-game choice.
## (When renpy.choice_for_skipping() is called.)

define config.autosave_on_choice = True

## If true, Ren'Py will attempt to autosave when the user attempts to quit,
## return to the main menu, or load a game over the existing game. (To save
## time, the autosave occurs while the user is being prompted to confirm his or her
## decision.)

define config.autosave_on_quit = True


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"


## Others ########################################################################
##
## Other config variables

## By doing this, we can use a simpler filename format when calling voice.
## We could also ommit the extension, but since I'm adding this info on the files
## I'm giving to the VAs, I'd rather keep it so we can use those files as they are.
##
## What it does right now is just remove the need for indicating the folder.
## ~MatKrulli

define config.voice_filename_format = "voice/{filename}"

## If not None, this is the upper limit on the number of frames Ren'Py will attempt
## to display per second. This is only respected by the software renderer. The GL
## renderer will synchronize to vertical blank instead.
## /r/pcmasterrace

define config.framerate = 144

## This is the background that is used when config.developer is True and an
## undefined image is used in a scene statement. This should be an image name
## (a string), not a displayable.

# define config.missing_background = "black"

## The mouse is hidden after this number of seconds has elapsed without any mouse
## input. This should be set to longer than the expected time it will take to read
## a single screen, so mouse users will not experience the mouse appearing then
## disappearing between clicks.
## If None, the mouse will never be hidden.

define config.mouse_hide_time = 30

init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True)
    if not persistent.ambience_volume:
        renpy.music.get_channel("ambience").chan_volume = 0.8
        persistent.ambience_volume = 0.8
    else:
        renpy.music.get_channel("ambience").chan_volume = persistent.ambience_volume
