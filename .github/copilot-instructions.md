# Copilot / AI Agent Instructions

Purpose
- Help AI coding agents be immediately productive in this small chatbot repo.

Big picture
- This is a small script-based chatbot prototype: `backend.py` trains a simple sklearn classifier on `data.csv` and then builds prompts for Google Gemini (via `google.generativeai`).
- Core flow: load CSV -> vectorize `text` -> train `MultinomialNB` -> predict `intent` -> call Gemini with role/tone instructions.

Key files to inspect
- `backend.py` — main entrypoint and training/prompt logic.
- `data.csv` — training dataset; two columns: `text,intent` (CSV header present).
- `test.py` — helper that lists available Generative AI models (also contains an example API key; treat as sensitive).

How to run (dev)
- Install typical deps: `pip install pandas scikit-learn google-generativeai`
- Train & run the bot: `python backend.py` (it runs `train_model()` at startup then prompts for input).
- Quick model check: `python test.py` (lists models with generation capability).

Project-specific conventions & patterns
- Single-file script style: global `vectorizer` and `model` are module-level globals in `backend.py` used across functions — avoid refactoring into classes without updating initialization order.
- Data format: `data.csv` rows are short text examples mapped to an `intent` label. New intents should be added consistently across rows.
- Prompt composition: agent role and tone are combined into a small system prompt before calling Gemini. See `get_ai_response()` in `backend.py` for the exact pattern.

Integration & secrets
- The code expects a Gemini-capable client via `google.generativeai` and an API key configured via `genai.configure(api_key=...)`. Prefer setting the key in environment variables and the module top-level constant `GENAI_API_KEY` rather than committing secrets.
- `test.py` currently contains an inline API key; rotate and remove any committed keys immediately.

What to change / safe-first edits for AI agents
- If editing initialization, ensure `vectorizer.fit_transform()` happens before any `transform()` calls during evaluation.
- If replacing the simple classifier, keep input/output shapes the same: `model.fit(X, df['intent'])` and `model.predict(text_vector)`.

Diagnostics & debugging
- If models fail to generate, run `python test.py` to confirm available generation methods.
- For reproducible training/debug runs, add a small `if __name__ == '__main__'` wrapper (already present) and avoid side-effects at import time.

Notes for reviewers
- No repository-level Copilot or AGENT files were found to merge; this file is an initial, targeted guide based on `backend.py`, `data.csv`, and `test.py`.

Please review for missing repository-specific facts or commands I should include.
