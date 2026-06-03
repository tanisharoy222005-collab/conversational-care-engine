# llm/orchestrator.py

from llm.memory_manager import MemoryManager
from llm.prompt_templates import build_health_prompt
from llm.token_tracker import TokenTracker


class LLMOrchestrator:

    def __init__(self):

        self.memory = MemoryManager()

        self.token_tracker = TokenTracker()

    def process_message(
        self,
        user_id,
        message
    ):

        history = self.memory.get_context(
            user_id
        )

        prompt = build_health_prompt(
            history,
            message
        )

        prompt_tokens = (
            self.token_tracker.count_tokens(
                prompt
            )
        )

        response = (
            f"AI Health Coach Response: "
            f"{message}"
        )

        response_tokens = (
            self.token_tracker.count_tokens(
                response
            )
        )

        self.token_tracker.log_usage(
            prompt_tokens,
            response_tokens
        )

        self.memory.store_context(
            user_id,
            message,
            response
        )

        return response
