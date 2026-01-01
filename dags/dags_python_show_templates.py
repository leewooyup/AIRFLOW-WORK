from airflow import DAG
from airflow.decorators import task
import pendulum


with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 12, 20, tz="Asia/Seoul"),
    catchup=True,
    tags=["example"],
) as dag:

    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs) # 리스트나 딕셔너리를 줄넘김이 이쁘게 출력된다

    show_templates()