'''
datahandling

A module of utilities for handling data files used in the cfsc2023_paths 
exercise of the 2023 Computational Fluency Short Course in Brown 
University's Carney Institute for Brain Science.
'''

import pandas as pd


def load_all_subjects(data_dir):
  '''
  This is a placeholder function. It should return a single DataFrame that
  concatenates all the subject data together.
  TODO: Add docstring
  TODO: Add functionality
  '''
  pass

def load_subject(file_path):
  '''
  Load data for a single subject.

  Parameters
  ----------
  file_path str
    A valid path to the data file

  Returns
  -------
  pandas.DataFrame
    A DataFrame as returned from read_csv. Returns None if load failed.
  '''

  try:
    return pd.read_csv(file_path)
  except:
    print(f'Unable to load data in \n  {file_path}')
    return None
