from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


# Define a function for the first task (_t1)
def _t1(ti):
    # Push a value (42) to XCom with the key 'my_key'
    ti.xcom_push(key='my_key', value=42)


# Define a function for the BranchPythonOperator task (_branch)
def _branch(ti):
    # Pull the value stored in XCom with the key 'my_key' from the first task (_t1)
    value = ti.xcom_pull(key='my_key', task_ids='t1')
    # Branch based on the value retrieved from XCom
    if value == 42:
        return 't2'  # If value is 42, go to task t2
    return 't3'  # If value is not 42, go to task t3


# Define a function for the second task (_t2)
def _t2(ti):
    # Pull the value stored in XCom with the key 'my_key' from the first task (_t1)
    ti.xcom_pull(key='my_key', task_ids='t1')


# Define the main DAG named 'xcom_dag'
with DAG("xcom_dag", start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:
    # Task 1: PythonOperator to execute the _t1 function
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )

    # Task 2: BranchPythonOperator to execute the _branch function and determine the next task dynamically
    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )

    # Task 3: PythonOperator to execute the _t2 function
    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )

    # Task 4: BashOperator (t3) with a simple echo command
    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"
    )

    # Task 5: BashOperator (t4) with a simple echo command and a trigger rule
    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''",
        trigger_rule='none_failed_min_one_success'
    )

    # Set task dependencies to create the execution flow
    t1 >> branch >> [t2, t3] >> t4
