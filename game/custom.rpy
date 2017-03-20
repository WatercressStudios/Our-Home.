init python:
    custom_gallery.room = Gallery()
    custom_gallery.room.transition = dissolve

init python in custom_gallery:
    cgs = {
        "alchemy":[
            "alchemy 1.jpg", "alchemy 2.jpg", "alchemy 3.jpg", "alchemy 4.jpg", "alchemy 5.jpg", "alchemy 6.jpg", "alchemy 7.jpg", "alchemy 8.jpg", "alchemy 9.jpg", "alchemy 10.jpg", "alchemy 11.jpg", "alchemy 12.jpg", "alchemy 13.jpg", "alchemy 14.jpg", "alchemy 15.jpg", "alchemy 15.jpg"
        ]
    }
    
    xgrid = 5
    ygrid = 3
    thumb_width = 100
    thumb_height = 100
    
    def cg_path(group, position):
        return "cgs/" + group + "/" + cgs[group][position]
    
    for i in range(len(cgs["alchemy"])):
        room.button(cg_path("alchemy", i))
        room.image(cg_path("alchemy", i))

init python in custom_music:
    list = [
        "01 - I'm here.mp3", "02 - in the living room.mp3", "03 - Still alive.mp3"
    ]
    pos = 0
    
    def move(delta):
        global pos
        pos = delta_pos(delta)
        if renpy.music.get_pause():
            renpy.music.stop()
        elif renpy.music.is_playing():
            renpy.music.play("music/" + list[pos], fadeout = 1.0)
    
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

screen gallery():
    
    tag menu

    use game_menu(_("Gallery")):
        
        grid custom_gallery.xgrid custom_gallery.ygrid:
            xfill True
            yfill True

            for i in range(custom_gallery.xgrid):
                for j in range(custom_gallery.ygrid):
                    if i + j * custom_gallery.xgrid < len(custom_gallery.cgs["alchemy"]):
                        add custom_gallery.room.make_button(
                            custom_gallery.cg_path("alchemy", i + j * custom_gallery.xgrid),
                            im.Scale(custom_gallery.cg_path("alchemy", i + j * custom_gallery.xgrid), custom_gallery.thumb_width, custom_gallery.thumb_height),
                            xalign = 0.5, yalign = 0.5, xsize = custom_gallery.thumb_width, ysize = custom_gallery.thumb_height)
                    else:
                        null

screen music_box():

    tag menu

    style_prefix "music_box"

    use game_menu(_("Music Box")):
        
        frame:
            
            hbox:
                align 0.5, 0.4

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
                        if len(custom_music.list) > (i * 2):
                            text custom_music.list[custom_music.delta_pos(-i)]

                    text custom_music.list[custom_music.pos]

                    for i in range(1, 6):
                        if len(custom_music.list) > (i * 2):
                            text custom_music.list[custom_music.delta_pos(i)]

            hbox:
                align 0.5, 0.9
                spacing 30

                textbutton _("Previous") action Function(custom_music.move, -1)
                if custom_music.true_playing():
                    textbutton _("Pause") action Function(custom_music.pause)
                else:
                    textbutton _("Play") action Function(custom_music.play)
                textbutton _("Stop") action Function(custom_music.stop)
                textbutton _("Next") action Function(custom_music.move, 1)

style music_box_frame is empty

style music_box_frame:
    background Frame(im.MatrixColor("gui/frame.png", im.matrix.opacity(0.7)))