################################################################################
## The episode window
################################################################################

# This is used to preserve the state of the scrollbar on the selection
# screen.
default episodes_adjustment = ui.adjustment()

label start:

    # Shows the episode screen
    call screen episodes(adj=episodes_adjustment)

    $ episode = _return

    # Jumps to episode
    call expression episode.label from _call_expression
    
    return
