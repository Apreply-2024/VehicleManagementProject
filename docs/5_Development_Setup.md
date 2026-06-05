# Development Setup

## Objective
Set up the development environment for the Vehicle Management System backend.

## Tools
* Python 3.12+
* VS Code
* Git
* FastAPI
* Uvicorn

## Folder Structure
VehicleManagementProject
│
├── docs
├── src
└── tests

## Development Process
1. Create project workspace.
2. Create Python virtual environment.
3. Install dependencies.
4. Initialize Git repository.
5. Create FastAPI application.
6. Verify APIs using Swagger UI.

# Python Environment

## Create Virtual Environment

Command:

python -m venv venv

## Activate Environment

Windows:

venv\Scripts\activate

Purpose:

Provides isolated dependency management for the project.

# Version Control

Tool:

Git

Commands:

git init

git add .

git commit -m "Initial project setup"

Purpose:

Track source code changes and support collaboration.

# Running the FastAPI Application

## Activate Virtual Environment

Windows PowerShell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

& "venv\Scripts\Activate.ps1"

## Start Server

python -m uvicorn main:app --reload

## Verify Application

URL:

http://127.0.0.1:8000

Expected Response:

{
"message": "Vehicle Management System"
}

## Swagger UI

URL:

http://127.0.0.1:8000/docs

Purpose:

Provides automatically generated API documentation and allows testing APIs directly from the browser.

## OpenAPI Specification

URL:

http://127.0.0.1:8000/openapi.json

Purpose:

Machine-readable API contract used by frontend applications and tools.

# Git Workflow

## Check Status

git status

## Stage Changes

git add .

## Commit Changes

git commit -m "Meaningful message"

Examples:

git commit -m "Initial project setup"

git commit -m "Completed Day 2 setup and FastAPI application"

## View Commit History

git log

Purpose:

Version control enables tracking changes and restoring previous versions of the project.
