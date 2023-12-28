import os
import sys

from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.padding import Padding
from rich.prompt import Prompt

from helper import openai_helper

console = Console()

input_token = 0
response_token = 0


def get_multiline_input(prompt=""):
    lines = []

    while True:
        line = Prompt.ask(f"\r[b]  {prompt}[/b]")
        if not line:
            sys.stdout.write("\033[F")
            break
        lines.append(line)

    return "\n".join(lines)


def chat_in_console(messages, query, **kwargs):
    global input_token, response_token
    response_text = ""

    try:
        while True:
            if query:
                input_text = " ".join(query)
                query = None
            else:
                input_text = get_multiline_input('You')
                if not input_text:
                    return response_text

            response_text = ""
            input_token += len(input_text.split())

            messages.append({'role': 'user', 'content': input_text})
            response = openai_helper.chat_completion(messages, stream=True, **kwargs)

            with Live(refresh_per_second=6) as live:
                for chunk in response:
                    for choice in chunk.choices:

                        if choice.finish_reason == 'stop':
                            live.update(Padding(Markdown('**AI:** ' + response_text), (1, 2, 2, 2)))
                            break

                        if choice.delta.content:
                            response_text += choice.delta.content
                            response_token += len(choice.delta.content.split())

                        live.update(Padding(Markdown(
                            '**AI:** ' +
                            response_text +
                            "\n\n---" +
                            f"\nInput: {input_token:<10} "
                            f"Output: {response_token:<10} "
                            f"Cost: {openai_helper.cost(input_token, response_token):<10.4f}"
                            "\n\n---"
                        ), (1, 2, 2, 2)))

            messages.append({'role': 'system', 'content': response_text})

            # print gray horizontal line
            console.rule(
                f"[dim]Model[/]: {openai_helper.config.model}    "
                f"[dim]Input[/]: {input_token:<6}"
                f"[dim]Output[/]: {response_token:<6}"
                f"[dim]Total[/]: {input_token + response_token:<6}"
                f"[dim]Cost[/]: {openai_helper.cost(input_token, response_token):<.4f}",
            )
    except KeyboardInterrupt:
        pass

    print('response_text', response_text)
    return response_text


def copy_to_clipboard(text):
    import pyperclip
    # noinspection PyBroadException
    try:
        pyperclip.copy(text.strip())
    except:
        if os.name == 'posix':
            os.system(f'echo "{text}" | xclip -selection clipboard')
        else:
            os.system(f'echo "{text}" | clip')
    console.log("[green]Copied to clipboard: [/green]", text)


def get_clipboard_text():
    import pyperclip

    # noinspection PyBroadException
    try:
        return pyperclip.paste()
    except:
        if os.name == 'posix':
            return os.popen('xclip -selection clipboard -o').read()
        else:
            return os.popen('clip -o').read()
