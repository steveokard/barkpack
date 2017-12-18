# The script of the game goes in this file.

image zack = "zack.png"
image zack talk = "zack-talk.png"
image zack smile = "zack-smile.png"
image dad = "zacks_dad.png"
image bg livingroom = "livingroom-bg.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define zc = Character("Zack Casey")
define zcdad = Character("Zack's Dad")


# The game starts here.

label start:
    
    scene bg livingroom

    show zack talk at left

    zc "You've created a new Ren'Py game."

    zc "Once you add a story, pictures, and music, you can release it to the world!"
    
    show zack
    
    show dad at right
    
    zcdad "Are you we in Ren'Py, son?"
    
    show zack smile
    
    zc "Umm.... Yes."
    
    zc "It's new. And different."
    
    show zack talk
    
    zc "But I wish we would move away from Flash."
    

    return
