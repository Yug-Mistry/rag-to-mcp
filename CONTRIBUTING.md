# Contributing to RAG-to-MCP

## The Mental Model

This repo is not a collaborative codebase. It is a portfolio of engineering evidence.

You are building three systems — one per UC — and leaving a trail that proves
you understood what failed and why, and what you did to fix it.

The trail is: your `agents.md` files, your `skills.md` files, your code,
and your commit history. The PR is the submission. The commit history is the argument.

---

## Branching

**One branch. All three UCs. The entire session.**

```bash
git checkout -b participant/[your-name]-[city]
```

| ✅ Correct | ❌ Wrong |
|---|---|
| `participant/arshdeep-pune` | `uc-rag-branch` |
| `participant/priya-hyderabad` | `main` |
| `participant/rahul-kolkata` | `feature/mcp-server` |

All three UCs — UC-0A, UC-RAG, UC-MCP — go into this one branch.
Your commit history tells the story of your CRAFT loop in sequence.

---

## Folder Structure

Work only inside your UC's folder.

```
uc-0a/      Your UC-0A work
uc-rag/     Your UC-RAG work
uc-mcp/     Your UC-MCP work
data/       Read-only — do not modify
```

For each UC, you create or update exactly three files:

| File | How |
|---|---|
| `agents.md` | Paste UC README into AI → generate YAML → update manually |
| `skills.md` | Paste UC README into AI → generate YAML → update manually |
| `classifier.py` / `rag_server.py` / `mcp_server.py` | Build using AI coder, run with python3, fix with CRAFT |

**Do not modify:**
- `uc-rag/stub_rag.py` — this is the fallback, not your submission
- `uc-mcp/test_client.py` — this is the test harness, not your submission
- `uc-mcp/llm_adapter.py` — only change if switching LLM provider

---

## The Workflow Per UC

Follow this sequence for every UC. Do not skip steps.

```
1. Read the UC README                     before touching any tool
2. Paste README into AI → generate agents.md → update it
3. Paste README into AI → generate skills.md → update it
4. Share agents.md + skills.md + README with AI coder
5. Ask AI to implement the .py file
6. Run with python3
7. Analyze output — name the failure mode
8. Fix one thing → re-run → compare
9. git add → git commit → continue
```

The naive run (running the .py file before fixing enforcement) is the Control step.
You cannot name a failure mode you have not seen.

---

## Commit Message Formula

```
[UC-ID] Fix [what]: [why it failed] → [what you changed]
```

**Good:**
```
UC-0A  Fix severity blindness: no keywords → added injury/child/school/hospital triggers
UC-RAG Fix chunk boundary: fixed-size split → sentence-aware chunking
UC-RAG Fix wrong retrieval: no doc filter → added document-level metadata filter
UC-MCP Fix vague tool description: no scope → added CMC policy scope + refusal note
```

**Will be flagged:**
```
update · done · fix · wip · final · working now
```

Minimum **3 commits** — one per UC.

---

## Submitting

```bash
git push origin participant/[your-name]-[city]
```

Open a Pull Request against `main` on the upstream repo.
Title: `[City] [Name] — RAG-to-MCP Submission`
Fill every section of the PR template before submitting.

---

## What Not to Do

- Do not modify files in `data/` — shared read-only inputs
- Do not push directly to `main`
- Do not create a new branch per UC — one branch for all three
- Do not submit with `stub_rag.py` as your UC-RAG implementation
- Do not accept AI-generated agents.md without reading and updating it
- Do not run `pip3 install` during the session — install everything the night before
