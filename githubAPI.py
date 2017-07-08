from github import Github
from dotenv import load_dotenv, find_dotenv
import os
import pdb
from pprint import pprint
import langid
import base64
import pymongo
import csv
# import pandas as pd

client = pymongo.MongoClient("mongo", 27017)
db = client.test

load_dotenv(find_dotenv())
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

g = Github(login_or_token=GITHUB_ACCESS_TOKEN, per_page=100)

# Get repositories which have over 5000 stars and count it
repositories = g.search_repositories('stars:>5000')
number_of_repos = 0
repos = []
# for page_number in range(9):
#   for repo in repositories.get_page(page_number):
#     number_of_repos += 1
#     # db.my_collection.insert_one([langid.classify(base64.b64decode(repo.get_readme().content)), repo]).inserted_id
#     print(number_of_repos)
#     db.my_collection.insert_one({'id': number_of_repos, 'lang': langid.classify(base64.b64decode(repo.get_readme().content)), 'repo_name': repo.full_name})

# Get stargazers of the repository
repository = g.get_repo('BoostIO/Boostnote')
stargazers = repository.get_stargazers()
for page_number in range(33, 0, -1):
  for stargazer in stargazers.get_page(page_number):
    f = open('stargazers.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')
    csvlist = []
    csvlist.append(stargazer.login)
    csvlist.append(stargazer.location)
    writer.writerow(csvlist)
    f.close()
    print(stargazer.location)
    # df = pd.read_csv('stargazers.csv', header=None, delim_whitespace=True)
    # se = pd.Series([stargazer.name, stargazer.login_or_token])
    # df.append(se)
    # df.to_csv('stargazers.csv')
    # db.my_collection.insert_one({'name': stargazer.name, 'location': stargazer.location})
    # pdb.set_trace()
    # print(stargazer)

def look_methods (obj):
  [attr for attr in dir(obj) if callable(getattr(obj,  str(attr)))]

# ~~~ MY PYTHON TRAINING ~~~
# pdb.set_trace()
# obj_methods = [attr for attr in dir(obj) if callable(getattr(obj,  str(attr)))]
# pprint(vars(object))
