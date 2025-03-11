# TODO: Add code here

# 1
class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

# 2
    def mark_completed(self):
        self.completed: bool = True

# 3
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

# 4
    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"

# 5
class TodoBook:
    def __init__(self):
        self.todos: dict = {}

# 6
    def add_todo(self, title: str, description: str) -> int:
        id_code = len(self.todos) + 1
        todo = Todo(id_code, title, description)
        self.todos[id_code] = todo
        return id_code

# 7
    def pending_todos(self) -> list[Todo]:
        

"""
# 8
    def compled_todos(self) -> list:
        #

# 9
    def tags_todo_count(self) -> dict[int]:
        #
"""
