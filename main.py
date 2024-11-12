!pip install pandasql

import random
import datetime as dt

import numpy as np
import pandas as pd
from pandasql import sqldf

# Datasets generation

def generate_phone_number(prefixs: list, probabilities: list):
    random_prefix = np.random.choice(prefixs, 1, p=probabilities)[0]
    return f"+{random_prefix}{''.join(random.choices('0123456789', k=10))}"

def generate_date_of_birth(start_year: int, end_year: int):
    start_date = dt.datetime(start_year, 1, 1)
    end_date = dt.datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + dt.timedelta(days=random_days)


size_clients = 5000
size_campaigns = 35000

df_clients = pd.DataFrame(
    {
        "CLIENT_ID": np.arange(size_clients),
        "PHONE_NUMBER": (
            [generate_phone_number([998, 7, 42], [0.60, 0.25, 0.15]) for _ in range(size_clients)]
        ),
        "DATE_OF_BIRTH": [generate_date_of_birth(1940, 2005) for _ in range(size_clients)],
        "SEX": np.random.choice(["M", "F"], size=size_clients, p=[0.50, 0.50]),
        "IS_ACTIVE": np.random.choice([0, 1], size=size_clients, p=[0.16, 0.84])
    }
)

df_marketing_campaigns = pd.DataFrame(
    {
        "CLIENT_ID": np.random.choice(df_clients["CLIENT_ID"].unique(), size=size_campaigns),
        "CAMPAIGN_TYPE": np.random.choice(["UPGRADE", "SERVICE", "CHURN"], size=size_campaigns, p=[0.42, 0.30, 0.28]),
        "CAMPAIGN_REVENUE": np.random.randint(0, 120000, size=size_campaigns)
    }
)

display(df_clients)
display(df_marketing_campaigns)