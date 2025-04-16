class Laptop:
    def __init__(self, cpu, ram=4096, gpu="AMD", price=3000):
        self.gpu = gpu
        self.price = price
        self.setCpu(cpu)
        
        
    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unknown"
            
    def setRam(self, ram):
        if type(ram) == int and ram>=2048:
            self.ram = ram
        else:
            self.ram = 2048
    def printData(self):
        print(self.cpu, self.ram, self.gpu, self.price)
        
lap1 = Laptop("Intel")
lap1.printData()
lap1 = Laptop("Geforce")
lap1.printData()
