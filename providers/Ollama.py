import os
import time

from rich.live import Live

from helper.Config import Config
from providers import ChatProvider


class OllamaChatProvider(ChatProvider):
    provider = "ollama"
    CONFIG_FILE = os.path.expanduser("~/.ollama_config")
    unit = 'tok/s'

    def __init__(self):
        import ollama
        super().__init__()

        self.config = Config(self.CONFIG_FILE, {"host": "http://localhost:11434"})
        self.client = ollama.Client(host=self.config.host)

    def models(self) -> list[str]:
        models = self.client.list()['models']

        return [model['name'] for model in models]

    def chat(self, messages, **kwargs):
        self.input_token = self.calculate_input_token(messages)
        self.total_input_token += self.input_token

        self.response_token = 0
        self.generation_start_time = time.time()

        return self.client.chat(model=self.config.model, messages=messages, stream=True, options={'num_ctx':4096})

    def print_messages(self, response):
        with Live(refresh_per_second=6) as live:
            for chunk in response:
                if chunk['done']:
                    self.update_live_ai_message(live)
                    break

                if chunk['message']['content']:
                    self.response_text += chunk['message']['content']
                    self.response_token += 1

                self.update_live_ai_message(live)

        self.total_response_token += self.response_token
        self.print_footer()
