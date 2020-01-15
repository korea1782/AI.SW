by. korea1782
```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# 엑셀(xlsx) 데이터 불러오기
data = pd.read_excel('homework1 data.xlsx')
data


# In[33]:


data_np = data.to_numpy()
# 결측이 아닌 위치 추출
notna_bool = data.notna()
notna_bool_arr = notna_bool.to_numpy()
print(notna_bool, )
non_missing_idx = np.argwhere(data.notna().to_numpy())
print(non_missing_idx)


# In[43]:


# 결측치 생성 (train_test_split 이용, test_size=0.1)
from sklearn.model_selection import train_test_split
idx = np.arange(non_missing_idx.shape[0])
train_idx, test_idx = train_test_split(idx, test_size=0.1)
data_incomplete = np.array(data.copy())# numpy array로부터 shallow copy 하지 않도록 주의
data_incomplete[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]] = np.nan
print(data_incomplete)
missing_true = data_np[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]


# In[21]:


# 평균으로 결측치 대입 (SimpleImpute)
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
imputer_mean = SimpleImputer(missing_values=np.nan, strategy ='mean')
imputer_mean.fit(data_incomplete)
data_filled_mean = imputer_mean.transform(data_incomplete)


# In[22]:


# test_idx에 대해 MSE 계산
missing_answer = data.to_numpy()[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]
missing_prediction_mean = data_filled_mean[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]
error = missing_answer - missing_prediction_mean
mse_mean = mean_squared_error(missing_answer, missing_prediction_mean)
print(f'MSE-Mean : {mse_mean}')


# In[25]:


# KNN 방법으로 결측치 대입(k=5)
from sklearn.impute import KNNImputer
imputer_knn = KNNImputer(n_neighbors=5)
data_filled_knn = imputer_knn.fit_transform(data_incomplete)

missing_prediction_knn = data_filled_knn[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]
mse_knn = mean_squared_error(missing_answer, missing_prediction_knn)
print('MSE-KNN: %f' % mse_knn)


# In[30]:


# test_idx에 대해 MSE 계산
missing_answer = data.to_numpy()[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]
missing_prediction_mean = data_filled_mean[non_missing_idx[test_idx, 0], non_missing_idx[test_idx, 1]]
error = missing_answer - missing_prediction_mean
mse_mean = mean_squared_error(missing_answer, missing_prediction_mean)
print(f'MSE-Mean : {mse_mean}')


# In[ ]:




```
