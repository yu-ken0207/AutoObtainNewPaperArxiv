# arxiv_fetcher.py
# arXiv API 使用
from arxiv import Client , Search , SortCriterion
from config import Config

config = Config()

def fetch_arxiv_papers():
    client = Client()
    arxiv_search = Search(
        query=config.query,
        max_results=config.max_results,
        sort_by=getattr(SortCriterion, config.sort_by)
    )
    try:
        results = client.results(arxiv_search)
        return results
    except Exception as e:
        print(f"Error fetching or processing results: {e}")
        return []
