from clearml import Task


def launch_training_task():
    task = Task.init(
        project_name="My ML Project", task_name="Model Training on Latest Script"
    )
    task.set_script("train_model.py")  # Assumes train_model.py is in the root directory
    task.execute_remotely(queue_name="gitarth", exit_process=True)

    # Write task ID to a file
    with open("task_id.txt", "w") as file:
        file.write(task.id)


if __name__ == "__main__":
    launch_training_task()
