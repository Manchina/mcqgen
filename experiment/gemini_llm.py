from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from langchain.callbacks.manager import CallbackManagerForLLMRun
import google.generativeai as genai
import os


class GeminiChatModel(BaseChatModel):
    """
    LangChain-compatible wrapper for Google Gemini API
    with callback manager support.
    """

    model_name: str = "gemini-1.5-flash"
    temperature: float = 0.7

    def __init__(self, model="gemini-2.5-flash", temperature=0.7, **kwargs):
        super().__init__(**kwargs)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        object.__setattr__(self, "_model", genai.GenerativeModel(model))
        object.__setattr__(self, "temperature", temperature)

    def _generate(
        self, messages, stop=None, run_manager: CallbackManagerForLLMRun = None, **kwargs
    ) -> ChatResult:
        """Generate a response with Gemini, with callback support."""
        # Extract text
        prompt = "\n".join([m.content for m in messages if isinstance(m, HumanMessage)])

        # Model call
        response = self._model.generate_content(prompt)
        output_text = response.text if hasattr(response, "text") else str(response)

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=output_text))]
        )

    @property
    def _llm_type(self) -> str:
        return "gemini-chat"
