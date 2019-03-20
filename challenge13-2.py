class Horse:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self,name):
        self.name = name

yusuke = Rider("Yusuke Yamada")
tarou = Horse("Tarou","sarabred",yusuke)

print(tarou.owner.name)
