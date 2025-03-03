#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# region Description
"""Only using this to download a save a sample page

Yes, I could have used wget, but I wanted to do this in Python 

Remember YAGNI and KISS

getRequest.0.py 'foo.com' 'foo.txt'
  # def main(url='', outputFile='', verbose=False):
    # url = 'https://en.wikipedia.org/wiki/foo'
    # outputFile = 'sampleFile.html'
Output file: sampleFile.html

TODO: Get it to run again and then clean it up 

# https://www.postjobfree.com/jobs?q=data+entry&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100 

TODO: DONE Rearrange the code to be more modular and use regions 
TODO: DONE Set up a decent formatter that actually works (unlike black)
TODO: Implement logging
TODO: Last statement is the filename (on success)
TODO: Check for output consolidation
TODO: Move screen output to single location
TODO: Replace all print statement to messaging()
TODO: I could change this to something like 'messaging' with an array of messages a \
  failure code and an exit code to handle the error messaging and exit in one place
TODO: Check that comments are correct
TODO: Avoid returning 'None' from a function - see notes and generally check for nulls 

Notes:
* Use # %% to run a cell in vscode
* Consider (using/transforming) this to be a library for other projects
"""
# endregion Description

import requests
import os
import sys
import logging
# from xmlrpc.client import Boolean
from urllib.parse import urlparse
from requests.compat import urlparse as requests_urlparse
from typing import NoReturn  # , ReadOnly

# endregion Imports

"""_summary_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
"""

# region Variables
VERBOSE: bool = True  # Global verbose flag for logging
STDOUT: bool = True  # Global flag for screen output
FILENAME: str = "FILENAME - set in init function"
URL: str = "URL - set in init function"
OUPUTFILE: str = "OUPUTFILE - set in init function"

# todo: set up a global log file WITH FILENAME ARG, FIRST VALUE
LOG_FILE: str = "app.log"  # Global log file name for logging output
LOG_LEVEL: int = (
    logging.DEBUG
)  # Global log level for logging output (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_FORMAT: str = (
    "%(asctime)s - %(levelname)s - %(message)s"  # Global log format for logging output
)
LOG_DATE_FORMAT: str = (
    "%m/%d/%Y %I:%M:%S %p"  # Global log date format for logging output  # 06/24/2018 12:00:00 PM  # '%Y-%m-%d %H:%M:%S' # '%m/%d/%Y %I:%M:%S %p'  # 06/24/2018 12:00:00 PM  # '%Y-%m-%d %H:%M:%S'
)
# endregion Variables


# region Logging
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# endregion


# region Messaging
def messaging(msg: str):
    """_summary_
    This is a placeholder for a more sophisticated messaging system
    """
    print(
        msg
        # logging.debug(msg)
    )  # Debugging message
    # logging.info(msg)  # Informational message
    
    # It doesn't like the type of NoReturn
    # def displayInputError(_isValid: int, _url: str, _outputFile: str, _verbose: bool) -> NoReturn:
    #   def displayInputError(
    #     _isValid: int, _url: str, _outputFile: str, _verbose: bool
    # ) -> None

    """_summary_
    The general idea is to display the error message and exit the program all in one place
    and not confuse the business logic and error handling with the presentation logic
    
    TODO: I could change this to something like 'messaging' with an array of messages a \
      failure code and an exit code to handle the error messaging and exit in one place
    """

    # huh stucks for compilation
    _isValid: int = 0
    _url: str = ""
    _outputFile: str = ""
    _verbose: bool = False

    if _isValid == 11:
        print(f"Error: URL is required.  URL: {_url}")
    elif _isValid == 12:
        print(f"Error: URL appears to be invalid.  URL: {_url}")
    elif _isValid == 21:
        print(f"Error: Output file is required.  Output file: {_outputFile}")
    elif _isValid == 31:
        print(f"Error: Verbose must be True or False.  Verbose: {_verbose}")
    else:
        print(f"Error: Unknown error occurred.  Error code: {_isValid}")


# endregion Messaging


# region Error Handling
def handle_error(e: Exception):
    """_summary_
    This is a placeholder for a more sophisticated error handling system
    """
    print(f"An error occurred: {e}")
    # logging.error
    # logging.error(f"An error occurred: {e}")
    
    # def validateInput(_url: str, _outputFile: str, _verbose: bool) -> int:


