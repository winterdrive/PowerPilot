from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from os import environ
from fastapi import File, UploadFile

import chat_agent

load_dotenv()

app = FastAPI()


class Message(BaseModel):
    message: str
    model_url: str
    api_key: str
    secret_key: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/commit-message-generator/text")
async def commit_message_generator(inspect: Message):
    if inspect.secret_key != environ.get("secret_key"):
        raise HTTPException(status_code=403, detail="Invalid secret key.")
    if inspect.model_url != environ.get("model_url"):
        raise HTTPException(status_code=403, detail="Invalid model URL.")
    if inspect.api_key != environ.get("api_key"):
        raise HTTPException(status_code=403, detail="Invalid API key.")
    if inspect.message is None or len(inspect.message) < 10:
        raise HTTPException(status_code=403, detail="Invalid message length. Must be over 10characters.")
    return {"message": chat_agent.commit_message_generator(inspect.message)}


@app.post("/commit-message-generator/file")
async def commit_message_generator(secret_key: str, model_url: str, api_key: str,
                                   message_file: UploadFile = File(...)):
    if secret_key != environ.get("secret_key"):
        raise HTTPException(status_code=403, detail="Invalid secret key.")
    if model_url != environ.get("model_url"):
        raise HTTPException(status_code=403, detail="Invalid model URL.")
    if api_key != environ.get("api_key"):
        raise HTTPException(status_code=403, detail="Invalid API key.")
    message_content = await message_file.read()
    if message_content is None or len(message_content) < 10:
        raise HTTPException(status_code=403, detail="Invalid message length. Must be over 10 characters.")
    return {"message": chat_agent.commit_message_generator(message_content.decode())}



# CMD uvicorn main:app --host 0.0.0.0 --port 8080 --reload
if __name__ == "__main__":
    #     http://127.0.0.1:8080/docs
    port = int(environ.get("PORT", default=8000))
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=port, reload=True)