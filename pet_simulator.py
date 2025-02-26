from abc import ABC, abstractmethod
import random
from tkinter import *
import time


class Pet:
    @abstractmethod
    def __init__(self, hunger: int = 50, happiness: int = 50, energy: int = 50, name="Pet"):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value < 0 or value > 100:
            raise ValueError("Hunger must stay between 0-100")
        self.__hunger = value

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value < 0 or value > 100:
            raise ValueError("Happiness must stay between 0-100")
        self.__happiness = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0 or value > 100:
            raise ValueError("Energy must stay between 0-100")
        self.__energy = value

    def feed(self):
        self.hunger -= 20
        self.energy += 10

    def play(self):
        self.happiness += 15
        self.energy -= 10

    def sleep(self):
        self.energy += 20
        self.hunger += 10

    def show_status(self):
        print(
            f"Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}")

    def random_event(self):
        sym = random.randint(1, 4)
        choose = random.randint(1, 3)
        if choose == 1:
            print("A random event has occured!")
            if sym == 1:
                print("Your pet found a snack!")
                self.hunger -= 10
                print("Hunger went down by 10!")
            elif sym == 2:
                print("Your pet felt lonely for too long!")
                self.happiness -= 10
                print("Happiness went down by 10!")
            elif sym == 3:
                print("Your pet had a bad dream!")
                self.energy -= 10
                print("Energy went down by 10!")
            elif sym == 4:
                print("Your pet found a new toy!")
                self.happiness += 15
                print("Happiness went up by 15!")


class Dog(Pet):
    def __init__(self, hunger: int = 50, happiness: int = 50, energy: int = 50, name="Pet"):
        super().__init__(hunger, happiness, energy, name)

    def play(self):
        self.happiness += 20
        self.energy -= 10

    def special_ability(self):
        proc = random.randint(1, 15)
        if proc == 1:
            for i in range(10):
                print("ERROR")
            self.happiness = 10
            self.energy = 10
            self.hunger = 10
            print("All status set to 10")
        elif proc != 1:
            print("Ability Successful!")
            self.happiness += 5
            self.energy += 5
            self.hunger -= 5
            print("Hunger went down by 5! Happiness went up by 5! Energy went up by 5!")


class Cat(Pet):
    def sleep(self):
        self.energy += 25
        self.hunger += 5

    def special_ability(self):
        if self.energy <= 20 and self.happiness <= 20:
            print("Ability Successful!")
            self.energy += 15
            self.happiness += 20
            print("Happiness went up by 20! Energy went up by 15!")
        else:
            print("Ability failed!")


class Dragon(Pet):
    def feed(self):
        self.hunger -= 30
        self.energy += 15
        self.happiness += 10

    def special_ability(self):
        if self.happiness <= 20 and self.energy >= 80:
            print("Ability Succesful!")
            self.happiness += 20
            self.energy -= 20
            self.hunger += 10
            print(
                " Hunger went up by 10! Happiness went up by 20! Energy went down by 20!")
        else:
            print("Ability failed!")


if __name__ == "__main__":
    p = Pet()
    d = Dog()
    c = Cat()
    dr = Dragon()
    user_in = input("Pick a pet: Dog(1), Cat(2), or Dragon(3)").lower().strip()
    if user_in == "dog" or user_in == "1":
        d.show_status()
        print("If any of your stats go above 100 or below 0, you fail.")
        time.sleep(1)
        while True:
            user_pick = input(
                "Select an action: Feed(1), Play(2), Sleep(3), Special(4), Exit(5)").lower().strip()
            if user_pick == "feed" or user_pick == "1":
                d.feed()
                print("Hunger went down by 20! Energy went up by 10!")
                d.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "play" or user_pick == "2":
                d.play()
                print("Happiness went up by 20! Energy went down by 10!")
                d.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "sleep" or user_pick == "3":
                d.sleep()
                print("Hunger went up by 5! Energy went up by 25!")
                d.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "special" or user_pick == "4":
                d.special_ability()
                d.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "exit" or user_pick == "5":
                print("Exiting")
                print("Final Status: ")
                d.show_status()
                break
            else:
                print("Invalid option. Please try again.")

    elif user_in == "cat" or user_in == "2":
        c.show_status()
        print("If any of your stats go above 100 or below 0, you fail.")
        while True:
            user_pick = input(
                "Select an action: Feed(1), Play(2), Sleep(3), Special(4), Exit(5)").lower().strip()
            if user_pick == "feed" or user_pick == "1":
                c.feed()
                print("Hunger went down by 20! Energy went up by 10!")
                c.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "play" or user_pick == "2":
                c.play()
                print("Happiness went up by 15! Energy went down by 10!")
                c.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "sleep" or user_pick == "3":
                c.sleep()
                print("Hunger went down by 5! Energy went up by 25!")
                c.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "special" or user_pick == "4":
                c.special_ability()
                c.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "exit" or user_pick == "5":
                print("Exiting")
                print("Final Status: ")
                c.show_status()
                break
            else:
                print("Invalid option. Please try again.")

    elif user_in == "dragon" or user_in == "3":
        dr.show_status()
        print("If any of your stats go above 100 or below 0, you fail.")
        while True:
            user_pick = input(
                "Select an action: Feed(1), Play(2), Sleep(3), Special(4), Exit(5)").lower().strip()
            if user_pick == "feed" or user_pick == "1":
                dr.feed()
                print(
                    "Hunger went down by 30! Happiness went up by 10! Energy went up by 15!")
                dr.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "play" or user_pick == "2":
                dr.play()
                print("Happiness went up by 15! Energy went down by 10!")
                dr.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "sleep" or user_pick == "3":
                dr.sleep()
                print("Hunger went up by 5! Energy went up by 25!")
                dr.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "special" or user_pick == "4":
                dr.special_ability()
                dr.show_status()
                p.random_event()
                print("\n")
                time.sleep(1)
            elif user_pick == "exit" or user_pick == "5":
                print("Exiting")
                print("Final Status: ")
                dr.show_status()
            else:
                print("Invalid option. Please try again.")
