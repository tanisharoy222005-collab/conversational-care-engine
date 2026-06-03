# llm/token_tracker.py

class TokenTracker:

    def __init__(self):

        self.total_prompt_tokens = 0

        self.total_response_tokens = 0

    def count_tokens(
        self,
        text
    ):

        return len(
            text.split()
        )

    def log_usage(
        self,
        prompt_tokens,
        response_tokens
    ):

        self.total_prompt_tokens += (
            prompt_tokens
        )

        self.total_response_tokens += (
            response_tokens
        )

    def get_usage_stats(self):

        return {
            "prompt_tokens":
                self.total_prompt_tokens,

            "response_tokens":
                self.total_response_tokens
        }
