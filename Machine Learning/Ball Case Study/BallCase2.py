from  sklearn import tree

def main():
    
    print("Ball Classification Case Study")
    
    #Rough = 1
    #Smooth = 0
    
    #Load The Data
    BallFeatures = [[32,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    Labels = ["Tenis","Tenis","Cricekt","Cricekt","Cricekt","Tenis","Cricekt","Cricekt","Cricekt","Cricekt","Cricekt","Tenis","Cricekt","Tenis","Cricekt"]
    
    obj = tree.DecisionTreeClassifier() #Decide The Algorithm
    
    obj =obj.fit(BallFeatures,Labels)   #Train The Model
    
    print(obj.predict([[23,"1"],[91,"0"]]))    #Test The Model
    

if __name__ == "__main__":
    
    main()
   