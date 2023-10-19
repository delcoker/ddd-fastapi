import requests

from src.domain.repositories.api.api_repository import ApiRepository
from src.infrastructure.models.dto.todo_dto import TodoDto


class ApiRepositoryImpl(ApiRepository):
    todo_uri = "https://jsonplaceholder.typicode.com/todos"

    def __int__(self):
        pass

    def fetch_data(self) -> list[TodoDto]:
        response = requests.get(self.todo_uri)
        todos_json = response.json()
        todos: list[TodoDto] = []

        for todo_data in todos_json:
            todo = TodoDto(id=todo_data["id"],
                           title=todo_data["title"],
                           completed=todo_data["completed"])
            todos.append(todo)

        return todos
