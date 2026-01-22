
class Car:
    def __init__(self, name, color, speed,tyreSize=None):
        self.name = name
        self.color = color 
        self.speed = speed
        self.tyreSize = tyreSize

    def carDetail(self,help):
        print(f"car name is {self.name}")
        print(f"car color is {self.color}")
        print(f"car speed is {self.speed}")
        if self.tyreSize is not None:
            print(f"car tyre size is {self.tyreSize}")
        print(f"car help is {help}")


def main():
    my_car = Car("civic", "black", 23, 16)
    details = "Service available"
    my_car.carDetail(details)
    print ("---------------")
    my_car2 = Car("corolla", "white", 30)
    my_car2.carDetail("24/7 support")

if __name__ == "__main__":
    main()
    
