#SB deneme class ve method

class Arabalar():
    def __init__(self,marka,model,renk,vites):

        self.marka  = marka
        self.model  = model
        self.renk   = renk
        self.vites  = vites


araba_1 = Arabalar("Ford", "Mustang", "Siyah", "Manuel")

print(araba_1.marka, araba_1.model, araba_1.renk, araba_1.vites)
