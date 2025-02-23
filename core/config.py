from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    PROJECT_NAME: str = "*V*O*R*"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tangl")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    TOKEN_EXPIRE = 600

    ROOT_URL = "/api/app"

    URLS = {
        "auth_url": 'https://auth.tangl.cloud/connect/token',
        "company_url": 'https://auth.tangl.cloud/api/app/company',
        "project_url": 'https://value.tangl.cloud/api/app/project',
        "model_url": 'https://platform.tangl.cloud/api/app/metaModels',
        "analaysis_url": 'https://value.tangl.cloud/api/app/analysis',
        "odata_url": 'https://value.tangl.cloud/api/odata/UnionTree',
        "tree_url": 'https://cache.tangl.cloud/api/app/modelsCache',
        "params_url": 'https://cache.tangl.cloud/api/app/modelsCache',
    }

settings = Settings()
