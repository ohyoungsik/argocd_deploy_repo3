from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_fortune():
    return {
        "service": "greet", 
        "message": "안녕하세요"
    }
    
@app.get("/greet2")
def get_fortune():
    return {
        "service": "greet", 
        "message": "안녕하세요222"
    }