# Assignment Guide
**RAG-to-MCP · Nasscom AI-Code Sarathi · Developer Workshop**

Follow every step in order. Do not skip sections.

---

## Contents

1. [Before You Start](#1-before-you-start)
2. [Fork and Clone](#2-fork-and-clone)
3. [Create Your Branch](#3-create-your-branch)
4. [How the Session Works](#4-how-the-session-works)
5. [The Workflow for Every UC](#5-the-workflow-for-every-uc)
6. [UC-0A — Done With Your Facilitator](#6-uc-0a--done-with-your-facilitator)
7. [UC-RAG — Build Your RAG Server](#7-uc-rag--build-your-rag-server)
8. [UC-MCP — Expose RAG as an MCP Tool](#8-uc-mcp--expose-rag-as-an-mcp-tool)
9. [Commit, Push, and Open a PR](#9-commit-push-and-open-a-pr)
10. [Quick Reference](#10-quick-reference)

---

## 1. Before You Start

Complete `docs/pre-session-install.md` the night before.
All items must show ✅ before you sit down for the session.

The session-day checklist:

- [ ] `python3 --version` shows 3.9+
- [ ] `chromadb` and `sentence-transformers` installed
- [ ] Embedding model pre-downloaded
- [ ] `GEMINI_API_KEY` environment variable set
- [ ] Repo forked and cloned
- [ ] Stub index built: `python3 uc-rag/stub_rag.py --build-index`
- [ ] GitHub Desktop open and signed in

---

## 2. Fork and Clone

1. Go to `https://github.com/nasscomAI/RAG-to-MCP`
2. Click **Fork** → **Create fork**
3. Open **GitHub Desktop** → File → Clone Repository
4. Select your fork → choose a local folder → **Clone**
5. Open the cloned folder in your code editor

---

## 3. Create Your Branch

In **GitHub Desktop**:
1. Click **Current Branch** → **New Branch**
2. Name it exactly:
   ```
   participant/[your-name]-[city]
   ```
3. Click **Create Branch**

Use this one branch for all three UCs. Do not create separate branches per UC.

---

## 4. How the Session Works

Three UCs. One path. No choices.

| UC | What you build | Time |
|---|---|---|
| UC-0A | Complaint Classifier | 45 min — with facilitator |
| UC-RAG | RAG Server | 60 min — independently |
| UC-MCP | MCP Server wrapping RAG | 30 min — independently |

UC-MCP calls UC-RAG. If your `rag_server.py` is not complete,
UC-MCP automatically uses `stub_rag.py` as a fallback.
You can complete UC-MCP even if UC-RAG is unfinished.

---

## 5. The Workflow for Every UC

Every UC follows the same sequence:

```
1. Read the UC README completely
2. Copy the README → paste into AI → generate agents.md
3. Update agents.md manually
4. Copy the README → paste into AI → generate skills.md
5. Update skills.md manually
6. Share agents.md + skills.md + README with AI coder
7. Ask AI to implement the .py file
8. Run with python3
9. Analyze output — name the failure mode
10. Fix one thing → re-run → compare
11. Commit with the formula
```

### Generating agents.md

Open your AI tool. Paste this prompt followed by the full README content:

```
Read the following UC README. Using the R.I.C.E framework,
generate an agents.md YAML with four fields:
role, intent, context, enforcement.

R.I.C.E:
- Role: who the agent is and its operational boundary
- Intent: what a correct output looks like — verifiable
- Context: what the agent may use — state exclusions explicitly
- Enforcement: every rule listed under
  "Enforcement Rules Your agents.md Must Include"

Output only valid YAML. No explanation, no code fences.

README:
[paste README here]
```

Then update the output — check every enforcement rule against the README.

### Generating skills.md

```
Read the following UC README. Generate a skills.md YAML
defining the skills described in the README.

Each skill needs: name, description, input, output, error_handling.
error_handling must address the failure modes in the README.

Output only valid YAML. No explanation, no code fences.

README:
[paste README here]
```

### Generating the .py file

```
Using the agents.md and skills.md provided, implement [filename].
Follow the enforcement rules in agents.md exactly.
Implement every skill in skills.md including error_handling.
Accept the run command arguments shown in the README.

agents.md:
[paste agents.md]

skills.md:
[paste skills.md]

README:
[paste README]
```

---

## 6. UC-0A — Done With Your Facilitator

UC-0A is the session anchor. Your facilitator walks through it with you.

**What you build:** A complaint classifier that reads city complaint CSVs
and outputs category, priority, reason, and flag.

**What you learn:** R.I.C.E enforcement — specifically, that a vague prompt
produces taxonomy drift and severity blindness. A precise Enforcement rule
with explicit keywords fixes both.

**After the exercise, confirm these files exist:**
- `uc-0a/agents.md` — updated, not the starter placeholder
- `uc-0a/skills.md` — updated
- `uc-0a/classifier.py` — runs without crash
- `uc-0a/results_[city].csv` — output present

**Run command:**
```bash
cd uc-0a
python3 classifier.py --input ../data/city-test-files/test_pune.csv \
                      --output results_pune.csv
```

---

## 7. UC-RAG — Build Your RAG Server

**What you build:** A retrieval-augmented generation server that chunks
three policy documents, embeds them with sentence-transformers, stores
vectors in ChromaDB, retrieves relevant chunks per query, and answers
using only retrieved context.

**The three failure modes you will fix:**

| Failure | What it looks like | What fixes it |
|---|---|---|
| Chunk boundary | Clause 5.2 split across two chunks — answer misses one approver | Sentence-aware chunking |
| Wrong retrieval | "Personal phone" query returns HR leave chunks | Similarity threshold + metadata |
| Context breach | Answer adds "as is standard practice" — not in any document | Enforcement: retrieved chunks only |

### Step-by-step

**Step 1 — Run the naive version first**

Before writing anything, run this to see the failures:
```bash
cd uc-rag
python3 stub_rag.py --query "Can I use my personal phone for work files?" --json
```

Note what it returns. Then ask yourself: does it blend IT and HR policies?
Does it add anything not in the documents?

**Step 2 — Read the README**

Open `uc-rag/README.md`. Read the enforcement rules, skill definitions,
and reference verification queries before generating any files.

**Step 3 — Generate and update agents.md**

Use the AI prompt from Section 5. Update the output to ensure all five
enforcement rules from the README are present and specific.

**Step 4 — Generate and update skills.md**

Use the AI prompt from Section 5. Verify `error_handling` for
`retrieve_and_answer` names the refusal template explicitly.

**Step 5 — Build rag_server.py**

Use the AI coding prompt from Section 5. The starter file has four
functions to implement: `chunk_documents`, `retrieve_and_answer`,
`build_index`, `naive_query`.

**Step 6 — Build the index**

```bash
python3 rag_server.py --build-index
```

**Step 7 — Run naive mode first**

```bash
python3 rag_server.py --naive --query "Can I use my personal phone for work files?"
```

Record the output. This is the failure you are fixing.

**Step 8 — Run RAG mode**

```bash
python3 rag_server.py --query "Can I use my personal phone for work files?"
python3 rag_server.py --query "Who approves leave without pay?"
python3 rag_server.py --query "What is the flexible working culture?"
```

Verify against the reference table in `uc-rag/README.md`.

**Step 9 — Fix and commit**

Fix the most significant failure. Commit:
```
UC-RAG Fix [failure mode]: [why] → [what you changed]
```

### Fallback

If `rag_server.py` is not working, `stub_rag.py` is used automatically
by UC-MCP. You can proceed to UC-MCP and return to UC-RAG later.

---

## 8. UC-MCP — Expose RAG as an MCP Tool

**What you build:** A plain HTTP server implementing the MCP protocol
(JSON-RPC 2.0) that exposes one tool: `query_policy_documents`.
An agent calls this server, discovers the tool, and invokes it with a question.

**The failure mode you will fix:**

A vague tool description gives agents permission to call your tool for
questions outside its scope. The tool description is the enforcement —
the same way the E in R.I.C.E is the enforcement.

### Step-by-step

**Step 1 — Read the README**

Open `uc-mcp/README.md`. Read the MCP protocol section carefully —
understand the two JSON-RPC methods before writing anything.

**Step 2 — Set your Gemini API key**

```bash
export GEMINI_API_KEY="your-key-here"
```

Test it:
```bash
python3 uc-mcp/llm_adapter.py
```

Must print a response. If using Claude or OpenAI, edit `llm_adapter.py`
and uncomment the relevant section.

**Step 3 — Generate and update agents.md and skills.md**

Use the AI prompts from Section 5 with `uc-mcp/README.md`.

**Step 4 — Build mcp_server.py**

Use the AI coding prompt. The starter has two things to implement:
- `TOOL_DEFINITION["description"]` — write a specific, scoped description
- `MCPHandler.do_POST` — handle `tools/list` and `tools/call`

**Step 5 — Start the server**

```bash
cd uc-mcp
python3 mcp_server.py --port 8765
```

Leave this running. Open a second terminal for the next step.

**Step 6 — Run the test client**

```bash
python3 test_client.py --run-all
```

Four tests run automatically. Review every result.
The budget forecast question must return `isError: true`.

**Step 7 — Fix the tool description**

If the budget forecast question does not refuse, your tool description
is too vague. Update `TOOL_DEFINITION["description"]` in `mcp_server.py`
to explicitly state the scope and the refusal condition. Re-run the test client.

**Step 8 — Commit**

```
UC-MCP Fix [failure mode]: [why] → [what you changed]
```

---

## 9. Commit, Push, and Open a PR

### Commit formula

```
[UC-ID] Fix [what]: [why it failed] → [what you changed]
```

### Push in GitHub Desktop

After each commit: click **Push origin** in GitHub Desktop.

### Open the PR

1. Go to `https://github.com/nasscomAI/RAG-to-MCP`
2. Click **Compare & pull request** on the banner
3. Title: `[City] [Name] — RAG-to-MCP Submission`
4. Fill every section of the PR template
5. Click **Create pull request**

### What your PR must contain

| File | Required |
|---|---|
| `uc-0a/agents.md` | ✅ |
| `uc-0a/skills.md` | ✅ |
| `uc-0a/classifier.py` | ✅ |
| `uc-0a/results_[city].csv` | ✅ |
| `uc-rag/agents.md` | ✅ |
| `uc-rag/skills.md` | ✅ |
| `uc-rag/rag_server.py` | ✅ (your implementation, not stub) |
| `uc-mcp/agents.md` | ✅ |
| `uc-mcp/skills.md` | ✅ |
| `uc-mcp/mcp_server.py` | ✅ |

---

## 10. Quick Reference

### AI prompt — generate agents.md
```
Read the following UC README. Using R.I.C.E, generate agents.md YAML
with: role, intent, context, enforcement. Enforcement must include
every rule listed under "Enforcement Rules Your agents.md Must Include".
Output only valid YAML.

README: [paste here]
```

### AI prompt — generate skills.md
```
Read the following UC README. Generate skills.md YAML for the skills
described. Each needs: name, description, input, output, error_handling.
error_handling must address the failure modes in the README.
Output only valid YAML.

README: [paste here]
```

### Run commands

```bash
# UC-0A
python3 uc-0a/classifier.py --input data/city-test-files/test_pune.csv --output uc-0a/results_pune.csv

# UC-RAG — build index
python3 uc-rag/rag_server.py --build-index

# UC-RAG — query
python3 uc-rag/rag_server.py --query "Who approves leave without pay?"

# UC-MCP — start server
python3 uc-mcp/mcp_server.py --port 8765

# UC-MCP — test
python3 uc-mcp/test_client.py --run-all
```

### Commit formula
```
[UC-ID] Fix [what]: [why it failed] → [what you changed]
```

### Getting help
- Blocked for 5+ minutes → flag your tutor
- RAG not working → use `stub_rag.py` and proceed to UC-MCP
- Git issues → GitHub Desktop docs: https://docs.github.com/en/desktop
- LLM not working → check `GEMINI_API_KEY` is set, test with `python3 uc-mcp/llm_adapter.py`
