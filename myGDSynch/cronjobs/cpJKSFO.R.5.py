"""
Saturday, May 10th, 2025 
Source: cpJKSFO.R.4.py 
Updating old files copied to new drive, synching everything 
For new file set exec permissions: cd ~/dev-git/jksfoTemp/python3/myGDSynch/cronjobs$   # chmod +x cpJKSFO.R.5.py

TODO:   
  Add comments, refactor for simplicity
  Implement date/time testing to prevent excessive copying
  Still need to set up the cronjob but get it right first. 
"""

import shutil
import os
import sys
import filecmp
import datetime
import logging


def filesAreSame(scrFile, destFile, info):
  try:
    sameFile = filecmp.cmp(scrFile, destFile, shallow=True)
    if (info):
      print(f"File same: " + str(sameFile) + " | scrFile: " + scrFile + " | destFile: " + destFile)

    return sameFile 
  except OSError as e:
    print(f"Error accessing files: {e}")
    logger.error(f"Error accessing files: {e}")
  except Exception as e:
    print(f"Unexpected error: {e}")
    logger.exception("Unexpected error:")

def copy_dir(src, dest, verbose):
  """Copies the contents of the source directory to the destination directory, overwriting existing files.
    sysArgs:
      exec: The exe. /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py
      src: The source directory path. ~/home/jk/Documents/WorkTEST/
      dest: The destination directory path.
      verbose: 0 | 1 
    Usage 
      (test):
        /usr/bin/python3 /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/WorkTEST/ ~/home/jk/JKSFO.Resume/WorkTEST/ 1
      (release/cronjob):
        # /usr/bin/python3 /home/jk/dev-git/jksfoTemp/python3/myGDSynch/cronjobs/cpJKSFO.R.5.py ~/home/jk/Documents/Work/ ~/home/jk/JKSFO.Resume/Work/ 0
        10 * * * * <cmd> 1
`  """
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
        # TODO: I think there is a logic error here but I am pretty tired right now ... 
        # if os.path.exists(dest_item):
        backup_file = dest_item + ".bak"
        try:
          # If files are NOT the same 
          if not(filesAreSame(src_item, dest_item, verbose)):
            # Remove any existing backup file and create a new one 
            if os.path.exists(backup_file):
              os.remove(backup_file)
              shutil.copy2(dest_item, backup_file)
            # Copy over the file 
            shutil.copy2(src_item, dest_item)
            if verbose == "1":
              print(f"File backed up and copied {dest_item}")
              logger.info(f"File backed up and copied {dest_item}")
        except OSError as e:
          print(f"Error creating backup for {dest_item}: {e}")
          logger.info(f"Error creating backup for {dest_item}: {e}")
        except Exception as e:
          print(f"Unexpected error: {e}")
          logger.exception("Unexpected error:")
        else: 
          # If files are the same 
          if verbose == "1":
            print(f"Nothing to do for {dest_item} ")
          logger.info(f"Nothing to do  {dest_item} ")
        # if verbose == "1":
        #  print(f"Copied {src_item} to {dest_item}")
        #  logger.info(f"Copied {src_item} to {dest_item}")
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
