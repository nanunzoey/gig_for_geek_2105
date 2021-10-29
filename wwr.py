import requests
from bs4 import BeautifulSoup

def get_wwr_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = []

  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_listings = soup.find('div', {'class':'jobs-container'}).find_all('section', {'class':'jobs'})

  for job_list in job_listings:
      features = job_list.find('ul').find_all('li', {'class':'feature'})
      for feature in features:
        link = feature.find('div',{'class':'tooltip'}).next_sibling['href']
        link = 'https://weworkremotely.com' + link
        company = feature.find('div',{'class':'tooltip'}).next_sibling.find('span',{'class':'company'}).string
        title = feature.find('div',{'class':'tooltip'}).next_sibling.find('span',{'class':'title'}).string
        region = feature.find('div',{'class':'tooltip'}).next_sibling.find('span',{'class':'region'}).string
        jobs.append({'title':title, 'company':company, 'region':region, 'link':link})

  return jobs