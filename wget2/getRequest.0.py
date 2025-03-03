#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# region Description
"""
Only using this to download a save a sample page
Yes, I could have used wget, but I wanted to do this in Python 
Remember YAGNI and KISS

# https://www.postjobfree.com/jobs?q=data+entry&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100 

TO
Notes:
* Use # %% to run a jupyter cell in vscode
* Consider (using/transforming) this to be a library for other projects
"""
# endregion Description

# region TODO
"""
TODO: Implement logging
TODO: Last statement is the filename (on success)
TODO: Check for output consolidation
TODO: Move screen output to single location
TODO: Replace all print statement to messaging()
TODO: I could change this to something like 'messaging' with an array of messages a \
  failure code and an exit code to handle the error messaging and exit in one place
TODO: Check that comments are correct
TODO: Avoid returning 'None' from a function - see notes and generally check for nulls 
"""
# endregion TODO 

# region Imports

import requests
import os
import sys
import logging
from urllib.parse import urlparse
from typing import NoReturn  # , ReadOnly

# endregion Imports

# region Variables

VERBOSE: bool = True  # Global verbose flag for logging
STDOUT: bool = True  # Global flag for screen output
FILENAME: str = "FILENAME - set in init function"
URL: str = "URL - set in init function"
OUPUTFILE2: str = "OUPUTFILE2 - set in init function"

# endregion Variables

# region Log Settings 
LOG_LEVEL: int = (logging.INFO
)  # Global log level for logging output (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FORMAT: str = ("%(asctime)s - %(levelname)s - %(message)s")  # Global log format for log output
LOG_DATE_FORMAT: str = (    
    "%m/%d/%Y %I:%M:%S %p"  # Global log date format for logging output  # 06/24/2018 12:00:00 PM  # '%Y-%m-%d %H:%M:%S' # '%m/%d/%Y %I:%M:%S %p'  # 06/24/2018 12:00:00 PM  # '%Y-%m-%d %H:%M:%S'
)

# endregion Log Settings 


# region Input Validation
    """ 
      NOT USED 
      # def validateInput(_url: str, _outputFile: str, _verbose: bool) -> int:
      # 
      # _summary_
      #       main already checks for the correct number of arguments, so \
      #         this is just to validate the inputs and types 

      #     Args:
      #         _url (_type_): _description_
      #         _outputFile (_type_): _description_
      #         _verbose (_type_): _description_
      #     """

      #     # Call to validate URL
      #     # is_valid = is_valid_url(str(url) if url is not None else "")
      #     if not _url:
      #         # print(f"Error: URL is required.  URL: {_url}")
      #         return 11
      #     if not is_valid_url(str(_url)):
      #         # print(f"Error: URL appears to be invalid.  URL: {_url}")
      #         return 12
      #     if not _outputFile:
      #         # print(f"Error: Output file is required.  Output file: {_outputFile}")
      #         return 21
      #     if _verbose not in [True, False]:
      #         # print(f"Error: Verbose must be True or False.  Verbose: {_verbose}")
      #         return 31
      #     # passed
      #     return 0
    """

# endregion Input Validation

# region Business Logic

def getURLObj(urlT: str) -> requests.Response:
    # """
    # _summary_
    # Args:
    #     urlT (_type_): _description_
    # Returns:
    #     _type_: _description_
    # """
    logger.info("Enter getURLObj")

    code: int = -1
    r: requests.Response = requests.Response()
    try:
        r = requests.get(urlT)
        code = r.status_code
        if code == 200:
            logger.info(f"Got it: {code}")
            logger.info(str({r}))
        else:
            logger.error(
                f"Error getting url: {urlT}  Response status code: {code}"
            )
    except requests.RequestException as e:
        logger.error(
            f"Error getting url: {urlT};  Response status code: {code}"
        )
    logger.info("Exit getURLObj")
    return r  # Return the response object

# endregion Business Logic

