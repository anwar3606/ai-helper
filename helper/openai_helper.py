import os
from pprint import pprint

import openai

API_KEY_FILE = os.path.expanduser("~/.openai_api_key")
CONFIG_FILE = os.path.expanduser("~/.openai_config")


class Config:
    model = "davinci"

    # to dict
    def __dict__(self):
        return {
            "model": self.model
        }

    # set from dict
    def __init__(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as f:
                c = eval(f.read())
                self.model = c["model"]

    def save(self):
        with open(CONFIG_FILE, "w") as f:
            f.write(str(self.__dict__()))


config = Config()


def get_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE) as f:
            return f.read().strip()


try:
    openai.api_key = get_api_key()
    if not openai.api_key:
        raise TypeError
except (FileNotFoundError, TypeError):
    save_api_key = input("Enter your OpenAI API key: ")
    with open(API_KEY_FILE, "w") as f:
        f.write(save_api_key)
    openai.api_key = save_api_key


def get_models():
    return openai.models.list()


def set_model(model_name):
    config.model = model_name
    config.save()


if __name__ == '__main__':
    pprint(get_models())


def cost(total_input_tokens: int, total_output_tokens: int):
    model_rate = {

        "gpt-3.5-turbo": {'input': 0.0015, 'output': 0.002},
        "gpt-3.5-turbo-16k": {'input': 0.003, 'output': 0.004},
        'gpt-3.5-turbo-1106': {'input': 0.001, 'output': 0.002},
        "gpt-4": {'input': 0.03, 'output': 0.06},
        'gpt-4-1106-preview': {'input': 0.01, 'output': 0.03},
    }.get(config.model, 0)

    return round(
        (total_input_tokens * model_rate['input'] / 1000) +
        (total_output_tokens * model_rate['output'] / 1000)
        , 4)


def chat_completion(messages: list, **kwargs):
    return openai.chat.completions.create(
        model=config.model,
        messages=messages,
        **kwargs
    )


def get_model_details():
    return openai.models.retrieve(config.model)
