import xml.sax

class UchwytZaw(xml.sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.imie = ""
        self.nazwisko = ""
        self.miasto = ""
        self.tel = ""
        self.email = ""
        self.zawody = ""

    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "zawodnik":
            print("_________Zawodnik________")

    def endElement(self, tag):
        if self.CurrentData == "id":
            print(f"identyfikator zawodnika: {self.id}")
        elif self.CurrentData == "imie":
            print(f"Imię zawodnika: {self.imie}")
        elif self.CurrentData == "nazwisko":
            print(f'Nazwisko zawodnika: {self.nazwisko}')
        elif self.CurrentData == "miasto":
            print(f"Zawodnik pochodzi z miasta: {self.miasto}")
        elif self.CurrentData == "tel":
            print(f"telefon: {self.tel}")
        elif self.CurrentData == "email":
            print(f"adres e-mail: {self.email}")
        elif self.CurrentData == "zawody":
            print(f"nazwa zawodów: {self.zawody}")
    def characters(self,content):
        if self.CurrentData == "id":
            self.id = content
        elif self.CurrentData == "imie":
            self.imie = content
        elif self.CurrentData == "nazwisko":
            self.nazwisko = content
        elif self.CurrentData == "miasto":
            self.miasto = content
        elif self.CurrentData == "tel":
            self.tel = content
        elif self.CurrentData == "email":
            self.email = content
        elif self.CurrentData == "zawody":
            self.zawody = content

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)

handler = UchwytZaw()
parser.setContentHandler(handler)
parser.parse("zawodnik.xml")

