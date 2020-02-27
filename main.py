from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

LINK_GIT = 'https://github.com'


class User(BaseModel):
    id: int


class Message(BaseModel):
    message_id: int
    date: int
    text: Optional[str]
    from_: Optional[User]


class UpdateTelegram(BaseModel):
    update_id: int
    message: Optional[Message]
    edit_message: Optional[Message]


app = FastAPI()


@app.post("/event_git")
async def get_message_info(upd_tel: UpdateTelegram):
    text = UpdateTelegram.message.text
    return {"message": "Hello World"}
