#!/usr/bin/env python3
''' async and await syntax '''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Function that returns asyncio task '''
    end = asyncio.create_task(wait_random(max_delay))
    return end
