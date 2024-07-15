define firstInteraction = True
label telly_interraction:
    scene bg telly home
    #This is an example, not finalized.
    "You head over to a strange home."
    "Looks quite identical to most other homes out there, but except, you can hear pretty loud music coming from the inside?"
    "Disregarding all that else, let's see whoever this man or woman will be willing to offer?"
    "{i}Knock knock...{/i}"
    "..."
    n "Oh? Uhhh... Hello there, are you gonna make a noise complaint?"
    p "No, I'm just here to ask around. Wanted to meet some new people."
    show telly greeting
    with characterDissolve
    Telly "Oh, well, hey there new guy. I've never seen someone like you. Forgive my manners, my name's Telly."
    show telly neutral
    with characterDissolve
    Telly "I’m a DJ if you couldn’t tell by my music playing."
    show telly happy
    with characterDissolve
    Telly "And yes, it does get loud inside, but well, it's nice meeting you there, new guy."

    menu tellyInteractions1: 
        "Help me with some rent?":
            jump tellyRent
        "Who are you again?":
            jump tellyWho
        "How's life in there?":
            jump tellyLife

    label tellyWho:
        show telly happy
        with characterDissolve
        Telly "Whew, you already getting some hearing damage just from my music or something?"
        Telly "Nah, it's alright. I'm playing with you."
        show telly neutral
        with characterDissolve
        Telly "Well, my life is revolved around being a plain old DJ."
        Telly "I can't say I don't enjoy it at all, being around music and lively people enjoy'in the time is what brings me alive."
        Telly "Can't really say much else, and you seem like a curious fellow as well."
        show telly question
        with characterDissolve
        Telly "Anything else?"
        jump tellyInteractions1

    label tellyLife:
        show telly happy
        with characterDissolve
        Telly "Well, there isn't much I can say about life, I suppose."
        Telly "Just a constant cycle of makin' music, playing with my guitar, hanging out in clubs..."
        show telly neutral
        with characterDissolve
        Telly "I'd say it is a pretty nice time to be in."
        show telly happy
        with characterDissolve
        Telly "...Maybe except for rent now that I think of it..!"
        show telly question
        with characterDissolve
        Telly "Anything else?"

        jump tellyInteractions1

    label tellyRent:
        show telly happy
        with characterDissolve
        Telly "Well, about that, I suppose  I'm under that same boat of yours as well."
        show telly neutral
        with characterDissolve
        Telly "...Hmmmm"
        show telly neutral
        with characterDissolve
        "She stands there and thinks to herself."
        "You can't help but have noticed the T.V. around her head. Definitely not your normal kind of person out there."
        "Maybe she's got her own face to hide or something, unless the TV is meant to be just a sensitive kind of info."
        "Curious, but best not ask about it for now..."
        show telly happy
        with characterDissolve
        Telly "Alright, come on in, I think you should be a bit accustomed to what my home looks like, because I do have a bit of things that I do want you do to."
        scene bg telly home inside
        with fade
        "You come inside."
        "It's, really nice looking, with all kinds of cyan and blue colors coating the entire room."
        "Very cozy like, you'd have to admit, with some musical instruments, a beanbag, and an overall well looking living room."
        
        show telly neutral with characterDissolve
        Telly "Alright, well, before I give you a share of some of the rent I did manage to pull from a small job I do..."
        Telly "How about some questions, hm?"

        Telly "Lets see... Do you like music?"
        menu: 
            "Yes":
                $ music = True
                show telly happy with characterDissolves
                Telly "Hey, at least one thing we both can agree on. It's a classic thing to love in this world anyways!"

            "No":
                $ music = False
                show telly disappointed with characterDissolve
                Telly "Oof, and  I really though that you would be someone that did enjoy music."
                show telly neutral with characterDissolve
                Telly "Guess everyone has different tastes."
                jump tellyInteractionDone
        
        if music:
            Telly "Well, what do you enjoy listening to?"
            menu: 
                "EDM":
                    show telly happy with characterDissolve
                    Telly "OH! I love EDM, I like the sounds that get played."
                    Telly "Glitch hop is also a neat choice I like listening to, but well hey, at least you like EDM too, y'know"
                    "{i}You gained a heart!{/i}"
                "Rock":
                    Telly "Hmmm, you got some interesting taste."
                    Telly "I'm more of a glitch pop or EDM genre kind of gal."
                    show telly question with characterDissolve
                    Telly "But well hey, I'm still open to your suggestions and what you'd like. No hate."
                    "{i}You gained half a heart!{/i}"
                "Lofi": 
                    Telly "Hmmm, you got some interesting taste."
                    Telly "I'm more of a glitch pop or EDM genre kind of gal."
                    show telly question with characterDissolve
                    Telly "But well hey, I'm still open to your suggestions and what you'd like. No hate."
                    "{i}You gained half a heart!{/i}"
                "Glitch Pop":
                    show telly happy with characterDissolve
                    Telly "OH! I love glitch pop. I like the sounds of the computer-ish noises it makes. "
                    Telly "EDM is also a neat choice I like listening to, but well hey, at least you like glitch pop too."
                    "{i}You gained a heart!{/i}"
                "Country": 
                    Telly "...Well you're a first time for me. That's quite surprising."
                    Telly "I'm more of a glitch pop or EDM genre kind of gal."
                    show telly question with characterDissolve
                    Telly "But well hey, I'm still open to your suggestions and what you'd like. No hate."
            #Will add job into this soon, but interaction should still be worked on first.
        label tellyInteractionDone:
            Telly "..."
            show telly greeting with characterDissolve
            Telly "Oh well, thanks for coming in."
        $ firstInteraction = False

        while False:
            Telly "Welcome back, whats up?"        
        jump atHome