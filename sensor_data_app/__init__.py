from datetime import date

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app.store import StoreSensor

def create_app() -> dict:

    store_name = ["Strasbourg", "Paris", "Vasteras", "Munich", "Milan"]
    store_avg_visit = [800, 10000, 6000, 2000, 2500]
    store_std_visit = [50, 800, 500, 400, 100]
    perc_malfunction = [0.05, 0.1, 0.08, 0.05, 0.05]
    perc_break = [0.05, 0.08, 0.05, 0.02, 0]

    store_dict = dict()

    for i in range(len(store_name)): # range(5)
        store_dict[store_name[i]] = StoreSensor(
            store_name[i],
            store_avg_visit[i],
            store_std_visit[i],
            perc_malfunction[i],
            perc_break[i],
        )
    return store_dict