import azure.functions as func
import HttpTrigger1


def test_HttpTrigger1_main():
    mock_request = func.HttpRequest(
        method="GET",
        url="/HttpTrigger1",
        body=bytearray(),
        params={"name": "world"})
    response = HttpTrigger1.main(mock_request)
    assert response.status_code == 200
    assert response.get_body() == b"Hello, world!. This HTTP triggered function executed successfully."
