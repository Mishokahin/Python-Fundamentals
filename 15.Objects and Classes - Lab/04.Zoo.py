class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        if species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        if species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        if species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo = Zoo(input())

for i in range(int(input())):
    animal = input().split(" ")
    zoo.add_animal(animal[0], animal[1])

print(zoo.get_info(input()))