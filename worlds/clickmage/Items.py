# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items, they need to be bundled in a list

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .Types import ItemData, ClickMageItem
from . import Options
from typing import TYPE_CHECKING

# This is just making sure nothing gets confused about what its doing exactly
if TYPE_CHECKING:
    from . import ClickMageWorld

# If you're curious about the -> list[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself
def create_itempool(world: "ClickMageWorld") -> list[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    itempool: list[Item] = []

    # In this function is where you would remove any starting items that you add in options such as starting chapter
    # This is also the place you would add dynamic amounts of items from options
    # This is also a good place to grab anything you need from options

    

    return itempool

# This is a generic function to create a singular item
def create_item(world: "ClickMageWorld", name: str) -> Item:
    data = item_table[name]
    return ClickMageItem(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
def create_multiple_items(world: "ClickMageWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> list[Item]:
    
    return [ClickMageItem(name, item_type, item_table[name].ap_code, world.player) for _ in range(count)]

# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers, but DO NOT USE 0. This is reserved for AP stuff
# I've seen some games that dynamically add item codes such as DOOM as well

item_table = {}




