from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


dag = DAG(
    'mi_dag_desde_git',
    description='DAG cargado desde Git Bundle',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
)

task1 = BashOperator(
    task_id='tarea_desde_git',
    bash_command='echo "Ejecutando desde Git Bundle!"',
    dag=dag
)