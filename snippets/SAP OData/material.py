class Material():

    matnr = ""
    meinh = ""
    ean11 = ""

    def __init__(self):
        pass

    def get_text(self):
        return self.matnr + " - " + self.ean11 + " (" + self.meinh + ")"