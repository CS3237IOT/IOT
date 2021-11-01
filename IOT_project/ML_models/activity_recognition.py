import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib



thisdict = {
  "0": "idle",
  "1": "jumping jack",
  "2": "push-up",
  "3": "running",
  "4": "sit-up",
  "5": "walking"
}

def read_data(filename):
    df = pd.read_csv(filename)
    df = df.drop(['Time', 'Temperature', 'Humidity', 'Pressure_Millibars'], 1)
    return df



def produce_magnitude(df, columns, activity):
    for column in columns:
        df['mag_' + column] = np.sqrt(df['x_'+ column]**2 + df['y_'+column]**2 + df['z_' + column]**2)
    df['activity'] = activity



def model(data):
    X=data[['x_accelerate','y_accelerate','z_accelerate','x_Gyroscope','y_Gyroscope','z_Gyroscope']]  # Features
    #X=data[['mag_accelerate','mag_Gyroscope','mag_Magnet']]
    y=data['activity']  # Labels
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
    #Create a Gaussian Classifier
    clf=RandomForestClassifier(n_estimators=10)
    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    #Import scikit-learn metrics module for accuracy calculation
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    joblib.dump(clf, "./random_forest.joblib")



# Time,Temperature,Humidity,x_accelerate,y_accelerate,z_accelerate,x_Gyroscope,y_Gyroscope,z_Gyroscope, x_Magnet,y_Magnet,z_Magnet,Pressure_Millibars
df_1 = read_data('sensorTag_idle.csv')
df_1 = df_1.set_index(np.arange(len(df_1)) // 50).mean(level=0)
produce_magnitude(df_1, ['accelerate','Gyroscope','Magnet'],int(0))

df_2 = read_data('sensorTag_walk.csv')
df_2 = df_2.set_index(np.arange(len(df_2)) // 50).mean(level=0)
produce_magnitude(df_2, ['accelerate','Gyroscope','Magnet'], int(5))
df_1 = df_1.append(df_2)
df_1 = df_1[df_1!=0].dropna()

df_3 = read_data('sensorTag_run.csv')
df_3 = df_3.set_index(np.arange(len(df_3)) // 50).mean(level=0)
produce_magnitude(df_3, ['accelerate','Gyroscope','Magnet'],int(3))
df_1 = df_1.append(df_3)
df_1 = df_1[df_1!=0].dropna()


df_4 = read_data('sensorTag_pushup.csv')
df_4 = df_4.set_index(np.arange(len(df_4)) // 50).mean(level=0)
produce_magnitude(df_4, ['accelerate','Gyroscope','Magnet'], int(2))
df_1 = df_1.append(df_4)
df_1 = df_1[df_1!=0].dropna()



df_5 = read_data('sensorTag_situp.csv')
df_5 = df_5.set_index(np.arange(len(df_5)) // 50).mean(level=0)
produce_magnitude(df_5, ['accelerate','Gyroscope','Magnet'],int(4))
df_1 = df_1.append(df_5)
df_1 = df_1[df_1!=0].dropna()



df_6 = read_data('sensorTag_jumping.csv')
df_6 = df_6.set_index(np.arange(len(df_6)) // 50).mean(level=0)
produce_magnitude(df_6, ['accelerate','Gyroscope','Magnet'], int(1))
df_1 = df_1.append(df_6)
df_1 = df_1[df_1!=0].dropna()

print(df_1)

model(df_1)





