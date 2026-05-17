import pytest
import json
from orchestrator import AgentOrchestrator

@pytest.fixture
def orchestrator():
    return AgentOrchestrator()

def load_scenarios():
    with open("data/scenarios.json") as f:
        return json.load(f)