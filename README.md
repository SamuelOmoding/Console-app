# Console-app
## Task Manager - Console CRUD Application with File Persistence

This is a simple console-based task management system implementing CRUD (Create, Read, Update, Delete) operations with persistent file storage using Python.

# Features
- 🆕 Create task with title, description, due date, and status
- 📋 View all tasks in a clean formatted list
- ✏️ Update/edit existing tasks
- ❌ Delete tasks with confirmation
- 📅 Status tracking (Not Started/InProgress/Completed)
- 💾 Automatic file persistence (tasks saved between sessions)
- 📂  JSON file storage for easy data management
- 🔍 Input validation for dates and status
- 🔄 Persistent menu until explicit exit

## Installation
1. Clone the repository
2. Ensure you have python3

**Run the Application** - pyhton3 crud.py

## Usage
- Task Manager
   1. Create Task
   2. View Task
   3. Update Task
   4. Delete Task
   5. Exit

## Data Persistence
- Tasks are automatically saved to tasks.json in the same directory
- The file is created automatically on first run
- Data is preserved between application sessions
- Files uses human-readable JSON format

## Technical Details
1. File operations use standard Python json module
2. Date validation ensures proper format (YYYY-MM-DD)
3. Status selection uses numbered menu for reliability
4. All changes are immediately persisted to disk
   