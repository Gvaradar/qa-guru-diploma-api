import allure


def attach_request(method: str, url: str, body: dict = None):
    with allure.step(f"{method} {url}"):
        if body:
            allure.attach(str(body), name="Request Body", attachment_type=allure.attachment_type.JSON)


def attach_response(status_code: int, body):
    allure.attach(str(status_code), name="Response Status", attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(body), name="Response Body", attachment_type=allure.attachment_type.JSON)