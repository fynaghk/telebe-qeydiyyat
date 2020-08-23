class Student:
    def __init__(self, name, surname, mail, password, number):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password
        self.number = number

    def get_student(self):
        return self.name, self.surname, self.mail, self.password, self.number


def name(studentName):
    return studentName


def surname(studentSurname):
    return studentSurname


def mail(studentMail):
    return studentMail


def password(studentPassword):
    return studentPassword


def number(studentNumber):
    return studentNumber


print("""
Yeni tələbə əlavə etmək üçün '1' 
Tələbənin məlumatlarının  silinməsi üçün '2'
Tələbənin məlumatlarının dəyişdirilməsi üçün '3'
Tələbənin məlumatlarını göstərmək üçün '4'
Bütün tələbələrin məlumatlarının göstərilməsi üçün '5'
""")

n = int(input("Daxil edin:"))


def registration():
    studentName = name(input("Adınızı daxil edin:"))
    studentSurname = surname(input("Soyadınızı daxil edin:"))
    studentMail = mail(input("Mail`inizi daxil edin:"))
    studentPassword = password(int(input("Parolunuzu daxil edin:")))
    studentNumber = number(int(input("Telefon nömrənizi daxil edin: +994")))


def registrationNew(students):
    studentName = name(input("Telebe adini daxil edin: "))
    studentSurname = surname(input("Telebe soyadini daxil edin: "))
    studentMail = mail(input("Telebe emailin daxil edin: "))
    studentPassword = password(input("3 reqemli telebe kodunu daxil edin: "))
    studentNumber = number(input("Telebe telefon nomresini daxil edin: "))

    students.append(Student(studentName, studentSurname, studentMail, studentPassword, studentNumber))

if n==1:
        registrationNew()


