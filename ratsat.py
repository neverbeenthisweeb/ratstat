import pandas as pd
import numpy as np

class Cramer:
  def __init__(self, data_frame, index, columns ):
    self.data_frame = data_frame
    self.index = index
    self.columns = columns
    self.pivot = pivot(data_frame, index, columns)
    self.index_sum = sum_index(self.pivot)
    self.columns_sum = sum_columns(self.pivot)
    self.cramer = cramer(self.pivot, 
                         self.index_sum, 
                         self.columns_sum) 
  
  def get_pivot(self):
    return self.pivot


def pivot(data_frame, index, columns):
  data_frame['counter'] = 1
  pivot_ = pd.pivot_table(df, 
                         values='counter', 
                         index=index, 
                         columns=columns,
                         aggfunc=np.sum)
  pivot_ = pivot_.fillna(0)                        
  return pivot_

def sum_index(pivot_frame):
  total = np.array([])
  index_ = np.asarray(pivot_frame.index) 
  for i in range(0, index_.size):
    total = np.append(total, pivot_frame.loc[index_[i]].sum())
  return total

def sum_columns(pivot_frame):
  total = np.array([])
  columns_ = np.asarray(pivot_frame.columns)
  for i in range(0, columns_.size):
    total = np.append(total, pivot_frame[columns_[i]].sum())
  return total

def cramer(pivot_frame, index_total, columns_total):
  observe = pivot_frame.values
  observe_total = observe.size
  r, k = observe.shape
  chi = 0
  for i in range(0, r):
    for j in range(0, k):
      expected = index_total[i] * columns_total[j] / observe_total
      chi += np.square(observe[i][j] - expected) / expected
  cramer = np.sqrt(chi / (observe_total * np.minimum(k-1, r-1)))
  return cramer, chi


