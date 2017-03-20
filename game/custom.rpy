init python:
    custom_gallery.room = Gallery()
    custom_gallery.room.transition = dissolve

init python in custom_gallery:
    cgs = [
        "BestphotoLI.png",
        "Birthday Cake.png",
        ["Composite 3.png", "InkedComposite 3_LI.png"],
        "Death.png",
        ["Heroin Box.png", "Heroin Box 2.png"],
        "Monochrome House.png",
        ["Park only.png", "Park only (Night).png", "Park with LI.png", "Park with LI (Night).png"],
        ["Plushie.png", "Plushie Damage.png"],
        "Scene 67.png",
        "sleepdead.png"
    ]
    
    ## Number of rows and columns on the grid. Change this to change gallery size.
    xgrid = 5
    ygrid = 4
    
    ## Total width and height available for the gallery. Don't mess with those.
    width = 1410
    height = 840
    
    ## Aspect ratio for the images used. Shouldn't need to mess with this one.
    aspect_ratio = 16.0 / 9.0
    
    ## Optional minimum border between images, given in pixels.
    border = 10
    
    ## Define what size should the thumbnails have according to the variables defined above.
    if (float(width) / xgrid) / (float(height) / ygrid) > aspect_ratio:
        thumb_height = height / ygrid - border
        thumb_width = thumb_height * aspect_ratio
    else:
        thumb_width = width / xgrid - border
        thumb_height = thumb_width / aspect_ratio
    
    ## Add the buttons
    for i in range(len(cgs)):
        if isinstance(cgs[i], list):
            room.button("cgs/" + cgs[i][0])
            for cg in cgs[i]:
                room.image("cgs/" + cg)
        else:
            room.button("cgs/" + cgs[i])
            room.image("cgs/" + cgs[i])
    
    ## Create a list of buttons to allow us to create the buttons automatically on the Scene
    buttons = [None] * len(room.buttons)
    for k, v in room.buttons.iteritems():
        buttons[v.index] = (k, v.images[0].displayables[0])

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
            
            $ custom_gallery.counter = 0

            for b in custom_gallery.buttons:
                if custom_gallery.counter < custom_gallery.xgrid * custom_gallery.ygrid:
                    add custom_gallery.room.make_button(
                        b[0],
                        im.Scale(b[1], custom_gallery.thumb_width, custom_gallery.thumb_height),
                        xalign = 0.5, yalign = 0.5, xsize = custom_gallery.thumb_width, ysize = custom_gallery.thumb_height)
                    $ custom_gallery.counter += 1
            for i in range(custom_gallery.xgrid * custom_gallery.ygrid - custom_gallery.counter):
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