
# import requests
import os
import sys
import logging
# from logging import FileHandler, Logger
# from urllib.parse import urlparse
# import argparse

class ControlValues:
    def __init__(self):
        self.path = ""
        self.file_name = ""
        self.log_name = ""
        self.url = ""
        self.outputfile = ""
        self.verbose: bool = False

# def configure_logging() : #  -> Logging: 
    #logging.basicConfig(level=logging.INFO, \
    #                  format="%(asctime)s %(message)s", filemode="a")
    # I will never understand how logging in python works. 
#    logger = logging.getLogger(__name__) 
  #  logging._Level .setLevel("INFO")
    # fh = logging.FileHandler("getRequest.1.log")
    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)
    # return logger
    
def setup_logger(log_file_name, log_level=logging.INFO):
    """Sets up a logger that writes to a specified file."""

    # Ensure the log directory exists
    log_directory = "logs"  # Or your desired directory
    os.makedirs(log_directory, exist_ok=True)

    # Construct the full log file path
    log_file_path = os.path.join(log_directory, log_file_name)

    logger = logging.getLogger(__name__)  # Or any logger name
    logger.setLevel(log_level)

    file_handler = logging.FileHandler(log_file_path)  # Specify the file path here!
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

# Example usage:
# my_logger = setup_logger("my_application.log", logging.DEBUG) #Specify the log file name here.
# my_logger.debug("This is a debug message.")


# move to function getValue() 0 1 2 3 
        # script_path = sys.argv[0]
        # script_name = os.path.basename(script_path)
        # log_file = sys.argv[0] + ".log" 
        # output_file = sys.argv[0] + ".txt"

        # get just the file name from argv[0] 
        # actually use argParse() 
        # fuck argParse, overkill 
        # if len(sys.argv) > 3:

def getValues(ctl) -> None:  
  foo: str = "hi"
  ctl.file_name = foo

#region main - POC 
def main():
    # logging = configure_logging()
    logging._Level = "Info"

    try:
        print ("main() start")
        logging.info("Log file: In main().")    
        # logging.fil
        
        control = ControlValues()

        getValues(control)

        print ("here " + control.file_name)

        
        # control = ControlValues = ControlValues()
        # control = getValues(())
        # function getValues(ctl) # 0 1 2 3 

        # valid url? 

        print ("foobar snoopy " + "")

    except Exception as e:
        print ('error' + str(type(e)) + " " + str(e) + \
          " " + str(e.args)) 
        logging.info("Log file: Error in Main(). " + \
          str(type(e)) + " " + str(e) + " " + str(e.args))

    finally:
        print ("Exiting main().")
        logging.info("Log file: Exiting main().")    
#endregion main - POC 

if __name__ == "__main__":
    
    try:
        print (os.system("clear"))
        print ("Calling main().")
        main()
    except Exception as e:
        print ('error' + str(type(e)) + " " + str(e) + \
          " " + str(e.args)) 
    finally:
        # LOGGER.error("Completed")        
        print ("Exiting __main__.")

