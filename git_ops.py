import subprocess

def fetch_commit_file(commit_id, repo_path, file_path):
    result = subprocess.run(['git', 'show', f'{commit_id}:{file_path}'], cwd=repo_path, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Error fetching file: {result.stderr}")
        return None

def save_commit_file(content, save_path):
    with open(save_path, 'w') as file:
        file.write(content)
