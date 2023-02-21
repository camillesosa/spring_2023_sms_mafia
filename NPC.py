class NPC:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        self.weapon = None;
        self.guilty = None;
        
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
        
    def talk(string):
        return print(f"{string}")
