#BS4
import requests
from bs4 import BeautifulSoup

# Make a request to the website you want to scrape
response = requests.get('https://www.google.com/')

# Create a BeautifulSoup object from the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Iterate over the links and print them out
for link in links:
    print(link['href'])

# Find all the elements with the class 'h3'
h3_elements = soup.find_all('h3')

# Extract the text from the h3 elements and print it out
for h3_element in h3_elements:
    print(h3_element.text)

# Find the first element with the id 'footer'
footer_element = soup.find('div', id='footer')

# Extract all the child elements of the footer element and print them out
footer_children = footer_element.find_all('*')
for footer_child in footer_children:
    print(footer_child.name)

# Save the scraped data to a file
with open('scraped_data.txt', 'w') as f:
    f.write(str(soup))
