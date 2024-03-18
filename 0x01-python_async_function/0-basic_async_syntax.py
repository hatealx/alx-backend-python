#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay=10):
    """my coroutine fuction"""
    delay = random.uniform(0, max_delay)  # Generate a random delay
    await asyncio.sleep(delay)  # Wait for the random delay
    return delay


async def main():
    """ my main function"""
    random_delay = await wait_random()

asyncio.run(main())
