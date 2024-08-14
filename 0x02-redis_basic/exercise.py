#!/usr/bin/env python3
'''A module for using the Redis NoSQL data storage.
'''
from functools import wraps
from typing import Any, Callable, Union
import redis
import uuid


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    # @call_history
    # @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in a Redis data storage and returns the key.'''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        # print(data_key)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieves a value from a Redis data storage.
        '''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data
