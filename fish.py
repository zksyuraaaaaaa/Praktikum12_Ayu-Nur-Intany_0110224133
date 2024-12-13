from Animal import animal

class fish(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,bernapas,habitat) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    # Method
    def info_fish(self):
        super().info_animal()
        print("Bernapas \t\t:",self.bernapas,"\nTempat Habitat\t\t:",self.habitat)

print()
fish = fish("Lumba-lumba","ikan","Di Laut","Melahirkan","Paru-paru","Air tawar atau Air asin")
print("## Info Fish ##")
fish.info_fish()
