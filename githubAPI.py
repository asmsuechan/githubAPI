from github import Github
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

g = Github(login_or_token=GITHUB_ACCESS_TOKEN, per_page=100)
r = g.get_repo("BoostIO/Boostnote")

for pull in r.get_pulls('all'):
    # You can access pulls
    print(pull)
