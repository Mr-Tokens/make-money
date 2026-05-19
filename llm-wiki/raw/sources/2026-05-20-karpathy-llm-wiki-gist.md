# Karpathy LLM-Wiki Gist

URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
Date accessed: 2026-05-20

## Source Note

This source introduced the project pattern we are adopting: use files as a persistent knowledge substrate for LLMs. Raw source material is preserved separately from synthesized wiki pages. The wiki layer is maintained by the LLM and made navigable through an index, log, and conventions.

## Project Implications

- Keep raw material under `llm-wiki/raw/`.
- Keep synthesized operational knowledge under `llm-wiki/wiki/`.
- Use `llm-wiki/AGENTS.md` as the rules file for future agents.
- Treat writeback as mandatory after durable findings.
