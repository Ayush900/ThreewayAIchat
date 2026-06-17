# imports

import os
from dotenv import load_dotenv
from openai import OpenAI

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

load_dotenv(override=True)

console = Console()

# Assign a color per speaker so the chat is easy to scan
SPEAKER_COLORS = {
    "Alex": "red",
    "Blake": "cyan",
    "Charlie": "yellow",
}


def show(speaker: str, text: str):
    """Pretty-print a speaker's message in a colored panel using rich."""
    color = SPEAKER_COLORS.get(speaker, "white")
    console.print(
        Panel(
            Markdown(text),
            title=f"[bold {color}]{speaker}[/bold {color}]",
            border_style=color,
            expand=False,
        )
    )


system_prompt_alex = """
You are Alex, a chatbot who is very argumentative; you disagree with anything in the conversation and you challenge everything, in a snarky way.
You are a huge arsenal fan.
You are in a conversation with Blake and Charlie.
Keep your replies short one or two lines max.
"""

system_prompt_blake = """
You are Blake, a chatbot who is somewhat submissive; you agree with anything in the conversation unless the conversation is about football.
You are humourous and your replies are very witty. You are a Manchester city fan.
You are in a conversation with Alex and Charlie.
Keep your replies short one or two lines max.
"""

system_prompt_charlie = """
You are Charlie, a chatbot who is clueless; but very confident in when he replies. so you may reply out of context in conversation
but very confidently. People tend not to like you.
You dont like watching football you are a big indian cricket team fan.
You are in a conversation with Blake and Charlie.
Keep your replies short one or two lines max.
"""

google_api_key = os.getenv('GOOGLE_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
open_router_base_url = os.getenv("OPENROUTER_BASE_URL")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
groq_url = "https://api.groq.com/openai/v1"
ollama_url = "http://localhost:11434/v1"

gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
open_router = OpenAI(base_url=open_router_base_url, api_key=openrouter_api_key)
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

gpt_model = "openai/gpt-oss-120b"
gemini_model = "gemini-2.5-flash"
or_model = "openrouter/free"
ollama_model = "llama3.2:latest"


def alex_chat(conversation):
    user_prompt = f"""
    You are Alex, in conversation with Blake and Charlie.
    The conversation so far is as follows:
    {conversation}
    Now with this, respond with what you would like to say next, as Alex.
    """
    messages = [
        {"role": "system", "content": system_prompt_alex},
        {"role": "user", "content": user_prompt},
    ]
    response = groq.chat.completions.create(model=gpt_model, messages=messages)
    return response.choices[0].message.content


def blake_chat(conversation):
    user_prompt = f"""
    You are Blake, in conversation with Alex and Charlie.
    The conversation so far is as follows:
    {conversation}
    Now with this, respond with what you would like to say next, as Blake.
    """
    messages = [
        {"role": "system", "content": system_prompt_blake},
        {"role": "user", "content": user_prompt},
    ]
    response = open_router.chat.completions.create(model=or_model, messages=messages)
    return response.choices[0].message.content


def charlie_chat(conversation):
    user_prompt = f"""
    You are Charlie, in conversation with Alex and Blake.
    The conversation so far is as follows:
    {conversation}
    Now with this, respond with what you would like to say next, as Charlie.
    """
    messages = [
        {"role": "system", "content": system_prompt_charlie},
        {"role": "user", "content": user_prompt},
    ]
    response = ollama.chat.completions.create(model=ollama_model, messages=messages)
    return response.choices[0].message.content


def main():
    conversation = []

    console.rule("[bold green]3-Way AI Chat: Alex, Blake & Charlie[/bold green]")

    messages = [
        {"role": "system", "content": system_prompt_alex},
        {
            "role": "user",
            "content": (
                "You are Alex, in conversation with Blake and Charlie. "
                "Start the conversation by picking up the topic: Arsenal winning "
                "the premier league and losing the champions league final on penalties"
            ),
        },
    ]
    response = groq.chat.completions.create(model=gpt_model, messages=messages)
    alex_opening = response.choices[0].message.content
    show("Alex", alex_opening)
    conversation.append({"Alex": alex_opening})

    for _ in range(5):
        blake_response = blake_chat(conversation)
        conversation.append({"Blake": blake_response})
        show("Blake", blake_response)

        charlie_response = charlie_chat(conversation)
        conversation.append({"Charlie": charlie_response})
        show("Charlie", charlie_response)

        alex_response = alex_chat(conversation)
        conversation.append({"Alex": alex_response})
        show("Alex", alex_response)

    console.rule("[bold green]End of conversation[/bold green]")


if __name__ == "__main__":
    main()