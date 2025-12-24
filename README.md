# holbertonschool-hbnb
A complete web application clone of AirBnB, starting with the backend console

# AirBnB Clone - The Console

## Description
This project is the first step towards building a full web application clone of AirBnB.
In this first phase, we are implementing the backend interface (The Console) to manage the application data.

## Command Interpreter
The console acts as a command-line interface (CLI) that allows us to:
* Create a new object (User, Place, etc.)
* Retrieve an object from a file, a database, etc.
* Do operations on objects (count, compute stats, etc.)
* Update attributes of an object
* Destroy an object

## Architecture
The project follows a specific architecture:
* **models/**: Contains all classes used for the application.
* **console.py**: The entry point of the command interpreter.
* **models/engine/file_storage.py**: Handles the serialization and deserialization of instances to a JSON file.

## Authors
* **OWAYS Abdulhakim Aljbreen**
* **Bahathiq Mohammed Rateel**
* **Raghad Abdullah Nassef**