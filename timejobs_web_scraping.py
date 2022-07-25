from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are familiar with')
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")



def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'html.parser')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        published_date = job.find('span', class_="sim-posted").span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.strip()
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a["href"]
            if (unfamiliar_skill not in skills) and (unfamiliar_skill.capitalize() not in skills):
                print(f"Company Name: {company_name.strip()}")
                print(f"Requiered Skills: {skills.strip()}")
                print(f"More info: {more_info}")

                print('')

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 0.5
        print(f"Waiting  {time_wait} minutes................. ")
        time.sleep(time_wait*60)
