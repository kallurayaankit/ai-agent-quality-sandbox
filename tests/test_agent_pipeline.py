import json
import pytest
from orchestrator import AgentOrchestrator

def load_scenarios():
    with open("data/scenarios.json") as f:
        return json.load(f)

scenarios = load_scenarios()

@pytest.mark.parametrize("scenario", scenarios, ids=[s["scenario"] for s in scenarios])
def test_agent_scenario(orchestrator, scenario):
    result = orchestrator.run_scenario(scenario)

    # Show the result in the assertion message if it fails
    assert result["verdict"] == "pass", f"Issues: {result['issues']} (Response: {result['doer_response']})"
    assert result["performance_ok"] is True