################################################################################
## Episode 1: New Home
## This script will be refined the more I study Ren'Py.
## For now this is as basic as basic gets
################################################################################

label newhome:

    # show bg station

    "I had just arrived at Zoo Heights."
    "It was nothing like the small town I had come from."
    "Mice roamed the station as elephants towered in and out."
    "I was waiting for a friend of mine who I'd be staying with."

    # show crashm smile at left

    unknown "There you are Kit."

    # show kitw talk at right

    kitw "Hey, Crash!"

    # show crashm talk

    crashm "So what do you think?"
    kitw "Busy."

    # hide crashm
    # hide kitw

    # show bg crashm livingroom

    crashm "Bedrooms are upstairs, and you'll find a bathroom on either floor."
    kitw "Thanks. Went before I got off. All the sleeper compartments had restrooms."
    crashm "More time for us."
    kitw "Yup!"

    # show bg crashm guestroom
    
    "I went upstairs. Unpacked. Got out a few goodies for the night."
    "I was't sure how long I was staying."

    crashm "You can rent this room if you'd like."

    "My ears perked at the sound of the sudden offer."

    kitw "Really?"
    crashm "Of course."

    "It was tempting. I had no where else to live. I figured I'd stay in a hotel."
    "Crash and I go back a pretty long ways away. I knew he'd understand if I declined ..."
    "... least I hoped ..."
    "... yet I didn't want to decline. Living with a friend is far better then any ol' hotel."

    kitw "So what's the price?"

    # show bg crashm livingroom

    crashm "You talked to me about this for a long time, but you never told me why you came to Zoo Heights."
    "It was at this moment that I wish I had to use the restroom."

    menu:
        crashm "Kit?"
        "Explain":
            jump explain
        "Don't explain":
            $ kitsreason = True
            jump sorry
               
label explain:

    kitw "I wanted to get away from my family."
    crashm "How come?"
    kitw "They're rich, powerful snobs,"
    kitw "and here I am being forced to live up to their high standards"
    kitw "in order to please them."
    crashm "And?"
    kitw "I didn't want to! I felt like I was living a lie. So I left."
    kitw "I wanted to be with someone tha-"

    # hide crashm
    # hide kitw
    # show crashkithug

    "At that moment, Crash hugged me."
    "I can't remember the last time I was hugged."
    
    jump start

label sorry:

    show screen notify("Kit's Reason")
    
    kitw "I'm sorry, Crash."
    "Crash stared into my eyes as I held in my tears,"
    "and gave me a pat on the back."
    crashm "I'm here for you."

    jump start