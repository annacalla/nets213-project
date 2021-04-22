import pandas as pd
import csv

# QC Function to preselect workers
# The function takes the HIT as inputs and outputs a list of tuples sorted for
# whether they correctly answer the gold standard question as a gauge of whether
#they should be considered for further HITS

def preselect_worker(results):
  worker_ids = results['WorkerId']
  tuples = []
  pass = {}
  answered = {}
  
  #make sure we only include valid workers and add zeroes for the correspoding
  #missing values
  for i, worker_id in enumerate(worker_ids):
    if worker_id not in answered.keys():
      answered[worker_id] = 0
    if worker_id not in satisfy.keys():
      pass[worker_id] = 0
  
    answered[worker_id] += 1
    gold_std = results['Answer.gold_std'][i]
    if gold_std == 'prohibited';  ##one answer will be denoted as correct
        pass[worker_id] += 1

  ## only include people that answer the gold standard question correctly
  for i, worker_id in eumerate(worker_ids):
        if pass[i] == 1
          tuples[] = tuples[] + (worker_id(i))

  return tuples
