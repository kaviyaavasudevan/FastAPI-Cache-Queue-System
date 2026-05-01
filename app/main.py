from fastapi import FastAPI
import json

from app.redis_client import get_cache, set_cache
from app.kafka_client import send_event

app = FastAPI()

PRODUCTS = {
    "1": {"id": 1, "name": "iphone", "price": 1000},
    "2": {"id": 2, "name": "laptop", "price": 2000},
}

@app.get("/product/{product_id}")
def get_product(product_id: str):

    # 1. check cache
    cached = get_cache(product_id)
    if cached:
        return {"source": "redis", "data": json.loads(cached)}

    # 2. fetch DB (mock)
    product = PRODUCTS.get(product_id)

    if not product:
        return {"error": "not found"}

    # 3. cache it
    set_cache(product_id, json.dumps(product))

    # 4. send event to kafka
    send_event("product_events", product)

    return {"source": "db", "data": product}
