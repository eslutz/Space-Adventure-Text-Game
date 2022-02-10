"""Space Adventure Text Based Game"""
from enum import Enum


class Action(Enum):
    """Define values for the Action type."""
    GET = 'get'
    GO = 'go'


class Direction(Enum):
    """Define values for the Direction type."""
    EAST = 'East'
    NORTH = 'North'
    SOUTH = 'South'
    WEST = 'West'


class Item(Enum):
    """Define values for the Item type."""
    ACCESS_CARD = 'Access Card'
    FIRST_AID_KIT = 'First Aid Kit'
    FLUX_CAPACITOR = 'Flux Capacitor'
    POWERED_ARMOR = 'Powered Armor'
    SOCKS = 'Socks'
    SONIC_SCREWDRIVER = 'Sonic Screwdriver'
    SPACE_GLUE = 'Space Glue'
    SPACE_SNACKS = 'Space Snacks'
    SPARE_PARTS = 'Spare Parts'
