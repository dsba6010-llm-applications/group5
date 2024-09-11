import requests
import pytest

@pytest.fixture
def app_url():
    # Replace with the actual URL of your deployed app
    return "https://lasyaed--vllm-openai-compatible-serve.modal.run"

def test_app_status(app_url):
    try:
        response = requests.get(f"{app_url}/docs")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"An error occurred during the deployment test: {str(e)}")

def test_health_check(app_url):
    try:
        response = requests.get(f"{app_url}/health")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    except requests.RequestException as e:
        pytest.fail(f"An error occurred during the health check: {str(e)}")

def test_version_endpoint(app_url):
    try:
        response = requests.get(f"{app_url}/version")
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        
        version_info = response.json()
        assert "version" in version_info, "Response should contain 'version' key"
        assert version_info["version"] == "0.4.1", f"Expected version '0.4.1' but got {version_info['version']}"
    except requests.RequestException as e:
        pytest.fail(f"An error occurred during the version endpoint test: {str(e)}")
