#!/usr/bin/bash

# mapJKRGDrive.sh
# Joseph Kelly <josephkelly.resume@gmail.com>
# Sat Jun 11 10:30:11 PM PDT 2024
#

# Testing for use of resource directory

echo "foose is geesiest"

# So we want to upen up the file superSecret.res
# which is 2 directories up and one down in res
# .sandbox/bash/driveMap/testRes.sh
# .sandbox/res/superSecret.res
#
# The idea is to use this in mapJKRGDrive.sh (as an import) to get the name of
# the user's # home directory for mapping the drive on login or remapping the
# drive
#
# Once the file is mapped the copy script, which would be a cronjob (can be run
# manually), should

# Test that the drive is mapped
# Run the copy operation for the current directory
#   Start traversing the directories
#   Existence first
#   Name
#   Timestamp
#   Directory existence
#   BAK dupe file .JKBAK
#   Other






# fil = sandbox/res/superSecret.res
filPath = r"../../res/superSecret.res"
with open(filPath, "r") as file1
  print(file1.read())

  file1.close



# ksdfl
