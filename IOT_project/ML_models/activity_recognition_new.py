import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier

files = ['sensorTag_idle.csv', 'sensorTag_jumping.csv', 'sensorTag_pushup.csv', 'sensorTag_run.csv', 'sensorTag_situp.csv', 'sensorTag_walk.csv']

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

temp_data = dict()
sensors = ['hax', 'hay', 'haz', 'hgx', 'hgy', 'hgz']
for i in range(len(files)):
    temp_data[i] = dict()
    temp_df = read_data(files[i])
    for j in range(len(temp_df)//50):
        temp = dict()
        temp['hax'] = temp_df.iloc[j*50:(j+1)*50, 0]
        temp['hay'] = temp_df.iloc[j*50:(j+1)*50, 1]
        temp['haz'] = temp_df.iloc[j*50:(j+1)*50, 2]
        temp['hgx'] = temp_df.iloc[j*50:(j+1)*50, 3]
        temp['hgy'] = temp_df.iloc[j*50:(j+1)*50, 4]
        temp['hgz'] = temp_df.iloc[j*50:(j+1)*50, 5]
        """
        temp['hmx'] = temp_df.iloc[j*50:(j+1)*50, 6]
        temp['hmy'] = temp_df.iloc[j*50:(j+1)*50, 7]
        temp['hmz'] = temp_df.iloc[j*50:(j+1)*50:, 8]
        for sensor in sensors:
            _, temp[sensor + '_Pxx_spec'] = signal.periodogram(temp[sensor], fs=10) # Estimate power spectral density using a periodogram
            _, _, temp[sensor + '_Sxx_spec'] = signal.spectrogram(temp[sensor], fs=10, return_onesided=False) # Compute a spectrogram with consecutive Fourier transforms
        """
        temp_data[i][j] = temp

data = []
for i in range(6):
    for j in range(len(temp_data[i])):
        temp = dict()
        for key, value in temp_data[i][j].items():
            temp[key + '_mean'] = np.mean(value)
            temp[key + '_max'] = np.max(value)
            temp[key + '_min'] = np.min(value)
            temp[key + '_median'] = np.median(value)
            temp[key + '_std'] = np.std(value)
            temp[key + '_var'] = np.var(value)
            temp[key + '_p10'] = np.percentile(value, 10)
            temp[key + '_p25'] = np.percentile(value, 25)
            temp[key + '_p75'] = np.percentile(value, 75)
            temp[key + '_p90'] = np.percentile(value, 90)
        temp['activity'] = i
        data.append(temp)

df = pd.DataFrame(data, columns=['hax_mean', 'hax_max', 'hax_min', 'hax_median', 'hax_std', 'hax_var', 'hax_p10', 'hax_p25', 'hax_p75', 'hax_p90', 'hay_mean', 'hay_max', 'hay_min', 'hay_median', 'hay_std', 'hay_var', 'hay_p10', 'hay_p25', 'hay_p75', 'hay_p90', 'haz_mean', 'haz_max', 'haz_min', 'haz_median', 'haz_std', 'haz_var', 'haz_p10', 'haz_p25', 'haz_p75', 'haz_p90', 'hgx_mean', 'hgx_max', 'hgx_min', 'hgx_median', 'hgx_std', 'hgx_var', 'hgx_p10', 'hgx_p25', 'hgx_p75', 'hgx_p90', 'hgy_mean', 'hgy_max', 'hgy_min', 'hgy_median', 'hgy_std', 'hgy_var', 'hgy_p10', 'hgy_p25', 'hgy_p75', 'hgy_p90', 'hgz_mean', 'hgz_max', 'hgz_min', 'hgz_median', 'hgz_std', 'hgz_var', 'hgz_p10', 'hgz_p25', 'hgz_p75', 'hgz_p90', 'activity'])

def model(data):
    X=data[['hax_p25', 'hgy_p75', 'hay_median', 'hgx_mean', 'hgy_mean', 'hgx_p25', 'hax_median', 'hay_p75', 'hgy_p25', 'hax_p10', 'hgx_median', 'hay_p90', 'hgx_p10', 'hay_min', 'hax_max', 'haz_median', 'hay_mean', 'hax_mean', 'hgy_var', 'hgz_min']]  # Features

    scaler= StandardScaler()
    scaler.fit(X)
    X=scaler.transform(X)

    scaler_filename = "scaler.joblib"
    joblib.dump(scaler, scaler_filename)

    #X=data[['mag_accelerate','mag_Gyroscope','mag_Magnet']]
    y=data['activity']  # Labels
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
    
    #Create a Gaussian Classifier
    #clf=RandomForestClassifier(n_estimators=10)
    
    clf = OneVsOneClassifier(LinearSVC(random_state=0))
    
    
    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    #Import scikit-learn metrics module for accuracy calculation
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    joblib.dump(clf, "./onevsonelinearsvc.joblib")

top20_df = df[['hax_p25', 'hgy_p75', 'hay_median', 'hgx_mean', 'hgy_mean', 'hgx_p25', 'hax_median', 'hay_p75', 'hgy_p25', 'hax_p10', 'hgx_median', 'hay_p90', 'hgx_p10', 'hay_min', 'hax_max', 'haz_median', 'hay_mean', 'hax_mean', 'hgy_var', 'hgz_min', 'activity']]

model(top20_df)
