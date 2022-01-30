"""Enum for creating a Room type."""
from enum import Enum


class Room(Enum):
    """Define values for the Room type."""
    AIRLOCK = 'Airlock'
    ARMORY = 'Armory'
    BRIDGE = 'Bridge'
    CARGO_BAY = 'Cargo Bay'
    COMMON_AREA = 'Common Area'
    CREW_QUARTERS = 'Crew Quarters'
    ENGINEERING = 'Engineering'
    GALLEY = 'Galley'
    MEDICAL_BAY = 'Medical Bay'
    SCIENCE_LAB = 'Science Lab'
