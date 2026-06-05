# Functional Requirements

## FR1: Add Vehicle
The system shall allow users to add a new vehicle.

Input:
* Make
* Model
* Year
* VIN
* Status

Output:
* Vehicle ID
* Success message

## FR2: Retrieve All Vehicles
The system shall return a list of all vehicles.

## FR3: Retrieve Vehicle by ID
The system shall return vehicle information using the vehicle identifier.

## FR4: Update Vehicle
The system shall allow users to modify vehicle information.

## FR5: Delete Vehicle
The system shall remove a vehicle from the system.

## FR6: Search Vehicle
The system shall allow searching vehicles using:
* Make
* Model
* Status

# Non-Functional Requirements

## Performance
Response time should be less than 200 ms.

## Reliability
The system shall provide error messages for invalid requests.

## Maintainability
The code shall follow modular architecture.

## Scalability
The system shall support thousands of vehicle records.
