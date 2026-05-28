import allure


def attach_request(method: str, url: str, body: dict = None):
    with allure.step(f"{method} {url}"):
        if body:
            allure.attach(str(body), name="Request Body", attachment_type=allure.attachment_type.JSON)


def attach_response(status_code, body):
    allure.attach(str(status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
    try:
        allure.attach(body, name="Response Body", attachment_type=allure.attachment_type.JSON)
    except:
        allure.attach(str(body), name="Response Body (raw)", attachment_type=allure.attachment_type.TEXT)