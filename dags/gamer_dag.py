from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from services.drivers.selenium_driver import SeleniumDriver
from services.gamer import GamerService
from services import CONFIG


@task(task_id="Login")
def login(**kwargs):
    browser = SeleniumDriver()
    gamer_service = GamerService(browser, CONFIG.get("gamer"))
    gamer_service.login()
    browser.wait(1)
    ti = kwargs['ti']
    ti.xcom_push("gamer_cookies", gamer_service.browser.get_cookies())


@task(task_id="Get_lottery")
def get_lottery(**kwargs):
    browser = SeleniumDriver()
    cookies = kwargs['ti'].xcom_pull(task_ids='login', key="gamer_cookies")
    gamer_service = GamerService(browser, CONFIG.get("gamer"), cookies)
    gamer_service.get_lotteries()


@task(task_id="Get_coin")
def get_coin(**kwargs):
    browser = SeleniumDriver()
    cookies = kwargs['ti'].xcom_pull(task_ids='login', key="gamer_cookies")
    gamer_service = GamerService(browser, CONFIG.get("gamer"), cookies)
    gamer_service.get_coin()


with DAG(
        'Gamer_Daily_Quest',
        default_args={
            'depends_on_past': False,
            'email': ['b01201008@gmail.com'],
            'retries': 0,
            'retry_delay': timedelta(minutes=5),
        },
        description='A dag for finish gamer daily quest',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,
        tags=['gamer'],
) as dag:
    login_task = login()
    get_lottery_task = get_lottery()
    get_coin_task = get_coin()
    start = EmptyOperator(task_id="Start")
    finish = EmptyOperator(task_id="Finish")

    start >> login_task >> [get_lottery_task, get_coin_task] >> finish
