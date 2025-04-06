import os
import json
from datetime import datetime

class Task:
    """
    Representing a task with basic attributes.
    Attributes:
    title (str): Short description of the task 
    description (str): Detailed task information
    due_date (str): Target completion date (format: YYYY-)
    status (str): Current state of the task (Not Started/In Progress/Completed)
    """
    def __init__(self, title, description, due_date, status="Not Started"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        """Clean string representation of a task (no duplicates)"""
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due_date: {self.due_date}\n"
            f"Status: {self.status}\n"
            "-" * 1  
        )    
    
    def to_dict(self):
        """Converting task to dictionary for serialization"""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        return cls(data["title"], data["description"], data["due_date"], data["status"])            
class TaskManager:
    """
    Manages CRUD operations for tasks using in-memory list storage.
    Main operations:
         - create_task(): Add new task
         - read_task(): View all tasks
         - update_task(): Update existing task
         - delete_task(): Remove task by index
    """            
    def __init__(self, filename="task.json",):
        self.filename = filename
        """Initialize empty task list"""
        self.tasks = []  
        self.load_task()
        
    def load_task(self):
        """ Load tasks from JSON file"""
        if os.path.exists(self.filename):
            if os.path.getsize(self.filename) > 0:
                file = open(self.filename, 'r')
                data = json.load(file)
                file.close()
                self.tasks = [Task.from_dict(task_data) for task_data in data]
            else:
                self.tasks = []
        else:
            self.tasks = []            
    
    def save_task(self):
        file = open(self.filename, 'w')
        json.dump([task.to_dict() for task in self.tasks], file, indent=2)
        file.close()
        
    def validate_date(self, date_str):
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            return False
        year, month, day = date_str.split('-')
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False
        if int(month) < 1 or int(month) > 12:
            return False
        if int(day) < 1 or int(day) > 31:
            return False
        return True   
            
    def create_task(self):
        print("\nCreate New Task")
        print("=========")  
        title = input("Enter Task Title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            return
        description = input("Enter Task Description: ").strip()
        due_date = ""
        while not due_date or not self.validate_date(due_date):
            due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
            if not self.validate_date(due_date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                due_date = ""
        
        """Input validation"""
        status = ""
        while status not in ["1", "2", "3"]:
            print("\nTask Status Options:")
            print("1. Not Started")
            print("2. In Progress")
            print("3. Completed")
            status = input("Enter Task Status (1-3): ").strip()
        
        status_map = {"1": "Not Started", "2": "In Progress", "3": "Completed"}   
                         
        """Create and store new task"""
        new_task = Task(title, description, due_date, status_map[status])
        self.tasks.append(new_task)
        self.save_task()  
        print("\nTask created successfully.")   
        
    def read_tasks(self):
        """Show all tasks"""
        print("\nTasks List:")
        print("=========")
        if not self.tasks:
            print("No tasks found.")
            return
        
        """Display each task with index number of tasks"""
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task #{i}")
            print(task)
            
    def update_tasks(self):
        """Edit tasks"""
        self.read_tasks()
        if not self.tasks:
            return
        
        """Get valid task selection"""
        task_num = input("\nEnter task number to update:").strip()
        if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(self.tasks):
            print("Invalid task number.")
            return
       
        task = self.tasks[int(task_num) - 1]
        print("\nCurrent Task Details:")
        print(task)
        
        """Get updated fields"""
        print("\nEnter new values (press Enter to keep current):") 
        title = input(f"Title [{task.title}]: ").strip()
        description = input(f"Description [{task.description}]: ").strip()
        due_date = input(f"Due Date [{task.due_date}]: ").strip()
        
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            if self.validate_date(due_date):
                task.due_date = due_date
            else:
                    print("Invalid date format. Date not updated.")
                    
        """Input validation"""
        while True:
            print("\nCurrent Status:", task.status)
            print("1. Not Started")
            print("2. In Progress")
            print("3. Completed")
            print("4. Keep Current Status")
            new_status = input("Choose option (1-4): ").strip()
            
            if new_status == "1":
               task.status = "Not Started"
               break
            elif new_status == "2":
                task.status = "In Progress"
                break
            elif new_status == "3":
                task.status = "Completed"
                break
            elif new_status == "4":
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
                
        self.save_task()        
        print("\nTask updated successfully.")
        
    def delete_task(self):
        self.read_tasks()
        if not self.tasks:
            return
        
        """Get valid task selection"""
        task_num = input("\nEnter task number to delete:").strip()
        if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(self.tasks):
            print("Invalid task number.")
            return
        
        """Confirm deletion"""
        confirm = input(f"Are you sure you want to delete Task #{task_num}? (y/n): ").lower().strip()
        if confirm!= "y":
            del self.tasks[task_num - 1]
            print("\nTask deleted successfully.")
        else:
            print("Deletion canceled.")
            
def display_menu():
        """Show application menu options"""
        print("\nTask Manager Menu:")
        print("=================")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
def main():
        """Main application loop"""
        manager = TaskManager()
        
        while True:
            display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                manager.create_task()
            elif choice == "2":
                manager.read_tasks()
            elif choice == "3":
                manager.update_tasks()
            elif choice == "4":
                manager.delete_task()
            elif choice == "5":
                print("\nExiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")    
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()                
        