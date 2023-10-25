# People Management Program

The People Management Program is a Python application that allows you to manage a list of people with their names and ages. This README provides an overview of the program, its functionality, and how to use it.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add people with names and ages.
- Serialize the list of people to a JSON file.
- Deserialize the list of people from a JSON file.
- Calculate the average age of the people in the list.
- Print the list of people with their details.

## Getting Started

To get started with the People Management Program, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/people-management.git

    Change to the program's directory:

    bash

cd people-management

Install the required Python packages if not already installed:

bash

    pip install -r requirements.txt

Usage

The program is organized as a Python script with a PeopleManager class. You can use this class to manage a list of people.

    Create a PeopleManager instance:

    python

manager = PeopleManager()

Add people to the list:

python

manager.add_person("John", 30)
manager.add_person("Alice", 25)

Serialize the list to a JSON file:

python

manager.serialize_to_json("people.json")

Deserialize the list from the JSON file:

python

manager.deserialize_from_json("people.json")

Calculate and print the average age:

python

average_age = manager.calculate_average_age()
print(f"Average Age: {average_age}")

Print the list of people:

python

    manager.print_people()

For further information and to customize the program, refer to the code and comments in the people_management.py script.
