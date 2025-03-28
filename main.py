import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def heal(self):
        heal_amount = 15
        self.health += heal_amount
        print(f"{self.name} восстанавливает {heal_amount} здоровья.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            print(f"{self.player.name} здоровье: {self.player.health}, {self.computer.name} здоровье: {self.computer.health}")
            action = input("Выберите действие: 1 - Атаковать, 2 - Исцелиться: ")

            if action == "1":
                self.player.attack(self.computer)
            elif action == "2":
                self.player.heal()
            else:
                print("Неверный ввод! Пожалуйста, выберите 1 или 2.")
                continue

            if not self.computer.is_alive():
                print(f"{self.computer.name} погиб! {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} погиб! {self.computer.name} победил!")
                break

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()