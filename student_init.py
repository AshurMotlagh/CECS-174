class Student:
    def __init__(self, name):
        self.name = name
        self.num_quiz = 0
        self.score = 0
        self.quiz_list = []

    def getName(self):
        return self.name

    def addQuiz(self, quiz):
        self.quiz_list.append(quiz)
        self.num_quiz += 1

    def getTotalScore(self):
        self.score = sum(self.quiz_list)
        return self.score

    def getAverageScore(self):
        return self.score / self.num_quiz


st1 = Student('Jim Black')
print(st1.getName())
st1.addQuiz(10)
st1.addQuiz(20)
print(st1.getTotalScore())
print(st1.getAverageScore())