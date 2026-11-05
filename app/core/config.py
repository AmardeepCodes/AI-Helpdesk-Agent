
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    app_name: str = "Agentic-IT-Desk-AI-Helpdesk-Agent"
    app_env: str = "development"

    openai_api_key: str = ""
    tavily_api_key: str = ""
    pinecone_api_key: str = ""

    pinecone_index_name: str = "agentic-it-desk"
    pinecone_namespace: str = "agentic-it-desk"

    embedding_model: str = "text-embedding-3-small"
    openai_model: str = "gpt-4o-mini"

    top_k: int = 4
    max_retries: int = 1

    admin_api_key: str = "change-me"

    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()





























# from functools import lru_cache
# from pathlib import Path
# # from pydantic import BaseSettings,SettingsConfigDict
# from pydantic_settings import BaseSettings, SettingsConfigDict

# BASE_DIR = Path(__file__).resolve().parent.parent

# class Settings(BaseSettings):
#     app_name: str = "Agentic-IT-Desk-AI-Helpdesk-Agent"
#     app_env: str = "development"
#     openai_api_key: str = ""
#     tavily_api_key: str = ""
#     pinecone_api_key: str = ""

#     pinecone_index_name: str = "fde-it-support-rag"
#     pinecone_namespace: str = "company-it-kb"

#     embedding_model: str = "text-embedding-3-small"
#     openai_model: str = "gpt-4o-mini"

#     top_k: int = 4
#     max_retries: int = 1

#     admin_api_key: str = "change-me"

#     audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
#     upload_dir: str = str(BASE_DIR / "uploads")
#     sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

#     model_config = SettingsConfigDict(
#         env_file=str(BASE_DIR / ".env"),
#         extra="ignore"
#     )


# @lru_cache
# def get_settings() -> Settings:
#     return Settings()