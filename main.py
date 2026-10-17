from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{
        "message":"ha sab thik hai ok aage badho"
    }
    