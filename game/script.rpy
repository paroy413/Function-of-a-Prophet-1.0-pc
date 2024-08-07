# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rhys", who_color="#19A7CE", what_color="#ACF3FD")
define c = Character("Cassandra", who_color="#900C3F", what_color="#FFCCCC", what_font="Neucha-Regular.ttf")
define narrator = Character(what_italic=True)

# The game starts here.

label start:

    play music "The Universe Blinks (Original Mix).mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rhys-closed-eyes

    # These display lines of dialogue.

    narrator "It sucks being the hero. Especially when you didn't ask for it. I would know. Cass would beg to disagree, though. Then again, she's not the one seeing her bones after a fight."

    hide rhys-closed-eyes

    show cass-offended

    c "You act like I'm not with you literally every step of the way."

    hide cass-offended

    show rhys-annoyed

    r "That's because you're not."

    scene bg-inn-bedroom
    with fade

    menu:

        narrator "I didn't really have a choice in it, to be fair. I can't really blame Cass. l'd say all I can choose is what I have for breakfast, but it feels like fate decides that, too, some days."

        "Have sunflower seeds." :

            jump sunflowerseeds

        "Have nothing." :

            jump nothing

label sunflowerseeds:

    scene bg-inn-bedroom
    with fade

    show rhys-closed-eyes

    narrator "I grabbed my rucksack, took out the pouch of seeds by feel, and shoveled a handful into my mouth. It wasn't much, but at least I wouldn't be facing the world on empty. As soon as I finished the handful, I yawned."

    c "You yawn like a grandpa and look like a raccoon."

    show rhys-annoyed

    r "No thanks to you. You don't let me get any well-rested sleep."

    c "That's a lie; my being awake when you're asleep should not affect a thing."

    show rhys-annoyed

    r "It does. Because you're still using my body. I wake up tired no matter how much sleep I've gotten."

    c "... I'm sorry, Rhys."

    r "It's fine."

    show rhys-closed-eyes-blush

    narrator "It wasn't fine. But it's not like I had a choice in the matter. Choices were a luxury."

    c "Speaking of choices, what do you want to do today?"

    show rhys-upset

    "I laughed out loud to the empty room. {i}Really?{/i} She had the audacity to ask me? Did I want to risk any number of injuries? No. Only made that mistake once."

    c "I still remember all the hands on you, trying to scratch, or get a piece of clothing, or hair, or a limb. It’s a wonder we’re alive."

    show rhys-neutral

    r "No, just me."

    c "Rhys—"

    r "I’m saying you put me in a lot of danger. It’s not personal. If you take it that way, that’s on you."

    narrator "She went silent after that."

    narrator "I paused, took a deep breath in. I wasn't sure if I could get more sleep, or if I'd feel compelled towards some grand quest. Maybe something to do with the Eternal Flame."

    c "Why would I want anything to do with that glorified inferno chicken?" 

    show rhys-smug

    r "I don't know; fate works in mysterious ways, or some bullshit like that?" 

    show rhys-playful
    
    narrator "I held back a snort of laughter at my own ironic joke."

    c "Are you saying I'm not mysterious?"

    show rhys-annoyed

    narrator "Oh, great. Now the all-powerful diety was pouting."

    narrator "I rolled my eyes. As if on cue, the gold strand in my hair lit up, as Cass telepathically punched me in the shoulder. It didn't hurt."

    c "Go back to sleep, dork."

    show rhys-annoyed

    r "Since when do I take orders from you?"

    c "You need the sleep."

    show rhys-embarrassed

    narrator "She had a point. As much I loathed to admit it, she had a point."

    menu:

        "Go back to bed." :

            jump sleep

        "Don't." :

            jump stayawake

    label sleep:

            narrator "I decided to go back to bed. May as well get whatever rest I could while the world wasn't ending for once. It loved to do that, as if to spite me. I didn't want to tempt Fate anymore than necessary. She was a cruel bitch. For once, I didn't dream."

            scene black
            with dissolve

            "{b}Neutral Ending{/b}."

            return

    label stayawake:

        show rhys-annoyed

        narrator "Even if she had a point, I was too wide awake now. Better to be prepared while I had the time. Not like I could really prepare for the inevitable."

        r "Hey, Cass?"

        c "Yeah?"

        r "We just… see what happens?"

        c "Yeah."

        narrator "I kept my gaze carefully trained on the dirty ceiling. How {i}did{/i} ceilings get dirty, anyway? ...Shit. Definitely wide awake."

        show rhys-upset

        r "Am I gonna know when all of this is finally over?"

        c "I told you: Time and space and dreams don't mix. Someone can dream an entire lifetime, wake up, and find only an hour or two has passed. That actually happened to a man, once. He still grieves his imaginary wife and child."

        r "So, you're saying that life has already happened, and we just haven't experienced it yet?"

        c "Essentially."

        show rhys-closed-eyes

        "I closed my eyes, trying to block out the light from outside. Just for once in my goddamn life, I wanted some sort of agency, or at least the ignorance of not knowing the future. Hope. Something like that. Something to look forward to."

        c "It's not a bad thing."

        show rhys-upset

        narrator "{i}Right.{/i} She wasn't the one dealing with the burdens."

        show rhys-annoyed

        r "Speak for yourself."

        c "Look, just because events are predetermined doesn't mean you don't have free will. The story will play out, {i}and{/i} you get to decide what you do in it."

        r "Within the confines of the narrative."

        show rhys-closed-eyes

        narrator "She went silent again. But, this time, it was a more contemplative silence, as if my words had actual meaning. Did they? Did that matter?"

    menu:

        "Yes." :

            jump yes

        "No." :

            jump no

    label yes:

    show rhys-closed-eyes-blush

    narrator "It mattered as much as the relief on people's faces when I told them everything would be fine."

    narrator "It mattered as much as the happiness on the little girl's face when I gave her some food because I knew if I didn't, she'd succumb to malnutrition that very night." 
    
    narrator "Caring about people mattered, because the world was already shitty. But I knew I wasn't a hero, not really. I was just an average guy, who happened to have a gold streak in his hair and the uncanny ability to dream visions."

    c "You're not average in the slightest."

    show rhys-upset

    narrator "My eyes shot open. Leave it to her to ruin what little peace I've got."

    show rhys-annoyed

    r "Yeah, I am."

    c "Don't argue with me, or I will smite you where you lay. Have faith."

    show rhys-upset

    r "{i}Have faith{/i}, says the literal goddess. You are a hypocrite."

    c "And you consider yourself a heathen. You're more like a hermit."

    r "Aimless, disdainful of others, and unable to be a part of society?"

    c "Willing to take things as they come, appreciative of the smallest blessings because you see them for what they are, and persistent in how you handle difficulty."

    show rhys-embarrassed

    narrator "Now I was the silent one. I didn't know how to feel about that. I wasn't a hero. I was certain about that, at least."

    c "Are you going to keep lying in bed, or are we going to go outside?"

    show rhys-annoyed

    r "I already ate the sun; you want me to feel it, too?"

    c "Sure, if that's how you want to take it. You need {i}some{/i} light in your life, yaknow."

    show rhys-upset

    r "Because fresh air and sunlight will solve all of my problems."

    narrator "I wasn't going to keep the sarcasm out of my voice. But Cass wasn't having it; she was trying to shove me out of bed. I blew a raspberry at the ceiling, which earned me a supernatural shove. Onto the cold, wooden, bedroom floor. I let out a groan of pain."

    show rhys-haughty

    r "I'm not taking it back!"

    show rhys-embarrassed

    narrator "No answer. I wasn't. She was going to give me the silent treatment? Don't care. I let out a sigh, eyes drifting from the ceiling to the door. {i}Have faith.{/i} Fine. Whatever."

    show rhys-haughty-blush

    narrator "I picked myself up off the floor, arms and legs, and headed to the door. Flung it open. She was right about one thing, I was too backwards to die out."
 
    "{b}Good Ending{/b}."

    return

    label no:

        show rhys-closed-eyes

        narrator "I didn't think it did. Because every decision was already a possibility. The only variance is what happened where, not if it happened at all. I could spend every second detailing every second and it wouldn't change a thing."
        
        narrator "I didn't know why I bothered with helping people. I didn't have anything to prove. And it wasn't because I was a good person, hell no. So, why? Why did I try if it--"

        c "Because -- deep down -- it matters to {i}you.{/i}"

        narrator "I didn't know what to say to that. Instead, I let out a groan of irration. I'd try to get some sleep, after all. Anything to get Big Sister to stop watching."

        c "Love you, too."

    "{b}Neutral Ending{/b}."

    return

