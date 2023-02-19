import pytest
from {{ cookiecutter.project_snake }}.config import settings


@pytest.fixture
def csv_data():
    return []


def test_csv_read():
    assert True


def test_settings():
    assert settings.PROJECT_NAME == "{{ cookiecutter.project_snake }}"
    
    
    assert settings.ROOT_DIR.exists()
    assert settings.DATA_DIR.exists()
    assert settings.SQL_DIR.exists()
    assert settings.NOTEBOOK_DIR.exists()
    assert settings.CONFIG_DIR.exists()   
    assert settings.LOG_DIR.exists()
    assert settings.TEMP_DIR.exists()    