from flask import Blueprint, Response, send_file
from markupsafe import escape

website = Blueprint("website_blueprint", __name__)


@website.get("/")
def get_index_page() -> str:
    """Return the index page"""
    return build_page(open("static/index.html").read())


@website.get("/<page>")
def get_page(page: str) -> str:
    """Return other pages"""
    return build_page(open(f"static/{escape(page)}.html").read(), page)


@website.get("/styles/<style>")
def get_style(style: str) -> Response:
    """Return selected script"""
    return send_file(f"../static/styles/{escape(style)}.css")


@website.get("/scripts/<script>")
def get_script(script: str) -> Response:
    """Return selected script"""
    return send_file(f"../static/scripts/{escape(script)}.js")


def build_page(file: str, page: str | None = None) -> str:
    file = set_head(file, page)
    file = set_navbar(file, page)
    file = set_script(file, page)
    return file


def set_head(file: str, page: str | None = None) -> str:
    return f"{open('static/components/head.html').read()}{file}".replace(
        "AOW - PAGENAME", f"AOW - {'Dashboard' if page is None else page.title()}"
    )


def set_navbar(file: str, page: str | None = None) -> str:
    file = file.replace("<!--NAVBAR-->", f"{open('static/components/navbar.html').read()}")
    return (
        file.replace('<a href="/">', '<a class="active" href="/">')
        if page is None
        else file.replace(f'<a href="/{page}">', f'<a class="active" href="/{page}">')
    )


def set_script(file: str, page: str | None = None) -> str:
    return file.replace("<!--SCRIPT-->", f'<script defer src="/scripts/{page}"></script>') if page is not None else file
