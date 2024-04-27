import sys
from clearml import Task
from train_model import train_and_evaluate


def launch_training_task(repo_url, branch_name, commit_hash):
    task = Task.init(
        project_name="My ML Project", task_name="Model Training on Latest Script"
    )
    # Print the task ID in a format that can be easily captured
    print(f"TASK_ID_OUTPUT: {task.id}")
    task.set_repo(repo=repo_url, branch=branch_name, commit=commit_hash)
    task.set_script("train_model.py")
    task.execute_remotely(queue_name="gitarth", exit_process=True)


if __name__ == "__main__":
    repo_url = sys.argv[1]
    branch_name = sys.argv[2]
    commit_hash = sys.argv[3]
    launch_training_task(repo_url, branch_name, commit_hash)
