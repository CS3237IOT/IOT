# NUS CS3237 Internet of Things Final Project
### Done by: Qing Bowen, Tsai Ming Chin, Mao Yiru, Lian Jiade


1. `IOT_project` Repository contains python scripts for laptop to receive sensor data from TI CC2650 SensorTags for data pre-processing, Machine learning prediction and upload of data to Firebase Real-Time Database 
2. `IOTAPP` Repository contains Java code for the Android App which displays real-time data of your current physical activity, long-term storage of past exercise data and Pose Detection of Push-up to determine the corectness of the push-up posture
3. `ActivityRecognition_ML` Repository contains machine learning model for fitness activity recognition using accelerometer and gyrometer data collected from TI CC2650 Sensor tags
4. `HeatInjury_ML` Repository contains machine learning model for heat injury risk warning using temperature and humudity data collected from TI CC2650 Sensor tags

# Product Name: FitTrack
**Product Description**<br />
A comprehensive IoT fitness product that aims to help Singapore and Chinese students prepare for their annual fitness exams and also for general users to monitior and track their daily physical activity levels for their long term health needs <br />

**App Interface**<br />
![App Interface Diagram](https://github.com/CS3237IOT/IOT/blob/main/resources/app_Interface.png)


# Main Features
1. **Fitness Activity Recognition** for Running, idle, walking, push-up, sit-up and Jumpig Jack
2. **Storage of all Fitness Data** for long-term analytics and activity tracking
3. **Pose Detection of Push-up Posture** Determines "standard close arm" and "not standard wide arm" push-up
4. **Heat injury Risk Warning** 5 heat injury risks levels (Safe, Attention, Warning, Dangerous and Extremely Dangerous) based on the NOAA Heat Index

# IOT System Architecture <br />
![Overall Block Diagram](https://github.com/CS3237IOT/IOT/blob/main/resources/System_Design.png)

### Detailed Explaination of Project
*Take a look at the final report* `Group22_final_report.pdf` *for more detailed description of the Features, Machine Learning Techniques and System Design*
