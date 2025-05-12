import os
import sys
import logging
import requests
from urllib.parse import urlparse

# TODO: change this to handle any form of url (http, https, www, etc.)  
# TODO: Avoid returning 'None' from a function ??? 


class ControlValues:
    def __init__(self):
        self.path = "./"
        self.file_name = "foo.py"
        self.log_name = "foo.log"
        self.url = "cnn.com"
        self.outputfile = "cnn.com.html"
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

    mylogger = logging.getLogger(__name__)
    mylogger.setLevel(logging.DEBUG)  # Or your desired level

    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    mylogger.addHandler(file_handler)
    return mylogger

def clearTerminal():
    # print("\033[H\033[J", end="")  # ANSI escape code to clear screen
    os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal

def get_application_directory():
    """Gets the directory of the currently running Python script."""
    return os.path.dirname(os.path.abspath(__file__))

def setControlValues():
    out: str = "" 
    ctl = ControlValues()
    # ctl.path = os.getcwd()
    ctl.path = get_application_directory() # Get the directory of the currently running script not the CWD 
    ctl.file_name = os.path.basename(__file__)
    ctl.log_name = "/logs/" + os.path.splitext(ctl.file_name)[0] + ".log"
    ctl.url = "https://www.google.com"
    # url = "https://www.postjobfree.com/jobs?q=data+entry&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100"
    # out = ctl.url.replace("//", "-") + ".html"
    # out = out.replace("https:", "")
    out = ctl.url.replace("https://", "")
    out = out.replace("//", "-") + ".html"
    # ctl.outputfile = "output.html"
    ctl.outputfile = out 
    ctl.verbose = True
    return ctl

def showControlValues(lgr, ctl: ControlValues):
    print(f"Path: {ctl.path}")
    print(f"File Name: {ctl.file_name}")
    print(f"Log Name: {ctl.log_name}")
    print(f"URL: {ctl.url}")
    print(f"Output File: {ctl.outputfile}")
    print(f"Verbose: {ctl.verbose}")  

    lgr.info(f"Path: {ctl.path}")
    lgr.info(f"File Name: {ctl.file_name}")
    lgr.info(f"Log Name: {ctl.log_name}")
    lgr.info(f"URL: {ctl.url}")
    lgr.info(f"Output File: {ctl.outputfile}")
    lgr.info(f"Verbose: {ctl.verbose}")  
             
def ensure_https(url):
    """Ensures a URL starts with 'https://'."""
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return "https://" + url
    elif parsed_url.scheme != 'https':
        return "https://" + parsed_url.netloc + parsed_url.path + "?" + parsed_url.query + "#" + parsed_url.fragment #Rebuild the url with https.
    return url

def setInputValues(lgr, controlValues): 
    print ("Begin setInputValues - to override defaults") 
    # mylogger.info(f"Begin setInputValues")
    lgr.info(f"Begin setInputValues")
    
    try: 
        # 3 inputs: url, outputfile, verbose  (filename is default at 0)
        if len(sys.argv) > 1 and len(sys.argv) < 5:
            # All I really care about here is the url 
            if sys.argv[1]: 
                url: str = sys.argv[1]

# ABC  problem is here 

                # append https:// if not there 
                out = ensure_https(url)
                out = out.replace("https://", "")  
                out = out.replace("http://", "")  

# I'm losing the last '/' here ... 

                out = "/" + out.replace("/", "-") + ".html"
                controlValues.outputfile = out # sys.argv[1] + ".html" 
        elif len(sys.argv) == 1:
            print (f"Using default arguments: {len(sys.argv)}") 
            lgr.info(f"Using default arguments: {len(sys.argv)}") 
        else:
            print (f"Too many arguments: {len(sys.argv)}") 
            lgr.info(f"Too many arguments: {len(sys.argv)}") 
    # TODO: Optional ... set verbose for extra logging or not 
    except Exception as e:
        print (f"An error occurred: {e}") 
        lgr.info(f"End setInputValues")

    finally:  
        # print ("End setInputValues")
        lgr.info(f"End setInputValues - Finally")
        # lgr.info(f"Result: {result}")

