"""Enum for creating an Item type."""
from enum import Enum


class Room(Enum):
    """Define values for the Item type."""
    ACCESS_CARD = 'Access Card'
    FIRST_AID_KIT = 'First Aid Kit'
    POWERED_ARMOR = 'Powered Armor'
    SOCKS = 'Socks'
    SONIC_SCREWDRIVER = 'Sonic Screwdriver'
    SPACE_GLUE = 'Space Glue'
    SPACE_SNACKS = 'Space Snacks'
    SPARE_PARTS = 'Spare Parts'
