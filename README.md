# Gamer Lottery Collector

[Gamer] is a popular forum in Taiwan. It provides prizes including furniture,electronic product, toy and os on.
User can get the lottery by spend coin or watch ads.
Gamer Lottery Collector can help you collect the coins and lotteries automatically.

## Features

- Login to gamer forum
- Earn the coin
- Collect the lotteries of the prize

## Tech

Gamer Lottery Collector uses some open source projects to work properly:

- [Apache Airflow] - programmatically author, schedule and monitor workflows.
- [Selenium] - automates browsers


## Installation
prepare environment for python 3.8

install [Chrome Driver] for selenium

```sh
pip install -r requirements.txt

export AIRFLOW_HOME= path of this project

airflow db init
```

Create airflow services:

```sh
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

## License

**Free Software, Hell Yeah!**

   [Gamer]: <https://www.gamer.com.tw/>
   [Apache Airflow]: <https://airflow.apache.org/>
   [Selenium]: <https://www.selenium.dev/>
   [Chrome Driver]: <https://chromedriver.chromium.org/>
