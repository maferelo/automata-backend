"""Website starter with fastapi.

https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    """Home page."""
    data = {"text": "hi"}
    return {"data": data}


@app.get("/page/{page_name}")
async def page(page_name: str):
    """Page."""
    data = {"page": page_name}
    return {"data": data}
