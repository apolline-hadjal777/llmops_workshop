from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any, Union

from core.models import (
    Provider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    TextEmbeddingRequest,
    TextEmbeddingResponse,
    ModelInfo
)


class BaseLLMService(ABC):
    """
    Abstract base class for LLM service implementations.
    All provider-specific services must implement these methods.
    """

    provider: Provider

    @abstractmethod
    async def get_chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        pass

    @abstractmethod
    async def get_embeddings(self, request: TextEmbeddingRequest) -> TextEmbeddingResponse:
        pass

    @abstractmethod
    async def list_models(self) -> List[ModelInfo]:
        pass

    @abstractmethod
    async def get_model_info(self, model_id: str) -> Optional[ModelInfo]:
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        pass

    @abstractmethod
    def convert_request(self, request: Union[ChatCompletionRequest, TextEmbeddingRequest]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def convert_response(self, response: Any, request_type: str) -> Union[ChatCompletionResponse, TextEmbeddingResponse]:
        pass

    @abstractmethod
    def count_tokens(self, text: str, model: Optional[str] = None) -> int:
        pass
