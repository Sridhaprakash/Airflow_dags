# Import necessary modules and classes from Airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads  # Assuming the correct path to your subdag_downloads module

# Import datetime module to specify the start date of the DAG
from datetime import datetime

# Define the main DAG named 'group_dag'
with DAG('group_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:

    # Define arguments to be passed to the subDAG
    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup}

    # Create a SubDagOperator named 'downloads' using the subdag_downloads SubDAG
    downloads = SubDagOperator(
        task_id='downloads',
        subdag=subdag_downloads(dag.dag_id, 'downloads', args)
    )

    # Define BashOperator task for checking files with simulated duration of 10 seconds
    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'  # Simulate checking files by sleeping for 10 seconds
    )

    # Define BashOperator tasks for transforming data (A, B, C) with simulated duration of 10 seconds each
    transform_a = BashOperator(
        task_id='transform_a',
        bash_command='sleep 10'  # Simulate transforming data A by sleeping for 10 seconds
    )

    transform_b = BashOperator(
        task_id='transform_b',
        bash_command='sleep 10'  # Simulate transforming data B by sleeping for 10 seconds
    )

    transform_c = BashOperator(
        task_id='transform_c',
        bash_command='sleep 10'  # Simulate transforming data C by sleeping for 10 seconds
    )

    # Set task dependencies to create the execution flow
    downloads >> check_files >> [transform_a, transform_b, transform_c]
    # Checking files must be completed before transforming data
