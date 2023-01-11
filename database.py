import redis


def build_redis_connection(host:str, port:int, db:int):
    return redis.Redis(host='localhost', port=6379, db=0)



db = build_redis_connection('localhost', 6379, 0)


a = db.get('foo')
print(a)

