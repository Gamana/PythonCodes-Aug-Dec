class mentor:
    def define_state(self):
        self.name = "Gamana"
        self.tech = "python"
        self.age = 20

    def teach(self):
        print(f"{m.name} is teaching")
    
    def groom(self):
        print(f"{self.name} is grooming")

m = mentor()
m.define_state()
print(f"Name: {m.name}")
print(f"Age: {m.age}")
print(f"Tech: {m.tech}")
m.teach()
m.groom()