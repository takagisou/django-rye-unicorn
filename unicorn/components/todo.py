from django_unicorn.components import UnicornView


class TodoView(UnicornView):
    task = ""
    tasks = []

    def add(self):
        if self.task == "":
            return
            
        self.tasks.append(self.task)
        self.task = ""
