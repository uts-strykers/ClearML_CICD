import sys
from clearml import Task
from train_model import train_and_evaluate


def launch_training_task(repo, branch, commit):
    task = Task.init(
        project_name="My ML Project", task_name="Model Training on Latest Script"
    )
    task.set_repo(repo=repo, branch=branch, commit=commit)
    # Print the task ID with a unique prefix
    print(f"TASK_ID_OUTPUT: {task.id}")
    task.execute_remotely(queue_name="gitarth", exit_process=True)
    train_and_evaluate(task)


if __name__ == "__main__":
    # Arguments order: repository URL, branch name
    repo_arg = sys.argv[1] if len(sys.argv) > 1 else None
    branch_arg = sys.argv[2] if len(sys.argv) > 2 else None
    launch_training_task(repo_arg, branch_arg)