label nothing:

    scene bg-inn-bedroom
    with fade

    show rhys-neutral

    narrator "Not going to eat anything. It wouldn't make sense; it's not like I ever feel full anyway. Far too full of nihilism and the awareness of Fate to take anything in. Instead, I stretch my arms above my head, letting out a groan at the sudden sun in my eyes. No way it was that fucking bright."

    c "Yes, way."

    show rhys-upset

    r "Fuck off."

    c "Can't really do that, unfortunately."

    show rhys-upset

    r "I swear to the rest of the pantheon: when I get up there, I am kicking your ass."

    c "Try me. I'd like to see it, little brother."

    narrator "I flipped off the sky and then rolled out of bed. More like {i}fell{/i}, because my body felt so heavy. Not as heavy as having Fate in my head. Not near as heavy as the annoyance of having Cass in my head. She was privy to everything. Talk about a nosy sister."

    narrator "Mine just happened to be a goddess of luck."

    show rhys-upset-hood

    narrator "My stomach rumbled. Channeling a mouthy goddess took serious energy. I paid it no mind, instead getting dressed to go out. Hood up, as always. Otherwise, I'd eat shit. No different from usual, but I didn't want to tempt Fate anymore than necessary. She was a cruel bitch."

    "{b}Bad Ending{/b}."

    # This ends the game.

    return
