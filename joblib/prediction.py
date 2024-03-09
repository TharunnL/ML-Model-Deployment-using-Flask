import joblib
model = joblib.load("C:\\Users\\Tarunn\\Desktop\\Deployment\\joblib\\Cardio_vascular.pkl")

input = [49,1,0,130,191,0,1,106,1,2.2,1,2,3]

output = model.predict([input])
 
if output[0] == 1:
    print("Patient has Cardio Vascular risk ")
else:
    print("Patient has no Cardio Vascular risk ")
