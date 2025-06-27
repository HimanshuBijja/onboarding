import os

class person:
    def __init__(self, cname):
        self.name = input(f"Enter {cname}'s name: ")

    def displ(self):
        print(f"Name: {self.name}")

class teacher(person):
    def __init__(self, name):
        super().__init__(name)
        self.sub = input("Enter subject taught: ")

    def displ(self):
        super().displ()
        print(f"Subject: {self.sub}")

class employee(teacher):
    def __init__(self, name):
        super().__init__(name)
        self.dept = input('Enter department: ')

    def displ(self):
        super().displ()
        print(f'Department: {self.dept}')

def main():
    while True:
        n = int(input('1. Create Teacher\n2. Create Employee\n3. Quit\nSelect an option: '))
        match n:
            case 1:
                t = teacher("Teacher")
                t.displ()
            case 2:
                e = employee("Employee")
                e.displ()
            case 3:
                return

main()
