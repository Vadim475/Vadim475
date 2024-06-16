import requests
from bs4 import BeautifulSoup
import os


base_url = 'https://docs.python.org/3/library/index.html'
response = requests.get(base_url)

if response.status_code != 200:
    raise Exception(f"Failed  {base_url}")

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('a.reference.internal')[:10]

output_dir = 'python_docs'
os.makedirs(output_dir, exist_ok=True)

for link in links:
    href = link.get('href')
    title = link.get_text()
    url = f'https://docs.python.org/3/library/{href}'
    
    page_response = requests.get(url)
    if page_response.status_code != 200:
        print(f"Failed {url}")
        continue
    
    
    file_name = f"{output_dir}/{title}.html"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(page_response.text)
    

    print(f"_Saved {title} to {file_name}_")



