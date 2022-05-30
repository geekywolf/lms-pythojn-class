class Student:
    # [assignment] Skeleton class. Add your code here
    name = ""
    age = 0
    tracks = []
    score = 0.0
    def __init__(self, name, age, tracks, score):
        Student.name = name
        Student.age = age
        Student.track = tracks
        Student.score = score

    def change_name(self,newName):
        self.name = newName
        return

    def change_age(self,newAge):
        self.age = newAge
        return

    def add_track(self,newTrack):
        self.track = newTrack
        return

    def get_score(self):
       return print(self.score)
    
    # def __init__(self)
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)



Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# Test
print(Bob.track)
