"""

Saturday, May 10th, 2025 

Source: cpJKSFO.R.4.py 

Updating old files copied to new drive, synching everything 

SourceTest: /home/jk/Documents/WorkTest/
DestTest: /home/jk/JKSFO.Resume/WorkTest/  

Source: /home/jk/Documents/Work/
Dest: /home/jk/JKSFO.Resume/Work/  

cd ~/dev-git/jksfoTemp/python3/myGDSynch/cronjobs$ 
# chmod +x cpJKSFO.R.5.py

# Testing
# /usr/bin/python3 
#   /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/WorkTEST/ ~/home/jk/JKSFO.Resume/WorkTest/
  
# Deploy to cronjob
# /usr/bin/python3 
#   /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/Work/ ~/home/jk/JKSFO.Resume/Work/
  
Old notes: 
  Fight this another day. There is some kind of issue copying over the files to 
  the RClone stage, was working earlier. It should do some kind of diff on date 
  anyway and not recopy the file every iteration; I may have exceeded some data 
  threshold with GDrive. I should also look into how to disable the RClone synch
  but as I am on a time schedule I didn't want have to reconfig rclone as well (
  but there are directions as for how to do that in Keep). 

  Still need to set up the cronjob but get it right first. 
  
"""

import shutil
import os
import sys
import datetime
import logging

def copy_dir(src, dest, verbose):
  """Copies the contents of the source directory to the destination directory, overwriting existing files.
  Args:
    src: The source directory path.
    dest: The destination directory path.
  Usage:
    test:
      /usr/bin/python3 /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/WorkTEST/ ~/home/jk/JKSFO.Resume/WorkTEST/ 1
    release:
      # /usr/bin/python3 /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/Work/ ~/home/jk/JKSFO.Resume/Work/ 0
  cronjob:
    test:
      10 * * * * <cmd> 1
    release:
      10 * * * * <cmd> 0

  I think where I left off I was going to implement an array diff type of tool 
  that did name, size and date diffs to determine if it would actually be copied 
  over, save I/O and bandwidth 

  """
  try:
    # Create the destination directory if it doesn't exist
    if not os.path.isdir(dest):
      os.makedirs(dest, exist_ok=True)
      print(f"Dir created: {dest}")
      logger.info(f"Dir created: {dest}")
    else:
      print(f"Dir exists: {dest}")
      logger.info(f"Dir exists: {dest}")

    # Copy files and directories recursively
    for item in os.listdir(src):
      src_item = os.path.join(src, item)
      dest_item = os.path.join(dest, item)
      if os.path.isdir(src_item):
        if verbose == "1":
          print(f"Recursion: " + src_item)
          logger.info(f"Recursion: " + src_item)
        copy_dir(src_item, dest_item, verbose)
      else: # It is a file, get to work
        if os.path.exists(dest_item):
          backup_file = dest_item + ".bak"
          if verbose == "1":
            print(f"File exists, creating backup: " + backup_file)
            logger.info(f"File exists, creating backup: " + backup_file)
          try:
            if os.path.exists(backup_file):
              os.remove(backup_file)
              shutil.copy2(dest_item, backup_file)
              shutil.copy2(src_item, dest_item)
              if verbose == "1":
                print(f"Created backup for {dest_item}")
                logger.info(f"Created backup for {dest_item}")
          except OSError as e:
            print(f"Error creating backup for {dest_item}: {e}")
            logger.info(f"Error creating backup for {dest_item}: {e}")
          except Exception as e:
            print(f"Unexpected error: {e}")
            logger.exception("Unexpected error:")
        else: 
          try:
            shutil.copy2(src_item, dest_item)
          except OSError as e:
            print(f"Error creating backup for {dest_item}: {e}")
            logger.info(f"Error creating backup for {dest_item}: {e}")
          except Exception as e:
            print(f"Unexpected error: {e}")
            logger.exception("Unexpected error:")
        if verbose == "1":
          print(f"Copied {src_item} to {dest_item}")
          logger.info(f"Copied {src_item} to {dest_item}")
  except OSError as e:
    print(f"Error copying files: {e}")
    logger.error(f"Error copying files: {e}")
  except Exception as e:
    print(f"Unexpected error: {e}")
    logger.exception("Unexpected error:")

if __name__ == "__main__":
  logger = logging.getLogger(__name__)

  script_dir = os.path.dirname(os.path.abspath(__file__))
  log_file = os.path.join(script_dir, 'WorkDirBAKs.log')
  logging.basicConfig(filename=log_file, level=logging.INFO, 
    format='%(asctime)s %(levelname)s: %(message)s')

  if len(sys.argv) != 4:
    print("Begin - Error - Usage: python cpJKSFO.R.5.py " + script_dir + "\n Were there 3 args passed? Source, Destination, Verbose (0|1)")
    logger.info("Begin - Error - Usage: python cpJKSFO.R.5.py " + script_dir)
    logger.info("\nWere there 3 args passed? ")
    logger.info("\n\targv1: |" + sys.argv[1] + "| ")
    logger.info("\n\targv2: |" + sys.argv[2] + "| ")
    logger.info("\n\targv3: |" + sys.argv[3] + "| ")
    sys.exit(1)

  src_dir = sys.argv[1]
  dest_dir = sys.argv[2]
  verboseYN = sys.argv[3]

  now = datetime.datetime.now()
  print(now.strftime("\nBegin: %H:%M:%S"))
  logger.info(now.strftime("\nBegin: %H:%M:%S"))

  copy_dir(src_dir, dest_dir, verboseYN)

  now = datetime.datetime.now()
  print(now.strftime("End: %H:%M:%S" + "\n"))
  logger.info(now.strftime("\nEnd: %H:%M:%S" + "\n"))
