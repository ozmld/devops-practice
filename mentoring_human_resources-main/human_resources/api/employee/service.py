from typing import List

from human_resources.api.employee.model import Employee, EmployeeCreate
from human_resources.api.employee.repository import EmployeeRepository


class EmployeeService:
    def __init__(self) -> None:
        self.repository = EmployeeRepository()

    def find_all(self) -> List[Employee]:
        return [Employee.model_validate(x) for x in self.repository.find_all()]

    def find_by_id(self, employee_id: int) -> Employee | None:
        employee = self.repository.find_by_id(employee_id)
        if employee is not None:
            return Employee.model_validate(employee)
        return employee

    def create(self, employee_create: EmployeeCreate) -> Employee:
        employee = self.repository.create(employee_create.model_dump())
        return Employee.model_validate(employee)

    def delete(self, employee_id: int) -> bool:
        return self.repository.delete(employee_id)
