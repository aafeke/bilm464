type_map = {
    0: "No information at all",
    1: "No ADS-B Emitter Category Information",
    2: "Light (< 15500 lbs)",
    3: "Small (15500 to 75000 lbs)",
    4: "Large (75000 to 300000 lbs)",
    5: "High Vortex Large (aircraft such as B-757)",
    6: "Heavy (> 300000 lbs)",
    7: "High Performance (> 5g acceleration and 400 kts)",
    8: "Rotorcraft",
    9: "Glider / sailplane",
    10: "Lighter-than-air",
    11: "Parachutist / Skydiver",
    12: "Ultralight / hang-glider / paraglider",
    13: "Reserved",
    14: "Unmanned Aerial Vehicle",
    15: "Space / Trans-atmospheric vehicle",
    16: "Surface Vehicle – Emergency Vehicle",
    17: "Surface Vehicle – Service Vehicle",
    18: "Point Obstacle (includes tethered balloons)",
    19: "Cluster Obstacle",
    20: "Line Obstacle",
} # Corresponding json field (flight[17]) does seem to be deprecated.

data_source_map = {
    0: "ADS-B",
    1: "ASTERIX",
    2: "MLAT",
    3: "FLARM"
}