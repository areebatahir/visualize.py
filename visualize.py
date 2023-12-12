import matplotlib.pyplot as plt
import numpy as np
class Animal:
    def making_sound(self):
        pass
    def visualize(self):
        pass
class Dog(Animal):
    def making_sound(self):
        print("Dog: Boaw")
    def visualize(self):
        x = np.linspace(5, 30, 1000)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("Dog's Visualization")
        plt.show()
class Cat(Animal):
    def making_sound(self):
      print("Cat: Meow")
    def visualize(self):
       x = np.linspace(0, 40, 800)
       y = np.cos(x)
       plt.plot(x, y)
       plt.title("Cat's visualization")
       plt.show()
cat = Cat()
cat.making_sound()
cat.visualize()
dog = Dog()
dog.making_sound()
dog.visualize()

