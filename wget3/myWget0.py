import os
import sys
import logging
import requests
# import wget 
import subprocess
from urllib.parse import urlparse


def setup_logger():
    """Sets up a logger to a local file named after the script."""

    script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]  # Extract script name
    log_file_name = f"{script_name}.log"

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

#    log_directory = os.path.join(script_dir,  "logs")
#    os.makedirs(log_directory, exist_ok=True)
#    log_file_path = os.path.join(log_directory, log_file_name)

    mylogger = logging.getLogger(__name__)
    mylogger.setLevel(logging.DEBUG)  # Or your desired level

#    file_handler = logging.FileHandler(log_file_path)
    file_handler = logging.FileHandler(log_file_name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  #  file_handler.setFormatter(formatter)
#    myloggr .formatter(formatter) 
    mylogger.addHandler(file_handler)
    return mylogger

def clearTerminal():
    # print("\033[H\033[J", end="")  # ANSI escape code to clear screen
    os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal

def main():
    mylogger = setup_logger()  # Set up logger before any logic
    mylogger.info("mylogger created.")

    try:
        clearTerminal()
        print ("In main()")
        thisFile = os.path.splitext(os.path.basename(sys.argv[0]))[0] # Extract script name
        thisLogFile = thisFile + ".log" # Extract script name
        mylogger.info("Starting main program logic.")
        mylogger.info("Log to write: " + thisLogFile)
        mylogger.info("File to write (wget): " + "thisOutFile" + ".html") 

        # implement wget 
        # wget https://www.google.com -O google.html -a google.log 
        # result = subprocess.run(['ls', '-l'])
        # result = subprocess.run(['wget https://www.google.com -O google.html -a google.log'])
        # result = subprocess.run(['wget https://www.google.com -O google.html -a google.log'])
        # result = subprocess.run(['wget', 'https://www.webscrapingapi.com/images/logo/logo-white.svg'])
        # result = subprocess.run(['wget', 'https://www.webscrapingapi.com/images/logo/logo-white.svg'])
        result = subprocess.run(['wget', 'https://www.google.com', '-O fgoogle.html', '-a ' + thisLogFile ])


        #https://www.google.com -O google.html -a google.log''
        
        print(result.stdout)

    # Why am I getting an error here? 
    except Exception as e:
        print(f"An error occurred: {e}")
        mylogger.error(f"An error occurred: {e}")
        # Handle the error or re-raise it if necessary.
        # raise #Re-raise the error.
    finally:
        print ("Main program logic finished")
        mylogger.info("Main program logic finished.")

if __name__ == "__main__":
    main()