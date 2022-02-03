try:
    from datetime import timedelta
    from datetime import datetime
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator

    print("All DAG modules are imported...")
except Exception as e:
    print("Error {}".format(e))


def hello_world_execute(*args, **kwargs):
    variable = kwargs.get("name", "NO NAME")

    return "hello world " + variable


with DAG(
        dag_id="hello_world_dag",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 31),
        },
        catchup=False,
) as f:
    hello_world_execute = PythonOperator(
        task_id="hello_world_execute_task",
        python_callable=hello_world_execute,
        op_kwargs={"name": "Sakthivel"},
    )
