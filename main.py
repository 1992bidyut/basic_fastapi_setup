import uvicorn
from fastapi import FastAPI
from schema.parties import Parties
app = FastAPI()


@app.post("/user/", response_model=Parties)
def create_user(user: Parties):
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
