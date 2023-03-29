import csv
import requests
from bs4 import BeautifulSoup

# URL of the website with the table
url = 'https://hl7.org/fhir/valueset-participant-role.html'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table on the webpage with the class of "codes"
table = soup.find('table', {'class': 'codes'})

# Find all rows in the table
rows = table.find_all('tr')

# Use a set to remove any duplicates from the list of rows
unique_rows = set(rows)

# Create a new CSV file to write the data to
with open('participant-role-codeset.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers to the CSV file
    writer.writerow(['Code', 'System', 'Display'])

    # Loop through each unique row in the table
    for row in unique_rows:
        # Find all cells in the row
        cells = row.find_all('td')

        # Extract the data from the cells and write it to the CSV file
        if len(cells) == 3:
            code = cells[0].text.strip()
            system = cells[1].text.strip()
            display = cells[2].text.strip()

            # Format the code cell as a string
            writer.writerow([str(code), system, display])
