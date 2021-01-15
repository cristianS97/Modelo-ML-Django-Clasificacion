# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 02:21:10 2021

@author: user
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

dataset = pd.read_csv('C:\\Users\\user\\Downloads\\Nueva carpeta\\glass.csv')

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 9]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

rcls = RandomForestClassifier(criterion='entropy', n_estimators=300, random_state=42)
rcls.fit(x_train, y_train)

y_pred = rcls.predict(x_test)

print(f'Accuracy is', rcls.score(x_test, y_test)*100, '%')

filename = 'C:\\Users\\user\\Downloads\\Nueva carpeta\\finalized_model.sav'

joblib.dump(rcls, filename)

