from clearml import Task
from train_model import train_and_evaluate


def launch_training_task():
    task = Task.init(
        project_name="My ML Project", task_name="Model Training on Latest Script"
    )
    # Print the task ID with a unique prefix
    print(f"TASK_ID_OUTPUT: {task.id}")
    task.execute_remotely(queue_name="gitarth", exit_process=True)
    train_and_evaluate(task)


if __name__ == "__main__":
    launch_training_task()
