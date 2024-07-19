# Task Management App

## Overview
The Task Management App is a Python-based tool designed for managing tasks with functionalities for adding, removing, listing, and recommending tasks. It uses machine learning to suggest high-priority tasks based on user input.

## Features
- Add Task: Allows users to add a new task with a description and priority.
- Remove Task: Enables users to remove a task by its description.
- List Tasks: Displays all existing tasks along with their descriptions and priorities.
- Recommend Task: Provides a recommendation for a high-priority task based on a trained machine learning model.

## Requirements
- Python 3.x
- pandas
- scikit-learn

## Installation
To install the required packages, use the following command:
pip install pandas scikit-learn

## Usage
- Running the App:
   Execute the Python script to start the application.
- Menu Options:
  - Add Task: Input a task description and specify its priority (Low, Medium, High).
  - Remove Task: Provide the description of the task you wish to delete.
  - List Tasks: View all tasks along with their descriptions and priorities.
  - Recommend Task: Get a recommendation for a high-priority task based on the machine learning model.
  - Exit: Exit the application.

## Functionality
Data Persistence
   The application reads from and writes to a CSV file (tasks.csv) to manage task data. If the file does not exist, it creates one with the appropriate columns.
Task Management
  - Adding a Task: New tasks are added to the CSV file and the model is retrained.
  - Removing a Task: Tasks can be removed by description, and the model is retrained.
  - Listing Tasks: Displays all tasks with their details.
  - Recommending a Task: Uses a machine learning model to recommend high-priority tasks.
Machine Learning Model
   The application employs a Naive Bayes classifier with a CountVectorizer for text data processing. The model is trained on task descriptions and priorities to make recommendations.

## Contributing
To contribute to this project, fork the repository, make your changes, and submit a pull request. Contributions and suggestions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
