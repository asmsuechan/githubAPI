from github import Github
from dotenv import load_dotenv, find_dotenv
import os
import pdb
from pprint import pprint

load_dotenv(find_dotenv())
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

g = Github(login_or_token=GITHUB_ACCESS_TOKEN, per_page=100)

# Get repositories which have over 5000 stars and count it
# repositories = g.search_repositories('stars:>5000')
# number_of_repos = 0
# for page_number in range(9):
#   for repo in repositories.get_page(page_number):
#     number_of_repos += 1
#     print(repo)
# print(number_of_repos)

# Get stargazers of the repository
repository = g.get_repo('BoostIO/Boostnote')
stargazers = repository.get_stargazers()
for page_number in range(100):
  for stargazer in stargazers.get_page(page_number):
      pdb.set_trace()
      print(stargazer)

# ~~~ MY PYTHON TRAINING ~~~
# pdb.set_trace()
# obj_methods = [attr for attr in dir(obj) if callable(getattr(obj,  str(attr)))]
# pprint(vars(object))
