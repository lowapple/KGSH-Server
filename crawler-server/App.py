import asyncio, sys
import MealParser
import datetime

if sys.platform == 'win32':
    print('win32')
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

def daterange(d1, d2):
    return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

async def main():
    date1 = datetime.date(2015, 1, 1)
    date2 = datetime.date(2017, 4, 24)
    
    for d in daterange(date1, date2):
        date = d.strftime('%Y-%m-%d')
        await MealParser.get_meal_list(date)
        
    # await MealParser.get_meal_list('2015-12-17')
    # await MealParser.get_meal_list('2016-09-09')
    # await MealParser.update()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())