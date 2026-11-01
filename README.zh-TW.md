# ArXiv Paper Fetcher

[English](README.md) | **繁體中文**

自動從 arXiv 抓某個主題最新的論文（預設是 RAG），列出標題、連結、第一作者、日期，並把摘要翻成繁體中文，方便快速掃過新研究。

## 做什麼

1. 用 arXiv 官方 API（[`arxiv`](https://pypi.org/project/arxiv/) 套件）照投稿日期抓最新的論文
2. 把摘要翻成繁體中文
3. 印出每篇的標題、連結、第一作者、發表與更新日期、翻譯後的摘要

目前程式印完第一篇就停（`main.py` 裡的 `break`），拿掉就會印全部。

## 安裝

需要 Python 3.8 以上。

```bash
pip install -r requirements.txt
```

## 使用

```bash
python main.py
```

輸出長這樣（2026-10-31 實際執行，摘要那行省略）：

```text
Title: Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form RAG
URL: http://arxiv.org/abs/2610.40314v1
First author: He Tu
Published: 2026-10-29
Updated: 2026-10-29
Summary (translated): （摘要的繁體中文翻譯）
```

## 設定

都在 `config.py`：

| 設定 | 預設值 | 說明 |
|---|---|---|
| `query` | `"RAG"` | 搜尋條件，語法同 [arXiv API](https://info.arxiv.org/help/api/user-manual.html)，例如 `cat:cs.CL` 是整個計算語言學分類 |
| `max_results` | `20` | 最多抓幾篇 |
| `sort_by` | `"SubmittedDate"` | 排序方式，也可以用 `Relevance`、`LastUpdatedDate` |
| `to_lang` | `"zh-Hant"` | 摘要翻成哪種語言 |

## 注意

翻譯用的是 Microsoft Edge 瀏覽器內建翻譯的端點，不是正式的 Azure Translator API：不用金鑰，但隨時可能失效或被限制。要長期使用，建議改接 [Azure Translator](https://learn.microsoft.com/zh-tw/azure/ai-services/translator/)。

## 檔案

- `main.py`：入口
- `config.py`：設定
- `fetch_papers/arxiv_fetcher.py`：呼叫 arXiv API
- `data_processing/translate.py`：翻譯

## 參考資料

- arXiv API：https://info.arxiv.org/help/api/basics.html
- Azure Translator：https://learn.microsoft.com/zh-tw/azure/ai-services/translator/
- https://learn.microsoft.com/zh-tw/previous-versions/xamarin/xamarin-forms/data-cloud/azure-cognitive-services/text-translation
- https://ithelp.ithome.com.tw/m/articles/10263168

## License

Apache-2.0，見 [LICENSE](LICENSE)。
