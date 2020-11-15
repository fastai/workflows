from github import Github, UnknownObjectException, Repository
from fastcore.all import *
from fastcore.script import SCRIPT_INFO

def get_repo(repo:str=None, token=None) -> Repository:
    "Get a `Repository` object.  Optionally supply a `token` for private repositories."
    repo=ifnone(repo, os.getenv('GITHUB_REPOSITORY'))
    token = ifnone(token, os.getenv('INPUT_TOKEN'))
    assert repo, 'You must specify the repo parameter or set the `GITHUB_REPOSITORY` the environment variable.'
    try: 
        return Github(token).get_repo(repo)
    except UnknownObjectException as e:
        raise Exception(f'Repo: `{repo}` not found. If this is a private repo make sure you provide an appropriate token\n {e}')
        
def get_issues(repo:str=None, state:str='open', token:str=None):
    "Get all issues for a repository"
    return [i for i in get_repo(repo).get_issues(state=state)]
    
 
def create_issue(repo:str, title:str, body:str, token:str, skip_if_exists=False):
    "Create an issue and optionally ignore if an open issue with the same title already exists"
    r = get_repo(repo=repo, token=token)
    incumbent_issue = first([i for i in get_issues(repo=repo, state='open', token=token) if i.title.strip() == title.strip()])
    if incumbent_issue and skip_if_exists: 
        issue = incumbent_issue
        new_issue_created = False
    else: 
        issue = r.create_issue(title, body=body)
        new_issue_created = True

    print(f"::set-output name=bool_new_issue_created::{new_issue_created}")    
    print(f"::set-output name=related_issue_num::{issue.number}")
    print(f"::set-output name=related_issue_url::: {issue.html_url}")
    return issue
