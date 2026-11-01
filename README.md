# ArXiv Paper Fetcher

**English** | [繁體中文](README.zh-TW.md)

Fetches the latest arXiv papers on a topic (default: RAG) through the official arXiv API, lists the title, link, first author, and dates, and translates each abstract (default: Traditional Chinese), so new research is quick to skim.

## What it does

1. Fetches the newest papers by submission date through the official arXiv API (the [`arxiv`](https://pypi.org/project/arxiv/) package)
2. Translates each abstract
3. Prints each paper's title, link, first author, published and updated dates, and the translated abstract

The program currently stops after the first paper (the `break` in `main.py`); remove it to print them all.

## Install

Python 3.8 or later.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Sample output (run on 2026-10-31, abstract omitted):

```text
Title: Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG
URL: http://arxiv.org/abs/2610.40314v1
First author: He Tu
Published: 2026-10-29
Updated: 2026-10-29
Summary (translated): (the abstract in Traditional Chinese)
```

## Settings

All in `config.py`:

| Setting | Default | Description |
|---|---|---|
| `query` | `"RAG"` | Search query, using the [arXiv API](https://info.arxiv.org/help/api/user-manual.html) syntax; for example `cat:cs.CL` is the whole Computation and Language category |
| `max_results` | `20` | Maximum number of papers |
| `sort_by` | `"SubmittedDate"` | Sort order; `Relevance` and `LastUpdatedDate` also work |
| `to_lang` | `"zh-Hant"` | Language to translate abstracts into |

## Note

Translation uses the endpoint behind Microsoft Edge's built-in translator, not the official Azure Translator API. It needs no key, but it may stop working or be rate-limited at any time. For long-term use, switch to [Azure Translator](https://learn.microsoft.com/azure/ai-services/translator/).

## Files

- `main.py`: entry point
- `config.py`: settings
- `fetch_papers/arxiv_fetcher.py`: calls the arXiv API
- `data_processing/translate.py`: translation

## References

- arXiv API: https://info.arxiv.org/help/api/basics.html
- Azure Translator: https://learn.microsoft.com/azure/ai-services/translator/

## License

Apache-2.0, see [LICENSE](LICENSE).
