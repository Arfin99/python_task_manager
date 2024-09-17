import statistics
from datetime import datetime


class Task:

	def __init__(self, title, description):
		self.title = title
		self.description = description
		self.completed = False
		self.created_at = datetime.now().isoformat()
		self.updated_at = datetime.now().isoformat()


class TaskManager:

	def __init__(self, storage):
		self.storage = storage

	def add_task(self, title, description):
		task = Task(title, description)
		self.storage.save_task(task)
		return task

	def complete_task(self, title):
		task = self.storage.get_task(title)
		if task:
			task.completed = True
			task.updated_at = datetime.now().isoformat()
			self.storage.update_task(task)
			return True
		return False

	def list_tasks(self, completed=None):
		tasks = self.storage.get_all_tasks()
		if completed is not None:
			tasks = [task for task in tasks if task.completed == completed]
			return tasks
		return tasks

	def generate_report(self):
		tasks = self.storage.get_all_tasks()
		total_tasks = len(tasks)
		completed_tasks_taken_time = [(datetime.fromisoformat(task.updated_at).timestamp() - datetime.fromisoformat(task.created_at).timestamp()) for task in tasks if task.completed]
		completed_tasks = len(completed_tasks_taken_time)

		report = {
		    "total": total_tasks,
		    "completed": completed_tasks,
		    "pending": total_tasks - completed_tasks,
			"average task completed time": statistics.mean(completed_tasks_taken_time)
		}

		return report

