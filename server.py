import asyncio
import logging
from unittest import result
from aiohttp import web, ClientSession
import requests

# Params
address = "127.0.0.1"
default_port = 5000
server_queue = []
request_queue = []
ports = [7001, 7002, 7003, 7004, 7005]

app    = web.Application()
routes = web.RouteTableDef()

# Getting data
async def getting_data(path):
    session = ClientSession()
    data = ''
    async with session.get(path) as resp:
        data = await resp.text()
    await session.close()
    return data

# "Hello World" func
@routes.get('/')
def hello_world(self):
    return web.Response(text="Hello World")

# Listener
@routes.get('/pinger')
async def pinger(self):
    for port in ports:
        if port not in server_queue:
            path = f"http://{address}:{port}"
            server_queue.append(port)
            response = await getting_data(path)
            server_queue.pop(server_queue.index(port))
    
    # Check if there are any prepared workers
    result_text = ''
    if len(server_queue) == len(ports):
        request_queue.append('ping')
        result_text = "Wait for it"
    else:
        result_text = response
    

    logging.info(result_text)
    return web.Response(text=result_text, status=200)

app.add_routes(routes)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=address, port=default_port)