# Digital Signal Processing (DSP) Project

This repository contains a Digital Signal Processing project developed for the Computer Science department at Ain Shams University by Mohab Ashraf and Moamen Sherif. It is designed to provide tools and functionalities for signal processing using Python. 

## Features

- Core signal processing operations and utilities.
- A modular and extensible structure for developing custom signal processing workflows.
- Comprehensive testing to ensure functionality and stability.

## How to Run the Project

### Requirements

This project requires Python 3.12. To install the required dependencies, run the following commands:

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the Project

After setting up the environment and installing dependencies, execute the main script or any specific module you wish to explore. For example:

```bash
python __init__.py
```

## Exploring the Project

### Project Structure

The project is organized into the following folders and files:

- **Bonus/**: Contains additional features or experimental functionalities that extend the main project capabilities.
- **Functions/**: Houses the core functionalities, including:
- **Gui/**: Includes files for the graphical user interface (GUI). While basic, this directory can be a focus area for future improvements.
    - `Gui_starter.py`: Script to launch the GUI.
- **Ref/**: Reference materials or resources used in the project.
- **Tests/**: Contains the test suite and `.txt` files used for validating the project's functionality.
- `utilities.py`: Contains helper functions for signal processing tasks.
- `RunAllTests.py`: A script to execute all the tests.
- **tests/**: main testing file .
- **Freestyle.py**: A standalone script for custom or freestyle operations outside the main project flow.
- `Signal.py`: Defines the `Signal` class, the central component of the project.
- `.flake8`: Configuration file for the `flake8` linter.
- `requirements.txt`: Lists the dependencies required for running the project.
- `requirements.dev.txt`: Lists the additional dependencies needed for development.
- `README.md`: This documentation file.

### Starting Point: The `Signal` Class

The `Signal` class is the heart of this project. It provides:

- Methods for reading and writing signal data.
- Utilities for manipulating and analyzing signals.

To explore the project, begin by examining the `Signal` class in `Functions/Signal.py`. Then, move to the `act` and `check` modules for additional processing and validation functionality.

## How to Develop

### Development Environment

All code must be written and tested in the same Python environment. To set up the development environment, you will need to install additional dependencies from `requirements.dev.txt`:

```bash
pip install -r requirements.dev.txt
```

A linter, `flake8`, is used to ensure code quality. Run the linter before committing changes:

```bash
flake8 
```

### Testing

The project includes a comprehensive suite of tests located in the `Tests/` folder. The tests are structured as follows:

- **read tests**: Validate signal reading functionality.
- **act tests**: Ensure actions on signals work as expected.
- **check tests**: Confirm that signals are properly validated.

Before making changes, ensure that all existing tests pass to avoid regressions. Run the tests using:

```bash
python -m unittest discover -s tests
```
## Side Notes

- The program was written on Ubuntu, so it has not been tested on Windows.
- The core focus of the project was on the functionalities, not the GUI. Improving the GUI could be a potential area for development.

## Contributing Guidelines

1. Always use the project’s virtual environment for development.
2. Maintain consistency with the existing code style and structure.
3. Run the linter and tests before submitting any code changes.

## Credits

This project was developed for the Computer Science department at Ain Shams University by:

- **Mohab Ashraf**
- **Moamen Sherif**

Special thanks to our teaching assistant:

- **Omar Sherif**

Special thanks to our supervisor:

- **Dr. Donia Gamal**