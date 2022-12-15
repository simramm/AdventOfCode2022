import os
import json
from datetime import datetime
import math

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"leaderboard.json"))

data=json.load(f)

dailytimes=[]
for member in data['members']:
    name = data['members'][member]['name']
    for day in range(1,25):
        try:
            first_star_ts=data['members'][member]['completion_day_level'][str(day)]['1']['get_star_ts']
        except:
            first_star_ts=1769957699
        try:
            second_star_ts=data['members'][member]['completion_day_level'][str(day)]['2']['get_star_ts']
        except:
            second_star_ts=1769957699

        dailytimes.append([name, day, datetime.utcfromtimestamp(first_star_ts).strftime('%Y-%m-%d %H:%M:%S'),datetime.utcfromtimestamp(second_star_ts).strftime('%Y-%m-%d %H:%M:%S')])

dailyTops=[]

for day in range(1,25):

    dailyTop1=dict()
    dailyTop2=dict()
    for x in dailytimes:
        name=x[0]
        today=x[1]
        star1time=x[2]
        star2time=x[3]

        if today==day:

            dailyTop1[name]=star1time
            dailyTop2[name]=star2time

    dailyTop1=(dict(sorted(dailyTop1.items(), key=lambda item: item[1])))
    dailyTops.append([day,1,dailyTop1])

    dailyTop2=(dict(sorted(dailyTop2.items(), key=lambda item: item[1])))
    dailyTops.append([day,2,dailyTop2])



for star in range(0,48):
    
    print('### Top 10 for Day ' + str(math.floor(star/2)+1) + ' Star No. '+ str(dailyTops[star][1]) +  ':')

    print(list(dailyTops[star][2].items())[:10])
    #print(list(dailyTops[star][2])[:10])




