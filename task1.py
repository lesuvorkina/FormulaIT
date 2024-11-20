# TODO решите задачу

import json
from pprint import pprint

def task()-> float: # нужно score*weight
  summ=0
  with open('input.json', 'r') as json_file:
    data = json.load(json_file)
    #pprint(data)
    for txt in data: #создали цикл, который будет работать построчно
      summ+= (txt['score']*txt['weight'])
  return round(summ,3)
print(task())
