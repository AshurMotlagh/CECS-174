class Notebook:
    def __init__(self):
        self.paper = ""

    def setText(self, text):
        self.paper += text + "\n"

    def getText(self):
        return self.paper

    # Overriding print() method to print out the object.
    def __repr__(self):
        return self.paper


class Student:
    def __init__(self, name):
        self.name = name

    def readText(self, a_notebook): # Passing in instance of obj.
        return self.name + " is reading the notebook ---> " + "\n" + a_notebook.getText()

    def writeText(self, a_notebook, text):
        a_notebook.setText(self.name + " wrote: " + text)

yellow_notebook = Notebook()
st_1 = Student("Sam")
st_2 = Student("Jenn")
st_1.writeText(yellow_notebook, "hi there")
print(st_2.readText(yellow_notebook))
st_2.writeText(yellow_notebook, "hello what's up?")
print(st_1.readText(yellow_notebook))
print(yellow_notebook)






























