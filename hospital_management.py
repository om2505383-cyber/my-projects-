class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        return self.medical_record


class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Position: {self.position}"
        )


class Department:
    def __init__(self, name: str):
        self.name = name
        self.patients = []
        self.staff_members = []

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff_members.append(staff_member)


class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department: Department) -> None:
        self.departments.append(department)


# =========================
# MAIN PROGRAM
# =========================

# Create hospital
hospital = Hospital("City Hospital", "Cairo")

# Create departments
cardiology = Department("Cardiology")
emergency = Department("Emergency")

# Hospital contains departments
hospital.add_department(cardiology)
hospital.add_department(emergency)

# Create patients
patient1 = Patient(
    "Ahmed",
    30,
    "Blood pressure check and treatment"
)

patient2 = Patient(
    "Omar",
    22,
    "Routine medical examination"
)

# Create staff
doctor = Staff("Dr. Ali", 45, "Doctor")
nurse = Staff("Mona", 32, "Nurse")

# Departments manage patients and employ staff
cardiology.add_patient(patient1)
cardiology.add_staff(doctor)

emergency.add_patient(patient2)
emergency.add_staff(nurse)


# =========================
# DISPLAY EVERYTHING
# =========================

print("===== HOSPITAL INFORMATION =====")
print("Hospital:", hospital.name)
print("Location:", hospital.location)

print("\n===== DEPARTMENTS =====")
for department in hospital.departments:
    print("\nDepartment:", department.name)

    print("Patients:")
    for patient in department.patients:
        print(" -", patient.view_info())
        print("   Medical Record:", patient.view_record())

    print("Staff:")
    for staff_member in department.staff_members:
        print(" -", staff_member.view_info())
