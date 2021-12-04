# National University of Singapore 
# CS3227 Internet of Things Final Project
# Product Name: FitTrack
# Done by: Qing Bowen, Tsai Ming Chin, Mao Yiru, Lian Jiade

1. Repository contains python scripts for laptop to receive sensor data from TI CC2650 SensorTags for data pre-processing, Machine learning prediction and upload of firebase Real-Time Database `IOT_project`
1. Repository contains Java code for the Android App which displays real-time data of your current physical activity and long-term storage of past exercise data `IOTAPP`
1. Repository contains machine learning model for fitness activity recognition using accelerometer and gyrometer data `ActivityRecognition_ML`
1. Repository contains machine learning model for heat injury risk warning using temperature and humudity data `HeatInjury_ML`


# Product Description
A comprehensive IoT fitness product that aims to help Singapore and Chinese students prepare for their annual fitness exams and also for users to monitior and track their daily physical activity levels for their long term

# Main Features
1. Fitness Activity Recognition for Running, idle, walking, push-up, sit-up and Jumpig Jack
1. Pose Detection of Push-up posture. Determines "standard close arm" and "not standard wide arm" push-up
1. Heat injury Risk warning. 5 heat injury risks levels (Safe, Attention, Warning, Dangerous and Extremely Dangerous) based on the heat index


![Overall Block Diagram](overall.png)



