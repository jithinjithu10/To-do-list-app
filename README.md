# Todo List App

## Overview

The **Todo List App** is a simple yet effective command-line application built in Python that helps users manage their daily tasks efficiently. With a user-friendly interface and essential functionalities, this app is perfect for anyone looking to organize their tasks, set priorities, and enhance productivity.

## Features

- **Add Tasks**: Quickly add new tasks to your list with a brief description.
- **Remove Tasks**: Easily remove tasks that are completed or no longer relevant.
- **View Tasks**: Display all tasks in a clear format, showing their current status.
- **Persistent Storage**: Tasks are saved in a local file (`tasks.txt`), ensuring they persist between sessions.
- **Mark Tasks as Complete**: Optionally mark tasks as completed without removing them from the list.
- **Prioritize Tasks**: Assign priority levels to tasks for better organization.
- **Search Tasks**: Find tasks quickly using a search function.
- **User-Friendly Menu**: Intuitive command-line interface with guided prompts for each action.

## Requirements

- Python 3.x
- No additional libraries are required for basic functionality.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd todo-list-app
   ```

3. **Run the application**:
   ```bash
   python todo.py
   ```

## Usage

Upon launching the application, users will be presented with a menu of options to manage their tasks. The interaction with the app can be summarized as follows:

### Menu Options

1. **Add a New Task**: Prompt the user to input a description for the task, along with optional priority (e.g., low, medium, high).
2. **Remove a Task**: Prompt the user to specify the task number they wish to remove from the list.
3. **View All Tasks**: Display all current tasks along with their status (e.g., complete, incomplete) and priority level.
4. **Mark Task as Complete**: Allow users to mark a specified task as complete.
5. **Search Tasks**: Prompt users to enter a keyword to search through tasks.
6. **Exit**: Close the application.

### Example Interaction

```
Welcome to the Todo List App!
1. Add a new task
2. Remove a task
3. View all tasks
4. Mark task as complete
5. Search tasks
6. Exit

Please select an option (1-6):
```

## Code Structure

- **`todo.py`**: The main application file where the logic for managing tasks is implemented.
- **`tasks.txt`**: A text file used to store tasks persistently. Each line represents a task with its status and priority.
  
### Main Functions

- **`add_task(description, priority)`**: Adds a new task to the task list and saves it to `tasks.txt`.
- **`remove_task(task_number)`**: Removes a specified task from the task list and updates `tasks.txt`.
- **`view_tasks()`**: Displays all current tasks in the list, including their status and priority.
- **`mark_complete(task_number)`**: Marks a specified task as complete in the task list.
- **`search_tasks(keyword)`**: Searches for tasks containing the specified keyword.

## Example Task Format in `tasks.txt`

```
1|Buy groceries|incomplete|medium
2|Read a book|complete|low
3|Finish project report|incomplete|high
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request. To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a new branch for your feature or bug fix**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes and commit them**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Jithin S.**  
Email: [jithinyakkara@gmail.com](mailto:jithinyakkara@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/jithins2003)  
[GitHub](https://github.com/jithinjithu10)  
