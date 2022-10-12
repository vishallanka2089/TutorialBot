import os
import openai

openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nVishal:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to Vishal, Tutorial bot influencer who was mentored by Elon Musk in the past."


def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
