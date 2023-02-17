#!/usr/bin/env python

import asyncio
import websockets
import json


async def hello():
    data = {"age": 10, "name": "paul"}
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(json.dumps(data))
        print("got message back")
        res = await websocket.recv()
        res = json.loads(res)
        print("response was:", res)

asyncio.run(hello())
