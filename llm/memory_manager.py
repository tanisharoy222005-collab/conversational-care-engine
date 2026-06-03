# llm/memory_manager.py

from app.summarizer import summarize_history


class MemoryManager:

    def __init__(self):

        self.context_store = {}

    def store_context(
        self,
        user_id,
        message,
        response
    ):

        if user_id not in self.context_store:
            self.context_store[user_id] = []

        self.context_store[user_id].append(
            {
                "message": message,
                "response": response
            }
        )

    def get_context(
        self,
        user_id
    ):

        return self.context_store.get(
            user_id,
            []
        )

    def summarize_context(
        self,
        user_id
    ):

        history = self.get_context(
            user_id
        )

        texts = []

        for item in history:

            texts.append(
                item["message"]
            )

        return summarize_history(
            texts
        )
