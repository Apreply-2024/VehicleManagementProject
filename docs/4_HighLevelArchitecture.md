# High-Level Architecture
The system follows a layered architecture.

Client
↓
API Layer
↓
Service Layer
↓
Repository Layer
↓
Database

## API Layer
Responsibilities:
- Receive HTTP requests.
- Validate request format.
- Return responses.

Implemented using:
FastAPI

## Service Layer
Responsibilities:
- Business logic.
- Validation.
- Rules.

## Repository Layer
Responsibilities:
- Database interaction.
- CRUD operations.

## Database Layer
Responsibilities:
- Persistent storage.

Future Technology:
PostgreSQL