import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Get the Data

data = pd.read_csv('WinePredictor1.csv')
print(data)

#Preprocess the data

alcohol	= data.Alcohol
malicAcid = data.Malic_acid
ash = data.Ash
alcalinity_of_ash = data.Alcalinity_of_ash
magnesium = data.Magnesium	
Total_Phenols = data.Total_phenols
Flavanoids = data.Flavanoids
Nonflavanoid_phenols = data.Nonflavanoid_phenols
Proanthocyanins = data.Proanthocyanins
Color_intensity = data.Color_intensity
Hue	= data.Hue
OD280OD315_of_diluted_wines = data.OD280OD315_of_diluted_wines
Proline = data.Proline

class_OF_Wine = data.Wine_Class

#Creating Label Encoder

le = preprocessing.LabelEncoder()

#Converting string labels into numbers

alcohol_encoding = le.fit_transform(alcohol)     

malicAcid_encoding = le.fit_transform(malicAcid)

ash_encoding = le.fit_transform(ash)

alcalinity_of_ash_encoding = le.fit_transform(alcalinity_of_ash)

magnesium_encoding = le.fit_transform(magnesium)

Total_Phenols_encoding = le.fit_transform(Total_Phenols)

Flavanoids_encoding = le.fit_transform(Flavanoids)

Nonflavanoid_phenols_encoding = le.fit_transform(Nonflavanoid_phenols)

Proanthocyanins_encoding = le.fit_transform(Proanthocyanins)

Color_intensity_encoding = le.fit_transform(Color_intensity)

Hue_encoding = le.fit_transform(Hue)

OD280OD315_of_diluted_wines_encoding = le.fit_transform(OD280OD315_of_diluted_wines)

Proline_encoding = le.fit_transform(Proline)


class_OF_Wine_encoding = le.fit_transform(class_OF_Wine) # it is the label of data set

#Combining All the Feature in One 

Features = list(zip(alcohol_encoding, malicAcid_encoding, ash_encoding, alcalinity_of_ash_encoding, magnesium_encoding, Total_Phenols_encoding, Flavanoids_encoding, Nonflavanoid_phenols_encoding, Proanthocyanins_encoding, Color_intensity_encoding, Hue_encoding, OD280OD315_of_diluted_wines_encoding, Proline_encoding))

#Data Spliting into Train And Test

X_train ,X_test ,Y_train , Y_Test = train_test_split(Features, class_OF_Wine_encoding,test_size=0.2,random_state=42)

#Train the Data

Model = KNeighborsClassifier(n_neighbors=3)

#Train the model using training set

Model.fit(X_train,Y_train)

#Test the Model

Predicted = Model.predict(X_test)
print("The Data Columns Of Predicted Model Is: ",Predicted)

#Test The Accuracy Of Model

Accuracy = accuracy_score(Y_Test,Predicted)

print("The Accuracy Of Model Is: ",Accuracy)