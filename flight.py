class Flight():
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.person = []
    
    def addpassenger(self,name):
        if  not self.open_seats():
            return False     
        self.person.append(name)
        return True
    
    def open_seats(self):
        return self.capacity-len(self.person)
    
f = Flight(3)
people = ["Junaid", "Majeed", "Zuhaib", "Mirha"]
for person in people:
    if f.addpassenger(people):
        print(f"Added {person} to the flight")    
    else:
        print(f"No Avaliable seats for {person}")


        
