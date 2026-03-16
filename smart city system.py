from abc import ABC, abstractmethod
class Citizen(ABC):
    def __init__(self, name , age, job , id_number):
       
        self.name = name 
        self.age = age 
        self.job = job
        self.id_number  = id_number
       
    def birthday(self):
        self.age +=1
    @property
    def id_number(self):
        return f"*****{self.__id_number[-4:]}"
    @id_number.setter
    def id_number(self, id):
        if isinstance(id, str) and len(id) == 9:
            self.__id_number = id
        else:
            
            print("Invalid id type or Invalid id length")
            self.__id_number="000000000"

    @abstractmethod        
    def perform_duty(self): #polymorphism and abstraction
        pass
    
    def __str__(self):
        return ("---Citizen profile---\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Job: {self.job}\n"
                f"Id: {self.id_number}"
                 )
    
class BankAccount:
    def __init__(self, citizen_object):
        self.__owner = citizen_object
        self.__balance = 0

    @property
    def balance(self):
        return f"${self.__balance}.00"
    
    def deposit(self, amount):
        self.__balance +=amount

    def withdraw(self, amount):
       if self.__balance >= amount:
          self.__balance -=amount
       else: 
           print(f"Insufficient funds for {self.__owner.name}")


    def __str__(self):
        return (
            f"OWNER NAME: {self.__owner.name}\n"
            f"OWNER ID: {self.__owner.id_number}\n"
            f"CURRENT BALANCE: {self.__balance}\n"
        )
    

class Bus:
    def __init__(self, route):
        self.__route_number = route
        self.__passengers = []
        self.__capacity = 5

    @property
    def passenger_count(self):
        return len(self.__passengers)
    

    @property
    def is_full(self):
        if len(self.__passengers) == self.__capacity:
              return True
    
    def board(self, citizen_obj):
        if self.passenger_count < self.__capacity:
            self.__passengers.append(citizen_obj)
    
        else:
            print(f"Bus is full! {citizen_obj} must wait for the next one")


    def show_passengers(self):
         for obj in self.__passengers:
           
            print(obj.name)
    
    def __str__(self):
        return f"Bus Route {self.__route_number} | Seats: {self.passenger_count}/{self.__capacity}"
         

class PowerPlant:
    def __init__(self, fuel):
        self.fuel_level = fuel
       


    @property
    def fuel_level(self):
        return self.__fuel_level
    
        
    @fuel_level.setter
    def fuel_level(self, value):
        if value > 100:
            self.__fuel_level = 100
            self.__is_active = True
        elif value <=0:
            self.__fuel_level = 0
            self.__is_active = False
        else:
            self.__fuel_level = value
            self.__is_active = True
    def generate_power(self):
        if self.__is_active:
            self.fuel_level -=10
        else:
            print("Error: plant is offline. Refuel needed!")
    def refuel(self, amount):
        
           self.fuel_level +=amount

    def __str__(self):
          status = "ONLINE" if self.__is_active else "OFFLINE"
          return f"Power plant status: {status} | Fuel: {self.__fuel_level}%"
              

class SmartHome:
    def __init__(self, address, temp, code):
        self.__address = address
        self.__temperature = temp
        self.__security_code = code
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, value):
        if value >= 18 and value <= 28:
            self.__temperature = value
        else:
            
            print("Climate control error: Temperature must be between 18 and 28.")
            self.__temperature = self.__temperature
    

    @property
    def address(self):
        return self.__address
    def enter_home(self, code):
        if code == self.__security_code:
            print(f"Access Granted. Welcome home to {self.__address}!")
        else:
            print("ACCESS DENIED. Alarm triggered!")

    def __str__(self):
        return f"HOme at {self.address} | Current Temp: {self.temperature}°C"
    

    
class CityHospital:
    def __init__(self, hos_name):
        self.__hospital_name = hos_name
        self.__patient_records = {}


    def admit_patient(self, citizen_obj, id_number):
        self.__patient_records[id_number] = citizen_obj
        print(f"Successfully admitted patient with ID: {citizen_obj.id_number}")



        
    @property
    def admit_patient_count(self):
        return len(self.__patient_records)
    

    def check_patient_status(self, id_num):
        if id_num in self.__patient_records:
            patient = self.__patient_records[id_num] 
            print(f"Patient {patient.name} is in the {patient.job} ward.")
        else:
            print(f"No record found for ID: {id_num}")


    def __str__(self):
        return f"Hospital name: {self.__hospital_name} | Total patients currently admitted: {self.admit_patient_count}"
    

