################################################################################
## Character images
################################################################################

image zackc = "zack/zack.png"
image zackc talk = "zack/zack-talk.png"
image zackc happy  = "zack/zack-happy.png"
image zackc happy talk = "zack/zack-happy-talk.png"
image zackc puzzled = "zack/zack-puzzled.png"
image zackc puzzled talk = "zack/zack-puzzled-talk.png"
image bobc = "bob-casey.png"
image bg livingroom = "livingroom-bg.png"

################################################################################
## Character definitions
################################################################################

define unknown = Character("Unknown")
define zackc = Character("Zack Casey")
define bobc = Character("Bob Casey")
define johng = Character("John Grenon")
define kitw = Character("Kit Welsh")
define crashm = Character("Crash McCloud")
define ruf75 = Character("RUF 751")

################################################################################
## Inventory
################################################################################

init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of the inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name):
            self.name=name
    # player = Player("Derp")
    
    class Item(store.object):
        def __init__(self, name, player=None, image="", cost=0):
            self.name = name
            self.player=player # which character can use this item?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element=self.element #item to change elemental damage; we don't drop it, since it's not a consumable item

    class Inventory(store.object):
        def __init__(self, money):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = True #turn True to debug the inventory
    # def display_items_overlay():
        # if showitems:
            # inventory_show = "Money:" + str(inventory.money) + " HP: " + str(player.hp) + " bullets: " + str(player.mp) + " element: " + str(player.element) + "\nInventory: "
            # for i in range(0, len(inventory.items)):
                # item_name = inventory.items[i].name
                # if i > 0:
                    # inventory_show += ", "
                # inventory_show += item_name
            
            # ui.frame()
            # ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)