from fastapi import FastAPI

app = FastAPI()

@app.get("/fortune")
def get_fortune():
    return {
        "service": "fortune", 
        "message": "용인으로오면 날 만나유223312321"
        # "message": "동쪽으로 가면 귀인을 만나요"
    }

@app.get("/fortune2")
def get_fortune():
    return {
        "service": "fortune", 
        # "message": "용인으로오면 날 만나유223312321"
        "message": "동쪽으로 가면 귀인을 만나요"
    }
