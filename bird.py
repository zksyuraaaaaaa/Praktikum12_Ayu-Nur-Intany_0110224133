from Animal import animal

class bird(animal):
    

    def __init__(self, nama, makanan, hidup, berkembang_biak,Warna,paruh) :
        super().__init__(nama,makanan, hidup, berkembang_biak)
        self.warna = Warna
        self.paruh = paruh

    # Method
    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t:",self.warna,"\njenis paruh\t\t:",self.paruh)

print()
bird = bird("Elang","Daging","Ditebing","Menghasilkan Telur","Coklat","Bengkok dan Lancip")
print("## Info Bird ##")
bird.info_bird()
