from langchain_core.callbacks.base import BaseCallbackHandler

class GeminiUsageCallback(BaseCallbackHandler):
    """Custom callback to simulate OpenAI-style token tracking for Gemini models."""

    def __init__(self):
        self.prompt_chars = 0
        self.completion_chars = 0

    def on_llm_start(self, serialized, prompts, **kwargs):
        for prompt in prompts:
            self.prompt_chars += len(prompt)

    def on_llm_end(self, response, **kwargs):
        if hasattr(response, "generations"):
            for gen in response.generations:
                for g in gen:
                    self.completion_chars += len(g.text)

    @property
    def total_chars(self):
        return self.prompt_chars + self.completion_chars

    def print_summary(self):
        print("🧮 Gemini Usage Summary:")
        print(f"Prompt chars: {self.prompt_chars}")
        print(f"Completion chars: {self.completion_chars}")
        print(f"Total chars: {self.total_chars}")
