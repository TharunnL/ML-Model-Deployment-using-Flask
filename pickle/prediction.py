import pickle
model = pickle.load(open("C:\\Users\\Tarunn\\Desktop\\Deployment\\pickle\\Cardio_vascular.pkl","rb"))

input = [49,1,0,130,191,0,1,106,1,2.2,1,2,3]

output = model.predict([input])
 
if output[0] == 1:
    print("Patient has Cardio Vascular risk ")
else:
    print("Patient has no Cardio Vascular risk ")
