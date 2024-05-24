import os

import pandas as pd
import requests
import streamlit as st

API_HOSTNAME = os.environ["API_HOSTNAME"]
API_PORT = os.environ["API_PORT"]
API_URL = f"http://{API_HOSTNAME}:{API_PORT}/employee"


def find_all() -> None:
    try:
        if st.button("Go"):
            response = requests.get(API_URL)
            response.raise_for_status()
            employees = response.json()
            if employees:
                st.table(pd.DataFrame(employees).set_index("id"))
            else:
                st.warning("No employees found.")
    except Exception as exception:
        st.error(f"An error occurred: {exception}.")


def find_by_id() -> None:
    try:
        employee_id = st.number_input("ID", min_value=0)
        if st.button("Go"):
            response = requests.get(API_URL + "/" + str(employee_id))
            response.raise_for_status()
            st.table(response.json())
    except Exception as exception:
        st.error(f"An error occurred: {exception}.")


def create() -> None:
    try:
        name = st.text_input("Name")
        email = st.text_input("Email")
        if st.button("Go"):
            response = requests.post(API_URL, json={"name": name, "email": email})
            response.raise_for_status()
            st.table(pd.Series(response.json()))
    except Exception as exception:
        st.error(f"An error occurred: {exception}.")


def delete() -> None:
    try:
        employee_id = st.number_input("ID", min_value=0)
        if st.button("Go"):
            response = requests.delete(API_URL + "/" + str(employee_id))
            response.raise_for_status()
            st.success(f"Employee {employee_id} has been deleted.")
    except Exception as exception:
        st.error(f"An error occurred: {exception}.")


st.title("Human Resources")

option = st.selectbox("Employee", ["Find All", "Find by ID", "Create", "Delete"])

if option == "Find All":
    find_all()
elif option == "Find by ID":
    find_by_id()
elif option == "Create":
    create()
else:
    delete()
