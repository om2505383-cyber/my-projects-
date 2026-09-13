from department import Department


class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments: list[Department] = []

    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def __str__(self) -> str:
        return (
            f"Hospital: {self.name}\n"
            f"Location: {self.location}\n"
            f"Departments: {len(self.departments)}"
        )
