#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# region Notes
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
# endregion Notes

"""
TODO: Implement logging
TODO: Re-implement input validation 
TODO: Last statement is the filename (on success)
TODO: Check for output consolidation
TODO: Move screen output to single location
TODO: Replace all print statement to messaging()
TODO: I could change this to something like 'messaging' with an array of messages a \
  failure code and an exit code to handle the error messaging and exit in one place
TODO: Check that comments are correct
TODO: Avoid returning 'None' from a function - see notes and generally check for nulls 
TODO: Test inputs - am I only using the default url? 
TODO: Check for null code paths and variable usage 
TODO: Change setLogger() to use argparse
TODO: Implement input validation 
TODO: Why is logging not happening? Is it done by level? 


  python3 getRequest.0.py

  args: 
    <filename> # default
    _url: str 
    _outputFile: str, 
    _verbose: bool
"""

import requests
import os
import sys
import logging
from urllib.parse import urlparse
import argparse

# Needed? 
# VERBOSE: bool = True  # Global verbose flag for logging
# FILENAME: str = "FILENAME - set in init function"
# URL: str = "URL - set in init function"
# LOGGER  = logging.getLogger(__name__)

# region Input Validation
    # def validateInput(_url: str, _outputFile: str, _verbose: bool) -> int:
    # 
    # _summary_
    #       main already checks for the correct number of arguments, so \
    #         this is just to validate the inputs and types 

    #     Args:
    #         _url (_type_): _description_
    #         _outputFile (_type_): _description_
    #         _verbose (_type_): _description_
    #    
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
# endregion Input Validation

# region Business Logic

def getURLObj(urlT: str) -> requests.Response:
    # LOGGER.info("Enter getURLObj")

    OUPUTFILE: str = "OUPUTFILE - set in init function"

    # logMe("Enter getURLObj")
    code: int = -1
    r: requests.Response = requests.Response()
    try:
        r = requests.get(urlT)
        code = r.status_code
        if code == 200:
            # LOGGER.info(f"Got it: {code} " + str({r}))
            # logMe(f"Got it: {code} " + str({r}))
            a: int = 0
        else:
            # LOGGER.error(f"Error getting url: {urlT};  Response status code: {code}")
            #logMe(f"Error getting url: {urlT};  Response status code: {code}")
            b: int = 0
    except Exception as e:
        # LOGGER.error(f"Exception occurred: {e}")
        # logMe(f"Exception occurred: {e}")
        # LOGGER.info("Exit getURLObj")
        g: int = 0
    return r
# endregion Business Logic

def writeObj(obj: requests.Response, outFile: str):

    # LOGGER.info("Enter writeObj")
    try:
        if obj is None:  # Handle case where no content was retrieved
            # LOGGER.error(f"No content to write to file: {obj} \n {outFile}")
            # logMe(f"No content to write to file: {obj} \n {outFile}")
            a: int = 4 
            return
        with open(outFile, "wt") as f:
            f.write(obj.content.decode("utf-8"))

    except Exception as e:
        # LOGGER.error(f"An error occurred writing the file: {e}")
        #logMe(f"An error occurred writing the file: {e}")
        aa: int = 4 
    finally:
        # LOGGER.info("Exit writeObj")
        # logMe("Exit writeObj")
        aaa: int = 4 

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
    res: bool = False
    try:
        parsed_url = urlparse(url_string)
        # LOGGER.info("Exit is_valid_url. 20")

        res = all([parsed_url.scheme, parsed_url.netloc])  # Check for both scheme and netloc
    except Exception as e:  # Catch potential parsing errors, consider more specific exception if needed
        # LOGGER.error(f"Error parsing URL: {e}")
        # LOGGER.info("Exit is_valid_url. 21")
        res = False
    finally: 
        return res

def setLogger() -> None:
    # Obviously I don't understand their implementation of logging ... 
    # LOGGER = logging.getLogger()
    try:
        # TODO: change for argParse () 
        logFile = sys.argv[0] + ".log" if sys.argv[0] else "foo" + ".log"
        #logging.basicConfig(filename=logFile, format="%(asctime)s %(message)s", filemode="a")
        # LOGGER.basicConfig(filename=logFile, format="%(asctime)s %(message)s", filemode="a")
        
        
        # LOGGER.setLevel(logging.DEBUG)
        if len(sys.argv) > 4:
            # LOGGER.error("Main() - too many arguments")
            # LOGGER.setLevel(logging.ERROR)3
            c: int = 3 
        elif len(sys.argv) > 3 and sys.argv[3] is not None and sys.argv[3] != "" and sys.argv[3] != "None":
            if bool(sys.argv[3]) == True:  
                VERBOSE = True 
                # LOGGER.setLevel(logging.DEBUG)
        else:
            # VERBOSE = False 
            # LOGGER.setLevel(logging.INFO)
            d: int = 5
    except: 
        
        # logMe("effed up")
        e: int = 6 

# No need for this ...
# def logMe(msg: str) -> None: 
#     if VERBOSE:
#         LOGGER.info(msg)

def main():

    # _summary_ 
    # TODO: Consider changing these to a ReadOnly class, tuple or const - singleton, this if fine

    # logMe("Main() Started.")

    try:
        setLogger() 
        # if (VERBOSE): 
        #     logMe("In main.")    

        OUPUTFILE = sys.argv[0] + ".txt"
        # logMe(OUPUTFILE)

        ## KISS 

        # # TODO: test if uri was supplied else set default 
        # url = "https://www.postjobfree.com/jobs?q=data+entry&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100"
      
        # # Should be good to go
        # obj = getURLObj(url)

        # logMe("In main ... ")
        
        # if obj:  # Only write if content was successfully retrieved
        #     writeObj(obj, OUPUTFILE)
        #     # Success ...
        #     logMe(f"Should be good. \n \t URL: {url} \
        #         \n\t File: {OUPUTFILE} \
        #         \n\t Output: {VERBOSE}"
        #     )
        
        #     logMe("Main: 12" + str(obj))
        #     return_status = 0
        # else: 
        #     logMe("Failed to retrieve content from URL.")
        #     return_status = -1

    except Exception as e:
        #  logMe(f"An error occurred: {e}")
        h: int = 0 

if __name__ == "__main__":
    
    #logFile = sys.argv[0] + ".log" if sys.argv[0] else "foo" + ".log"
    #LOGGER.setLevel(logging.DEBUG)
    try:
        setLogger()
        main()
    except Exception as e:
        # logging.critical("Beyond fubar: " + str(type(e)) + " " + str(e) + " " + str(e.args))
        # LOGGER.error("Error: __main__ - program won't start. " + str(type(e)) + " " + str(e) + " " + str(e.args))
        #logMe("Beyond fubar: " + str(type(e)) + " " + str(e) + " " + str(e.args)) 
        j: int = 0 
    finally:
        # logging.info("Done")
        # logMe("Done")
        # LOGGER.error("Completed")        
        k: int = 0 

