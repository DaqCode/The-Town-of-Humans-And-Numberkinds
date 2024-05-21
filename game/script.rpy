#Characters defined jumbled
define n = Character("???", who_color="#4800C6")
define c1 = Character("???900")
define BadGuy = Character("Bad Guy", who_color="#ff820e")
define Alex = Character("Alex", who_color="#b300ffc7")
define Jerry = Character("Jerry", who_color="#06b200")
define E = Character("E", who_color="#ff0000")
define Kalk = Character("Kalkov", who_color="#bebebe")

#Custom Variables sets here
define characterDissolve = Dissolve(0.1)
define bgDissolve = Dissolve(0.75)

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
    # modal True
    window:
        background "#66edff99"
        xsize 600
        ysize 150
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

label start:
    camera:
        perspective True
    label prolouge:
        scene bg chapterzero
        with dissolve
        pause 2.0

        scene bg void
        with bgDissolve
        "You slowly opened your eyes. You feel a puple void, swirling around you. Your stomach is in knots, your brain is confused and anxious, your heart feeling like it'll pump right out of your chest.
        {i}\“Where am I? What is this?”{/i}\ You questioned yourself."
        "Suddenly, you see a discolored figure, walking towards you. It looked human, at least thats what you thought."
        define n = Character("???", color="#4800C6")
        show narrator neutral
        with characterDissolve
        n "Welcome in. I didn't expect a guest."
        show narrator too interested 
        with characterDissolve
        n "You seem quite new here, huh? Nice to meet you. Now how about you tell me who  you are? 
        Or maybe your intentions?"
        python:
            player = renpy.input("What's your name? (This is your permanent name for the remainder of the game, so it cannot be changed.)")
        define p = Character("[player]")
        p "Uh, my name is [player], where am I? Who are you?"
        show narrator thinking
        with characterDissolve
        n "Nice to meet you, [player]. I have a feeling you came here not by mere chance, but with purpose. 
        So let’s make haste; I’m quite busy with a lot, you know."
        show narrator guide
        with characterDissolve
        "You were confused, indeed. But whoever that \“thing”\ was didn't even bother answering your questions at all. 
        You wanted answers, yes, but there was something more interesting from your eyes."
        scene bg portal
        with bgDissolve
        "The thing leads you to a small portal. The portal looked like your average sized town; buildings, people walking around..."
        scene bg portal2 
        with bgDissolve
        "And, a floating number..?"
        p "So, you mind explaining what this place is or-"
        n "Have fun!"
        scene bg bye
        with Dissolve(0.25)
        "You are then kicked down the portal, without any answers."
        scene bg bye2
        with bgDissolve
        "As you fall, you can feel the change in atmosphere, the change in nature. 
        You didn’t know why or how, but you could feel that this place wasn’t earth at all. Now you just have to live with these conditions."   
        scene bg bye3
        with bgDissolve
        "And maybe. Just maybe. You’ll get along with the people."
        scene black
        with vpunch
        "*Thud*"
    label welcome:
        scene bg inworld
        with bgDissolve
        p "Aughhh... My head..."
        scene bg inworld2
        with bgDissolve
        p "Where the hell am I?"
        "You wake up from your nap of some sort. You’re lying on a bed of leaves and notice that there’s just trees and even more trees. It feels like Earth, but something doesn’t seem off."
        scene bg inworld3
        with bgDissolve
        "You dust yourself off and start to walk on the path. As you walk, you notice that there are some people. Thank god, you can finally get some answers now."
        "Of course, when you don't expect it, you notice that one similar number you saw through that portal. It seems like he didn't notice you and walked away. But now, you're tempted."
        "You want to check out the city, or be a lazy man and stay in the park?"
        menu:
            "Go back towards the park":
                jump c1_no
            "Go to the town":
                jump c1_yes

        label c1_no:
            $ park = True
            scene bg parkgo
            with bgDissolve 
            "Yep, you were just here. You still see that same flower pile you laid on."
            "Looking further, you see some odd looking, berries. Or at least thats what you think."
            scene bg parkback
            show got berries
            with dissolve
            show screen inventory_display_toggle
            $ inventory_items.append("Strange Berries")
            "You got...Berries?" 
            "You packed it into your bag and moved on."
            jump c1_done

        label c1_yes:
            $ park = False
            jump c1_done
        
        label c1_done:
        scene bg stunseed 1
        with dissolve
        "You walk over to the city, and, nothing weird so far..."
        "You see a couple of buildings, utility stores, grocery stores, so it must be similar to your own planet you've been in before."
        "And then once you lease expect it, the one number you saw last time, the digits 900, start floating towards you. You can’t really do much, so you go towards him and talk."
        show decent silhouette:
            xoffset -150.00
            yoffset -144.00
        with characterDissolve
        c1"Hello there! Welcome to Stunseed, a land of magical and complex beings of all the works. What got you here pal?"
        if park:
            c1"I saw you looked back, that park is a nice place huh?"
        c1"By the way, you look like you fell from 900 meters from the sky. You ok?"
        menu:
            "Get rid of your confusion, say something":
                jump c2_speak
            "Stay curious, say nothing":
                jump c2_noSpeak
        label c2_speak:
            p "Uh, hey. I’m [player]. I’m not sure who the hell you might be, but nice to meet you? Also, yeah. I somehow survived that fall. No idea how the hell I did."
            jump c2_done

        label c2_noSpeak:
            "You say nothing. Probably stunned by whatever the hell you’re just looking at."
            c1"Hey, you there pal? Are you a silent protagonist or mute?"
            "You try not to say anything. You still feel a bit nervous, and feel like you wanted to say something, but maybe you'll wait a little later."
            c1"Alright, guess you'll just stay mute, unless you want to talk later. Well, anyways..."
            jump c2_done

        label c2_done:
            c1"So, you actually fell from 900 fe-"
        "You both are then interrupted by some \“people.”\ One looks like your generic gangstar, the other, looks like some witch, and the other is just, a snake?"
        "With a sigh, you breathe and go with the flow, having that slight feeling of nausea and butterflies in your stomach. Except with the additional feeling of them being boiled instead."
        define n2 = Character("???", color = "#9b9b9bff")
        n2 "Decent! What are you doing? We were supposed to go right... Now..? Who's the new guy? Or gal?"
        c1"A new town member named [player], he also supposedly fell from 900 feet from the sky."
        p "Why is it that so many people have fallen from that exact same hole I've been in as well?"
        c1"They really didn't, but I'll introduce them I suppose."
        show decent smile talking:
            xoffset -150.00
            yoffset -144.00
        with fade    
        $ c1= 'Decent900'
        c1 "Well, my name is Decent900. "
        # This part is when Decent900 introduces characters. Every click introduces one after another, and a character model shows up.
        show alex neutral:
            xoffset 1089.00
        with characterDissolve
        extend "My friend here is named Alex. We are good friends- oh there’s 2 other members. " 
        show badguy unaware:
            xoffset 756.00
        with characterDissolve
        extend "Their names are Bad guy "
        show jerry neutral
        with characterDissolve
        extend "and Jerry. "
        show decent neutral
        with characterDissolve
        Alex "Bad Guy is the stick figure, Jerry is the snake."
        p "Nice to meet you Bad Guy, and nice to meet you Jerry. Ya’ll look like you’d be nice people."
        "Bad Guy looked pretty spaced out, guess he looked quite chill."
        "For a stick figure, that is." 
        show badguy neutral
        with characterDissolve
        "And then, it's just a snake. Nothing much he can do, other than bite me or something..?"
        "Lets hope thats not the case."
        "And a... witch. If thats what I had to assume. I'll probably figure it out later."
        BadGuy "... Sup"
        show jerry excited
        with characterDissolve
        Jerry "sss... sssss ssss ss ssss ss ssss sss..."
        show jerry aware
        with characterDissolve
        p "Poor thing, wish that thing could talk in this cartoon of a world."
        "He seems, friendly, I think? Something in my mind tells me that he wants a pet."
        "No reason? Just out of curiousity? {i}I do like reptiles I suppose{/i}"
        menu: 
            "Pet Jerry":
                jump c3_pet
            "Don't pet Jerry, Ignore him":
                jump c3_noPet

        label c3_pet:
            show jerry excited with vpunch
            with characterDissolve
            "You pet jerry and felt some warmness coming off, then last second his tongue hit your hand, you were somewhat calm with him and Jerry looked happy."
            show decent smile talking
            with characterDissolve
            c1 "Seems like Jerry got the best of you. Well, who knows, maybe you'll get into good hands one day."
            Jerry "Sssss sss sSSssss ss..!"
            show decent neutral
            with characterDissolve
            "You still can't tell what he said, but you can tell he appreciate the pat you gave him"
            jump c3_done

        label c3_noPet:
            "You don't pet Jerry. "
            "Even Jerry seemed slightly disapointed, but he's a snake, he won't really know."
            jump c3_done
        label c3_done:
            show decent smile talking
            with characterDissolve
            c1 "Well uhh... Nice to meet you, but since you are new, you should probably find a place to stay. Here, go in there and meet the mayors, I'm sure they will be happy to see new people."
        
        c1 "You see that ginormous tree out there? Search 'round there, and you'll find the mayors house."
        c1 "Kay byeeee..."
        #Template for later bg
        scene bg stunseed 1
        with bgDissolve

        "Before you wanted to ask him more questions, the strange number already disapeared."
        "Even his friends also just, left with him somehow. How in the world do people just know how to do that?"
        "{b}Mayors? House?{/b} What in the hell is it talking about? More confusion seeps into your mind as you try to decrypt his message, even though its not even a riddle."
        "After another heavy {i}sigh{/i}, you start walking on the sidewalk, practically guessing where each of your steps would take you."
        
        "Many lefts and rights and other turns later, you find a somewhaht odd looking house, that looked like it had a more complete with a better looking roof."
        "Somehow, the other houses out there just looked quite... odd looking now that you compared it with the mayor's home instead."
        "It looked quite decieving, but right before you entered, you heard a odd noise nearby the arera. It sounded like {i}rumaging{/i}."
        "Before you could even tell what the hell it was, you turn around, and see a small slime. It had a ridiculous looking tie and it also looked like it was about to attack."
        "You quickly dashed backwards to distance yourself away from such creature as the slime grows confused of your actions."

        show e slime happy
        with characterDissolve
        E "Woah there, are you fine? I’m not a threat don’t worry. What’s your name? Oh sorry I should probably say mine first heh. Name is E, I’m the second mayor, The first is through that door."
        p "E... Hey, nice to meet you I suppose. Name's [player]. I really didn't think your name would ever be that short, but, do you know where the hell I'm in?"
        p "Still quite confused on my entire part of falling through this, weird portal or whatever, wondering if you'd know anything about it."
        show e slime neutral
        with characterDissolve
        "The slime thinks for a second. As she just stands there, you can't help but notice the strange orb in the middle of her. A strange sight indeed."
        show e slime interested
        with characterDissolve
        E "Nope, got really no idea. I feel like I just appeared here, and you know, I'm still living my dream like how I wanted. As the town mayor, I suppose."
        show e slime neutral
        with characterDissolve
        p "Oh, so you're the mayor? I've been redirected by one of your friends, Decent... I think it was 600?"
        show e slime happy
        with characterDissolve
        E "900. I see, I've known him quite well, and I think I do have some things that you could do. Let me flip through my notes real quickly..."
        show e slime neutral
        with characterDissolve
        "She slowly flips through her notes, from inside her body..? You dare not question it, and just wait for her response. After around a short minute, she closes the book."
        show e slime happy
        with characterDissolve
        E "Alright, you can come with me. I have another important member that you should be acquainted with. Don't worry, he won't be as weird as you think he might look like."
        #Template for later bg
        scene bg stunseed 1
        with bgDissolve

        "You follow the slime up into the house. The house itself looked quite comfy. It looked nearly identical to your average looking chapel, with benches, couple of cabinets..."
        "{b}And a marble statue..?{/}"

        "As you entere inside the home, the marble state starts shaking and shivering, oddly."
        "Before you know it, it rises higher than you, and now it just has a suit, ready for its usual profession"

        Kalk "Hello there."
        "It spoke in such a threatening voice, but you don't know if you should respond or not."
        "Did Decent teach you anything with talking yet? You should probably break out of that space of being quiet anyways..."

        menu:
            "Speak to Kalkov":
                jump c4_speak
            "Don't speak":
                jump c4_nspeak

        label c4_speak:
            p "Hello there. I've been told by your friend your name is, Kalkov?"
            Kalk "Indeed it is. Well, its nice to know you aren't one of the shy ones. Welcome to Stun Seed Town."
            jump c4_done

        label c4_nspeak:
            "You stand there, not saying a word."
            "Of course, you can already feel the judgement rise from the ginourmous marble statue, and you start feeling tense and feel goosebumps forming."
            Kalk "Well, so you are one of them."
            "He {i}sighs{/i} before rising up from his chair."
            Kalk "Welcome to Stun Seed Town, hopefully you make a nice use of this place"
            jump c4_done
        
        label c4_done:
            "You feel slightly concered. That can't just be it, with simple admission; There's got to be a catch."

        p "Uhhh, so what exactly am I going to do? Where am I going to live?"
        Kalk "Thank you for bringing that up. I actually do have a couple of things to share with you to make your living life a bit more comfortable."
        p "He ruffles around with some papers, and eventually gets everything ordered as it is, stacking right on top of each other."

    return
