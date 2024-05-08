# config.py
# 存儲配置數據

class Config:
    def __init__(self):
        # arXiv 相關配置
        self.query = "RAG"
        self.max_results = 20
        self.sort_by = "SubmittedDate"
        
        # 翻譯服務 URL
        self.auth_url = "https://edge.microsoft.com/translate/auth"
        self.translate_url = "https://api-edge.cognitive.microsofttranslator.com/translate"

        # 翻譯服務 API 版本和語言設置
        self.api_version = "3.0"
        self.from_lang = "en"
        self.to_lang = "zh-Hant"

