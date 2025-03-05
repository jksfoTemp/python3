import logging
import os
import sys


class ControlValues:
    def __init__(self):
        self.path = ""
        self.file_name = ""
        self.log_name = ""
        self.url = ""
        self.outputfile = ""
        self.verbose: bool = False

def setup_logger():
    """Sets up a logger to a local file named after the script."""

    script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]  # Extract script name
    log_file_name = f"{script_name}.log"

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    log_directory = os.path.join(script_dir,  "logs")

    os.makedirs(log_directory, exist_ok=True)
    
    log_file_path = os.path.join(log_directory, log_file_name)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Or your desired level

    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

def clear_terminal():
    print("\033[H\033[J", end="")  # ANSI escape code to clear screen

def show_control_values(ctl: ControlValues):
    print(f"Path: {ctl.path}")
    print(f"File Name: {ctl.file_name}")
    print(f"Log Name: {ctl.log_name}")
    print(f"URL: {ctl.url}")
    print(f"Output File: {ctl.outputfile}")
    print(f"Verbose: {ctl.verbose}")  

def set_control_values():
    ctl = ControlValues()
    ctl.path = os.getcwd()
    ctl.file_name = os.path.basename(__file__)
    ctl.log_name = "/logs/" + os.path.splitext(ctl.file_name)[0] + ".log"
    ctl.url = "https://www.google.com"
    ctl.outputfile = "output.html"
    ctl.verbose = True
    return ctl

def main():
    logger = setup_logger()  # Set up logger before any logic

    try:
        logger.info("Starting main program logic.")
        # Your programming/business logic here...
        clear_terminal()
        print ("snoopy")
        
        ctl = set_control_values()

        # TODO: actual logic 

        show_control_values(ctl)  

        # Example:
        result = 10 / 2
        logger.info(f"Result: {result}")
        raise ValueError("Actually it didn't, this is a sample.") #Raise an error to test logging.

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        # Handle the error or re-raise it if necessary.
        # raise #Re-raise the error.

    logger.info("Main program logic finished.")

if __name__ == "__main__":
    main()