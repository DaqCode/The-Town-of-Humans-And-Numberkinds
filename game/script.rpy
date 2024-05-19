define c1 = Character("???900")
define BadGuy = Character("Bad Guy")
define Alex = Character("Alex")
define Jerry = Character("Jerry")

label start:
    camera:
        perspective True
    label prolouge:
     
        scene bg chapterzero
        with dissolve
        pause 2.0
        
        scene bg void
        "You slowly opened your eyes. You feel a puple void, swirling around you. Your stomach is in knots, your brain is confused and anxious, your heart feeling like it'll pump right out of your chest.
        {i}\“Where am I? What is this?”{/i}\ You questioned yourself."

        "Suddenly, you see a discolored figure, walking towards you. It looked human, at least thats what you thought."

        define n = Character("???", color="#4800C6")
        show narrator neutral
        n "Welcome in. I didn't expect a guest."

        show narrator too interested 
        n "You seem quite new here, huh? Nice to meet you. Now how about you tell me who  you are? 
        Or maybe your intentions?"

        python:
            player = renpy.input("What's your name? (This is your permanent name for the remainder of the game, so it cannot be changed.)")
 
        define p = Character("[player]")
        
        p "Uh, my name is [player], where am I? Who are you?"       

        show narrator thinking
        n "Nice to meet you, [player]. I have a feeling you came here not by mere chance, but with purpose. 
        So let’s make haste; I’m quite busy with a lot, you know."

        show narrator guide
        "You were confused, indeed. But whoever that \“thing”\ was didn't even bother answering your questions at all. 
        You wanted answers, yes, but there was something more interesting from your eyes."

        scene bg portal
        with dissolve

        "The thing leads you to a small portal. The portal looked like your average sized town; buildings, people walking around..."

        scene bg portal2 
        with dissolve

        "And, a floating number..?"

        p "So, you mind explaining what this place is or-"
        
        n "Have fun!"

        scene bg bye

        "You are then kicked down the portal, without any answers."

        scene bg bye2
     
        "As you fall, you can feel the change in atmosphere, the change in nature. 
        You didn’t know why or how, but you could feel that this place wasn’t earth at all. Now you just have to live with these conditions."   

        scene bg bye3

        "And maybe. Just maybe. You’ll get along with the people."

        scene black

        "*Thud*"
  
    label welcome:
        scene bg inworld
        p "Aughhh... My head..."
        scene bg inworld2
        with dissolve
        p "Where the hell am I?"
        "You wake up from your nap of some sort. You’re lying on a bed of leaves and notice that there’s just trees and even more trees. It feels like Earth, but something doesn’t seem off."

        scene bg inworld3
        with dissolve
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
            with dissolve 
            
            "Yep, you were just here. You still see that same flower pile you laid on."
            "Looking further, you see some odd looking, berries. Or at least thats what you think."

            scene bg parkback
            show got berries
            with dissolve
            "You got...Berries?" 
            "You packed it into your bag and moved on."

            jump c1_done

        label c1_yes:
            $ park = False
            jump c1_done

            
        label c1_done:

        scene bg city 
        "You walk over to the city. The first thing you saw was a number, regular humans, a human with a TV as a head, and a giant slime. And of course, you still don't know what's going on?"
            
        "You see a couple of buildings, utility stores, grocery stores, so it must be similar to your own planet you've been in before."

        "And then once you lease expect it, the one number you saw last time, the digits 900, start floating towards you. You can’t really do much, so you go towards him and talk."
        show decent silhouette
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

        "With a sigh, you breathe and go with the flow, having that slight feeling of nausea."

        define n2 = Character("???", color = "#000000")
        n2 "Decent! What are you doing? We were supposed to go right... Now..? Who's the new guy? Or gal?"

        c1"A new town member named [player], he also supposedly fell from 900 feet from the sky."

        p "Why is it that so many people have fallen from that exact same hole I've been in as well?"

        "{i}I guess now I can somewhat confirm this is no longer a coincidence then, huh?{/i}"
        p "Soo... Who's those people?"
        c1"They really didn't, but I'll introduce them I suppose."
        show decent smile talking:
            xoffset -150.00
        with fade    
        $ c1= 'Decent900'
        c1 "Well, my name is Decent900. "
        # This part is when Decent900 introduces characters. Every click introduces one after another, and a character model shows up.
        show alex neutral:
                xoffset 1089.00
        extend "My friend here is named Alex. We are good friends- oh there’s 2 other members." 
        show badguy unaware:
                xoffset 756.00
        extend "Their names are Bad guy "
        show jerry neutral
        extend "and Jerry. "
        show decent neutral
        Alex "Bad Guy is the stick figure, Jerry is the snake."

        p "Nice to meet you Bad Guy, and nice to meet you Jerry. Ya’ll look like you’d be nice people."

        "Bad Guy looked pretty spaced out, guess he looked quite chill."
        "For a stick figure, that is." 
        "And then, it's just a snake. Nothing much he can do, other than bite me or something..?"
        "Lets hope thats not the case."
        "And a... witch. If thats what I had to assume. I'll probably figure it out later."
        show badguy neutral

        BadGuy "... Sup"
            
        show jerry excited
        Jerry "sss... sssss ssss ss ssss ss ssss sss..."
        
        show jerry aware

        p "Poor thing, wish that thing could talk in this cartoon of a world."

        "He seems, friendly, I think? I think it might be worth trying to pet him?"
        menu: 
            "Pet Jerry":
                jump c3_pet
            "Don't pet Jerry, Ignore him":
                jump c3_noPet

        label c3_pet:
            show jerry excited with vpunch
            "You pet jerry and felt some warmness coming off, then last second his tongue hit your hand, you were somewhat calm with him and jerry looked happy."
            c1 "Seems like Jerry got the best of you. Well, who knows, maybe you'll get into good hands one day."
            Jerry "Sssss sss sSSssss ss..!"
            "You still can't tell what he said, but you can tell he appreciate the pat you gave him"
            jump c3_done

        label c3_noPet:
            "You don't pet Jerry. "
            extend "You"
            extend " unkind"
            extend " man."
            "Even Jerry seemed slightly disapointed, but he's a snake, he won't really know."
            jump c3_done
        label c3_done:
            c1 "Well uhh... Nice to meet you, but since you are new, you should probably find a place to stay. Here, go in there and meet the mayors, I'm sure they will be happy to see new people."
        
        c1 "You see that ginormous tree out there? Search 'round there, and you'll find the mayors house."
        c1 "Kay byeeee..."
        "Before you wanted to ask him more questions, the strange number already disapeared."
        "All of the other people also just, left with him somehow. How in the world do people just know how to do that?"
        "{b}Mayors? House?{/b} What in the hell is it talking about? More confusion seeps into your mind as you try to decrypt his message, even though its not even a riddle."
        "After another heavy {i}sigh{/i}, you start walking on the sidewalk, practically guessing where each of your steps would take you."
        
        #test

    return
