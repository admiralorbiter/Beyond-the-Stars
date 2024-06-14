define elle = Character('Elle', color="#c8c8c8", image="sally")
image side sally = "sally.png"

define harper = Character('Harper', color="#c8c8c8", image="harper")
image side harper = "harper.jpg"

define ant = Character('Ant', color="#c8c8c8", image="sally")
# image side ant = "ant.png"

define kody = Character('Kody', color="#c8c8c8", image="kody")
image side kody = "kody.jpg"

image camp = "camp.png"
image spooky forest = "forest-spooky.jpg"
image forest walking = "forest-walking.jpg"
image new camp = "camp-new.jpg"
image cult = "cult-in-forest.jpg"

label start:

    scene camp:
        zoom 1.5

    harper "You gotta try these s'mores, Elle. They're amazing!"
    elle "We just opened the hot dogs?!"
    elle "Why are you eating dessert?"
    kody "You are going to ruin your dinner.."
    harper "This IS dinner!"
    ant "I'll take one!"
    elle "Fine, just make sure you save enough for the rest of us."
    elle "You know why they are called smores?"

    scene spooky forest:
        zoom 1.5

    kody "What...what..was that?"
    harper "An owl maybe? Or a bear!"
    ant "Or a ghost!"
    elle "There are no bears in this forest."
    kody "What about ghost?"
    harper "Lets check it out"
    ant "You want to go out there?"
    harper "I came to get some pictures, maybe we will see something cool."

    menu:
        "Go with Harper":
            jump exploring
        "Stay here":
            jump new_camp
    return

label exploring:
    scene forest walking:
        zoom 1.5

    harper "Doubtful we will even find this bear."
    harper "At least it's a nice walk in nature."
    elle "We can just call you Thoreau."
    harper "What?"
    kody "Figures. You never pay attention in English"
    ant "Ms. Kluthe would be so disappointed."
    kody "What was that?"
    harper "You all saw that right?"
    elle "Like the light..changed?"
    ant "Light doesn't just change like that."
    elle "Maybe a cloud is blocking the moon?"
    elle "Hard to tell with all these trees."
    harper "It doesn't feel darker...just redder."

    scene cult:
        zoom 1.5

    elle "Shhh. I hear something up ahead."
    kody "IS that antlers?"
    ant "It has to be branches or something."
    elle "We should go back.."
    harper "Shh..."
    # Culitst walks out
    harper "Oh my god.."
    harper "Lets go."
    jump new_camp
    return

label new_camp:
    scene new camp:
        zoom 1.5
    kody "What did we just see?"
    ant "Probably just two guys in the woods."
    elle "With antlers?"
    ant "They were far away, it could have been branches or hats."
    harper "Is this our camp?"
    elle "Wait, where is our car? The path?"
    kody "My bag is here. It has to be our camp."
    elle "But where is the car? The road!"
    kody "I'm starting to freak out."
    kody "Do you think it was the same guys?"
    ant "They couldn't have taken our car."
    elle "They could have moved our stuff, maybe our camp is down this path."
    harper "I don't know if we should go down there."
    harper "But we need to find our car."
    
    return