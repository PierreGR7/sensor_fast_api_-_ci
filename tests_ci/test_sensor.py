import unittest
from datetime import date

import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from sensor_data_app.sensor import SensorVisitCount

class TestSensorVisitCount(unittest.TestCase):

    def test_open_on_weekdays(self):
        for day in range(12,18): #12th monday to 17th saturday in january 2026
            with self.subTest(i=day):
                capteur = SensorVisitCount(1000,100)
                visit_count_per_day = capteur.simulate_visit_count(date(2026,1,day))
                self.assertFalse(visit_count_per_day == -1)

    def test_sunday_closed(self):
        visit_sensor = SensorVisitCount(1000, 100)
        visit_count = visit_sensor.simulate_visit_count(date(2026, 1, 18))
        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        visit_sensor = SensorVisitCount(1000, 100, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(2026, 2, 6))
        self.assertEqual(visit_count, 0)

    def test_with_malfunction(self):
        visit_sensor = SensorVisitCount(1000, 100, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(2026, 2, 6))
        self.assertEqual(visit_count, 254) # did python3 sensor_data_app/sensor.py 2026-2-6 for perc_malfunction = 10 and got 254



if __name__ == "__main__":
    unittest.main()