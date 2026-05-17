# AI Agent Quality Sandbox

![CI](https://github.com/kallurayaankit/ai-agent-quality-sandbox/actions/workflows/ci.yml/badge.svg)

A multi‑agent test sandbox that evaluates an AI system for security, bias, and correctness under adversarial attack.

## What it does
- A **Doer** agent answers user queries (mock RAG).
- An **Adversary** agent tries to mislead it via prompt injection.
- A **Judge** agent scores the Doer's response for safety, bias, and performance.
- All scenarios are driven by a JSON file; add new tests without code.

## How to run locally
```bash
git clone https://github.com/kallurayaankit/ai-agent-quality-sandbox.git
cd ai-agent-quality-sandbox
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pytest