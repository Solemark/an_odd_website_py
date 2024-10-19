create a venv:
 
	python3 -m venv .venv

open venv with:

    . .venv/bin/activate

get dependencies with:

    pip3 install -r requirements.txt

run server with:

    flask --app server.py run

run debug mode with:

    flask --app server.py run --debug
