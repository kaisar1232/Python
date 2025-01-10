from  sklearn import tree

def main():
    
    print("Ball Classification Case Study")
    
    #Load The Data
    BallFeatures = [[32,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]
    
    Labels = ["Tenis","Tenis","Cricekt","Cricekt","Cricekt","Tenis","Cricekt","Cricekt","Cricekt","Cricekt","Cricekt","Tenis","Cricekt","Tenis","Cricekt"]

    obj = tree.DecisionTreeClassifier() #Decide The Algorithm
    
    obj =obj.fit(BallFeatures,Labels)   #Train The Model
    
    print(obj.predict([[23,"Rough"],[91,"Smooth"]]))    #Test The Model
    




if __name__ == "__main__":
    
    main()
   

