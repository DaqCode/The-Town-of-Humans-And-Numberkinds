#Characters defined jumbled
define n = Character("???", who_color="#4800C6")
define c1 = Character("???900", who_color="ffffff")
define c2 = Character("Decent900", who_color="#ffae00")
define BadGuy = Character("Bad Guy", who_color="#ff820e")
define Alex = Character("Alex", who_color="#b300ffc7")
define Jerry = Character("Jerry", who_color="#06b200")
define E = Character("?", who_color="#ff0000")
define Kalk = Character("Kalkov", who_color="#bebebe")
define Telly = Character("Telly", who_color="#00ffe5")

#Custom Variables sets here
define characterDissolve = Dissolve(0.1)
define bgDissolve = Dissolve(0.75)
define normalLoopHome = False

#Movement data
define wiperight = CropMove(1.0, "wiperight")
define wipeleft = CropMove(1.0, "wipeleft")
define wipeup = CropMove(1.0, "wipeup")
define wipedown = CropMove(1.0, "wipedown")

define slideright = CropMove(1.0, "slideright")
define slideleft = CropMove(1.0, "slideleft")
define slideup = CropMove(1.0, "slideup")
define slidedown = CropMove(1.0, "slidedown")

define slideawayright = CropMove(1.0, "slideawayright")
define slideawayleft = CropMove(1.0, "slideawayleft")
define slideawayup = CropMove(1.0, "slideawayup")
define slideawaydown = CropMove(1.0, "slideawaydown")

define irisout = CropMove(1.0, "irisout")
define irisin = CropMove(1.0, "irisin")

#Gane begins from here
label start:
##########################################################################################################################################
    # Chapter 0: Where the hell am I?    
    camera:
        perspective True
    label WhereAmI:
        scene bg chapterzero
        with dissolve
        pause 2.0

        scene bg void
        with bgDissolve
        "You slowly opened your eyes. You feel a puple void, swirling around you."

        show screen show_screenMap

        "Your stomach is in knots, your brain is confused and anxious, your heart feeling like it'll pump right out of your chest."
        "{i}\“Where am I? What is this?”{/i}\ You questioned yourself."
        "Suddenly, you see a discolored figure, walking towards you. It looked human, at least thats what you thought."
        define n = Character("???", color="#4800C6")
        show narrator neutral
        with fade
        n "Welcome in. I didn't expect a guest."
        show narrator too interested
        with characterDissolve
        n "You seem quite new here, hm? Nice to meet you. Now how about you tell me who  you are? Or maybe your intentions?"
        show narrator neutral 2
        with characterDissolve

        define  p = Character("[player]", who_color="#00c8ff")                             # The player character
        define  npcNames = ["Decent900", "Decent", "Alex", "BadGuy", "Jerry", "E", "Kalkov", "StunSeed"] # Names the PC can't choose
        default player = "Unknown"                                                           # What to call the PC

        label chooseName:
            $ renpy.dynamic('done', 'name', 'prompt')
            $ done = False
            while not done:
                $ prompt = "Write your name down."
                $ prompt += " Only gotta be letters, no spaces, or weird characters. Or potential names of the others. Hopefully your name isn't longer than 10 letters..."
                $ name = renpy.input(prompt, length=10, exclude='" ", "?", "!", "@"').strip().capitalize() or "Unknown"
                if name in npcNames:
                    show narrator too interested
                    with fade 
                    n "Naming yourself a character of our world? Quite foolish."
                    n "I'd suggest having a different name..."
                    show narrator neutral 
                    with characterDissolve
                else:
                    $ done = True
                if name == "Daq":
                    n "Have fun playtesting my friend."
                    n "The code is all in your hands."
                    $ done = True
            $ player = name
        
        p "Uh, my name is [player]. Where am I? Who are you?"
        show narrator thinking
        with fade
        n "Nice to meet you, [player]. I have a feeling you came here not by mere chance, but with purpose. 
        So let’s make haste; I’m quite busy with a lot, you know."
        show narrator guide
        with characterDissolve
        "You were confused, indeed. But whoever that \“thing”\ was didn't even bother answering your questions at all. 
        You wanted answers, yes, but there was something more interesting that captivated your sight."
        scene bg portal
        with bgDissolve
        "The thing leads you to a small portal. The portal looked like your average sized town. It has buildings, people walking around..."
        "With a giant pink tree acting as the heart of the town."
        scene bg portal2 
        with bgDissolve
        "And... a floating number..?"
        p "Uhh, so you mind explaining what this place is or-"
        n "Have fun!"
        scene bg bye
        with Dissolve(0.25)
        "You are then kicked down the portal, without any answers."
        scene bg bye2
        with bgDissolve
        "As you fall, you can feel the change in atmosphere, the change in nature. 
        You don’t know why or how, but you could feel that this place isn't earth at all. Now you just have to live with these conditions."   
        scene bg bye3
        with bgDissolve
        "And maybe. Just maybe. You’ll get along with the people."
        scene black
        with vpunch
        "*Thud*"

