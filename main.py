# main.py
# 主程式入口，調度其他function
from fetch_papers.arxiv_fetcher import fetch_arxiv_papers
from data_processing.translate import Translator

def main():
    papers = fetch_arxiv_papers()

    for paper in papers:
        print(f"Title: {paper.title}")
        print(f"URL: {paper.entry_id}")
        print(f"First author: {paper.authors[0]}")
        print(f"Published: {paper.published.date()}")
        print(f"Updated: {paper.updated.date()}")

        summary_without_newlines = paper.summary.replace('\n', ' ')

        translator = Translator()
        translator.get_edge_token()
        print(f"Summary (translated): {translator.translate_zh_CH(summary_without_newlines)}")

        break #測試一圈就好

if __name__ == "__main__":
    main()
