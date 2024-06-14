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

    return