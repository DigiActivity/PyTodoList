from task_manager import TaskManager
from cli import TaskCLI

cli = TaskCLI(TaskManager())

cli.start()
