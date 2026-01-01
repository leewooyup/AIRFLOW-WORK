from airflow import DAG
from airflow.decorators import task
import pendulum
from common.common_func import regist2
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id='regist2_t1',
        python_callable=regist2,
        op_args=['foo', 'man', 'kr', 'seoul'],
        op_kwargs={'email': 'foo@naver.com', 'phone': '010-0000-0000'}
    )

    regist2_t1