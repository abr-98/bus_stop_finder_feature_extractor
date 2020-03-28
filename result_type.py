import pandas as pd 
import numpy as np
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from keras.layers.normalization import BatchNormalization
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

s=MinMaxScaler()


df=pd.read_csv('feature.csv')

df.info()
model=Sequential()
#print(len(df))

#TRain
X=df[['zone','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_density','rsi','Weekend/day']].values
X_d=pd.DataFrame(X)
#X_d_2=pd.get_dummies(X_d)

y=df[['bus_stop','Signal','Turn']].values
y_d=pd.DataFrame(y)
#y_d_2=pd.get_dummies(y_d)

X_train, X_test, y_train, y_test = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
print(X_train)
X_train_2=pd.get_dummies(X_train,columns=[0,1,6,8])
#X_train_2[1] = X_train_2[1].astype(float)

#y_train_2=pd.get_dummies(y_train)
X_test_2=pd.get_dummies(X_test,columns=[0,1,6,8])
X_train_2=s.fit_transform(X_train_2)
X_test_2=s.transform(X_test_2)
#X_test_2[1] = X_test_2[1].astype(float)

#y_test_2=pd.get_dummies(y_test)
#n_cols=X_train_2.shape[1]
n_cols=X_train_2.shape[1]
print(n_cols)

model.add(Dense(20, activation='relu', input_shape=(n_cols,)))
model.add(BatchNormalization())
#model.add(Dropout(0.2))
model.add(Dense(40, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(80, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(3, activation='sigmoid'))

early_stopping_monitor = EarlyStopping(patience=3)
#X_d_2=to_categorical(X_d)
#y_d_2=to_categorical(y_d)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train_2, y_train, epochs=10000, callbacks=[early_stopping_monitor],batch_size=100)


#3
# evaluate the model
scores = model.evaluate(X_test_2, y_test)
scores_2 = model.evaluate(X_train_2, y_train)
#print(X_test)
#print(y_test)
#new_y_2=y_train[0].copy()
#new_y_d_2=pd.DataFrame(new_y_2)
#new_y=y_test[0].copy()
predictions=model.predict(X_test_2)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print("\n%s: %.2f%%" % (model.metrics_names[1], scores_2[1]*100))
