from flask import Blueprint

from src.routes.client import Client

client = Blueprint("client_blueprint", __name__)


@client.get("/data/clients")
def get_client_list() -> list[dict[str, int | str | bool]]:
    data: list[str] = open("data/clients.csv").readlines()
    clients: list[Client] = build_clients(data)
    return clients_to_dict(clients)


def build_clients(data: list[str]) -> list[Client]:
    output: list[Client] = []
    for item in data:
        i: list[str] = item.split(",")
        output.append(Client(int(i[0]), i[1], i[2], i[3], bool(i[4])))
    return output


def clients_to_dict(clients: list[Client]) -> list[dict[str, int | str | bool]]:
    output: list[dict[str, int | str | bool]] = []
    for client in clients:
        output.append(client.jsonify())
    return output
