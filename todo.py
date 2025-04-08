import json

def save_tasks(filename="tasks.json"):
	try:
		with open(filename, "w") as file:
			json.dump(tasks, file, indent=4)
		print("Tasks saved to file.")
	except Exception as e:
		print(f"Error saving tasks: {e}")

def load_tasks(filename="tasks.json"):
	try:
		with open(filename, "r") as file:
			loaded_tasks = json.load(file)
			if loaded_tasks != []:
				print(f"Loaded tasks: {loaded_tasks}")
				return loaded_tasks
			else:
				print("No previous tasks found. Starting with an empty list.")
				return []
	except FileNotFoundError:
		print("No previous tasks found. Starting with an empty list.")
		return []
	except json.JSONDecodeError:
		print("Error reading the file. The data may be corrupted.")
		return []

tasks = []
tasks = load_tasks()

def add_task():
	task = input("Enter new task: ")
	tasks.append({"desc": task, "done": False})
	print("> Task added!")

def show_tasks():
	for i, task in enumerate(tasks, 1):
		status = "[x]" if task["done"] else "[ ]"
		print(f"{status} {i}. {task['desc']}")

def mark_done(user_input):
	try:
		index = int(user_input)
		if 0 < index <= len(tasks):
			if (tasks[index - 1]["done"]):
				print(f"Task {index} is already marked as done!")
				return
			tasks[index - 1]["done"] = True
			print(f"Task {index} marked as done!")
		else:
			print("Invalid task index.")
		return
	except ValueError:
		task_name = user_input.strip() # strip extra spaces
		for task in tasks:
			if task["desc"].lower() == task_name.lower():
				if task["done"]:
					print(f"Task {task_name} is already marked as done!")
					return
				task["done"] = True
				print(f"Task {task_name} marked as done!")
				return
		print(f"Task {task_name} not found.")

def remove_task(user_input):
	try:
		index = int(user_input)
		if 0 < index <= len(tasks):
			del tasks[index - 1]
			print(f"Task {index} deleted.")
		else:
			print("Invalid task index.")
		return
	except ValueError:
		task_name = user_input.strip()
		for i, task in enumerate(tasks):
			if task["desc"].lower() == task_name.lower():
				del tasks[i]
				print(f"Task {task_name} deleted.")
				return
		print(f"Task {task_name} not found.")

while True:
	print("\n[1] Add Task\n[2] Show Tasks\n[3] Mark task as done\n[4] Remove task\n[5] Quit")
	choice = input("> ")

	if choice == "1":
		add_task()
	elif choice == "2":
		show_tasks()
	elif choice == "3":
		user_input = input("> Enter the task index or name to mark as done: ")
		mark_done(user_input)
	elif choice == "4":
		user_input = input("> Enter the task index or name to remove it: ")
		remove_task(user_input)
	elif choice == "5":
		save_tasks()
		break
	else:
		print("Invalid choice.")
