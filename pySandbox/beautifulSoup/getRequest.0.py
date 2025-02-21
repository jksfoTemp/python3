#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Only using this to download a save a sample page
getRequest.0.py 'foo.com' 'foo.txt'
  # def main(url='', outputFile='', verbose=False):
    # url = 'https://en.wikipedia.org/wiki/foo'
    # outputFile = 'sampleFile.html'
Output file: sampleFile.html

TODO: Parse with PyLance (remove other linters)
TODO: Implement variable typing
TODO: Set up a decent formatter that actually works (unlike black)
TODO: Implement logging
TODO: Set up debugging

Notes:
* Use vscode, not vscodium  (vscodium doesn't have the same features)
* Use # %% to run a cell in vscode

"""

import requests
import os
import sys

# Removed - was just being used for testing
# class Stubb(object):
#   def __init__(self, status_code, content):
#     self._status_code = status_code
#     self._content = content

#   def name(self):
#     return self._status_code, self._content


def getURLObj(urlT):
    """_summary_

    Args:
        urlT (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        # REMOVEME
        # r = stubb (200, "foo")
        # print (r.status_code)
        # print (r.content)

        r = requests.get(urlT)
        code = r.status_code
        if code == 200:
            print(f"Got it: {code}")
            return r.content
        else:
            print(
                f"Error getting url: {urlT}  Response status code: \
                  {code}"
            )
            return None

    except requests.exception.RequestException as e:
        print(
            f"Error getting url: {urlT};  Response status code: \
            {code}"
        )
        return None


def writeObj(obj, outFile):
    """Handle writing the object to a file."""
    if obj is None:  # Handle case where no content was retrieved
        print(f"No content to write to file: {obj} \n {outFile}")
        return

    try:
        with open(outFile, "wt") as f:
            # f.write(str(obj.content)) # bad
            f.write(obj.decode("utf-8"))  # Decode bytes to string before writing

    except Exception as e:
        print(f"An error occurred writing the file: {e}")


# def main(url='https://en.wikipedia.org/wiki/foo',
#  outputFile='sampleFile.html', verbose=False):
def main(
    url="https://en.wikipedia.org/wiki/foo", outputFile="sampleFile.html", verbose=False
):
    try:
        obj = getURLObj(url)  # verbose
        if obj:  # Only write if content was successfully retrieved
            writeObj(obj, outputFile)

            ### TODO:  output is not being decoded
            ### TODO:  validate inputs, return go/no-go status and error message (array?)

            print(
                f"Should be good. \n \t URL: {url} \
                \n\t File: {outputFile} \
                \n\t Output: {verbose}"
            )
            return_status = 0
        else:
            print("Failed to retrieve content from URL.")
            return_status = -1
    except Exception as e:
        print(f"An error occurred in main: {e}")
        return_status = 1
    finally:
        sys.exit(return_status)  # Exit with the determined status code


if __name__ == "__main__":
    url_arg = ""
    # Should input validation be done here or in main?
    # main(sys.argv[0], sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4:  # Check for correct number of arguments
        url_arg = sys.argv[1]
        output_file_arg = sys.argv[2]
        verbose_arg = sys.argv[3]
        main(url_arg, output_file_arg, verbose_arg)
    elif len(sys.argv) == 3:
        url_arg = sys.argv[1]
        output_file_arg = sys.argv[2]
        main(url_arg, output_file_arg)
    elif len(sys.argv) == 2:  # Allow URL only, use default output file
        url_arg = sys.argv[1]
        main(url_arg)
    elif len(sys.argv) == 1:  # Allow URL only, use default output file
        main()
    else:
        print(
            "Usage: getRequest.0.py 'URL_to_download' 'output_file.html' \
            [TRUE/FALSE] \
            (\t getRequest.0.py {sys.argv[1]}, {sys.argv[2]}, {sys.argv[3]})"
        )
        print(
            "\tgetRequest.0.py 'URL_to_download' 'output_file.html' \
            (\t getRequest.0.py {sys.argv[1]}, {sys.argv[2]})"
        )
        print(
            "\tgetRequest.0.py 'URL_to_download' \
            (\t getRequest.0.py {sys.argv[1]})"
        )
        print(
            "\tgetRequest.0.py \
            (\t getRequest.0.py)"
        )
        print("Error: Incorrect number of arguments.")
