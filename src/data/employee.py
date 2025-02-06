from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    visible: bool

    def jsonify(self) -> dict[str, int | str | bool]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role": self.role,
            "visible": self.visible,
        }

    def __str__(self) -> str:
        return f"{self.id},{self.first_name},{self.last_name},{self.email},{self.role},{self.visible}"
