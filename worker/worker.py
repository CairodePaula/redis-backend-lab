import redis
import time

r = redis.Redis(host="redis", port=6379, decode_responses=True)

print("Worker iniciado...")

while True:
    job = r.brpop("queue", timeout=0)
    if job:
        _, value = job
        print(f"Processando: {value}")
        time.sleep(3)
        print(f"Finalizado: {value}")
