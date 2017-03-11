# Doing this in a separate file just to make it easier for me to understand.
# I'll merge it with screens once it's good enough.

# Also, remove those musics once we get the actual ones, since they're copyrighted as shit.

init python in music:
    list = ["01 - I'm here.mp3", "02 - in the living room.mp3", "03 - Still alive.mp3"]
    pos = 0
    
    def next():
        global pos
        pos = delta_pos(1)
        if true_playing():
            renpy.music.play("music/" + list[pos])
        elif renpy.music.is_playing():
            renpy.music.stop()
    
    def prev():
        global pos
        pos = delta_pos(-1)
        if true_playing():
            renpy.music.play("music/" + list[pos])
        elif renpy.music.is_playing():
            renpy.music.stop()
    
    def play():
        if renpy.music.is_playing():
            renpy.music.set_pause(False)
        else:
            renpy.music.play("music/" + list[pos])
    
    def pause():
        renpy.music.set_pause(True)
    
    def stop():
        renpy.music.stop()
    
    def true_playing():
        return renpy.music.is_playing() and not renpy.music.get_pause()
    
    def delta_pos(delta):
        delta = pos + delta
        while delta < 0:
            delta += len(list)
        while delta >= len(list):
            delta -= len(list)
        return delta

screen music_box():

    tag menu

    use game_menu(_("Music Box")):
        
        fixed:
            
            hbox:
                align 0.3, 0.2

                if renpy.music.is_playing():
                    if renpy.music.get_pause():
                        text "Paused: " align 0.5, 0.5
                    else:
                        text "Playing: " align 0.5, 0.5
                else:
                    text "Stopped: " align 0.5, 0.5

                vbox:
                    spacing 5

                    for i in range(5, 0, -1):
                        if len(music.list) > (i * 2):
                            text music.list[music.delta_pos(-i)]

                    text music.list[music.pos]

                    for i in range(1, 6):
                        if len(music.list) > (i * 2):
                            text music.list[music.delta_pos(i)]

            hbox:
                align 0.3, 0.7
                spacing 30

                textbutton _("Previous") action Function(music.prev)
                if music.true_playing():
                    textbutton _("Pause") action Function(music.pause)
                else:
                    textbutton _("Play") action Function(music.play)
                textbutton _("Stop") action Function(music.stop)
                textbutton _("Next") action Function(music.next)