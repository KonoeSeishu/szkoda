class Computer():
    def __init__(self, modelName, ram, storage):
        self.modelName = modelName
        self.ram = ram
        self.storage = storage
        
    def showSpecs(self):
        print({self.modelName}, {self.ram}, {self.storage})
    
    def upgradeRam(self, ram):
        self.name + ram
        
    def __del__(self):
        print("object deleted")
        
        
        
comp1 = Computer("DELL", 64, 512)