# region File Handling 
def writeObj(obj: requests.Response, outFile: str):

    logger.info("Enter writeObj")

    try:
        """Handle writing the object to a file."""
        if obj is None:  # Handle case where no content was retrieved
            # TODO: Move screen output to single location
            logger.warning(f"No content to write to file: {obj} \n {outFile}")
            return
        with open(outFile, "wt") as f:
            # f.write(str(obj.content)) # bad
            f.write(
                obj.content.decode("utf-8")
             )  # Decode bytes to string before writing

    except Exception as e:
        logger.error("Error writeObj ... ")
        logger.error(f"An error occurred writing the file: {e}")
    finally:
        logger.info("Exit writeObj")

# endregion File Handling

# region Valid 

def is_valid_url(url_string: str) -> bool:
    """
    Checks if a string is likely a valid URL based on syntax,
    without making an HTTP request (no POST involved in validation).

    Source: Ripped from gemini.google.com

    Uses urllib.parse.urlparse to break down the URL and checks for
    the presence of a scheme and a network location (netloc).

    Args:
        url_string: The string to validate.

    Returns:
        True if the string is likely a valid URL, False otherwise.
    """
    try:
        # parsed_url = urlparse(url_string)
        # for requests consistency
        parsed_url = requests_urlparse(url_string)
        result = all(
        result = all(
            [parsed_url.scheme, parsed_url.netloc]
        )  # Check for both scheme and netloc
    except:  # Catch potential parsing errors, consider more specific exception if needed
        result = False
    logger.info("Exit is_valid_url")
    return result
        return False
    logger.info("Exit is_valid_url")
    logger.info("Exit is_valid_url")

# endregion

# region Main

def main():
    """
    # _summary_ 
    # TODO: Consider changing these to a ReadOnly class, tuple or const - singleton, this if fine
    global VERBOSE
    global STDOUT
    global LOG_FILE

    # region Set Default Values
    # return_status:
    # i: int = -1

    # use a function for this and just globals, no need for a class. Could use a tuple
    # for url and output file but this is a singleton use case

    LOG_FILE = sys.argv[0] + ".log"
    OUPUTFILE2= sys.argv[0] + ".txt"

    logger.info("Main() Started.")

    try:
        if len(sys.argv) > 5:
            raise Exception("Too many arguments")
    
        try:
            STDOUT = bool(sys.argv[4])

        except IndexError:
            STDOUT = False
            logger.info("Main() output not specified.")

        try:
            VERBOSE = bool(sys.argv[3])
        except IndexError:
            VERBOSE = False
            logger.info("Main() has four arguments.")

        url = "https://www.postjobfree.com/jobs?q=data+entry&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100"
      
        # Should be good to go
        # obj: requests.Response = getURLObj(url)
        obj = getURLObj(url)

        logger.info("In main ... ")
        
        if obj:  # Only write if content was successfully retrieved
            writeObj(obj, OUPUTFILE2)
            # Success ...
            logger.info(f"Should be good. \n \t URL: {url} \
                \n\t File: {OUPUTFILE2} \
                \n\t Output: {VERBOSE}"
            )
        
            logger.info(str(obj))
            return_status = 0
        else: 
            logger.error("Failed to retrieve content from URL.")
            logger.info("6")
            return_status = -1
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error("An error occurred in main", exc_info=True)

# endregion Main 

# region  Entry

if __name__ == "__main__":
    """_summary_
    * verbose
    * stdout
    * url
    * file
    """
    try:
        logFile = sys.argv[0] + ".log" if sys.argv[0] else "foo" + ".log"
        logging.basicConfig(
            filename=logFile, format="%(asctime)s %(message)s", filemode="a"
        )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.info("__name __ Started. Calling main()")
        
        main()

    except Exception as e:
        logger.critical("Beyond fubar: " + str(type(e)) + " " + str(e) + " " + str(e.args))

    finally:
        logger.info("Done")

#endregion Entry 
