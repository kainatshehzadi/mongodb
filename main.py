from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hi vescel deploy fastapi app successfully."}