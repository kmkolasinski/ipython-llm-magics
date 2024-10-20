import openai
from openai.types.chat import ChatCompletion


class OpenAIChatClient:
    def __init__(
        self,
        model: str = "gpt-4o",
        system_message: str = "You are a helpful assistant.",
    ) -> None:
        self.chat_history: list[dict[str, str]] = []
        self.system_message = system_message
        self.client = openai.Client()
        self.model = model
        self._response: ChatCompletion | None = None

    def append_user_message(self, message: str) -> None:
        self.chat_history.append({"role": "user", "content": message})

    def append_assistant_message(self, message: str | None) -> None:
        if message:
            self.chat_history.append({"role": "assistant", "content": message})

    def set_system_message(self, message: str) -> None:
        self.system_message = message

    def set_model(self, model: str) -> None:
        self.model = model

    def clear_chat(self) -> None:
        self.chat_history = []

    def get_chat_history(self) -> list[dict[str, str]]:
        return self.chat_history

    def send_message(self, message: str) -> str | None:
        messages = []
        if self.system_message or self.model not in ["o1-preview"]:
            messages.append({"role": "system", "content": self.system_message})
        messages += [
            *self.chat_history,
            {"role": "user", "content": message},
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,  # type: ignore
        )
        self.append_user_message(message)
        self.append_assistant_message(response.choices[0].message.content)
        self._response = response
        return response.choices[0].message.content
