from flask import Flask, send_file, Response
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def get_index_page() -> Response:
    """Return the index page"""
    file: str = open("static/index.html").read()
    return build_page(file)


@app.get("/<page>")
def get_page(page: str) -> Response:
    """Return other pages"""
    file: str = open(f"static/{escape(page)}.html").read()
    return build_page(file, page)


@app.get("/styles/<style>")
def get_style(style: str) -> Response:
    """Return selected script"""
    return send_file(f"static/styles/{escape(style)}.css")


@app.get("/scripts/<script>")
def get_script(script: str) -> Response:
    """Return selected script"""
    return send_file(f"static/scripts/{escape(script)}.js")


def build_page(file: str, page: str | None = None) -> str:
    file = set_head(file, page)
    file = set_navbar(file, page)
    file = set_script(file, page)
    return file


def set_head(file: str, page: str | None = None) -> str:
    return f"{open('static/components/head.html').read()}{file}"


def set_navbar(file: str, page: str | None = None) -> str:
    file = file.replace(
        "<!--NAVBAR-->", f"{open('static/components/navbar.html').read()}"
    )
    if page is None:
        file = file.replace('<a href="/">', '<a class="active" href="/">')
    else:
        file = file.replace(f'<a href="/{page}">', f'<a class="active" href="/{page}">')
    return file


def set_script(file: str, page: str | None = None) -> str:
    return (
        file.replace("<!--SCRIPT-->", f'<script defer src="/scripts/{page}"></script>')
        if page is not None
        else file
    )
