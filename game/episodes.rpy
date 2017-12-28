################################################################################
## Episodes
################################################################################
## This is based off of the Ren'Py tutorial; 
## however, it's considered a bad example of
## the Ren'Py programming style, and 
## should be improved.
################################################################################

init python:

    # A list of section and episode objects.
    episodes = [ ]

    class Section(object):
        """
        Represents a section of the episode menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            episodes.append(self)


    class Episode(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "episode"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            episodes.append(self)


    Section(_("Episodes"))

    Episode("newhome", _("New Home"))