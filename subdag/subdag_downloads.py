from airflow import DAG
from airflow.operators.bash import BashOperator

# Function to define a SubDAG for downloads
def subdag_downloads(parent_dag_id, child_dag_id, args):

    # Create a SubDAG with a unique name using parent and child DAG IDs
    with DAG(f"{parent_dag_id}.{child_dag_id}",
             start_date=args['start_date'],
             schedule_interval=args['schedule_interval'],
             catchup=args['catchup']) as dag:  # Define the SubDAG as part of the DAG context

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

    return dag  # Return the SubDAG definition
