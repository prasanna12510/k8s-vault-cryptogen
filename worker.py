import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']

redis_url = os.getenv('REDIS_URL', 'vaultstore.redis.cache.windows.net')
redis_token = os.getenv('REDIS_TOKEN','SoofWT5O2ZS88+MirB5ltw7fLzrysn+3PhCdHshnpfo=')
redis_port = os.getenv('REDIS_PORT','6379')


conn = redis.Redis(host=redis_url,port=redis_port,password=redis_token)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
