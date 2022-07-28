# Import player data from swgohhelp
print("Getting player game data...")
from liveapi import gpd
gpd()

# # Create DB tables
# import os
# if os.path.exists("cfa.db"):
#   os.remove("cfa.db")

# f = open('cfa.db', 'w')
# f.close

# from create_player import create_player
# create_player()

# from create_toons import create_toons
# create_toons()

# from create_skills import create_skills
# create_skills()

# from create_gear import create_gear
# create_gear()

# from create_mods import create_mods
# create_mods()

# from create_mod_stats import create_mod_stats
# create_mod_stats()
