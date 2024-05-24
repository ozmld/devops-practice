from fastapi import FastAPI

from human_resources.api.employee.controller import employee_router

app = FastAPI(title="Human Resources", version="0.1.0", root_path="/api/v1")
app.include_router(router=employee_router, tags=["employee-controller"])
