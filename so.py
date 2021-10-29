import requests
from bs4 import BeautifulSoup


def get_last_page(word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find('div', {'class':'s-pagination'}).find_all('a', {'class':'s-pagination--item'})
  last_page = pagination[-2].find('span').string
  return int(last_page)


def get_so_jobs(word):
  jobs = []
  last_page = get_last_page(word)
  for page in range(1, last_page+1):
    url = f"https://stackoverflow.com/jobs?r=true&q={word}&pg={page}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    rows = soup('div', {'class':'grid--cell fl1'})
    for row in rows:
      title = row.find('a')['title']
      link = row.find('a')['href']
      link = 'https://stackoverflow.com' + link
      company = row.find('h3').find('span').get_text(strip=True)
      region = row.find('h3').find('span',{'class':'fc-black-500'}).get_text(strip=True)
      jobs.append({'title':title, 'company':company, 'region':region,  'link':link})
  
  return jobs
