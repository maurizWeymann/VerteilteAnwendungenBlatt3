from pydantic import BaseModel

class QuestionBuilder(BaseModel):
    id: int = 0
    question: str = "Your Question"
    options: list[str] = ["Option1", "Option2", "Option3"]
    answer: str = "The answer of your question"

class User(BaseModel):
    name: str = "UserName"
    password: str = "Password"
    highscore: int = 0
