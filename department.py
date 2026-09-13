from patient import Patient
from staff import Staff


class Department:
    def __init__(self, name: str):
        self.name = name
        self.patients: list[Patient] = []
        self.staff_members: list[Staff] = []

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff_members.append(staff_member)

    def __str__(self) -> str:
        return (
            f"Department: {self.name}\n"
            f"Patients: {len(self.patients)}\n"
            f"Staff: {len(self.staff_members)}"
        )