def is_valid_url(lgr, url_string: str) -> bool:
    """
    Checks if a string is likely a valid URL based on syntax,
    without making an HTTP request 
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
        res = all([parsed_url.scheme, parsed_url.netloc])  # Check for both scheme and netloc
    except Exception as e:  # Catch potential parsing errors, consider more specific exception if needed
        print(f"An error occurred, looks like a bad URL: " + url_string + "{e}")
        lgr.error(f"An error occurred, looks like a bad URL: " + url_string + " {e}")
        res = False
    finally: 
        return res

def getURLObj(lgr, urlT: str) -> requests.Response:
    lgr.info(f"Enter getURLObj")

    code: int = -1
    r: requests.Response = requests.Response()
    try:
        r = requests.get(urlT)
        code = r.status_code
        if code == 200:
            lgr.info(f"Got it: {code} " + str({r}))
        else:
            lgr.error(f"Error getting url: {urlT};  Response status code: {code}")
    except Exception as e:
        lgr.error(f"Exception occurred: {e}")
    finally: 
        # print(f"Exit getURLObj")
        lgr.info(f"Exit getURLObj")
        return r

def writeObj(lgr, obj: requests.Response, outFile: str):
    print("Enter writeObj - this is the output file name: " + outFile)
    lgr.info("Enter writeObj - this is the output file name: " + outFile)
    try:
        # Already tested for this in getURLObj 
        # if obj is None:  # Handle case where no content was retrieved
        #   # mylogger.error(f"No content to write to file: {obj} \n {outFile}")
        #   # logMe(f"No content to write to file: {obj} \n {outFile}")
        # return
        with open(outFile, "wt") as f:
            f.write(obj.content.decode("utf-8"))
        lgr.info(f"exiting writeObj: {outFile} - success")
    except Exception as e:
        print(f"An error occurred writing the file: {e}")
        lgr.error(f"An error occurred writing the file: {e}")
    finally:
        # print("Exit writeObj")
        lgr.info("Exit writeObj")

def main():
    mylogger = setup_logger()  # Set up logger before any logic
    mylogger.info("mylogger created.")

    try:
        clearTerminal()
        mylogger.info("Starting main program logic.")
        print ("In main()")
        
        ctl = setControlValues()
        showControlValues(mylogger, ctl)  

        # TODO: actual logic 

          # Next - new modules 
          #   - soup (by domain - for now, could take and argument object) to parse file input 
          # and export to csv
          #   - append csv to file (LO Calc 'db')
          #   - need consistent schema 
        setInputValues(mylogger, ctl)
        
        # Validate the URL
        #if (is_valid_url(mylogger, ctl.url)): 
        if (is_valid_url(mylogger, "https://" + ctl.url)): 
            print ("Valid URL")
            mylogger.info("Valid URL")

            # Actually get the response 
            response = getURLObj(mylogger, ctl.url)

            # validate the response
            if response.status_code == 200:
                # print ("Response 200")
                # mylogger.info("Response 200")
                # Actually write to file 
                # thisOutFile  = ctl.path + "/" + ctl.outputfile
                # thisOutFile  = ctl.path + "-" + ctl.outputfile
                # thisOutFile  = ctl.path + "-" + ctl.outputfile
                thisOutFile  = ctl.path + "/" + ctl.outputfile

                print ("File to write: " + thisOutFile)
                mylogger.info("File to write: " + thisOutFile)

                # Bob's your uncle 

                writeObj(mylogger, response, thisOutFile)
                # mylogger.info("Where is the mylogger ergror?")

            else:
                print ("Response not 200")
                mylogger.info("Response not 200")

            # print ("Should be done, why am I getting a logging error")
            # mylogger.info("Should be done, why am I getting a logging error?")

        else: 
            #Raise an error to test logging.
            # raise ValueError("Actually it didn't, this is a test.") 
            err: str = "Apparently invalid URL." + ctl.url
            raise ValueError(err) 

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