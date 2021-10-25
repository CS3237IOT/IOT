# Scripts to run to test the sensor and ML Model

## Instructions

For 1 Sensor (hand): 
1. `run python3 cc2650_1s.py` 
1. `run python3 middle_1s.py` 

For 2 Sensor (hand+body): 
1. `run python3 cc2650_1s.py` 
1. `run python3 cc2650_2s.py.py` 
1. `run python3 middle_2s.py`


## Reminders
1. The current machine learning model in the repository random_forest.joblib is generated using MC's Classify.ipynb code. It is for hand-only data and uses x,y,z accelrometer, gyrometer and magnetometer values.

1. If you want to use different ML model such as hand+body data or use magnitude data instead, remeber to change the code in Classify.ipynb and package a new ML model and replace it with the current one. Also change the code in `cc2650_1s.py` and `cc2650_1s.py` accordingly to reflect the new model inputs
