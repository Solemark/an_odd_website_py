# An Odd Website - Python

## Installation

### uv (recommended)

create a venv:

    uv venv

get dependencies with:

    uv pip install -r requirements.txt

run server with:

    uv run flask --app src/server.py run -p 8080

run debug mode with:

    uv run flask --app src/server.py run -p 8080 --debug

-p 8080 sets the port to 8080, this is optional

### pip

create a venv:
 
	python3 -m venv .venv

open venv with:

    . .venv/bin/activate

get dependencies with:

    pip3 install -r requirements.txt

run server with:

    flask --app server.py run -p 8080

run debug mode with:

    flask --app server.py run -p 8080 --debug

-p 8080 sets the port to 8080, this is optional
