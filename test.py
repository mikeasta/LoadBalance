import asyncio

from aiohttp import ClientSession

async def fetch(path, session):
    async with session.get(path) as resp:
        return await resp.text()

async def main():
    result = ''
    async with ClientSession() as session:
        result = await fetch('http://127.0.0.1:7005', session)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())