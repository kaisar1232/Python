#function accepts more parameter and returm nothing

def Marvellous(Name,Age,City):
    print("Inside Marvellous Function")
    print("Welcome",Name)
    print("age is:",Age)
    print("City is:",City)
    
    
def main():
    Marvellous("Kaisar",20,"Satara")
    Marvellous(City="pune",Age=30,Name="rahul")
    
if __name__=="__main__":
    main()    