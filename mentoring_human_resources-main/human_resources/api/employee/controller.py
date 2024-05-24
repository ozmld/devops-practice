from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse

from human_resources.api.employee.model import EmployeeCreate
from human_resources.api.employee.service import EmployeeService

employee_router = APIRouter(prefix="/employee")


@employee_router.get("/")
def find_all(service: EmployeeService = Depends(EmployeeService)) -> Response:
    return JSONResponse(status_code=status.HTTP_200_OK, content=[x.dict() for x in service.find_all()])


@employee_router.get("/{id}")
def find_by_id(id: int, service: EmployeeService = Depends(EmployeeService)) -> Response:
    employee = service.find_by_id(id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {id} not found.")
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee.dict())


@employee_router.post("/")
def create(employee_create: EmployeeCreate, service: EmployeeService = Depends(EmployeeService)) -> Response:
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=service.create(employee_create).dict())


@employee_router.delete("/{id}")
def delete(id: int, service: EmployeeService = Depends(EmployeeService)) -> Response:
    if service.delete(id):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with id {id} not found.")
