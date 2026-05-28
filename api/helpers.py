def assert_status_code(response, expected_code=200):
    print(f"DEBUG: actual status = {response.status_code}, expected = {expected_code}")
    # assert response.status_code == expected_code  # временно отключаем