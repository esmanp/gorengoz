# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JMYGj5qouK0i7mVVfOV2h3AmpFBByy7f
"""

import numpy as np
import pandas as pd
     

#!pip install simpletransformers
from simpletransformers.classification import ClassificationModel

dt= pd.read_csv("/content/teknofest_train_final.csv",sep="|")
dt.head()

"""loodos/bert-base-turkish-uncased"""

dt["target"].unique()

dt["labels"] = pd.factorize(dt.target)[0]

dt

from sklearn.model_selection import train_test_split

train, test = train_test_split(dt, test_size=0.2, random_state=42)
     

train=train[["text","labels"]]
test=test[["text","labels"]]
     

#for bert text = string      label = int
train["text"]=train["text"].apply(lambda r: str(r))
train['labels']=train['labels'].astype(int)

"""--------------------------------------------------------------------------------"""

model = ClassificationModel('bert', 'dbmdz/bert-base-turkish-128k-cased', num_labels=5, use_cuda=False,args={'reprocess_input_data': True, "output_dir": "bert_model"})
model.train_model(train)

result, model_outputs, wrong_predictions = model.eval_model(test)

predictions = model_outputs.argmax(axis=1)
     
actuals = test.labels.values

from sklearn.metrics import accuracy_score
accuracy_score(actuals, predictions)

test

dene = test.iloc[752]['text']
print(dene)
     
tahmin=model_from_pickle.predict([dene])

tahmin

dt[(dt["text"]=="kıl herif gibi davranma")==True]