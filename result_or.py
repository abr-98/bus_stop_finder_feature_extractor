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


df=pd.read_csv('feature.csv')

df.info()
model=Sequential()
#print(len(df))

#TRain
X=df[['zone','time_level','next_stop_distance','total_waiting_time','Day','wifi_count','honks','Population_density','rsi']].values
X_d=pd.DataFrame(X)
#X_d_2=pd.get_dummies(X_d)

y=df['bus_stop'].values
y_d=pd.DataFrame(y)
#y_d_2=pd.get_dummies(y_d)

X_train, X_test, y_train, y_test = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
print(X_train)
X_train_2=pd.get_dummies(X_train,columns=[0,1,4,7])
#X_train_2[1] = X_train_2[1].astype(float)

#y_train_2=pd.get_dummies(y_train)
X_test_2=pd.get_dummies(X_test,columns=[0,1,4,7])
#X_test_2[1] = X_test_2[1].astype(float)

#y_test_2=pd.get_dummies(y_test)
#n_cols=X_train_2.shape[1]
n_cols=X_train_2.shape[1]
print(n_cols)

model.add(Dense(200, activation='relu', input_shape=(n_cols,)))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(300, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(300, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))
model.add(Dense(400, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(300, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(450, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(600, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(700, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(800, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
'''model.add(Dense(800, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(1000, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))'''
model.add(Dense(1, activation='sigmoid'))


early_stopping_monitor = EarlyStopping(patience=3)
#X_d_2=to_categorical(X_d)
#y_d_2=to_categorical(y_d)
model.compile(optimizer='RMSprop', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train_2, y_train, epochs=350, callbacks=[early_stopping_monitor],batch_size=100)


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
