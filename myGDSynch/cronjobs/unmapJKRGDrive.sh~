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
