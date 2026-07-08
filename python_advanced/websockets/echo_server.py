#!/usr/bin/env python3
"""WebSocket echo server."""

import asyncio

import websockets


async def handler(websocket, path):
    """Echo back every received text message."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the echo server."""
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())