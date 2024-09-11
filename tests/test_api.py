import requests
import pytest

@pytest.fixture
def app_url():
    # Replace with the actual URL of your deployed app
    return "https://lasyaed--vllm-openai-compatible-serve.modal.run"

def test_app_status(app_url):
    try:
        response = requests.get(app_url)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"An error occurred during the deployment test: {str(e)}")

def test_health_check(app_url):
    try:
        response = requests.get(f"{app_url}/health")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"An error occurred during the health check: {str(e)}")
