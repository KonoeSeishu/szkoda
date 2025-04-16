class Museum():
    def __init__(self, name):
        self.name = name
        self.collection = []
        
    def addPainting(self,title,author, year):
        printing = {
            "tytul obrazu": title,
            "autor obrazu": author,
            "rok obrazu": year
        }
        self.collection.append(printing)
        
    def showCollection(self):
        for i in self.collection:
            print(f"autor: {i.name}, title: {i.title}, author: {i.author}, year: {i.year}")
            
    def countPaintings(self):
        return len(self.collection)
        
        
Museum1 = Museum.addPainting("Museum", "jakis tytol", "jan jakis", 1000)
            
            
    
        