# pip install python-jobspy

from jobspy import scrape_jobs
from datetime import datetime

job_title_to_search = 'Head of Procurement'

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "glassdoor"],
    search_term=job_title_to_search,
    location="London, UK",
    results_wanted=30,
    country_indeed='UK'  # only needed for indeed / glassdoor
)

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv(f"{job_title_to_search} __ {current_datetime} .csv", index=False) # to_xlsx