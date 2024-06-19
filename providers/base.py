import time
from abc import ABC, abstractmethod

import inquirer
from inquirer import prompt
from rich.live import Live
from rich.markdown import Markdown
from rich.padding import Padding
from rich.prompt import Prompt

from helper.Config import Config
from helper.console import console


class ChatProvider(ABC):
    CONFIG_FILE = None
    provider = None
    config: Config = None

    input_token: int = 0
    response_token: int = 0
    total_input_token: int = 0
    total_response_token: int = 0
    response_text: str = ""

    def __init__(self):
        self.UNIT = None
        self.generation_start_time = None

    @abstractmethod
    def chat(self, messages, **kwargs):
        pass

    @abstractmethod
    def print_messages(self, response):
        pass

    @property
    @abstractmethod
    def unit(self):
        pass

    def cost(self) -> float:
        return 0.0

    def total_cost(self) -> float:
        return 0.0

    def get_model(self) -> str:
        try:
            return self.config.model
        except AttributeError:
            self.set_model()
            self.save()

            return self.config.model

    @abstractmethod
    def models(self) -> list[str]:
        pass

    def set_model(self, model: str = None):
        if not model:
            questions = [
                inquirer.List(
                    'model',
                    message="Select a model",
                    choices=self.models(),
                )
            ]
            model = prompt(questions)['model']

        self.config.model = model

    def _get_api_key(self):
        try:
            return self.config.api_key
        except AttributeError:
            self.config.api_key = Prompt.ask(f"Enter your {self.provider} API key")
            self.save()
            return self.config.api_key

    def save(self):
        self.config.save()

    def update_live_ai_message(self, live: Live):
        time_diff = time.time() - self.generation_start_time
        try:
            speed = self.response_token / time_diff
        except ZeroDivisionError:
            speed = 0.0

        live.update(
            Padding(
                Markdown(
                    f'**AI:** {self.response_text}\n'
                    f"\nInput: {self.input_token:<10} "
                    f"Output: {self.response_token:<10} "
                    f"Cost: {self.cost():<.4f}      \n"
                    f"Speed: {speed:.2f} {self.unit}"
                    "\n---"
                ),
                (1, 2, 2, 2)
            )
        )

    def print_footer(self):
        console.rule(
            f"[dim]Model[/]: {self.config.model}    "
            f"[dim]Input[/]: {self.total_input_token:<6}"
            f"[dim]Output[/]: {self.total_response_token:<6}"
            f"[dim]Total[/]: {self.total_input_token + self.total_response_token:<6}"
            f"[dim]Cost[/]: {self.total_cost():<.4f}",
        )

    @staticmethod
    def calculate_input_token(messages):
        import tiktoken
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

        return sum(len(encoding.encode(message['content'])) for message in messages)
