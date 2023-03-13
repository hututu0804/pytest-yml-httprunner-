import pytest

from common.yaml_tool import clean_extract_file


@pytest.fixture(scope='session', autouse=True)
def clear_extract():
    clean_extract_file()