##########################################################################################################################################
    # Chapter 1: Welcome to StunSeed
    label welcomeToStunseed:
        scene bg inworld
        with bgDissolve
        p "Aughhh... My head..."

        $tellyCharacter = True    

        scene bg inworld2
        with bgDissolve
        p "Where the hell am I?"
        "You wake up from being knocked out by the giant fall. You’re lying on a bed of flowers and slowly rise up. The place really does indeed feel like Earth."
        scene bg inworld3
        with bgDissolve
        "You dust yourself off and start to walk on the road path. Seemed more of a road for vehicles, but you haven't spotted any so far."
        "The air felt more clean than on Earth, considering that you also probably heard no cars either."
        "As you walk, everything seems to be, normal. Trees rooted, roads layed, and flowers expressing themselves with their colors."
        "Walking through, you see a sign with the text \“Stun Seed”\. Is this a practical joke? Or is that an actual place now?"
        "You want to check out the so called Stun Seed, or head back to the park?"
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
            "The flower bed looks much more flatter even after the 300 feet fall. It doesn't look like the pile is going to wilt away either."
            "Turns out there really isn't much else you can do, so why'd you even bother coming back here?"
            "Well, looking more closely, you noticed some odd looking berries. Or at least thats what you thought."
            "You stroll over to it and swiftly pick it up from where it sat: on the glassy plains of the very area you fell upon."
            scene bg parkback
            show got berries
            with dissolve
            show screen inventory_display_toggle
            $ inventory_items.append("Strange Berries")
            "You got...Berries?" 
            "Quite shiny. It reminds you of blueberries. Maybe not based on taste, but looks."
            "You packed it into your pocket and moved on."
            jump c1_done

        label c1_yes:
            $ park = False
            jump c1_done
        
        label c1_done:
        scene bg stunseed 1
        with dissolve
        "You walk over to the city, and, nothing weird so far..."
        "{i}Maybe except that mushroom home you see in the distance...{/i}"
        "You see a couple of buildings, utility stores, grocery stores, so it must be similar to your own planet you've been in before."
        "And then once you least expect it, the one number you saw last time, the digits 900, starts floating towards you." 
        "You can’t really do much, so you approach him."
        #Should be in middle, make it move once characters are about to be announced
        #Also put him down
        show decent silhouette:
            xoffset -150.00
            yoffset -144.00
        with characterDissolve
        c1"Hello there! Welcome to Stunseed, a land of magical and complex beings of all the works. What got you here pal?"
        if park:
            c1"I saw you looked back, that park is a nice place huh?"
        c1"By the way, you look like you fell right out of the sky. You ok?"
        menu:
            "Get rid of your confusion, say something":
                jump c2_speak
            "Stay curious, say nothing":
                jump c2_noSpeak
        label c2_speak:
            p "Uh, hey. I’m [player]. I’m not sure who the hell you might be, but nice to meet you?" 
            p "And yes. I somehow survived the fall. No idea how the hell I did."
            jump c2_done

        label c2_noSpeak:
            "You say nothing. Probably stunned by whatever the hell you’re just looking at."
            c1"Hey, you there pal? Are you a silent protagonist or mute?"
            "You try not to say anything. You still feel a bit nervous, and feel like you wanted to say something, but maybe you'll wait a little later."
            c1"Alright, guess you'll just stay mute, unless you want to talk later. Well, anyways..."
            jump c2_done

        label c2_done:
            c1 "So is it only reasonable to assume you just suddenly fe-" 
        define n2 = Character("???", color = "#9b9b9bff")        
        with vpunch
        n2 "DECCCENNNNTTT!"
        show decent silhouette:
            xoffset -675.00
            yoffset -45.00
            xzoom -1.00
        with characterDissolve
        "You both are then interrupted by some \“people”\. You really can't see them at all, but the flying number goes towards them."
        show decent silhouette:
            xoffset -150.00
            yoffset -144.00
            xzoom 1.00
        with characterDissolve    
        c1 "You should follow me, it'll be worth your trip."        
        
        window auto hide
        show decent silhouette:
            subpixel True 
            parallel:
                offset (-675.0, -45.0) yzoom 1.0 
                linear 3.00 offset (990.0, -684.0) yzoom 0.0 
            parallel:
                xzoom -1.0 
                linear 1.63 xzoom -0.46 
                linear 1.37 xzoom 0.0 
        with Pause(3.10)
        show decent silhouette:
            offset (990.0, -684.0) xzoom 0.0 yzoom 0.0 
        window auto show

        "Before you can even recollect your thoughts and figure out what just happeened, Decent is off to his next location to locate his friends."
        "They're probably just aquaintances or something, nothing to be worried of. {i}Right?{/i}"
        "With a sigh, you breathe and go with the flow, having that slight feeling of nausea and butterflies in your stomach."
        "Except with the additional feeling of them being boiled instead."
        show decent silhouette:
            xoffset -150.00
            yoffset -144.00
            xzoom 1.00
            yzoom 1.00
        with characterDissolve
        n2 "Decent! What are you doing? We were supposed to go right... Now..? Who's the new guy?"
        c1 "A new town member named [player]. He apparently fell out of the sky to this place."
        p "Did they also fall down just like I did?"
        c1 "Nope, not at all. Although, since you mention it, I might as well just introduce myself, and them as well."
        show decent smile talking:
            xoffset -150.00
            yoffset -144.00
        with fade    
        $ c1 = Character("Decent900", who_color="#ffae00")
        c1 "{i}Ahem,{/i} my name is Decent900. "
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
        c2 "Bad Guy is the stick figure, Jerry is the snake."
        p "Nice to meet you Bad Guy,  nice to meet you Alex, and nice to meet you Jerry. Ya’ll look like you’d be nice people."
        show badguy neutral
        with characterDissolve
        "Bad Guy looks pretty spaced out, and seemed quite chill."
        "For a stick figure, that is." 
        show badguy unaware
        with characterDissolve
        "And then, it's just a snake. Nothing much he can do, other than bite me or something..?"
        "Lets hope thats not the case."
        "And a... witch. If thats what I had to assume. I'll probably figure it out later."
        show badguy neutral
        with characterDissolve
        BadGuy "... Sup."
        show jerry excited
        with characterDissolve
        Jerry "sss... sssss ssss ss ssss ss ssss sss..."
        show jerry aware
        with characterDissolve
        p "Poor thing, wish that thing could talk in this cartoon of a world."
        "It seems, friendly, I think?"
        "Random curiosity now makes me want to pet it."
        "No reason? Just out of curiousity? {i}I do like reptiles I suppose, but it could be a bit of a risk{/i}..?"
        menu: 
            "Pet Jerry":
                jump c3_pet
            "Don't pet Jerry, Ignore him":
                jump c3_noPet

        label c3_pet:
            show jerry excited with vpunch
            with characterDissolve
            "You pet Jerry and felt some warmness radiating off of him."
            "You were somewhat calm with him and Jerry looked happy."
            show decent smile talking
            with characterDissolve
            c1 "Seems like Jerry got the best of you. Well, who knows, maybe you'll get into good hands one day."
            show decent neutral
            with characterDissolve
            Jerry "Sssss sss sSSssss ss..!"
            show decent neutral
            with characterDissolve
            "You still can't tell what he said, but you can tell he appreciate the pat you gave him."
            jump c3_done

        label c3_noPet:
            "You don't pet Jerry. "
            "Even Jerry seemed slightly disapointed, but he's a snake, he won't really know."
            jump c3_done
        label c3_done:
            show decent smile talking
            with characterDissolve
            c1 "Well uhh... Nice to meet you, but since you are new, you should probably find a place to stay."
        
        show jerry neutral 
        with characterDissolve
        c1 "You see that ginormous tree out there? Search 'round there, and you'll find the mayors house."
        c1 "Go in there and meet the mayors, I'm sure they will be happy to see a new town member."
        c1 "Kay byeeee..."
        #Template for later bg
        scene bg stunseed 1
        with bgDissolve

        "Before you wanted to ask him more questions, the strange number disapeared."
        "Even his friends also just left with him somehow. How in the world do people just know how to do that?"
        "{b}Mayors? House?{/b} What in the hell is it talking about? More confusion seeps into your mind as you try to decrypt his message, even though its not even a riddle."
        "After another heavy {i}sigh{/i}, you start walking on the sidewalk, practically guessing where each of your steps would take you."
        
        scene bg stunseed mayorhome
        with bgDissolve
        "Many lefts and rights and other turns later, you find the mayors home, that looked much more complete."
        "Complete, as in, it had a roof, where many others, simply didn't."
        "Somehow, the other houses out there just looked completely dilapidated. They had some broken walls, a missing roof, and not as many nice flowers as the mayor's home did."  
        "Comparing it with the house you stand in front of, it was interesting, to say the least."
        "It looked quite decieving, but right before you entered, you heard a odd noise nearby the arera. It sounded like {i}rumaging{/i}."
        "Before you could even tell what the hell it was, you turn around, and see a small slime. It had a ridiculous looking tie and it's intention didn't seem good either."
        "You quickly backed up to distance yourself away from the monster as the slime grew confused of your actions."
        show e slime happy
        with wipeup

        E "Woah there, are you fine? I’m not a threat, don’t worry. What’s your name?"
        E "Oh sorry I should probably say mine first, heh."
        $ E = Character("E", who_color="#ff0000")

        E "Name is E, and I’m the second mayor. The first is through that door."
        p "E... Hey, nice to meet you, I suppose. My name's [player]. I really didn't think your name would be that short, but, do you know where the hell I am?"
        p "Still quite confused on my entire part of falling through this, weird portal or whatever, wondering if you'd know anything about it."
        show e slime neutral
        with characterDissolve
        "The slime thinks for a second. As it just stands there, you can't help but notice the strange orb in the middle of her. A strange sight indeed."
        show e slime interested
        with characterDissolve
        E "Nope, got no idea. I came across here somehow, and I'm still living my dream like how I wanted. As the town mayor, I suppose."
        show e slime neutral
        with characterDissolve
        p "Oh, so you're the mayor? I've been redirected by one of your friends, Decent... I think it was 600?"
        show e slime happy
        with characterDissolve
        E "900. I see, I've known him quite well, and I think I do have some things that you could do. Let me flip through my notes real quickly..."
        show e slime neutral
        with characterDissolve
        "It slowly flips through its notes, from inside its body? You dare not question it, and just wait for its response. After around a short minute, it closes the book."
        show e slime happy
        with characterDissolve
        E "Alright, you can come with me. I have another important member that you should be acquainted with inside that house. Don't worry, he won't be as weird as you think he might look like."
        scene bg stunseed mayorinside
        with bgDissolve

        "You follow the slime into into the house."
        "The moment you entered the home, the slime leaves you inside the home and shuts the door."
        "The house itself looked quite comfy. It looked nearly identical to your average looking home."
        "It had a kitchen, you could assume you currently stood in a living room, and in that living room had a desk filled with stacks of paperwork."
        "{b}And a marble statue..?{/b}"
        "As you stand in the carpeted living room, the marble statue starts shaking and shivering, oddly."
        "Before you know it, it rises higher than you, with a suit, reading paperwork for 24 hours straight."
        with hpunch
        
        show kalkov greeting with moveinbottom
        Kalk "Hello there."

        #Make it conditional, unless if the player did speak the first time with Decent.
        "It spoke in such a threatening voice, but you don't know if you should respond or not."
        "Did Decent teach you anything with talking yet? You should probably break out of that space of being quiet anyways..."

        menu:
            "Speak to Kalkov":
                jump c4_speak
            "Don't speak":
                jump c4_nspeak

        label c4_speak:
            p "Hello there. I've been told by your friend your name is, Kalkov?"
            show kalkov neutral
            with characterDissolve
            Kalk "Indeed it is. Well, its nice to know you aren't one of the shy ones. Welcome to Stun Seed."
            $ nospeak = False
            jump c4_done

        label c4_nspeak:
            "You stand there, not saying a word."
            show kalkov neutral
            with characterDissolve
            "Of course, you can already feel the judgement rise from the ginourmous marble statue, and you start feeling tense and feel goosebumps forming."
            Kalk "Well, so you are one of them."
            "He {i}sighs{/i} before rising up from his chair."
            Kalk "Welcome to Stun Seed Town, hopefully you make a nice use of this place."
            $ nospeak = True
            jump c4_done
        
        label c4_done:
        
        "You feel slightly concered. That can't just be it, with simple admission; There's got to be a catch."
        p "Uhhh, so what exactly am I going to do? Where am I going to live?"
        if nospeak:
            Kalk "Spoken? I see you've quickly switched up."
        Kalk "Thank you for bringing that up. I actually do have a couple of things to share with you to make your living life a bit more comfortable."
        "He ruffles around with some papers, and eventually gets everything ordered as it is, stacked right on top of each other."
        Kalk "Alright, so here's what I got in store for you. I'll just be giving you house, and all you got to do to maintain rent is to pay $50. Every 3 weeks will suffice."
        Kalk "Do not worry about other signend paperwork. I was expecting newcomers to occupy this small town of ours."
        p "And how am I going to get money? Could I just assume doing jobs or commissions will be enough to pay it off?"
        Kalk "Absolutely. And to make it a little bit more easier on your toes, I'll cut your pay for this first rent by {u}half{/u}."
        Kalk "Which will mean you have to pay 25$ this time, but 50$ next time."

        Kalk "If you do want more space and fix up your house, well, that'll come with increased costs, but it will make your home, more home-ly, if that makes sense."
        Kalk "Which also means you can probably make your home seem somewhat like ours."
        Kalk "If you do happen to collect any gifts or items along the way you don't really want to use, why not drop it off at your home?"
        Kalk "It'll look nice, thats for sure, and it'll maybe boost your feel of home."
        Kalk "You just got to come over and visit my home for your house contracts. I'll be willing to help you out with the costs and materials."
        Kalk "Heh, reminds me of  little green bobs."

        p "That, sounds like a handful to take on. What other ways do you have of being able to pay this off?"
        Kalk "Well, my other suggestion for getting some money other than jobs or commissions..."
        Kalk "How about making some friends you can work with?"
        p "Huh? So just befriending them or something?"
        Kalk "You decide. I'm simply here to give you some directions and if you need, I think your other friend there, Decent900 can help you out."
        Kalk "I believe thats all I have to say. Any questions?"
        
        menu questions:
            "About my house? How do I repay it? How do I fix it?":
                jump c5_repay
            "How can I get money?":
                jump c5_money
            "No questions.":
                jump c5_nq
        
        label c5_repay:
            Kalk "Sure thing. The home you have is going to cost 25$ for the first 3 weeks, but 50$ later for rent."
            Kalk "If you want, you can come over to me and I'll be willing to fix up your home with the nessessary money and materials."
            Kalk "That way, your house will look much more, un-broken like."
            Kalk "And you'll hopefull give good insight to those that decide to visit your home from time to time."
            Kalk "Or you know, you could just do it just for the sake of your ego, but thats hard to assume."
            Kalk "Anything else?"
            jump questions
        label c5_money:
            Kalk "Sure sure. You can earn money by doing commissions or doing jobs."
            Kalk "You can also get more money by scavenging in nearby trash cans or bushes."
            Kalk "Get ceative with how you get your pay, but you'll need a lot to be able to pay off your debt and customize to your wants in the end."
            Kalk "If you find it difficult, well, there will be more alternatives that you'll discover."
            Kalk "If you're more curious about that, I can only suggest that you talk to Decent about it."
            Kalk "Heard he was rambling about bullets or something, but thats all I remember."
            Kalk "Anything else?"
            jump questions
        label c5_nq:
        show kalkov greeting with characterDissolve
        Kalk "Great then. Thanks for stopping by, and I wish you best of luck then."
        show kalkov neutral with characterDissolve
        p "Thanks for the help. Hope you have a good day."

        Kalk "Hold on, [player]. I didn't even show you where your home is."
        Kalk "It's my duty as mayor and land lord to guide you to your home. Hopefully you'll remember where it is later."
        Kalk "Don't worry about the looks of your home."
        Kalk "But it'll look interesting to you if I could read your mind."
        Kalk "You do seem like as if you'd like to live in luxary, but that'll come at a long time and a price to pay for."
        p "Understood."
        scene black with bgDissolve
        "After a bit of a walk, Kalkov leads you to find your home."
        "..."
        scene bg player home outside with bgDissolve
        "Jesus christ. What am I looking at."
        window auto hide
        show kalkov neutral:
            subpixel True xpos -522 
            ypos 0.96 
            linear 0.18 ypos 0.06 
        with hpunch
        with Pause(0.4)
        show kalkov neutral:
            pos (-522, 0.06) 
        window auto show
        Kalk "Well, here we are. It might not look like much, but it's honest work with a hint of charm."
        p "...Jesus christ. I don't know whether to be happy or dissapointed."
        Kalk "Well then, {i}ahem{/i}, I fully welcome you to Stun Seed."
        Kalk "Remember! Your rent will be due in 3 weeks and you only need to pay 25$ this time around."
        show kalkov greeting with characterDissolve
        Kalk "With that being said, I've got to leave for work. Good luck [player], and enjoy your stay!"

        #Change to make him slide right instead of going down.
        window auto hide
        show kalkov greeting:
            subpixel True 
            ypos 0.06 
            linear 0.20 ypos 0.95 
        with hpunch
        with Pause(0.30)
        show kalkov greeting:
            ypos 0.95 
        window auto show
        "He then just disappears. Right into the ground."
        "Well, time to go in."
    label atHome:
        while normalLoopHome:
            scene bg player home inside with bgDissolve
            "The white loop has been accessed."
            "Repeating..."
        screen atHomeChoices:
                imagebutton:
                    xalign 0.978
                    yalign 0.171
                    idle "images/Choices/choices_player_home_customize_idle.png"
                    hover "images/Choices/choices_player_home_customize_zoom.png"
                    action Jump("decentHelp")

                imagebutton:
                    xalign 0.978
                    yalign 0.455
                    idle "images/Choices/choices_player_home_storage_idle.png"
                    hover "images/Choices/choices_player_home_storage_zoom.png"
                    action Jump("decentGlitch")
                
                imagebutton:
                    xalign 0.98
                    yalign 0.71
                    idle "images/Choices/choices_player_end_idle.png"
                    hover "images/Choices/choices_player_end_zoom.png"
                    action Jump("decentLeave")
                imagebutton:
                    xalign 0.98
                    yalign 0.71
                    idle "images/Choices/choices_player_decent_idle.png"
                    hover "images/Choices/choices_player_decent_zoom.png"
                    action Jump("decentLeave")


        scene bg player home inside with fade
        "Here's your home. It looks, quite... detrimental."
        "The seating looks like it lost its own ability to become a seat."
        "The walls look pretty deteriorated."
        "Kalkov was right. Maybe you do need his help for fixing up your home..."
        "Oh well. Lets see what to do this time around..."
        $ normalLoopHome = True
        jump atHome

    #Change ALL the decent sprites to decent floating.
    label atDecentHome:
        scene bg decent home
        with bgDissolve
        "There's Decent's home."

        show decent floating:
            ypos -0.1
        with characterDissolve
        show jerry sleep
        with characterDissolve  
        c2 "Heya buddy. Need some help?"
        
        label atDecentChoices:
            screen decentHelpChoices:
                imagebutton:
                    xalign 0.978
                    yalign 0.171
                    idle "images/Choices/choices_help_decent_idle.png"
                    hover "images/Choices/choices_help_decent_zoom.png"
                    action Jump("decentHelp")

                imagebutton:
                    xalign 0.978
                    yalign 0.455
                    idle "images/Choices/choices_help_glitch_idle.png"
                    hover "images/Choices/choices_help_glitch_zoom.png"
                    action Jump("decentGlitch")
                
                imagebutton:
                    xalign 0.98
                    yalign 0.71
                    idle "images/Choices/choices_help_leave_idle.png"
                    hover "images/Choices/choices_help_leave_zoom.png"
                    action Jump("decentLeave")
                
                    
            window auto hide
            show choices_help_decent_idle:
                subpixel True ypos 153 
                xpos 1.0 
                linear 0.34 xpos 0.7 
            show choices_help_glitch_idle:
                subpixel True ypos 405
                xpos 1.0 
                linear 0.54 xpos 0.7 
            show choices_help_leave_idle:
                subpixel True ypos 630 
                xpos 1.0 
                linear 0.88 xpos 0.7 
            with Pause(0.98)
            show choices_help_decent_idle:
                pos (0.7, 153) 
            show choices_help_glitch_idle:
                xpos 0.7 
            show choices_help_leave_idle:
                pos (0.7, 630) 
            window auto show
            
            show decent floating with characterDissolve
            call screen decentHelpChoices

            c2 "Take your time, what do you want to choose?"

        label decentHelp:
            scene bg decent home 
            show jerry sleep 
            show decent floating
            c2 "You need some help?"
            c2 "Well, you're quite the quick witted man, considering that you've came over to immediately ask questions."
            c2 "Well I'd advise you go meet up with some people make friends, learn a thing or two about the town."
            c2 "I've lived here for a good 4 years so I got the gist of things."
            c2 "Nifty ain't it?"
            c2 "So I believe in you, and I also believe you should press the map icon to navigate around the town?"
            c2 "Well thats the most I have to say!"
            jump atDecentChoices
    
        label decentGlitch:
            scene bg decent home 
            show jerry sleep 
            show decent floating
            c2 "..."
            c2 "I see you found one of my bullets. I've always wondered where they get placed."
            c2 "I got a deal for ya, If you give me my glitch bullets I'm willing to help you out by giving you certain buffs."
            c2 "I don't know where the bullets are, so keep an eye out for me, ok?"
            c2 "Narrator has his methods to keeping these things difficult to find."
            c2 "But, if you do find glitch bullets, let me know, alright [player]?"
            c2 "Anthing else?"
            jump atDecentChoices

        label decentLeave:
            scene bg decent home 
            show jerry sleep 
            show decent floating
            c2 "Nice meeting you. Thanks for coming in!"
            c2 "See ya!"
        jump atHome

        


