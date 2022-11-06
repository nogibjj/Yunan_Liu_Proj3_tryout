from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/workspaces/Yunan_Liu_Proj3_tryout/fresh-span-361719-e4e6a5688c1e.json')

project_id = 'fresh-span-361719'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
    SELECT distinct pl.id, pl.creation_date, pa.score
    FROM `bigquery-public-data.stackoverflow.post_links` pl
    LEFT JOIN `bigquery-public-data.stackoverflow.posts_answers` pa
    on pl.id = pa.id
    order by score desc """)

results = query_job.result()
count = 0
for row in results:
    print(row)
    count += 1
    if count == 5:
        break