# Import necessary modules and classes from Airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

# Function to define a SubDAG for downloads
def download_task():

    # Define a TaskGroup named 'downloads' with a tooltip for better visualization
    with TaskGroup("downloads", tooltip="Downloads tasks") as group:
        # Task to simulate downloading data A by sleeping for 10 seconds
        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )

        # Task to simulate downloading data B by sleeping for 10 seconds
        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )

        # Task to simulate downloading data C by sleeping for 10 seconds
        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )

    return group  # Return the TaskGroup definition
