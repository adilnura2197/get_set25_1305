class Course:
    def __init__(self, title, lessons):
        self.title = title
        self.__lessons = lessons

    def get_lessons(self):
        return self.__lessons

    def set_lessons(self, new_lessons):
        self.__lessons = new_lessons


c1 = Course('Python', 40)

print(c1.title)
print(c1.get_lessons())

c1.set_lessons(60)

print(c1.get_lessons())
