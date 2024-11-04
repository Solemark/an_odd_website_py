from flask import Blueprint

from src.routes.client import Client

client = Blueprint("client_blueprint", __name__)


@client.get("/data/clients")
def get_client_list() -> list[dict[str, int | str | bool]]:
    data: list[str] = open("data/clients.csv").readlines()
    clients: list[Client] = build_clients(data)
    return [client.jsonify() for client in clients if client.get_visible() is True]


def build_clients(data: list[str]) -> list[Client]:
    output: list[Client] = []
    for item in data:
        i: list[str] = item.split(",")
        output.append(Client(int(i[0]), i[1], i[2], i[3], bool(i[4])))
    return output
