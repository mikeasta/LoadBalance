import asyncio
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
def getRequestUrl(port):
    return f"http://{address}:{port}"

# Check if there is any available server
def isAvailablePort():
    return not len(server_queue) == len(ports)

# Look for available port
def getAvailablePort():
    for port in ports:
        if port not in server_queue:
            return port


# * API
# Root func
def hello_world(self):
    return web.Response(text="/")


# Getting data from special worker
async def fetch(url, session):
    async with session.get(url) as resp:
        return await resp.text()
    


# Listener
async def pinger(self):
    response = ''
    
    # Check if all servers are working
    if isAvailablePort():
        # Look for available ports
        port = getAvailablePort()

        # Getting prepared server url   
        url = getRequestUrl(port)

        # Adding server to busy-servers-list
        # Performs request to that server
        server_queue.append(port)

        # Get result from workers
        async with ClientSession() as session:
            response = await fetch(url, session)
        server_queue.remove(port)

        # Logging response
        logging.info(response)
        if bool(request_queue):
            context = request_queue.pop()
            await pinger(context)

        # Result
        logging.info(time.ctime(time.time()))
        return web.Response(text=response, status=200)
    else: 
        request_queue.append(self)
        logging.info("All Servers Are Busy Now!")
        return web.Response(text=response, status=200)


# * Server start-up
app.add_routes([
    web.get('/', hello_world),
    web.get('/pinger', pinger)
])

if __name__ == "__main__":    
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=address, port=default_port)