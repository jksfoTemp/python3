
# del file s  up/down
# chronjob viewer
# rclone setup to keep notes

#################3
# Copy job notes
#
# from dirA
# /home/jku/MyHome/Pers/Work/
#
# to dirB
#  /home/jku/JKSFO.Resume
#
# Please create a python script that copies everything from dirA to dirB, overwriting anything that exists, with error checking.

# python3 SimpleCopyPub2Cloud.py  ~/MyHome/Pers/Work/Supporting/Summaries/ ~/JKSFO.Resume/Work/

# I would think that the line
#   os.remove(backup_file + ".bak")  # Remove older backup
# should be
#   os.remove(backup_file)  # Remove older backup
# and that the corrected version should be called b
#   shutil.copy2(dest_item, backup_file)
#
#

#################3

org notes
clean work folder

#!/bin/bash

# mapJKRGDrive.sh
# Joseph Kelly <josephkelly.resume@gmail.com>
# Sat Jun 1 10:30:11 PM PDT 2024
#
# Source: https://rclone.org/docs/
#
# Mount Google Drive as a local folder, run at login
# Requires RClone installation and configuration
# Will harmlessly error out if already mapped
#
# NOTE CHANGE PATH - SUBSTITUTE USER
#
# Note: for mounting a local drive https://rclone.org/commands/rclone_mount/
#
#     To mount it as a drive:
#         Nope: rclone mount JKRGDrive: /home/user/JKRGDrive/
#     or silent
#         rclone mount --daemon JKRGDrive: /home/user/JKRGDrive/
#     unmount
#         fusermount -u /home/user/JKRGDrive/
#

rclone mount --daemon JKRGDrive: /home/jku/JKRGDrive/
#     unmount
#  fusermount -u /home/jku/JKRGDrive/
