def assert_status_code(response, expected_code=200):
    assert response.status_code == expected_code