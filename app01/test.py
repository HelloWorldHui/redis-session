# coding=utf
"""
author=Hui_T
"""
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)
print(redis.keys())
# b'jkg4wduptrnjm8rulkfe1o2y7cvqqnjv'
#[b'session:7fgwiet5yj3ghpxuoazu66g93iwrtn8v']
print(redis.get(b'jkg4wduptrnjm8rulkfe1o2y7cvqqnjv'))
# YmM2ZjhmYjAxMGM0ZTMyMzc1NzhmMTRiYTZlOWEyNzk0NGY3ZDIxNTp7InVzZXJuYW1lIjoiMTIzIiwicGFzc3dvcmQiOiI0NTYifQ==
# b'OGRjZDhkNjJmMmJhYjAzMTZmODYwNmIzYTU5ODBkNDA3MWVmYmE0Nzp7InVzZXJuYW1lIjoibGkiLCJhZ2UiOjE4fQ=='