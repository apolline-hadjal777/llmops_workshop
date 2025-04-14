from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel


class Provider(str, Enum):
    openai = "openai"
    anthropic = "anthropic"
    groq = "groq"
    ollama = "ollama"


class Message(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    provider: Provider
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 256
    top_p: Optional[float] = 1.0
    stream: Optional[bool] = False


class ChatCompletionResponse(BaseModel):
    model: str
    choices: List[dict]


class TextEmbeddingRequest(BaseModel):
    provider: Provider
    model: str
    input: Union[str, List[str]]


class TextEmbeddingResponse(BaseModel):
    embeddings: List[List[float]]
    model: str


class ModelInfo(BaseModel):
    name: str
    provider: Provider
    capabilities: List[str]