import asyncio
import logging
from aiohttp import web, ClientSession
import requests

# Params
address       = "127.0.0.1"
default_port  = 5000
server_queue  = []
request_queue = []
ports         = [7001, 7002, 7003, 7004, 7005]

# Server initialization
app    = web.Application()
routes = web.RouteTableDef()

# root func
@routes.get('/')
def hello_world(self):
    return web.Response(text="/")

# Get request path
def req_path(port):
    return f"http://{address}:{port}"


# * Pinger
# Getting data from special worker
async def fetch(path, session):
    async with session.get(path) as resp:
        return await resp.text()

# Listener
@routes.get('/pinger')
async def pinger(self):
    response = 'null'

    # Check if all servers are working
    if len(server_queue) == len(ports):
        request_queue.append(1)
        logging.info("All servers are busy. Your request will be performed later.")
        return web.Response(text="null", status=200)

    # Look for available ports
    for port in ports:
        if port not in server_queue:
            # Available port found
            path = req_path(port)
            server_queue.append(port)
            async with ClientSession() as session:
                response = await fetch(path, session)
            server_queue.remove(port)

    logging.info(response)
    return web.Response(text=response, status=200)

app.add_routes(routes)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=address, port=default_port)