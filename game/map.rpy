# Control Variables
default tellyCharacter = False

# Defining location information
define locations = [
    # Location 1 details
    {
        "name": "Telly",
        "unlocked": "tellyCharacter",
        "idle_image": "tellyPin_idle.png",
        "hover_image": "tellyCharacter_hover.png",
        "scene": "telly_interraction",
        "xalign": 0.4,
        "yalign": 0.2
    }
]

# Screen button to show the Map
screen show_screenMap:
    frame:
        xalign 1.0
        yalign 0.0
        textbutton "Show the Map" xalign 0.5 yalign 0.5 action [Show("map_screen"), Hide("show_screenMap")]


# Map screen
screen map_screen:
    modal True
    add "stunseed_bg"

    # Create buttons for each location
    for location in locations:
        $unlocked = eval(location["unlocked"])

        if unlocked:
            imagebutton:
                # Button for unlocked locations
                idle location["idle_image"]
                hover location["hover_image"]
                xalign location["xalign"]
                yalign location["yalign"]
                action [Show("show_screenMap"), Hide("map_screen"), Jump(location["scene"])]

        else:
            imagebutton:
                # Button for locked locations
                idle "images/locked.png"
                xalign location["xalign"]
                yalign location["yalign"]
                action Notify("This location is locked for the moment...")

    frame:
        xalign 1.0
        yalign 0.0
        textbutton "Return" xalign 0.5 yalign 0.5 action [Show("show_screenMap"), Hide("map_screen")]



# label start:
#     show screen show_screenMap
#     "You have the map, but surprise surprise, no locations are allowed. Still stuck at home hm?"

#     # Scenario to unlock locations
#     $location1_unlocked = True
#     "You finally cut off the trees nearby the pond. Lets get going there."

#     $location2_unlocked = True
#     "Cave was cleared up. Lets check it out!"

#     # Return to the Main Menu
#     return 


# # Scene for location 1
# label location1_scene:
#     "There's the pond. And there's Brookie. But maybe not yet."
#     return
    

# # Scene for location 2
# label location2_scene:
#     "There's the cave. Lets start working. But maybe not yet."
#     return