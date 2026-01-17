from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id":1,
        "author":"Akshay Satasiya",
        "title":"FastAPI is Awesome",
        "content":"This framework is really eassy to use and super fast.",
        "date_posted":"Jan 13, 2026"
    },
    {
        "id":2,
        "author":"Akshay Satasiya",
        "title":"LLMs",
        "content":"Large Language Models!",
        "date_posted":"Jan 14, 2026"
    },
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title": "Home"})


@app.get("/api/posts")
def get_post():
    return posts