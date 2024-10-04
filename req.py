import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://ollama.com/library"
file_name = 'models.json'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h2> elements with the specified class
    model_elements = soup.find_all('h2', class_='truncate text-lg font-medium underline-offset-2 group-hover:underline md:text-2xl')

    # Extract model names and format them into a list of dictionaries
    model_names = [{"name": model.find('span').text.strip()} for model in model_elements if model.find('span')]

    # Print and save model names to JSON
    print("Model Names:")
    with open(file_name, 'w') as json_file:
        json.dump(model_names, json_file, indent=4)
        for model in model_names:
            print(model["name"])
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
