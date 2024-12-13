from Animal import animal

class snake(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,warna,habitat) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.warna = warna
        self.habitat = habitat

    # Method
    def info_snake(self):
        super().info_animal()
        print("Warna \t\t\t:",self.warna,"\nTempat Habitat\t\t:",self.habitat)

print()
snake = snake("King Cobra","Daging","Di Hutan","Bertelur","Hitam","Hutan atau Rawa")
print("## Info Snake ##")
snake.info_snake()