class CityCouncil:
    def __init__(self,city_name, budget, key):
        self.__city_name = city_name
        self.__total_budget = budget
        self.__admin_key = key
    
    def update_budget(self, new_amount, key_provider):
        if key_provider == self.__admin_key:
            self.__total_budget = new_amount
            print("Budget updated successfully")
        else:
            print("ACCESS DENIED: invalid Admin key . security notified.")
    @property
    def total_budget(self):
        return self.__total_budget
    @property
    def city_name(self):
        return self.__city_name
        

    def __str__(self):
        return f"City Name: {self.city_name}  | Current Budget: ${self.total_budget:,}"
    


class  PoliceOfficer(Citizen):
    def __init__(self, name, age, job, id_number, badge):
        super().__init__(name, age, job, id_number)
        self.__badge_number = badge
    def __str__(self):
        return super().__str__() + f'\nBadge Number: {self.__badge_number}' + f"\n-----------------------------------"
    
    def patrol(self):
        print(f"Addis ababa is patroled by pollice officers every day.")

    def perform_duty(self):#polymorphism
        print(f"Officer {self.name} is patrolling the streets of Addis.")
class Doctor(Citizen):
    def __init__(self, name, age, job, id_number, specialty):
        super().__init__(name, age, job, id_number)
        self.specialty = specialty
    
    def __str__(self):
        return super().__str__() + f"\nSpecialty: {self.specialty.upper()}" + f"\n-----------------------"

    def prescribe_medicine(self):
        print(f"{self.name} prescribe  paracetamole for me")
    def perform_duty(self):#polymorphism 
        print(f"Dr.{self.name} is treating patients in the {self.specialty} ward.")

class Constructor(Citizen):
    def __init__(self, name, age, job, id_number, specialty):
        super().__init__(name, age, job, id_number)
        self.specialty = specialty
    def __str__(self):
        return super().__str__() + f"\nspecialty: {self.specialty}" + f"\n------------------------"
    def perform_duty(self):
        print(f"Engineer {self.name} is working on  the corridor development in {self.specialty} ward.")
# ---------CODE TESTING PORTION-----


# --- TEST 1: The Citizen & The Bank ---
print("\n---Identity & Finance ---")
abel = Constructor("Abel micheal", 28, "Engineer", "123456789", "corridor development")
account = BankAccount(abel)
account.deposit(1000)
print(abel)
print(account)

# --- TEST 2: The Infrastructure ---
print("\n---City Transport ---")
city_bus = Bus(101)
city_bus.board(abel)
print(city_bus)

# ---TEST 3: Health & Safety ---
print("\n---Public Services ---")
hospital = CityHospital("ADDIS ABABA City General HOSPITAL")
hospital.admit_patient(abel, "123456789")
hospital.check_patient_status("123456789")

# ---TEST 4: Energy Grid Check---
print("---POWER GRID ---")
grid = PowerPlant(15)
grid.generate_power() 
grid.generate_power() 
print(grid)
grid.refuel(100)
print(f"Post-Refuel: {grid}")

# ---TEST 5: The Private Sector ---
print("\n---Secure Living ---")
home = SmartHome("456 BOLE DEMBLE", 22, "1996")
home.enter_home("1996")
print(home)

# ---TEST 6: The Government ---
print("\n---Administration ---")
council = CityCouncil("ADDIS ABABA CITY", 10000000, "ADMIN_99")
council.update_budget(12000000, "ADMIN_99")
print(council)
#---TEST 7: inheritance---
officer1= PoliceOfficer('amir', 21, 'police officer','998877', 'AA-101')
print(officer1)
doctor1 = Doctor('selam', 35, 'doctor', '112233', 'surgeon')
print(doctor1)
constract1 = Constructor('dagmawi', 22, 'constructor', '111222333', 'engineering')
print(constract1)
#----TEST 8: polymorphism---
addis_population = [abel, officer1, doctor1,constract1]

print("\n----Morning in Addis Ababa")
for person in addis_population:
    person.perform_duty()
