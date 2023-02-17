#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        print("got message back")
        res = await websocket.recv()
        print("response was:", res)

asyncio.run(hello())
