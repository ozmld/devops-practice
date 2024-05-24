import os
from typing import Dict, Any, List

from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session

from human_resources.api.employee.model import EmployeeTable

DATABASE_USER = os.environ["DATABASE_USER"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOSTNAME = os.environ["DATABASE_HOSTNAME"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}"


class EmployeeRepository:
    def __init__(self) -> None:
        self.engine = create_engine(url=DATABASE_URL)
        EmployeeTable.metadata.create_all(self.engine)

    def create(self, employee: Dict[str, Any]) -> Dict[str, Any]:
        with Session(self.engine) as session:
            employee_table = EmployeeTable(**employee)
            session.add(employee_table)
            session.commit()
            session.refresh(employee_table)
            return employee_table.__dict__

    def delete(self, employee_id: int) -> bool:
        with Session(self.engine) as session:
            result = session.execute(delete(EmployeeTable).where(EmployeeTable.id == employee_id))
            session.commit()
            return result.rowcount > 0

    def find_by_id(self, employee_id: int) -> Dict[str, Any] | None:
        with Session(self.engine) as session:
            result = session.execute(select(EmployeeTable).where(EmployeeTable.id == employee_id)).scalar()
            if result:
                return result.__dict__
            return None

    def find_all(self) -> List[Dict[str, Any]]:
        with Session(self.engine) as session:
            result = session.execute(select(EmployeeTable)).scalars().all()
            return [employee.__dict__ for employee in result]
