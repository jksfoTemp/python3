
# pjfParse.py

'''
Boilerplate python3 template code with error handling that calls a sub that prints 
the current time. It should have  reference to numpy, datetime, pdf and string libraries.

Demonstrates file access ... 

TODO: Add and print arguments to the main function to accept the job posting file path as input.
TODO: Add parsing code to extract the job description from the job posting.
 
'''

import datetime
import string
# import numpy as np  # Although not strictly needed for this example, included as requested
# from reportlab.pdfgen import canvas  # Although not strictly needed for this example, included as requested

def print_current_time():
    """Prints the current time in a formatted string."""
    try:
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time: {formatted_time}")

        # Example of string manipulation (as requested)
        uppercase_time = formatted_time.upper()
        print(f"Uppercase time: {uppercase_time}")

    except Exception as e:
        print(f"An error occurred in print_current_time: {e}")
        return None  # Or handle the error as appropriate

    return formatted_time # Return the formatted time if successful

# Might want this 
# def generate_pdf(filename, content):
#     """Generates a simple PDF with the given content."""
#     try:
#         c = canvas.Canvas(filename)
#         c.drawString(100, 750, content) # Example content placement
#         c.save()
#         print(f"PDF '{filename}' generated successfully.")
#     except Exception as e:
#         print(f"An error occurred during PDF generation: {e}")

def main():
    """Main function to demonstrate usage."""
    try:
        time_string = print_current_time()
        # if time_string: # Check if time_string is not None (meaning print_current_time was successful)
        #     generate_pdf("current_time.pdf", f"The current time is: {time_string}")
        # else:
        #     print("Could not retrieve the current time, so PDF was not created.")

    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()

'''

Install Libraries: Make sure you have the required libraries installed: pip install numpy reportlab
Save: Save the code as a .py file (e.g., time_pdf.py).
'''
