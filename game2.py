class College:
    def __init__(self, name: str, quota: int, preference_list: list[str]):
        self.name = name
        self.quota = quota
        self.preference_list = preference_list
        self.accepted_students = []

    def is_full(self) -> bool:
        return len(self.accepted_students) >= self.quota

    def prefers(self, student1: str, student2: str) -> bool:
        """
        Return True if college prefers student1 over student2, else False
        """
        return self.preference_list.index(student1) < self.preference_list.index(student2)

class Student:
    def __init__(self, name: str, preference_list: list[str]):
        self.name = name
        self.preference_list = preference_list
        self.assigned_college = None

    def prefers(self, college1: str, college2: str) -> bool:
        """
        Return True if student prefers college1 over college2, else False
        """
        return self.preference_list.index(college1) < self.preference_list.index(college2)

class CollegeAdmissionsGame:
    def __init__(self, colleges: list[College], students: list[Student]):
        self.colleges = colleges
        self.students = students

    def deferred_acceptance(self) -> None:
        """
        Implement the deferred acceptance algorithm
        """
        while True:
            unmatched_students = [s for s in self.students if s.assigned_college is None]
            if not unmatched_students:
                break

            for student in unmatched_students:
                for college in student.preference_list:
                    college = next((c for c in self.colleges if c.name == college), None)
                    if not college.is_full() and (not student.assigned_college or college.prefers(student.name, student.assigned_college)):
                        if student.assigned_college:
                            student.assigned_college.accepted_students.remove(student.name)
                        college.accepted_students.append(student.name)
                        student.assigned_college = college
                        break

    def run(self) -> None:
        """
        Run the college admissions game using the deferred acceptance algorithm
        """
        self.deferred_acceptance()

        # Print the results
        for college in self.colleges:
            print(f"{college.name} accepted students:")
            for student_name in college.accepted_students:
                print(f" - {student_name}")