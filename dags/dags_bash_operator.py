# DAG에 대한 정의
from airflow import DAG
import datetime
import pendulum

from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # DAG의 이름 (DAG 파일명과 일치시키는것이 좋다)
    schedule="0 0 * * *", # cron 스케줄
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # task 이름 (객체명과 일치시키는 것이 좋다)
        bash_command="echo whoami", # 수행할 쉘스크립트
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    # task들의 수행 순서
    bash_t1 >> bash_t2