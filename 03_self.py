class Employee:
  
    language = "hindi"
    salary = 12000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
harry = Employee()
harry.language = "English"

harry.getinfo()

