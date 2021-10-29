import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

def get_re_jobs(word):
  jobs = []
  url = f"https://remoteok.io/remote-{word}-jobs"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, 'html.parser')

  rows = soup('tr',{'class':'job'})
  for row in rows:
    if 'closed' in row:
      continue
    company = row['data-company']
    link = 'remoteok.io' + row['data-href']
    title = row.find('h2', {'itemprop':'title'}).string
    try:
      region = row.find('td', {'class':'company_and_position'}).find('div', {'class':'location'}).text
    except AttributeError:
      region = "No location"
    jobs.append({'title':title,'company':company, 'region':region, 'link':link})

  return jobs