class Grades():
    def __init__(self, number):
        self.number = number
        
    def getGrades(self):
        self.number = int(input("Enter the numeric grade: "))
        if self.number > 89:
            letter = 'A'
        elif self.number > 79:
            letter = 'B'
        elif self.number > 69:
            letter = 'C'
        else:
            letter = 'F'
        print("The letter grade is", letter)

def main():
    grades = Grades(self, number)
    grades.getGrades()
main()