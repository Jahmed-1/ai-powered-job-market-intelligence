import requests
import pandas as pd


def fetch_arbeitnow_jobs():
    url = "https://www.arbeitnow.com/api/job-board-api"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return pd.DataFrame()

    data = response.json()
    jobs = data.get("data", [])

    job_list = []

    for job in jobs:
        job_list.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": job.get("description"),
            "url": job.get("url")
        })

    return pd.DataFrame(job_list)


if __name__ == "__main__":
    df = fetch_arbeitnow_jobs()
    print(df.head())
    print("Total jobs:", len(df))