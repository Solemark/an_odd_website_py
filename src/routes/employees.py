from flask import Blueprint

from src.data.employee import Employee

employee = Blueprint("employee_blueprint", __name__)


@employee.get("/data/employees")
def get_employee_list() -> list[dict[str, int | str | bool]]:
    data: list[str] = open("data/employees.csv").readlines()
    employees: list[Employee] = build_employees(data)
    return [employee.jsonify() for employee in employees if employee.visible is True]


def build_employees(data: list[str]) -> list[Employee]:
    output: list[Employee] = []
    for item in data:
        i: list[str] = item.split(",")
        output.append(Employee(int(i[0]), i[1], i[2], i[3], i[4], bool(i[4])))
    return output
