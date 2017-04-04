init python:
    custom_gallery.room = Gallery()
    custom_gallery.room.transition = dissolve

init python in custom_gallery:
    cgs = [
        ["cgs/BestphotoLI.png", "supergoodending"],
        ["cgs/Birthday Cake.png", "cake"],
        ["cgs/Composite 3.png", "neutralminusending", "neutralplusending"],
        ["cgs/Death.png", "funeralending"],
        ["cgs/fashion book.png", "fashionbook"],
        ["cgs/Heroin Box 2.png", "heroin"],
        ["cgs/li_mc_kissing_scene.png", "kissniagara"],
        ["cgs/out.png", "superbadending"],
        ["cgs/Park with LI.png", "parkdate", "parkdate dark"],
        ["cgs/Plushie.png", "plushie", "plushie damage"],
        ["cgs/Scene 67.png", "dreamepilogue"],
        ["cgs/sleepdead.png", "dreamending"],
        ["cgs/suicided.png", "suicideending"]
    ]
    unused_cgs = [
        ["cgs/Monochrome House.png"],
        ["cgs/Park only.png", "cgs/Park only (Night).png"],
    ]
    
    ## Number of rows and columns on the grid. Change this to change gallery size.
    xgrid = 4
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
    
    
    ## List of buttons so we can create them automatically in the scene
    buttons = [None] * (len(cgs) + len(unused_cgs))
    
    ## Add the buttons
    for i in range(len(unused_cgs)):
        room.button(unused_cgs[i][0])
        for cg in unused_cgs[i]:
            room.image(cg)
        buttons[i] = (unused_cgs[i][0], unused_cgs[i][0])

    for i in range(len(cgs)):
        room.button(cgs[i][1])
        for cg in (cgs[i])[1:]:
            room.unlock_image(cg)
        buttons[len(unused_cgs) + i] = (cgs[i][1], cgs[i][0])

init python in custom_music:
    mylist = [
        ["Main Menu", "bgmmenuloop - mainmenuloop.ogg"],
        ["Hijinks", "bgmhijinksloop - Hijinks Theme Loop.ogg"],
        ["Mood Music", "bgmmood - Mood Music #1.ogg"],
        ["Sad Song", "bgmsad1loop - Sad Song 1 Loop.ogg"],
        ["Creepy Dream", "bgmcreep - Creepy Dream Theme.ogg"],
        
        ["Dream", "bgmdream - Dream.ogg"],
        ["Dream v2", "bgmdream2 - Dream ver2.ogg"],
        
        ["Brother", "bgmbroloop - brotherthemeloop.ogg"],
        ["Sister", "bgmsis - Sister Theme.ogg"],
        ["Sister Orchestral", "bgmsis2 - Orchestral Sister Theme.ogg"],
        ["Love Interest", "bgmlov - Love Interest Theme.ogg"],
        ["Love Interest Orchestral", "bgmlov2 - Orchestral Love Interest Theme.ogg"],
        ["Father", "bgmdad - Father Theme.ogg"],
        ["Mother", "bgmmomloop - Mother Theme Loop.ogg"],
        
        ["Finale", "bgmfinaleloop - Finale Fight Loop.ogg"],
        ["Good Ending", "bgmgoodending - GoodEnding.ogg"],
        ["Neutral Ending", "bgmneutralloop - Neutral Ending Loop.ogg"],
        ["Bad End 1", "bgmbadendingloop - BadEndLoop.ogg"],
        ["Bad End 2", "bgmbadbro - badend-missingbrother.ogg"],
        ["Bad End 3", "bgmfuneral - Funeral End.ogg"],
        ["Credits", "bgmcreditsloop - CreditsLoop.ogg"]
    ]
    pos = 0
    xgrid = 4
    ygrid = 6
    
    def move_to(aux_pos):
        global pos
        pos = aux_pos
        if renpy.music.get_pause():
            renpy.music.stop()
        elif renpy.music.is_playing():
            renpy.music.play("music/" + mylist[pos][1], fadeout = 1.0)
    
    def move_by(delta):
        move_to(delta_pos(delta))
    
    def play():
        if renpy.music.is_playing():
            renpy.music.set_pause(False)
        else:
            renpy.music.play("music/" + mylist[pos][1])
    
    def pause():
        renpy.music.set_pause(True)
    
    def stop():
        renpy.music.stop()
    
    def true_playing():
        return renpy.music.is_playing() and not renpy.music.get_pause()
    
    def delta_pos(delta):
        delta = pos + delta
        while delta < 0:
            delta += len(mylist)
        while delta >= len(mylist):
            delta -= len(mylist)
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
                        im.Scale("cgs/Locked.png", custom_gallery.thumb_width, custom_gallery.thumb_height),
                        xalign = 0.5, yalign = 0.5, xsize = custom_gallery.thumb_width, ysize = custom_gallery.thumb_height)
                    $ custom_gallery.counter += 1
            for i in range(custom_gallery.xgrid * custom_gallery.ygrid - custom_gallery.counter):
                null

screen music_box():

    tag menu

    style_prefix "music_box"

    use game_menu(_("Music Box")):
        
        frame:
            
            frame:
                background None
                area 100, 20, 1210, 600
                grid custom_music.xgrid custom_music.ygrid:
                    xfill True
                    yfill True

                    $ custom_music.counter = 0

                    for bgmpos in range(len(custom_music.mylist)):
                        if custom_music.counter < custom_music.xgrid * custom_music.ygrid:
                            textbutton _(custom_music.mylist[bgmpos][0]) action Function(custom_music.move_to, bgmpos) align 0.5, 0.5
                            $ custom_music.counter += 1
                    for i in range(custom_music.xgrid * custom_music.ygrid - custom_music.counter):
                        null
            
            hbox:
                align 0.5, 0.8

                if renpy.music.is_playing():
                    if renpy.music.get_pause():
                        text "Paused: " align 0.5, 0.5
                    else:
                        text "Playing: " align 0.5, 0.5
                else:
                    text "Stopped: " align 0.5, 0.5

#                vbox:
#                    spacing 5
#
#                    for i in range(5, 0, -1):
#                        if len(custom_music.mylist) > (i * 2):
#                            text custom_music.mylist[custom_music.delta_pos(-i)][0]

                text custom_music.mylist[custom_music.pos][0]

#                    for i in range(1, 6):
#                        if len(custom_music.mylist) > (i * 2):
#                            text custom_music.mylist[custom_music.delta_pos(i)][0]

            hbox:
                align 0.5, 0.9
                spacing 30

                textbutton _("Previous") action Function(custom_music.move_by, -1)
                if custom_music.true_playing():
                    textbutton _("Pause") action Function(custom_music.pause)
                else:
                    textbutton _("Play") action Function(custom_music.play)
                textbutton _("Stop") action Function(custom_music.stop)
                textbutton _("Next") action Function(custom_music.move_by, 1)

style music_box_frame is empty

style music_box_frame:
    background Frame(im.MatrixColor("gui/frame2.png", im.matrix.opacity(0.7)))