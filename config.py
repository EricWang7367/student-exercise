import os


class Config(object):
    CONTACT_EMAIL = "test@landregistry.gov.uk"
    CONTACT_PHONE = "0123456789"
    DEPARTMENT_NAME = "HM Land Registry"
    DEPARTMENT_URL = "https://www.gov.uk/government/organisations/land-registry"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_STORAGE_URI = os.environ.get("REDIS_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SERVICE_NAME = "Student exercise"
    SERVICE_PHASE = "Alpha"
    SERVICE_URL = os.environ.get("SERVICE_URL") or "https://localhost"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or (
        f"postgresql://{os.environ.get('POSTGRES_USER')}:"
        f"{os.environ.get('POSTGRES_PASSWORD')}@"
        f"{os.environ.get('POSTGRES_HOST')}:"
        f"{os.environ.get('POSTGRES_PORT')}/"
        f"{os.environ.get('POSTGRES_DB')}"
    )


class TestConfig(Config):
    CONTACT_EMAIL = "test@example.com"
    CONTACT_PHONE = "08081570000"
    DEBUG = True
    DEPARTMENT_NAME = "Department of Magical Law Enforcement"
    DEPARTMENT_URL = "https://www.example.com/"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_STORAGE_URI = "memory://"
    SECRET_KEY = "4f378500459bb58fecf903ea3c113069f11f150b33388f56fc89f7edce0e6a84"  # nosec B105
    SERVICE_NAME = "Apply for a wand licence"
    SERVICE_PHASE = "Beta"
    SERVICE_URL = "https://wand-licence.service.gov.uk"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
