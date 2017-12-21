# The script of the game goes in this file.

# The game starts here.

label start:
    
    scene bg livingroom
    
    bobc "Happy birthday!"
    
    "November 14th. My birthday. I just turned 18 years old today."
    
    "I got various sorts of gifts as well as a new phone, console games, and a gift card."
    
    python:
        user = Player("Zack Casey")
        inventory = Inventory(money=50)
        trucksimitem = Item("Truck simulator", image="gui/inv_trucksim.png", cost=10)
    
    show zackc happy talk

    zackc "Thank you! Thank you! Thank you!"
    
    show zackc puzzled at left
    
    show bobc at right
    
    bobc "Don't get what's on your list."
    
    show zackc puzzled talk
    
    zackc "Okay."
    
    show zackc puzzled
    
    bobc "Now go upstairs, and have fun."
    
    hide bobc
    hide zackc
    
    # scene bg zacksroom
    
    "Later John Grenon stopped by while I was setting up my console games."
    "He is still a pissed at me for using his underwear as a flag on 4th of July."
    
    show zackc at left
    
    johng "So what are you going to get with your money?"
    
    show zackc talk
    
    zackc "Dad told to not get anything on the list."
    
    show zackc
    
    johng "Do you remember what was on it?"
    
    show zackc talk
    
    zackc "Only stuff my family could have purchased online with their existing Atlantic accounts."
    zackc "But! They're are a few things I've wanted on Piston."
    
    show zackc
    
    johng "Yeah?"
    
    show zackc talk
    
    zackc "Tom has been playing this truck simulator game. Looks cool."
    
    show zackc
    
    johng "You? Trucks? Is this the same Zack Casey I met primary school?"
    
    show zackc talk
    
    zackc "What? Trains can be restricting at times."
    
    show zackc
    
menu:
    
    "Buy truck simulator":
        jump trucksim
        
    "Skip":
        jump question
    
label trucksim:
    
    # show bg pistonstore
    
    hide johng
    hide zackc
    
    zackc "Luckily Piston is having one of their sales."
    
    johng "When don't have they have sales?"
    
    zackc "Good point."
    
menu:
    
    "Purchase game":
        zackc "Done!"
        $inventory.buy(trucksimitem)
        
    "Maybe later":
        zackc "I'll get a little later."
        johng "How long does it have?"
        zackc "Two days."
        jump question
    
label question:
    
    johng "Question."
    
    zackc "Shoot."
    
    johng "Have you ever stole something before?"
    
    zackc "Hmm..."
    zackc "There was that one time I forgot to ask dad to purcahse some bubble gum I had in my pocket."
    
    johng "What happended!?"
    
    zackc "The censors went off but the guard took it as a false alarm."
    
    johng "Did you do it again?"
    
    zackc "What?! No! I didn't mean do it in the first place. I'd be rather pay for my own goods."
    
    johng "Huh..."
    
    zackc "Anyway! Truck simulator is done."
    
    johng "... Okay."
    
    return
