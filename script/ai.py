import os
import re

import rich_click as click
from pick import pick
from rich_click.cli import patch

from helper import prompt_helper, openai_helper, console_helper
from helper.console_helper import chat_in_console

patch()


@click.group()
def cli():
    pass


@click.command('model', help="Select a model")
def select_model():
    from pprint import pprint

    print("Current model:", openai_helper.config.model)
    models = list(openai_helper.get_models())
    models.sort(key=lambda x: x.id)
    option, index = pick([model.id for model in models], title="Select a model")
    openai_helper.set_model(option)
    model = openai_helper.get_model_details()
    pprint(model)


@click.command('cli', help="Generates cli command using GPT-3")
@click.argument('query', nargs=-1)
@click.option('--model', '-m', help="Model to use")
@click.option('--long', '-l', is_flag=True, help="provides additional information")
def cli_gpt_completion(query, model, long):
    if model:
        openai_helper.set_model(model)
    console_helper.console.log("Model: ", openai_helper.config.model)

    if os.name == 'posix':
        prompt_text = prompt_helper.unix_prompt_gpt35 if long else prompt_helper.unix_prompt_gpt35_short
    else:
        console_helper.console.log("[yellow]Windows detected[/yellow]")
        prompt_text = prompt_helper.windows_prompt_gpt35 if long else prompt_helper.windows_prompt_gpt35_short

    messages = [{'role': 'system', 'content': prompt_text}]
    last_message_text = chat_in_console(messages, query, temperature=0)

    try:
        command = re.findall(r'```(?:\w+\n)?(.*?)```', last_message_text, re.MULTILINE | re.DOTALL)[0]
        if command:
            console_helper.copy_to_clipboard(command)
    except IndexError:
        console_helper.console.log("[yellow]No command found[/yellow]")


@click.command('gr', help="Grammar")
@click.argument('query', nargs=-1)
@click.option('--model', '-m', help="Model to use")
def gr_completion(query, model):
    if model:
        openai_helper.set_model(model)
    console_helper.console.log("Model: ", openai_helper.config.model)

    messages = [{'role': 'system', 'content': prompt_helper.grammer_system_prompt}]
    chat_in_console(messages, query)


@click.command('assessment', help="Guess assessment hours")
@click.argument('query', nargs=-1)
@click.option('--model', '-m', help="Model to use")
def assessment_completion(query, model):
    if model:
        openai_helper.set_model(model)
    console_helper.console.log("Model: ", openai_helper.config.model)

    messages = [
        {'role': 'system', 'content': prompt_helper.assessment},
    ]

    chat_in_console(messages, query)


@click.command('chat', help="Chat with GPT-3")
@click.argument('query', nargs=-1)
@click.option('--model', '-m', help="Model to use")
def chat(query, model):
    if model:
        openai_helper.set_model(model)
    console_helper.console.log("Model: ", openai_helper.config.model)

    messages = [
        {'role': 'system', 'content': 'You are a helpful AI assistant. Respond always with Markdown.'},
    ]

    chat_in_console(messages, query)


@click.command('summary', help="Summarize text")
@click.argument('query', nargs=-1)
@click.option('--model', '-m', help="Model to use")
def summary(query, model):
    if model:
        openai_helper.set_model(model)
    console_helper.console.log("Model: ", openai_helper.config.model)

    messages = [
        {'role': 'system', 'content': prompt_helper.ts_summary_prompt},
    ]
    if not query:
        # get from clipboard
        query = console_helper.get_clipboard_text()
    chat_in_console(messages, query)


cli.add_command(select_model)
cli.add_command(gr_completion)
cli.add_command(cli_gpt_completion)
cli.add_command(assessment_completion)
cli.add_command(chat)
cli.add_command(summary)

if __name__ == '__main__':
    cli()
