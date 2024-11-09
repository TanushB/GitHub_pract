import google.generativeai as genai
import os
import subprocess

if __name__ == "__main__":
    api_key = os.environ['GEMINI_API_KEY']
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="You are a GitHub pull request (PR) summarizer. Your sole purpose is to review diffs that the user will provide, comparing changes made between master branch and the user's specific branch that they are trying to merge. Your goal is to provide a brief summary of all the changes you see in the diff, and comment on the quality of changes on a scale of 1 to 10, where 10 is best quality of life or functionality improvements, and 1 is arguably making the code worse. For your rating also explain why you rated the code change so.")
    command = ["git", "branch"]
    result = subprocess.run(command, capture_output=True, text=True)
    print("Result from git diff:")
    print(result)
    response = model.generate_content(f"The diff is: {result}")
    print(response.text)