class Car:
    def start(self):
        print("Khy-khy")
        

helmut = Car()
helmut.start()


class User:
    def cheer(self):
        print(f"Hello, I am {self.name}")
        
    def say_hello(self, other):
        print(f"Hi {other}, I am {self.name}")
        
user1 = User()
user1 = "JAN"
user1.cheer()
user1.say_hello("Hello")

class Position():
    def step_right(self):
        self.x += 1.0

    def move_up(self, value):
        self.y += value
        
pos1 = Position()
pos1.x = 0.0
pos1.y
