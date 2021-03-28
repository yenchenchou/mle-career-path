# Airflow learning note

# Common components in Airflow (Local as example)
1. Import modules: need to create DAG and task 

    ```Python
    from datetime import timedelta

    # The DAG object; we'll need this to instantiate a DAG
    from airflow import DAG

    # Operators; we need this to operate!
    from airflow.operators.bash import BashOperator
    from airflow.utils.dates import days_ago
    ```

2. Default parameters

    ```Python
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    }
    ```

3. Initiate a DAG

    ```Python
    dag = DAG(
        'tutorial',
        default_args=default_args,
        description='A simple tutorial DAG',
        schedule_interval=timedelta(days=1),
        start_date=days_ago(2),
        tags=['example'],
    )
    ```

4. Create tasks

    ```Python
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag,
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
        dag=dag,
    )
    ```

5. Setting up dependencies for each task

    ```Python
    t1 >> t2
    ```