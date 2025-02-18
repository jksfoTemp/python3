  # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract relevant data
    job_title = soup.find('h3', class_='itemTitle').get_text(strip=True) if soup.find('h3', class_='itemTitle') else 'N/A'
    company_name = soup.find('span', class_='colorCompany').get_text(strip=True) if soup.find('span', class_='colorCompany') else 'N/A'
    location = soup.find('span', class_='colorLocation').get_text(strip=True) if soup.find('span', class_='colorLocation') else 'N/A'
    salary = soup.find('div', class_='colorSalary').get_text(strip=True) if soup.find('div', class_='colorSalary') else 'N/A'
    job_description = soup.find('span', class_='jdSnippet').get_text(strip=True) if soup.find('span', class_='jdSnippet') else 'N/A'
    posting_date = soup.find('span', class_='colorDate').get_text(strip=True) if soup.find('span', class_='colorDate') else 'N/A'

    return {
        'job_title': job_title,
        'company_name': company_name,
        'location': location,
        'salary': salary,
        'job_description': job_description,
        'posting_date': posting_date
    }




# Function to write extracted data to the .out file and optionally to stdout
def write_to_file_or_stdout(output_data, output_filepath, write_to_stdout=False):
    try:
        with open(output_filepath, 'a', encoding='utf-8') as file:
            file.write(f"Job Title: {output_data['job_title']}\n")
            file.write(f"Company Name: {output_data['company_name']}\n")
            file.write(f"Location: {output_data['location']}\n")
            file.write(f"Salary: {output_data['salary']}\n")
            file.write(f"Job Description: {output_data['job_description']}\n")
            file.write(f"Posting Date: {output_data['posting_date']}\n")
            file.write("\n---\n")

        # Optionally print to stdout
        if write_to_stdout:
            print(f"Job Title: {output_data['job_title']}")
            print(f"Company Name: {output_data['company_name']}")
            print(f"Location: {output_data['location']}")
            print(f"Salary: {output_data['salary']}")
            print(f"Job Description: {output_data['job_description']}")
            print(f"Posting Date: {output_data['posting_date']}")
            print("\n---\n")

    except IOError as e:
        print(f"Error writing to file '{output_filepath}': {e}")
        sys.exit(1)




# Main function to orchestrate the extraction and writing process
def main(filepath, filename, write_to_stdout=False):
    # Ensure file exists before proceeding
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' does not exist.")
        sys.exit(1)

    # Set output file path with '.out' extension
    output_filepath = os.path.splitext(filename)[0] + '.out'

    # Extract data from HTML file
    extracted_data = extract_data_from_html(filepath)

    # Write extracted data to file and/or stdout
    write_to_file_or_stdout(extracted_data, output_filepath, write_to_stdout)



# Entry point to the script
if __name__ == '__main__':
    # Argument parsing
    if len(sys.argv) < 3:
        print("Usage: python script.py <filepath> <filename> [--stdout]")
        sys.exit(1)

    filepath = sys.argv[1]
    filename = sys.argv[2]
    write_to_stdout = '--stdout' in sys.argv  # Check if we need to print to stdout

    # Call the main function with provided arguments
    main(filepath, filename, write_to_stdout)
