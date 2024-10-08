from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

<<<<<<< HEAD

=======
>>>>>>> 236d516e9d29686f2f55b28783eb73637efe89d2
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

import joblib

<<<<<<< HEAD
import joblib

# import sklearn.externals
model = joblib.load("knn_model.joblib")
scaler = joblib.load("scaler.joblib")

from pydantic import BaseModel
import sklearn.metrics


# Define a Pydantic model for input data validation
=======
model = joblib.load('knn_model.joblib')
scaler = joblib.load('scaler.joblib')

from pydantic import BaseModel
import sklearn.metrics
Define a Pydantic model for input data validation
>>>>>>> 236d516e9d29686f2f55b28783eb73637efe89d2
class InputFeatures(BaseModel):
    Year: int
    Engine_Size: float
    Mileage: float
    Type: str
    Make: str
    Options: str


<<<<<<< HEAD
def preprocessing(input_features: InputFeatures):
    dict_f = {
        "Year": input_features.Year,
        "Engine_Size": input_features.Engine_Size,
        "Mileage": input_features.Mileage,
        "Type_Accent": input_features.Type == "Accent",
        "Type_Land Cruiser": input_features.Type == "LandCruiser",
        "Make_Hyundai": input_features.Make == "Hyundai",
        "Make_Mercedes": input_features.Make == "Mercedes",
        "Options_Full": input_features.Options == "Full",
        "Options_Standard": input_features.Options == "Standard",
    }
    # Convert dictionary values to a list in the correct order
=======

def preprocessing(input_features: InputFeatures):
    dict_f = {
        'Year': input_features.Year,
        'Engine_Size': input_features.Engine_Size,
        'Mileage': input_features.Mileage,
        'Type_Accent': input_features.Type == 'Accent',
        'Type_Land Cruiser': input_features.Type == 'LandCruiser',
        'Make_Hyundai': input_features.Make == 'Hyundai',
        'Make_Mercedes': input_features.Make == 'Mercedes',
        'Options_Full': input_features.Options == 'Full',
        'Options_Standard': input_features.Options == 'Standard'
        }
   
>>>>>>> 236d516e9d29686f2f55b28783eb73637efe89d2
    features_list = [dict_f[key] for key in sorted(dict_f)]
 
    scaled_features = scaler.transform([list(dict_f.values())])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}
