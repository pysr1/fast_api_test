from datetime import datetime
from fastapi import FastAPI
import numpy as np 

app = FastAPI()

@app.get("/")
def root():
    return { "message": 'hello world'}

@app.get("/random_numbers")
def random_numbers():
    return { "random numbers": list(np.random.normal(0,1, 100))}