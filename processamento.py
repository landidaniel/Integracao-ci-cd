import pandas as pd
import os 
import sys

def limpa_dados( df):
  df_limpo=df.dropna()
  return  df_limpo