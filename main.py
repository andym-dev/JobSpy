# pip install python-jobspy

from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "glassdoor"],
    search_term="Brand Manager",
    location="London, UK",
    results_wanted=10,
    country_indeed='UK'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", index=False) # to_xlsx

