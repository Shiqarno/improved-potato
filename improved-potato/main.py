import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from os import path as os_path

app = FastAPI()
COLLECT_FILE_PATH = "data/collected.csv"
TO_PREDICT_FILE_PATH = "data/to_predict.csv"

class Tick(BaseModel):
    name : str
    date : str
    open : float
    high : float
    low : float
    close : float
    volume : float
    close_1 : float
    close_2 : float
    close_3 : float
    close_4 : float
    close_5 : float
    close_6 : float
    close_7 : float
    close_8 : float
    close_9 : float
    offset_1 : float
    offset_2 : float
    offset_3 : float
    offset_4 : float
    offset_5 : float
    offset_6 : float
    offset_7 : float
    offset_8 : float
    offset_9 : float
    offset_10 : float
    offset_11 : float
    offset_12 : float
    offset_13 : float
    offset_14 : float
    offset_15 : float
    offset_16 : float
    offset_17 : float
    offset_18 : float
    offset_19 : float
    offset_20 : float
    offset_21 : float
    offset_22 : float
    offset_23 : float
    offset_24 : float
    offset_25 : float
    offset_26 : float
    offset_27 : float
    offset_28 : float
    offset_29 : float
    ind_0 : float
    ind_1 : float
    ind_2 : float
    ind_3 : float
    ind_4 : float
    ind_5 : float
    ind_6 : float
    ind_7 : float
    ind_8 : float
    ind_9 : float
    ind_10 : float
    ind_11 : float
    ind_12 : float
    ind_13 : float
    ind_14 : float
    ind_15 : float
    ind_16 : float
    ind_17 : float
    ind_18 : float
    ind_19 : float

class ToCollectTick(BaseModel):
    name : str
    date : str
    category: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/collect")
def update_item(tick: ToCollectTick):
    file_exists = os_path.exists(COLLECT_FILE_PATH)
    text_file = open(COLLECT_FILE_PATH, "a")
    if not file_exists:
        text_file.write(','.join([str(i) for i in tick.dict().keys()]))
        text_file.write('\n')    
    text_file.write(','.join([str(i) for i in tick.dict().values()]))
    text_file.write('\n')
    text_file.close()
    return {"result": True}

@app.put("/predict")
def update_item(tick: Tick):
    text_file = open(TO_PREDICT_FILE_PATH, "w")
    text_file.write(','.join([str(i) for i in tick.dict().keys()]))
    text_file.write('\n')
    text_file.write(','.join([str(i) for i in tick.dict().values()]))
    text_file.close()

    action = "none"
    return {"action": action, "sl": 0, "tp": 0, "comment": ""}    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=55655, log_level="info")