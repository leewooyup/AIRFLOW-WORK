from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task


with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date': '{{data_interval_start | ds}}', 'end_date':'{{data_interval_end | ds}}'}
        # jinja template 변수를 직접 주는 방식
    )

    @task(task_id='python_t2')
    def python_function2(**kwargs): # jinja template 변수들이 이미 들어있으니 꺼내 쓰는 방식
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + str(kwargs['data_interval_start']))
        print('data_interval_end:' + str(kwargs['data_interval_end']))
        print('task_instance:' + str(kwargs['ti']))

    python_t1 >> python_function2()