# (       )     )        (                )                             )
# )\ ) ( /(  ( /( (      )\ )    *   ) ( /(   *   )       )     (    ( /(    )
# (()/( )\()) )\()))\ )  (()/(  ` )  /( )\())` )  /(    ( /(     )\   )\())( /(
# /(_)|(_)\ ((_)\(()/(   /(_))  ( )(_)|(_)\  ( )(_))   )\())  (((_)|((_)\ )(_))
# (_))   ((_) _((_)/(_))_(_))   (_(_())__((_)(_(_())   ((_)\   )\___|_ ((_|(_)
# / __| / _ \| \| (_)) __/ __|  |_   _|\ \/ /|_   _|  | | (_) ((/ __| |/ /|_  )
# \__ \| (_) | .` | | (_ \__ \    | |   >  <   | |    |_  _|   | (__  ' <  / /
# |___/ \___/|_|\_|  \___|___/    |_|  /_/\_\  |_|      |_|     \___|_|\_\/___|

# Author :
# +-+-+-+-+-+-+-+-+-+
# |I|A|m|T|e|r|r|o|r|
# +-+-+-+-+-+-+-+-+-+

# Licence :
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Notes :
# Python script tested on Ubuntu Linux. It can run on Windows with minor adjustements.


########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

# VARIABLES ------------------------------------------------------------------------------------------------------------

pathToScan = ""
songsTxtFileName = "songs.txt"


# FUNCTIONS ------------------------------------------------------------------------------------------------------------

def file_write_from_songs_txt_pattern(a_file_name):
    file.write('song = {')
    file.write('\n')
    file.write('        name = "' + a_file_name + '"')
    file.write('\n\n')
    file.write('        chance = {')
    file.write('\n')
    file.write('                modifier = {')
    file.write('\n')
    file.write('                        factor = 1')
    file.write('\n')
    file.write('                }')
    file.write('\n')
    file.write('        }')
    file.write('\n')
    file.write('}')
    file.write('\n')
    file.write('\n')


# Parsing and displaying of folders, subfolders and descendants of the selectionned folder (path)
def parse_dirs(path):
    nb_files_name = 0  # Debug stuff
    for root, dirs, files in os.walk(path):
        for fileName in files:
            if fileName != "songs.txt":
                nb_files_name += 1
                print("DEBUG - nom du fichier : " + fileName)
                file_write_from_songs_txt_pattern(fileName)
    print("DEBUG - nombre de fichiers ajoutés a songs.txt : " + str(nb_files_name))


# SCRIPT ---------------------------------------------------------------------------------------------------------------

file = open(songsTxtFileName, "w", encoding="utf-8")
parse_dirs(pathToScan)
file.close()
