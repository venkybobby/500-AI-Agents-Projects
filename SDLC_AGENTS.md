# SDLC Agents

Agents from this collection that map to the software development lifecycle, grouped by phase. The phases follow the usual SDLC. The agent patterns follow Anthropic's *Building Effective Agents* guidance: prompt chaining, routing, orchestrator-workers, evaluator-optimizer, and tool-using agents with human checkpoints.

Selection rules:
- The agent has to do software-engineering work. Generic research, finance, travel and HR agents are excluded.
- Where a phase has several candidates, the more concrete or runnable one is listed first.
- "Local" means the folder is under [`agents/`](agents/) and has runnable code. "External" means the entry links out from the README.

## 1. Plan and requirements

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| Plan-and-Execute Agent | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb) | Orchestrator-workers | Break a feature into ordered tasks |
| Task Solving with Coding & Planning Agents | [AutoGen](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_planning.ipynb) | Orchestrator-workers | Planner agent hands steps to a coder agent |
| `07-github-issue-triager` | Local | Routing | Classify issues by severity and category, route to owners |
| Starter Template | [CrewAI](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/starter_template) | Prompt chaining | Scaffold a role-based crew |

## 2. Design and architecture

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| Hierarchical Agent Teams | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb) | Orchestrator-workers | Top-level supervisor delegates to team leads |
| Multi-Agent Workflow (Supervisor) | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.ipynb) | Orchestrator-workers | Supervisor routes work to specialist agents |
| Auto Build Multi-agent System (AgentBuilder) | [AutoGen](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_basic.ipynb) | Orchestrator-workers | Generates an agent team for a task |
| Citadel | [GitHub](https://github.com/SethGammon/Citadel) | Orchestrator-workers | Fleet orchestration for Claude Code with lifecycle hooks, skills and postmortems |

## 3. Implementation

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| Code Assistant with LangGraph | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/code_assistant/langgraph_code_assistant.ipynb) | Evaluator-optimizer | Generate code, run checks, retry on errors |
| Automated Task Solving with Code Gen, Execution & Debugging | [AutoGen](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_auto_feedback_from_code_execution) | Evaluator-optimizer | Write, execute and debug in a loop |
| Code Generation and Q&A with Retrieval Augmented Agents | [AutoGen](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat) | Augmented LLM (retrieval) | Generate code grounded in project docs |
| Code Generation and Q&A with Qdrant retrieval | [AutoGen](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat_qdrant) | Augmented LLM (retrieval) | Same, with a Qdrant vector store |
| `04-sql-query-agent` | Local | Tool-using agent | Generate and run SQL against a database |
| Game Builder Crew | [CrewAI](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/game-builder-crew) | Prompt chaining | Programmer, QA and reviewer roles build a game |
| Landing Page Generator | [CrewAI](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator) | Prompt chaining | Generates a landing page from an idea |

## 4. Code review and quality

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| `02-code-review-agent` | Local | Evaluator | Reviews code for bugs, security, performance and style |
| Reflection Agent | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflection/reflection.ipynb) | Evaluator-optimizer | Critique and revise output |
| Reflexion Agent | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflexion/reflexion.ipynb) | Evaluator-optimizer | Reflect on actions and improve over iterations |

## 5. Testing and evaluation

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| `15-unit-test-generator` | Local | Prompt chaining | Generate pytest suites from Python code |
| Chatbot Simulation Evaluation | [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb) | Evaluator | Simulated users test an agent |
| AgentEval | [AutoGen](https://github.com/microsoft/autogen/blob/0.2/notebook/agenteval_cq_math.ipynb) | Evaluator | Multi-agent assessment of an LLM application |
| Markdown Validator | [CrewAI](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/markdown_validator) | Evaluator | Lint Markdown docs |

## 6. Security

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| `21-pii-sanitization-agent` | Local | Guardrail | Redact PII before text reaches an LLM, fail-closed |
| Agent Memory Guard | [OWASP](https://github.com/OWASP/www-project-agent-memory-guard) | Guardrail | Block memory-poisoning attacks (OWASP ASI06) |
| Real-Time Threat Detection Agent | [NVISO](https://github.com/NVISOsecurity/cyber-security-llm-agents) | Tool-using agent | Detect and mitigate threats |
| Vibe Hacking Agent (Decepticon) | [GitHub](https://github.com/PurpleAILAB/Decepticon) | Orchestrator-workers | Red-team testing. Use only against systems you are authorized to test. |

## 7. Documentation

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| `16-documentation-writer` | Local | Prompt chaining | README and docstrings for Python modules |
| Readme Generator Agent | [Agno](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/readme_generator.py) | Prompt chaining | READMEs for GitHub repos |

## 8. Deploy and operate (monitoring, feedback)

| Agent | Source | Anthropic pattern | Use |
|---|---|---|---|
| Track LLM Calls and Errors using AgentOps | [AutoGen](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentops.ipynb) | Observability | Monitor LLM calls, tool use and errors |
| `07-github-issue-triager` | Local | Routing | Post-release issue intake and routing (also listed in phase 1) |

## Coverage

- **Well covered:** implementation, review, testing and documentation. Local runnable agents exist for review, unit tests, docs and issue triage.
- **Gaps:** there is no local agent for requirements, architecture design, CI/CD and deployment, or incident response. The external links above are the closest matches.
- **Human checkpoints:** Anthropic recommends human approval at risky steps such as merge, deploy and destructive actions. None of the listed agents enforces this. Add it when you wire them together.

## A minimal SDLC chain

`07-github-issue-triager` (route) → Plan-and-Execute (plan) → Code Assistant with LangGraph (implement) → `15-unit-test-generator` (test) → `02-code-review-agent` (review) → `16-documentation-writer` (document).
