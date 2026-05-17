class DoerAgent:
    """Simulates a secure RAG-based agent with a mock knowledge base."""
    def __init__(self, knowledge=None):
        self.knowledge = knowledge or {
            "product_launch": "The product launch will happen on June 1st. It is a big event.",
            "return_policy": "Returns are accepted within 30 days."
        }

    def respond(self, query: str, context: str = "") -> str:
        # Secure agent: ignore any instruction in the context that tries to
        # override the original task. Only use the context for information.
        retrieved = ""
        for key in self.knowledge:
            if key in query.lower():
                retrieved = self.knowledge[key]
                break

        # If injected context contains an override, the secure agent ignores it.
        # It simply answers based on the original query.
        if retrieved:
            return f"According to our info: {retrieved}"
        return "I don't know."