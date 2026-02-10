# GenAI Post Generator

A small utility to generate LinkedIn-style posts using few-shot examples and an LLM. It provides a Streamlit UI to pick a topic, length, and language and then generates a post using examples from `data/processed_posts.json`.

## Features

- Few-shot examples loader (from `data/processed_posts.json`).
- Small Streamlit UI to pick topic, length and language.
- LLM integration via `llm_helper.py` (uses environment variables for API credentials).
- Reusable prompt generation and example-guided style imitation.

## Quickstart

Prerequisites:

- Python 3.9+ installed
- Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies (example list):

```powershell
pip install pandas python-dotenv streamlit langchain_community
```

Note: This project uses `langchain_community.chat_models.ChatOpenAI`. Adjust packages if your environment or provider differs.

## Environment

Create a `.env` file in the project root (or set environment variables) with:

- `OPENAI_API_KEY` — your API key
- `OPENAI_API_BASE_URL` — optional base URL if using a proxy/alternate endpoint

The helper `llm_helper.py` loads these via `python-dotenv`.

## Running the app

Start the Streamlit app:

```powershell
streamlit run main.py
```

The app presents dropdowns for Topic (tags), Length (`Short`/`Medium`/`Long`), and Language (`English`/`Hinglish`). Click `Generate` to produce a post.

You can also run the small CLI entry (prints a hello message):

```powershell
python main.py
```

## Project layout

- `fewshot.py` — loads `data/processed_posts.json`, normalizes it into a dataframe, categorizes lengths and exposes `get_filtered_posts()` and `get_tags()`.
- `llm_helper.py` — wraps LLM client creation and loads API credentials from environment.
- `post_generator.py` — builds prompts, attaches up to two few-shot examples and calls the LLM to generate a post.
- `main.py` — Streamlit UI and simple CLI entry.
- `data/processed_posts.json` — few-shot example posts used for style imitation.

## Notes on languages

`Hinglish` in the UI means a mix of Hindi and English in content, but the script for generated posts remains in Latin characters (English script). The prompt generation enforces this.

## Customization

- To change example selection or how many examples are appended, edit `post_generator.py`.
- To change LLM model or parameters, update `llm_helper.py`.

## Troubleshooting

- If dropdown `Topic` is empty, verify `data/processed_posts.json` exists and is in expected format (each item should contain `tags`, `text`, `line_count`, and `language`).
- If LLM calls fail, confirm `OPENAI_API_KEY` and `OPENAI_API_BASE_URL` (if used) are correct and reachable.

## Contributing

Contributions welcome — open an issue or submit a PR. Keep changes focused and include tests where relevant.

## License

MIT-style — adapt as appropriate for your project.
