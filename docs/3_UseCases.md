# Actors

## Fleet Manager
Responsible for managing vehicles.

## Administrator
Responsible for maintaining vehicle records.


# Use Cases

## UC1 Add Vehicle
Actor:
Fleet Manager

Description:
User adds a new vehicle.

Flow:
1. User enters vehicle information.
2. System validates input.
3. System stores vehicle.
4. System returns success response.

## UC2 Retrieve Vehicle
Actor:
Fleet Manager

Description:
User retrieves vehicle information.

Flow:
1. User provides vehicle ID.
2. System searches for vehicle.
3. System returns vehicle information.

## UC3 Update Vehicle
Actor:
Fleet Manager

Description:
User updates vehicle information.

Flow:
1. User selects vehicle.
2. User modifies information.
3. System validates data.
4. System updates record.

## UC4 Delete Vehicle
Actor:
Fleet Manager

Description:
User removes vehicle.

Flow:
1. User provides vehicle ID.
2. System deletes vehicle.
3. System returns success message.