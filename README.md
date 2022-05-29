# Gamer Lottery Collector

running on airflow, using selenium to implement

## Features

- Login to gamer
- Earn the coin
- Collect the lotteries

Gamer is a popular forum in Taiwan. It provides prizes including funiture,electronic product, toy and os on.
User can get the lottry by spend coin or watch ads.
Gamer Lottery Collector can help you collect the coins and lotteries automatically.

## Tech

Gamer Lottery Collector uses some open source projects to work properly:

- [Apache Airflow] - programmatically author, schedule and monitor workflows.
- [Selenium] - automates browsers


## Installation
prepare environment for python 3.8

```sh
pip install -r requirements.txt

export AIRFLOW_HOME= path of this project

airflow db init

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```

Start airflow service:

```sh
airflow webserver --port 8080

airflow scheduler
```

**Free Software, Hell Yeah!**

   [Apache Airflow]: <https://airflow.apache.org/>
   [Selenium]: <https://www.selenium.dev/>
