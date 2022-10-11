from ast import Num, Str
import asyncio
from typing import Literal
from xmlrpc.client import Boolean
from aiojobs.aiohttp import setup, spawn
import logging
from aiohttp import web, ClientSession
import requests
import time


# Params
address       = "127.0.0.1"
default_port  = 5000
server_queue  = []
request_queue = []
ports         = [7001, 7002, 7003, 7004, 7005]


# Server initialization
app    = web.Application()
routes = web.RouteTableDef()


# * Utils
# Get request path
def getRequestUrl(port: int) -> str:
    return f"http://{address}:{port}"

# Check if there is any available server
def isAvailablePort() -> bool:
    return not len(server_queue) == len(ports)

# Look for available port
def getAvailablePort() -> int:
    for port in ports:
        if port not in server_queue:
            return port


# * API
# Root func
def hello_world(self):
    return web.Response(text="/")


# Getting data from special worker
async def fetch(session):
    response = ''

    # Look for available ports
    port = getAvailablePort()

    # Getting prepared server url   
    url = getRequestUrl(port)

    # Adding server to busy-servers-list
    # Performs request to that server
    server_queue.append(port)

    async with session.get(url) as resp:
        response = await resp.text()
    
    server_queue.remove(port)
    return response
    

# Listener
async def pinger(req):
    response = ''
    
    while not isAvailablePort():
        await asyncio.sleep(1)

    # Check if all servers are working
    if isAvailablePort():

        # Getting data
        async with ClientSession() as session:
            response = await fetch(session)

        # Logging response
        logging.info(response)
        
        # Result
        logging.info(time.ctime(time.time()))
        return web.Response(text=response, status=200)


# * Server start-up
app.add_routes([
    web.get('/', hello_world),
    web.get('/pinger', pinger)
])

if __name__ == "__main__":    
    setup(app)
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=address, port=default_port)