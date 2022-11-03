from fastapi import FastAPI
import aiohttp
import asyncio

# https://api.dictionaryapi.dev/api/v2/entries/en/<word>
url_dict_en = "https://api.dictionaryapi.dev/api/v2/entries/en"

ITEMS_cache = {
    1: "item 1",
    2: "item 2",
    3: "item 3"
}

app = FastAPI()

# One session per-app is recommended in the
# aiohttp documentation, so an instance is referenced
# globally here.
session = aiohttp.ClientSession()

def main(): 
    pass

@app.get("/")
def root_handler():
    return {"hello": "world"}

@app.post("/items")
def post_item(item_id: int, item_desc: str):
    ITEMS_cache[item_id] = item_desc
    return "POST", 200

@app.get("/items/{item_id}")
def get_item(item_id: int):
    
    if item_id in ITEMS_cache:
        # Request is cached, return immediately:
        return {item_id: ITEMS_cache[item_id]}
    
    else:
        # we need threading for asynchronous disk I/O
        # pretend like doing that stuff here
        return "ID Not Found", 503

@app.get("/model")
async def model_handler(x1: int, x2: int) -> int:

    # imagine a CPU intensive task execution here,
    # such as neural network evaluation. Pretend futures/threading
    # being used again. To keep the method non-blocking I prefer to
    # put await here anyway.
    await asyncio.sleep(2)
    return x1 ** x2

@app.get("/dict")
async def model_handler(word: str) -> dict:
    """
    Middleware for the English Dictionary of dictionaryapi.com
    """
    async with session.get(url_dict_en + f"/{word}") as resp:
        return await resp.json()


if __name__ == "__main__":
    main()
