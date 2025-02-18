# pjfParse.py

""" Boilerplate python3 template code with error handling that calls a sub 
that prints the current time. It should have reference to numpy, datetime, pdf and 
string libraries. Demonstrates file access ...

TODO: Add and print arguments to the main function to accept the job posting file path as input.
TODO: Add parsing code to extract the job description from the job posting.
"""

#TODO: find class values
#TODO: do I have the URL? 
#TODO: load object as file 
#TODO: find class values in file 
#TODO: hook wget as an option 
#TODO: sorting? 
#TODO: store in a database 
#TODO: someting else ... 
 
import datetime
import string
import sys

''' # import numpy as np 
# Although not strictly needed for this example, included as requested
# from reportlab.pdfgen import canvas # Although not strictly needed for this example, included as requested
# Call syntax 
# (.venv) jku@jkMain:~/git/jksfoTemp$ python3
# ./python3/postJobFreeParse/pjfParse.py "/home/jku/git/jksfoTemp/python3/postJobFreeParse"
'''
# # pip3 install beautifulsoup4
from bs4 import BeautifulSoup

def print_current_time():
# Prints the current time in a formatted string.
  try:
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {formatted_time}")

    # Example of string manipulation (as requested)
    uppercase_time = formatted_time.upper()
    print(f"Uppercase time: {uppercase_time}")

  except Exception as e:
    print(f"An error occurred in print_current_time: {e}")
    return None # Or handle the error as appropriate

    return formatted_time # Return the formatted time if successful

def extract_data_from_html (html_content, outToTerm): 
  try:
    print ("hi", outToTerm)
     # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # A'
    
    link = soup.find('a')['href']

    company_name = soup.find('span', class_='colorCompany').get_text(strip=True) if soup.find('span', class_='colorCompany') else 'N/A'
    location = soup.find('span', class_='colorLocation').get_text(strip=True) if soup.find('span', class_='colorLocation') else 'N/A'
    salary = soup.find('div', class_='colorSalary').get_text(strip=True) if soup.find('div', class_='colorSalary') else 'N/A'
    job_description = soup.find('span', class_='jdSnippet').get_text(strip=True) if soup.find('span', class_='jdSnippet') else 'N/A'
    posting_date = soup.find('span', class_='colorDate').get_text(strip=True) if soup.find('span', class_='colorDate') else 'N/A'

    print(f"Job Title: {job_title}")
    print(f"Job link: {link}")
    print(f"company_name: {company_name}")
    print(f"location: {location}")
    print(f"salary: {salary}")
    print(f"job_description: {job_description}")
    print(f"posting_date: {posting_date}")
    #print(f"Job Title: {job_title}")


    # return {
    #     'job_title': job_title,
    #     'company_name': company_name,
    #     'location': location,
    #     'salary': salary,
    #     'job_description': job_description,
    #     'posting_date': posting_date
    # }
    
  except Exception as e:
    print(f"An error occurred in extract_data_from_html: {e}")
    return None # Or handle the error as appropriate
    
  
  
''' Creating a PDF example 
# Might want this for the sake of the demo code 
# def generate_pdf(filename, content):
# """Generates a simple PDF with the given content."""
# try:
# c = canvas.Canvas(filename)
# c.drawString(100, 750, content) # Example content placement
# c.save()
# print(f"PDF '{filename}' generated successfully.")
# except Exception as e:
# print(f"An error occurred during PDF generation: {e}")
'''

# pjfParse.py ("/home/jku/git/jksfoTemp/python3/postJobFreeParse", "pjfParse.py", False)
def main(filepath, filename, write_to_stdout=False):
# def main():
  '''Main function to demonstrate usage.'''
  try:
    
    # sub call 
    time_string = print_current_time()
    
    if time_string: # Check if time_string is not None (meaning print_current_time was successful)
    # generate_pdf("current_time.pdf", f"The current time is: {time_string}")
      print(f"The current time is: {time_string}")
    else:
      print("Could not retrieve the current time, so PDF was not created.")

    # Sample HTML snippet
    html = """<h3 class="itemTitle"><a href="https://www.postjobfree.com/job/v1hyua/data-entry-clerk-san-francisco-ca" 
    rel="nofollow">Data Entry Clerk</a></h3><div class="normalText"><span class="colorCompany">Sciolex Corporation / 
    Advantech Global</span>&nbsp;–&nbsp;<span class="colorLocation">San Francisco, CA</span><div class="colorSalary">
    22.5USD per hour</div><div><span class="jdSnippet">... Responsibilities The <b>Data</b> <b>Entry</b> Clerk is a permanent,
    full-time position supporting the overall mission of the U.S. Citizenship and Immigration Services(USCIS) by facilitating 
    the operations of a local Field Office. As a <b>Data</b> <b>Entry</b> Clerk, your ...</span> - <span class="colorDate">
    Feb 17</span></div></div>"""
    # print (html)

    print(filepath, filename, write_to_stdout) 
    ''' Template code for parsing HTML data 
    # def main(filepath, filename, write_to_stdout=False):
    # # Ensure file exists before proceeding
    # if not os.path.exists(filepath):
    # print(f"Error: The file '{filepath}' does not exist.")
    # sys.exit(1)

    # # Set output file path with '.out' extension
    # output_filepath = os.path.splitext(filename)[0] + '.out'

    # # Extract data from HTML file
    # extracted_data = extract_data_from_html(filepath)
    '''
    
    extract_data_from_html(html, write_to_stdout) # strObj 
    
  except Exception as e:
    print(f"An error occurred in main: {e}")

if __name__ == "__main__":
  main(sys.argv[0], sys.argv[1], sys.argv[2])

'''
Install Libraries: Make sure you have the required libraries installed: pip install numpy reportlab
Save: Save the code as a .py file (e.g., time_pdf.py).
'''