def validateInput(_url: str, _outputFile: str, _verbose: bool) -> int:
    """_summary_
      main already checks for the correct number of arguments, so \
        this is just to validate the inputs and types 

    Args:
        _url (_type_): _description_
        _outputFile (_type_): _description_
        _verbose (_type_): _description_
    """

    # Call to validate URL
    # is_valid = is_valid_url(str(url) if url is not None else "")
    if not _url:
        # print(f"Error: URL is required.  URL: {_url}")
        return 11
    if not is_valid_url(str(_url)):
        # print(f"Error: URL appears to be invalid.  URL: {_url}")
        return 12
    if not _outputFile:
        # print(f"Error: Output file is required.  Output file: {_outputFile}")
        return 21
    if _verbose not in [True, False]:
        # print(f"Error: Verbose must be True or False.  Verbose: {_verbose}")
        return 31
    # passed
    return 0


# endregion Input Validation


# region Business Logic
def getURLObj(urlT: str) -> requests.Response:
    """_summary_
    Args:
        urlT (_type_): _description_
    Returns:
        _type_: _description_
    """
    code: int = -1
    r: requests.Response = requests.Response()
    try:
        r = requests.get(urlT)
        code = r.status_code
        if code == 200:
            print(f"Got it: {code}")
        else:
            print(
                f"Error getting url: {urlT}  Response status code: \
                  {code}"
            )
    except requests.RequestException as e:
        print(
            f"Error getting url: {urlT};  Response status code: \
            str({code})"
        )
    return r  # Return the response object


def writeObj(obj: requests.Response, outFile: str):

    try:
        """Handle writing the object to a file."""
        if obj is None:  # Handle case where no content was retrieved
            # TODO: Move screen output to single location
            print(f"No content to write to file: {obj} \n {outFile}")
            return
            with open(outFile, "wt") as f:
                # f.write(str(obj.content)) # bad
                f.write(
                    obj.content.decode("utf-8")
                )  # Decode bytes to string before writing

    except Exception as e:
        print(f"An error occurred writing the file: {e}")


# Move me
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
        return all(
            [parsed_url.scheme, parsed_url.netloc]
        )  # Check for both scheme and netloc
    except:  # Catch potential parsing errors, consider more specific exception if needed
        return False


# endregion


# region Main
def main():
    """_summary_"""
    # TODO: Consider changing these to a ReadOnly class, tuple or const - singleton, this if fine
    global VERBOSE
    global STDOUT
    global LOG_FILE

    # region Set Default Values
    # return_status:
    # i: int = -1

    # use a function for this and just globals, no need for a class. Could use a tuple
    # for url and output file but this is a singleton use case

    logger.info("Main() Started.")

    try:
        if len(sys.argv) > 5:
            raise Exception("Too many arguments")

        try:
            STDOUT = bool(sys.argv[4])
        except IndexError:
            STDOUT = False

        try:
            VERBOSE = bool(sys.argv[3])
        except IndexError:
            VERBOSE = False

        LOG_FILE = sys.argv[0] + ".log"

    # chang to use globals , a cheat but makes sense for this purpose
    # try:
    #     outputFile: str = str(sys.argv[2]) + ".html"
    # except:
    #     outputFile = sys.argv[0] + ".html"

    # try:
    #     url: str = str(sys.argv[1]) + ".html"
    # except:
    #     url = "https://en.wikipedia.org/wiki/foo"
    except:
        print("some error and the exception")

    # url_arg = ""

    #     # Actually perform the input validation
    #     # TODO: change signature to validateInput(url, outputFile)
    #   isValid = validateInput(url, outputFile)

    #     # Separate the messaging
    #     if isValid != 0:
    #       # TODO: change signature to displayInputError(isValid, url, outputFile)
    #         displayInputError(isValid, url, outputFile)
    #         sys.exit()

    #     # Should be good to go
    #     obj: requests.Response = getURLObj(url)

    #     if obj:  # Only write if content was successfully retrieved
    #         writeObj(obj, outputFile)
    #         # Success ...
    #         print(
    #             f"Should be good. \n \t URL: {url} \
    #             \n\t File: {outputFile} \
    #             \n\t Output: {verbose}"
    #         )
    #         return_status = 0
    #         # dump the file name
    #         # messaging(fname) for piping to next step
    #     else: 
    #         print("Failed to retrieve content from URL.")
    #         return_status = -1


# endregion


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
            filename=logFile, format="%(asctime)s %(message)s", filemode="w"
        )
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        main()

    except Exception as e:
        print("Beyond fubar: " + str(type(e)) + " " + str(e) + " " + str(e.args))

    finally:
        print("Done")
#endregion Main 
