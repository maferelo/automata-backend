"""Website starter with fastapi.

https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864
"""
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page."""
    data = {"page": "Home page"}
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/healthcheck")
async def healthcheck():
    """Healthcheck."""
    data = {"status": "ok"}
    return {"data": data}


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    """Page."""
    data = {"page": page_name}
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
