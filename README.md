# ClearML ML Model CI/CD Pipeline README
by Strykers Team
## Introduction

This repository contains a CI/CD pipeline designed to automate the training and monitoring of machine learning models using ClearML and GitHub Actions. This guide provides detailed instructions on how to set up and use the pipeline effectively, from forking the repository to making a pull request.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Fork the Repository](#fork-the-repository)
   - [Setting Up GitHub Secrets](#setting-up-github-secrets)
   - [Set Up Branch Protection Rules](#set-up-branch-protection-rules)
3. [Workflow Usage](#workflow-usage)
   - [Create a New Branch](#create-a-new-branch)
   - [Make Changes](#make-changes)
   - [Commit and Push Changes](#commit-and-push-changes)
   - [Create a Pull Request](#create-a-pull-request)
4. [CI/CD Pipeline Details](#cicd-pipeline-details)
5. [Files and Scripts Description](#files-and-scripts-description)
6. [Additional Resources](#additional-resources)

## Overview

This CI/CD pipeline is designed to automatically trigger on pull requests to the master branch, facilitating the execution of model training tasks via ClearML. It helps ensure all changes are thoroughly tested for performance and accuracy before merging.

## Getting Started

### Prerequisites

- **GitHub Account**: Necessary for repository operations.
- **ClearML Account**: Required for managing ML tasks. Sign up at [ClearML](https://clear.ml).

### Fork the Repository

Fork this GitHub repository to your own account to get started:
- Navigate to the repository URL.
- Click on the "Fork" button at the top right corner of the page.

### Setting Up GitHub Secrets

After forking the repository, set up the following secrets in your GitHub repository to ensure the Actions workflows can communicate securely with external services:

1. **Go to your forked repository** on GitHub.
2. Navigate to **Settings > Secrets > Actions**.
3. Click on **New repository secret** for each of the following:
   - **`ACCESS_KEY`**: Your ClearML API access key.
   - **`SECRET_KEY`**: Your ClearML API secret key.
   - **`CLEARML_API_HOST`**: Your ClearML API server URL.
   - **`CLEARML_WEB_HOST`**: Your ClearML web server URL.
   - **`CLEARML_FILES_HOST`**: Your ClearML files server URL.
   - **`GH_TOKEN`**: A GitHub token with permissions to access repositories and make comments on pull requests.

### Set Up Branch Protection Rules
Branch protection rules help safeguard your master (or main) branch against unwanted changes.
1. **Go to your forked repository on GitHub.**
2. **Click on "Settings"**, then select "Branches" in the sidebar.
3. **Add a branch protection rule** by clicking on "Add rule".
4. **Enter 'master'** in the "Branch name pattern" field (or 'main' if your default branch is named 'main').
5. **Configure the protection rules** such as:
   - Require pull request reviews before merging.
   - Require status checks to pass before merging.
   - Include administrators to enforce these rules even on repository administrators.
6. **Save the changes** by clicking on "Create" or "Save changes".


### Workflow Usage

#### 1. Create a New Branch
For new features or changes, always create a new branch:
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
git checkout -b feature-branch
```

#### 2. Make Changes
Modify the training script or other relevant files within your new branch.

#### 3. Commit Changes
After making changes, commit them to your branch:
```bash
git add .
git commit -m "Detailed description of changes"
git push origin feature-branch
```

#### 4. Create a Pull Request

- Go to your forked repository on GitHub.
- Click on "Compare & pull request" next to your new branch.
- Review the changes, ensure the base branch is set correctly, and submit the pull request.

## CI/CD Pipeline Details

The GitHub Actions workflow defined in `.github/workflows/clearml_ci_cd.yml` automates the following upon a pull request:
- Set environment variables using GitHub Secrets.
- Launch and monitor ClearML tasks.
- Post task results back to the pull request as comments.

## Files and Scripts Description

- `.github/workflows/clearml_ci_cd.yml`: Defines the GitHub Actions workflow.
- `check_clearml_task_running.py`: Monitors the status of the ClearML task and exits if the task fails.
- `create_stats_comment.py`: Retrieves the task metrics from ClearML and posts them as a comment to the pull request.
- `launch_training_task.py`: Initializes and starts a training task in ClearML.
- `train_model.py`: Contains the code for training the machine learning model.
- `requirements.txt`: Lists all the Python libraries required for the project.

## Additional Resources

For more detailed information on using ClearML and GitHub Actions, refer to:
- [ClearML Documentation](https://clear.ml/docs/latest/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)