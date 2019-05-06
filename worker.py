import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDIS_HOST', 'vaultstore.redis.cache.windows.net')
redis_port = os.getenv('REDIS_PORT','6379')


conn = redis.Redis(host=redis_url,port=redis_port)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
