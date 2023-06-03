"""Main module."""
from fastapi import FastAPI
from fastapi import Request

from src.app.db import Books
from src.app.db import BooksReaders
from src.app.db import Readers
from src.app.db import Reminders
from src.app.db import User
from src.app.db import database

app = FastAPI(title="Automata")


@app.get("/")
async def read_root():
    """Return list of users."""
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    """Connect to database."""
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Disconnect from database."""
    if database.is_connected:
        await database.disconnect()


@app.get("/books")
async def get_books():
    """Return list of books."""
    return await Books.objects.all()


@app.post("/books")
async def create_book(request: Request):
    """Create a book."""
    data = await request.json()
    book = await Books.objects.create(**data)
    return {"id": book.id}


@app.get("/readers")
async def get_readers():
    """Return list of readers."""
    return await Readers.objects.all()


@app.post("/readers")
async def create_reader(request: Request):
    """Create a reader."""
    data = await request.json()
    book = await Readers.objects.create(**data)
    return {"id": book.id}


@app.post("/read")
async def create_books_readers(request: Request):
    """Create a books_readers."""
    data = await request.json()
    books_readers = await BooksReaders.objects.create(**data)
    return {"id": books_readers.id}


@app.get("/reminders")
async def get_reminders():
    """Return list of reminders."""
    return await Reminders.objects.all()


@app.post("/reminders")
async def create_reminder(request: Request):
    """Create a reminder."""
    data = await request.json()
    reminder = await Reminders.objects.create(**data)
    return {"id": reminder.id}
