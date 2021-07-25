class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.model=model
    
    def start(self):
        print("Started")
    
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")
    
    def changegear(self,geartype):
        print("changing gear", geartype)
    
audi=Car("A6","blue","audi","220")
print(audi.color)
print(audi.company)
print(audi.model)
print(audi.speedlimit)
 
audi.start()
audi. accelerate()
audi.changegear(4)
audi.stop()

