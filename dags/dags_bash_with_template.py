from airflow import DAG
import pendulum

from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo "data_interval_end: {{ data_interval_end }} "'
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE':'{{data_interval_start | ds}}',
            'END_DATE': '{{data_interval_end | ds}}'
        },
        bash_commands='echo $START_DATE && echo $END_DATE'
        # && 앞에 있는 cmd 가 성공하면 뒤에 있는 cmd를 실행하겠다
    )

    bash_t1 >> bash_t2