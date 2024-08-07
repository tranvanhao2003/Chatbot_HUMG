from langchain_core.pydantic_v1 import BaseModel, Field

class GradeID(BaseModel):
    """The majors ID is in the user's question."""
    ID: list[int] = Field(description="ID of the majors, just give the number")


class GradeReWrite(BaseModel):
    """Viết lại câu hỏi của người dùng dựa trên câu hỏi và lịch sử."""
    rewrite: str = Field()