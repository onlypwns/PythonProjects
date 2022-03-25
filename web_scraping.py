import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(id='ResultsContainer')

job_elements = result.find_all('div', class_='card-content')

for job_element in job_elements:
    title = job_element.find('h2', class_='title')
    company = job_element.find('h3', class_='company')
    location = job_element.find('p', class_='location')
    print(title.text.strip())
    print(company.text.strip())
    print(f'{location.text.strip()}\n\n')
