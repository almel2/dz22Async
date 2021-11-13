import asyncio
import aiohttp


async def OpenUV(session):
    async with session.get('https://api.open-meteo.com/v1/forecast?latitude=49.59&longitude=36.13&hourly=temperature_2m&current_weather=true') as response:
        print('Status:', response.status)
        data = await response.json()
        temp = data['current_weather']['temperature']
        return temp




async def weatherbit(session):
    city = 'Kharkiv'
    async with session.get(f"https://api.weatherbit.io/v2.0/current?&city={city}&key=571a2acc64344dcbb408bc652f95f5c2") as response:
        print('Status:', response.status)
        data = await response.json()
        temp = data['data'][0]['temp']
        return temp


async def metaweather(session):
    async with session.get('https://www.metaweather.com/api/location/922137/') as response:
        print('Status:', response.status)
        data = await response.json()
        temp = data['consolidated_weather'][0]['the_temp']
        return temp




async def main():
    async with aiohttp.ClientSession() as session:
       sred = await asyncio.gather(metaweather(session), weatherbit(session), OpenUV(session))
    print('Температура в Харькове', round((sum(sred) / 3), 2), 'градусов')






if __name__ == '__main__':
    asyncio.run(main())
