import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import sys

ascii_logo = r"""
    ____                        _          ______                            _           
   / __ \____  ____ ___  ____ _(_)___     / ____/  ______  ____ _____  _____(_)___  ____ 
  / / / / __ \/ __ `__ \/ __ `/ / __ \   / __/ | |/_/ __ \/ __ `/ __ \/ ___/ / __ \/ __ \
 / /_/ / /_/ / / / / / / /_/ / / / / /  / /____>  </ /_/ / /_/ / / / (__  ) / /_/ / / / /
/_____/\____/_/ /_/ /_/\__,_/_/_/ /_/  /_____/_/|_/ .___/\__,_/_/ /_/____/_/\____/_/ /_/ 
                                                 /_/                                                       
"""

# Check if the user has provided the necessary arguments
if len(sys.argv) < 2:
    print("Usage: python3 scanner.py <url> [-o <output_file>]")
    sys.exit(1)

# Parse the command line arguments
url = sys.argv[1]
output_file = None
if '-o' in sys.argv:
    output_file = sys.argv[sys.argv.index('-o') + 1]

# Send a request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the anchor elements in the HTML
anchors = soup.find_all('a')

# Extract the extensions from the anchor elements
extensions = []
for anchor in anchors:
    href = anchor.get('href')
    if href and '.' in href:
        extension = href.split('.')[-1]
        if extension not in extensions:
            extensions.append(extension)

# Sort the extensions alphabetically
extensions.sort()

# Create a table with the extensions
table_data = [[extension] for extension in extensions]
table_headers = ["Extensions"]
table = tabulate(table_data, headers=table_headers, tablefmt="grid", colalign=("center",))

# Print the table or save it to a file if specified
if output_file:
    with open(output_file, 'w') as file:
        file.write(table)
else:
    print(table)

print(ascii_logo)
print("Bababoi - Alfred")