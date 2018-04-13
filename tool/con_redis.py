import redis
r = redis.Redis(host='10.110.1.97', port=6379, db=0)
a = r.set('foo', 'bar')
print(a)
print(r.get('foo'))