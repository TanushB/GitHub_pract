import google.generativeai as genai
import requests
import os

pr_number = os.getenv('GITHUB_REF').split('/')[-2]
repo = os.getenv('GITHUB_REPOSITORY')  # e.g., 'username/repo-name'
token = os.getenv('GITHUB_TOKEN')

def get_pr_diff(repo, pr_number, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3.diff'
    }
    url = f'https://api.github.com/repos/{repo}/pulls/{pr_number}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text  # This will be the raw diff
    else:
        raise Exception(f"Failed to fetch diff: {response.status_code} - {response.text}")

if __name__ == "__main__":
    api_key = os.environ['GEMINI_API_KEY']
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are a GitHub pull request (PR) summarizer. Your sole purpose is to review diffs that the user will provide, comparing changes made between master branch and the user's specific branch that they are trying to merge. Your goal is to provide a brief summary of all the changes you see in the diff, and comment on the quality of changes on a scale of 1 to 10, where 10 is best quality of life or functionality improvements, and 1 is arguably making the code worse. For your rating also explain why you rated the code change so.")
    response = model.generate_content(f"The diff is: {get_pr_diff(repo, pr_number, token)}")
    print(response.text)