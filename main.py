from typing import Optional

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def formulaire():
    with open("formulaire.html", "r") as formulaire:
        return HTMLResponse(content=formulaire.read(), status_code=200)


@app.post("/send")
def send_email(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return {"name": name, "email": email, "message": message}
