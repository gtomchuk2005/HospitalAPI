import requests

serviceurl = "http://127.0.0.1:5000/"

data = [
    {"name": "greg", 
    "pregnancies": 1, 
    "glucose": 2.0, 
    "BP": 3, 
    "ST": 2, 
    "insulin": 3,
    "BMI" : 200, 
    "DPF": 5, 
    "age": 23
    },{"name": "Nabil", 
    "DPF": 20, 
    "age": 18, 
    "pregnancies": 0, 
    "glucose": 2.0, 
    "BP": 3, 
    "ST": 20, 
    "insulin": 4, 
    "BMI" : 140, }
    ]

for i in range(len(data)):
    response = requests.put(serviceurl + "user/" + str(i), data[i])
    print(response.json())



#response = requests.put(serviceurl + "user/1", {
    #"name": "nabil", 
    #"pregnancies": 4, 
    #"glucose": 2.0, 
    #"BP": 3, 
    #"ST": 2, 
    #"insulin": 4, 
    #"BMI" : 150, 
    #"DPF": 5, 
    #"age": 23
    #})
#print(response.json())

#input()

#response = requests.patch(serviceurl + "user/1",{
    #"name": "jackie", 
    #"pregnancies": 4303, 
    #"glucose": 30, 
    #"BP": 3, 
    #"ST": 2, 
    #"insulin": 4, 
    #"BMI" : 302, 
    #"DPF": 5, 
    #"age": 40
    #})
#print(response.json())
