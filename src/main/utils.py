import math



def convert_coordinate(value):
    toReturn = ""
    if value:
        try:
            value = float(value)
            if value and value!=0:
                toReturn = value/((2**32)/360)
        except(ValueError):
            pass
    return toReturn


# Configuration .yaml?
activity_nb = {
    "Randonnée" : 1,    
    "Hike" : 1,
    "Course à pied" : 2,
    "Run" : 2,
    "Ski de randonnée" : 3,
    "Backcountry Ski" : 3,
    "Ski alpin" : 4,
    "Alpine Ski" : 4,
    "Escalade" : 5,
    "Rock Climb": 5,
    "Vélo": 6,
    "Ride" : 6,
    "Marche" : 7,
    "Walk" : 7,
    "Stand Up Paddling" : 8,
    "Rowing" : 9,
    "Virtual Ride" : 10,
    "Ski nordique" : 11,
    "Nordic Ski": 11,
    "Natation" : 12,
    "Swim" : 12,
    "Entraînement" : 13,
    "Workout" :13,
    "Snowshoe": 14,
    "Raquettes" : 14}


description_activity= {
    1 : "Hike",
    2 : "Run",
    3 : "Ski de rando",
    4 : "Ski Alpin",
    5 : "Escalade",
    6 : "Vélo",
    7 : "Walk",
    8 : "Stand Up Paddling",
    9 : "Rowing",
    10 : "Virtual Ride",
    11 : "Ski nordique",
    12 : "Natation",
    13 : "Training",
    14 : "Raquette de ses morts"
}

color_palette = {
    "" : [255, 255, 255],   # WHITE - null
    1 : [129, 38, 192],     # PURPLE - hike
    2 : [42, 75, 215],      # BLUE - run
    3 : [173, 35, 35],      # RED - ski de rando
    4 : [129, 197, 122],    # LIGHT GREEN - ski alpin
    5 : [255, 255, 255],    # WHITE - escalade
    6 : [255, 238, 51],     # YELLOW - vélo
    7 : [160, 160, 160],    # LIGHT GREY - walk
    8 : [255, 146, 51],     # ORANGE - Stand Up Paddling
    9 : [157, 175, 255],    # LIGHT BLUE - rowing
    10 : [255, 146, 51],    # ORANGE - virtual ride
    11 : [41, 208, 208],    # CYAN - ski nordique
    12 : [87, 87, 87],      # DARK GREY - natation
    13 : [129, 74, 25],     # BROWN - training
    14 : [129, 74, 25]      # BROWN - raquette
}