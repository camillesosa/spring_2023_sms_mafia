class NPC:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        self.weapon = None;
        self.guilty = None;
        self.jail = False;
        
    def getWeapon(self):
        return self.weapon;
        
    def getName(self):
        return self.name;
    
    def setGuilty(self, is_evil):
        self.guilty = is_evil;
        
    def getGuilty(self):
        return self.guilty;
        
    def setWeapon(self, weapon):
        self.weapon = weapon
        
    def setJail(self, decision):
        self.jail = decision;
        
    def inJail(self):
        return self.jail;
        
    def talk(string):
        return print(f"{string}")
