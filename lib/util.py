import csv
from datetime import datetime # 1
from datetime import timedelta # 2


#출처 [https://velog.io/@choraeng/Python-n%EC%9B%94-n%EC%A3%BC%EC%B0%A8-%EA%B5%AC%ED%95%98%EA%B8%B0]
def week_no(y, m, d):
    def _ymd_to_datetime(y, m, d): # 3
        s = f'{y:04d}-{m:02d}-{d:02d}'
        return datetime.strptime(s, '%Y-%m-%d')

    target_day = _ymd_to_datetime(y, m, d) # 4
    firstday = target_day.replace(day=1) # 5
    while firstday.weekday() != 0: # 6
      firstday += timedelta(days=1)
      
    if target_day < firstday: # 7
      return 0
  
    return (target_day - firstday).days // 7 + 1 # 8

def save_meal_menu_this_weekend(latest_meal_menu):
    # images > [0] > fields > [0] > monday
    with open('mealmenu/w.csv', 'w', newline='') as f:
       wr = csv.writer(f)
       for line in latest_meal_menu['images'][0]['fields']:
          wr.writerow(line['inferText'].splitlines())
       
def save_meal_menu_all_weekend(latest_meal_menu):
    # images > [0] > fields > [0] > monday
    with open('mealmenu/total_meal.csv', 'a', newline='') as f:
       wr = csv.writer(f)
       for line in latest_meal_menu['images'][0]['fields']:
          wr.writerow(line['inferText'].splitlines())
       