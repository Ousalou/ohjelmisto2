# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä Talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan selfn ominaisuutena.
# Kirjoita Talon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


class House:
    def __init__(self, house_floors):
        self.house_floors = house_floors
        self.elevators = []
        if self.house_floors <= 3:
            self.elevator_amount = 2
        elif self.house_floors > 2:
            self.elevator_amount = self.house_floors // 2
        for i in range(self.elevator_amount):
            h = Elevator(house_floors)
            self.elevators.append(h)

    def aja_hissia(self, el_number, move_to_floor):
        self.elevators[el_number].siirry_kerrokseen(move_to_floor)

class Elevator:
    hissit_amount = 0

    def __init__(self, max_floor):
        Elevator.hissit_amount += 1
        self.name = Elevator.hissit_amount
        self.max_floor = max_floor
        self.min_floor = 1
        self.current_floor = 1

    def kerros_alas(self, move_to_floor):
        while self.current_floor != move_to_floor:
            self.current_floor = self.current_floor - 1
            print(f".... olemme kerroksessa {self.current_floor} ....")
        print(f"\n Olemme saapuneet kerrokseen {self.current_floor}!\n")

    def kerros_ylos(self, move_to_floor):
        while self.current_floor != move_to_floor:
            self.current_floor = self.current_floor + 1
            print(f".... olemme kerroksessa {self.current_floor} ....")
        print(f"\n Olemme saapuneet kerrokseen {self.current_floor}!\n")

    def siirry_kerrokseen(self, move_to_floor):
        print(f"\nOlemme kerroksessa {self.current_floor}\nSiirrytään kerrokseen {move_to_floor}!\n")
        if move_to_floor > self.max_floor:
            print(f"Ylin kerros on {self.max_floor}!\n")
        elif move_to_floor < self.min_floor:
            print(f"Alin kerros on {self.min_floor}!\n")
        elif self.current_floor > move_to_floor:
            self.kerros_alas(move_to_floor)
        elif self.current_floor < move_to_floor:
            self.kerros_ylos(move_to_floor)
        elif self.current_floor == move_to_floor:
            print(f"Olet jo kerroksessa {self.current_floor}!\n")


max_floor = int(input("Anna ylimmän kerroksen numero: "))
talo = House(max_floor)

while True:
    el_number = int(input("Mitä hisseistä haluat ajaa? ")) - 1
    move_to_floor = int(input("Mihin kerrokseen haluat mennä?"))
    talo.aja_hissia(el_number, move_to_floor)
    print(f"Hissi {talo.elevators[el_number].name } on kerroksessa {talo.elevators[el_number].current_floor}")
