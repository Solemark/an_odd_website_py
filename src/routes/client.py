class Client:
    def __init__(
        self, id: int, first_name: str, last_name: str, email: str, visible: bool
    ):
        self.__id: int = id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__visible: bool = visible

    def set_id(self, id: int) -> None:
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def set_first_name(self, name: str) -> None:
        self.__first_name = name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, name: str) -> None:
        self.__last_name = name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_email(self, email: str) -> None:
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    def set_visible(self, visible: bool) -> None:
        self.__visible = visible

    def get_visible(self) -> bool:
        return self.__visible

    def jsonify(self) -> dict[str, int | str | bool]:
        return {
            "id": self.__id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "email": self.__email,
            "visible": self.__visible,
        }
