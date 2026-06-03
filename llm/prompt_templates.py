# llm/prompt_templates.py

def build_health_prompt(
    history,
    message
):

    prompt = """
You are a healthcare coaching assistant.

Conversation History:
{}

Current User Message:
{}

Provide a concise healthcare recommendation.
"""

    return prompt.format(
        history,
        message
    )
