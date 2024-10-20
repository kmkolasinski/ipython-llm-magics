from ipykernel import zmqshell  # type: ignore
from IPython.core import magic  # type: ignore

from llm_magics import client, rendering


@magic.magics_class
class LLMMagics(magic.Magics):  # type: ignore
    def __init__(self, shell: zmqshell.ZMQInteractiveShell):
        """Initialize the REPLMagic class state."""
        super().__init__(shell)
        self._client = client.OpenAIChatClient()

    @magic.line_magic  # type: ignore
    def llm_get_client(self, line: str) -> client.OpenAIChatClient:
        """Get the chat client.
        Usage: %llm_get_client
        """
        return self._client

    @magic.line_magic  # type: ignore
    def llm_set_model(self, model: str) -> None:
        """Set the model for the chat client.
        Usage: %llm_set_model gpt-40
        """
        model = model.strip()
        self._client.set_model(model)

    @magic.line_magic  # type: ignore
    def llm_set_system_message(self, message: str) -> None:
        """Set the system message for the chat client.
        Usage: %llm_set_system_message "You are a helpful assistant."
        """
        message = message.strip()
        self._client.set_system_message(message)

    @magic.cell_magic  # type: ignore
    def llm_chat(self, line: str, cell: str) -> None:
        """Send a message to the chat client and get the response."""
        response = self._client.send_message(cell)
        rendering.render_response(response)

    @magic.line_magic  # type: ignore
    def llm_clear(self, line: str):
        """Clear the chat history."""
        self._client.clear_chat()
