import numpy as np
import pandas as pd

# NOTE: This data is for testing purpose, later will be deleted
df = pd.read_csv('dataset/fifa.csv', index_col=0, low_memory=False)


def cramer(df, idx, col):
  df['counter'] = 1
  df_pivot = pd.pivot_table(df,
                            values='counter',
                            index=[idx],
                            columns=[col],
                            aggfunc=np.sum)
  df_pivot = df_pivot.fillna(0)
  
  idx_array = np.asarray(df_pivot.index)
  col_array = np.asarray(df_pivot.columns)

  # Getting total of each cols and rows
  idx_total = np.array([])
  col_total = np.array([])

  for i in range(0, idx_array.size):
    idx_total = np.append(idx_total, df_pivot.loc[idx_array[i]].sum())

  for j in range(0, col_array.size):
    col_total = np.append(col_total, df_pivot[col_array[j]].sum())

  obs = df_pivot.values
  obs_total = obs.size

  # print(obs, obs_total)

  r, k = obs.shape
  # NOTE: chi is for chi-squared
  chi = 0

  for i in range(0, r):
      for j in range(0, k):
          expected = idx_total[i] * col_total[j] / obs.size
          chi += np.square(obs[i][j] - expected) / expected

  # print(chi)
  cramer = np.sqrt(chi / (obs.size * np.minimum(k - 1, r - 1)))

  # print(cramer)
  return cramer


print(cramer(df, 'Nationality', 'Club'))
