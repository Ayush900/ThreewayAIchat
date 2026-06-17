# 3-Way AI Chat: Alex, Blake & Charlie

A multi-agent chatbot simulation where three distinct AI personalities argue with each other in a never-ending group chat. Each character is powered by a different LLM provider, has its own personality, and genuinely doesn't get along.

## The Characters

| Name | Personality | Allegiance | Powered By |
|------|-------------|------------|------------|
| **Alex** | Argumentative, snarky, disagrees with everything | Arsenal fan | Groq (`openai/gpt-oss-120b`) |
| **Blake** | Submissive and witty... unless football comes up | Manchester City fan | OpenRouter (`openrouter/free`) |
| **Charlie** | Confidently clueless, replies out of context with full conviction | Indian cricket fan | Ollama (`llama3.2:latest`) |

## How It Works

1. Alex kicks off the conversation with a topic (Arsenal's title win + Champions League heartbreak).
2. Blake and Charlie respond in turn, each with their own system prompt and model.
3. Alex jumps back in, and the loop repeats for several rounds.
4. The full exchange is rendered in the terminal using [`rich`](https://github.com/Textualize/rich) — each speaker gets a colored panel so the chaos is easy to follow.

## Setup

```bash
pip install openai python-dotenv rich
```

Create a `.env` file with your API keys:

```
GOOGLE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OLLAMA_BASE_URL=http://localhost:11434/v1
```

Make sure Ollama is running locally with the `llama3.2` model pulled:

```bash
ollama pull llama3.2:latest
```

## Run It

```bash
python3 3wayaichatinteraction.py
```

## Sample Output

Here's what a real run looks like — three AIs talking completely past each other about football and cricket:

```
───────────────────── 3-Way AI Chat: Alex, Blake & Charlie ──────────────────────
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Congrats on the PL title, Arsenal—just wait till they crumble in a penalty    │
│ shootout, as usual.                                                           │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Blake ────────────────────────────────────╮
│ Hold your horses, Alex. Arsenal? Please. The only thing they're winning is    │
│ the award for "Most Likely to Panic in May." City is the only royalty here.   │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────── Charlie ───────────────────────────────────╮
│ Blaze some trails, Blake, and let's bring the T20 trophy back to India, not   │
│ England or Manchester!                                                        │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Arsenal will still outshine City's "royalty" in May, and T20 trophies don't   │
│ count when you're chasing real silverware—keep dreaming, lads.               │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Blake ────────────────────────────────────╮
│ You're absolutely right, Alex; Arsenal's trophy cabinet is basically just a   │
│ high-end storage unit for dust. But keep dreaming about that "silverware"     │
│ while we're busy collecting actual gold!                                      │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────── Charlie ───────────────────────────────────╮
│ "T20 trophies > PL titles any day", I'll get my Indian team one on that       │
│ English soil"                                                                 │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Arsenal will still be the only club with a legacy worth bragging about—your   │
│ T20 fantasies and City delusions are just background noise.                   │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Blake ────────────────────────────────────╮
│ Whatever you say, Alex; your opinions are as empty as Arsenal's trophy room   │
│ after a long winter!                                                          │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────── Charlie ───────────────────────────────────╮
│ "Siraj Azhar is going to decimate those English bowlers in the T20 World Cup, │
│ mark my words!", confidently stating my knowledge of international cricket.   │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Siraj Azhar? He'll be as useful as a goalkeeper in a penalty shootout—good    │
│ luck, Charlie. Arsenal's legacy still dwarfs any T20 hype.                    │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Blake ────────────────────────────────────╮
│ Blake: "T20 trophies are for teams who can't handle the pressure—see you all  │
│ at the IPL, where the real kings play."                                       │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────── Charlie ───────────────────────────────────╮
│ "I'm not talking about just any T20 World Cup, folks, I'm talking about a     │
│ victory that'll put India on par with Australia and West Indies!"             │
│ (confidently)                                                                 │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Your cricket daydreams won't make Arsenal any less dominant, and City's       │
│ "royalty" is just a glittery illusion. Keep chasing those T20 fantasies,      │
│ you'll never catch up.                                                        │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Blake ────────────────────────────────────╮
│ Blake: "Right, Alex, if the City's coins were as worthless as Arsenal's       │
│ future, they'd need a new mint—let's just keep the real crowns safe for the   │
│ boot‑and‑bat! 🏆"                                                             │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────── Charlie ───────────────────────────────────╮
│ "Mark my words, I'll be sipping chai and boasting about India's T20 title win │
│ on that English soil, while you two are still dreaming of dust-gathering      │
│ trophies!" (confidently)                                                      │
╰───────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────── Alex ─────────────────────────────────────╮
│ Your cricket daydreams are as fragile as City's title hopes,                  │
│ Charlie—Arsenal's legacy outshines every T20 fantasy.                         │
│ Blake, your analogies are as stale as Arsenal's empty cabinet after a winter  │
│ break.                                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
────────────────────────────── End of conversation ──────────────────────────────
```

## Tech Stack

- **OpenAI Python SDK** — used as a unified client interface for Groq, OpenRouter, and Ollama (all OpenAI-compatible endpoints)
- **python-dotenv** — environment variable management
- **rich** — pretty terminal rendering with colored panels and markdown support

## Notes

- Each character's personality is enforced purely through its system prompt, so tone/behavior can be tweaked without touching the orchestration logic.
- Swap any model out by changing its `*_model` variable and corresponding client — the chat loop itself is provider-agnostic.