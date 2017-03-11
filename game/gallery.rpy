init python in gallery:
    cgs = {
        "memes":[
            "kawaii.png", "kininarimasu.jpg", "mathematical.png", "merchant.jpg", "trouble.jpg", "well.jpg", "whatsthis.jpg", "bullshit.jpeg", "butthurt.png", "cooperation.jpg", "dog.jpg", "facepalm.jpg", "goddesses.jpg"
        ],
        "alchemy":[
            "alchemy 1.jpg", "alchemy 2.jpg", "alchemy 3.jpg", "alchemy 4.jpg", "alchemy 5.jpg", "alchemy 6.jpg", "alchemy 7.jpg", "alchemy 8.jpg", "alchemy 9.jpg", "alchemy 10.jpg", "alchemy 11.jpg", "alchemy 12.jpg", "alchemy 13.jpg", "alchemy 14.jpg", "alchemy 15.jpg"
        ]
    }
    
    xgrid = 4
    ygrid = 3
    selected = 0
    
    def cg_path(group, position):
        return "cgs/" + group + "/" + cgs[group][position]

screen gallery():
    
    tag menu

    use game_menu(_("Gallery")):
        
        grid gallery.xgrid gallery.ygrid:
            xfill True
            yfill True

            for i in range(gallery.ygrid):
                for j in range(gallery.xgrid):
                    if j + i * gallery.xgrid < len(gallery.cgs["memes"]):
                        button:
                            action SetField(gallery, "selected", j + i * gallery.xgrid), ShowMenu("gallery_chosen")
                            
                            xysize 1380 / gallery.xgrid, 820 / gallery.ygrid
                            
                            add gallery.cg_path("memes", j + i * gallery.xgrid):
                                size 1380 / gallery.xgrid, 820 / gallery.ygrid
                                align 0.5, 0.5
                    else:
                        null

screen gallery_chosen():
    
    tag menu
    
    use game_menu(_("Gallery")):
        
        add gallery.cg_path("memes", gallery.selected):
            align 0.5, 0.4

        textbutton "Back" align 0.5, 1.0 action ShowMenu("gallery")