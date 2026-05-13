from fastapi import FastAPI, Request, HTTPException
import redis
import time

app = FastAPI()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

CACHE_TTL = 30

def slow_function(x: int):
    time.sleep(2)
    return {"result": x * 2}

@app.get("/cache/{x}")
def cache_endpoint(x: int):
    key = f"cache:{x}"

    cached = r.get(key)

    if cached:
        return {"source": "cache", "data": cached, "X-Cache": "HIT"}

    result = slow_function(x)
    r.setex(key, CACHE_TTL, str(result))

    return {"source": "db", "data": result, "X-Cache": "MISS"}

@app.post("/queue")
def enqueue(data: str):
    r.lpush("queue", data)
    return {"status": "queued", "data": data}

RATE_LIMIT = 10
WINDOW = 60

def rate_limit(ip: str):
    key = f"rate:{ip}"
    current = r.incr(key)

    if current == 1:
        r.expire(key, WINDOW)

    if current > RATE_LIMIT:
        return False
    return True

@app.middleware("http")
async def limit_middleware(request: Request, call_next):
    ip = request.client.host

    if not rate_limit(ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return await call_next(request)

@app.get("/count")
def count():
    return {"requests": r.incr("global:count")}
