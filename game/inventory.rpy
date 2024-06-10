# Inventory system initiated. May change depending
screen inventory_display_toggle:
    zorder 92
    frame:
        background "#ff8800d9"
        xalign 0.05
        yalign 0.05
        textbutton "Inventory":
            action ToggleScreen("inventory_item_description")
    on "hide" action Hide("inventory_item_description")

default item_descriptions = {"Strange Berries" : "It smells strong, thats for sure. You feel unsure if its even safe for human consumption, so best if you leave it for now in your bag."}
default inventory_items = []
default item_description = ""

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory_item_description:
    window:
        background "#66edff99"
        xsize 750
        ysize 175
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True

    window:
        background "#fffb8a9d"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                textbutton item:
                    action SetVariable("item_description", item_descriptions.get(item))
                    selected False
    on "hide" action SetVariable("item_description", "")