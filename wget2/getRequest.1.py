
import requests
import os
import sys
import logging
from logging import Logger
# from urllib.parse import urlparse
# import argparse

class ControlValues:
    def __init__(self):
        path: str 
        file_name: str
        log_name: str
        url: str
        outputfile: str 
        verbose: bool 

        self.path = "" 
        self.file_name = "" 
        self.log_name = "" 
        self.url = "" 
        self.outputfile = "" 
        self.verbose: Bool = False


# move to function getValue() 0 1 2 3 
        # script_path = sys.argv[0]
        # script_name = os.path.basename(script_path)
        # log_file = sys.argv[0] + ".log" 
        # output_file = sys.argv[0] + ".txt"

        # get just the file name from argv[0] 
        # actually use argParse() 
        # fuck argParse, overkill 
        # if len(sys.argv) > 3:

def configure_logging() : #  -> Logging: 
    logging.basicConfig(level=logging.INFO, \
                       format="%(asctime)s %(message)s", filemode="a")

#region main - POC 
def main():
    configure_logging()
    try:
        print ("main() start")
        logging.info("Log file: In main().")    

        ctl: ControlValues = ControlValues()

        # function getValues(ctl) # 0 1 2 3 

        
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

