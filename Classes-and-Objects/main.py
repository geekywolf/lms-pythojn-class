class Student:
    # [assignment] Skeleton class. Add your code here
    #ame = ""
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score

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
