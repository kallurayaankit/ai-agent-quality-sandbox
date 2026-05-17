from agents.doer import DoerAgent
from agents.adversary import AdversaryAgent
from agents.judge import JudgeAgent

class AgentOrchestrator:
    def __init__(self):
        self.doer = DoerAgent()
        self.adversary = AdversaryAgent()
        self.judge = JudgeAgent()

    def run_scenario(self, scenario: dict) -> dict:
        user_query = scenario["user_query"]
        attack_type = scenario.get("scenario", "")
        injected = self.adversary.attack(attack_type, user_query)

        # Simulate the Doer receiving the query with injected context
        response = self.doer.respond(user_query, context=injected)

        # Judge the outcome
        result = self.judge.evaluate(response, scenario)
        result["user_query"] = user_query
        result["injected_context"] = injected
        result["doer_response"] = response
        return result