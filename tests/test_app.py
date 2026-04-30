from app import create_app


def test_health_endpoint_returns_ok() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_intentional_break_flag() -> None:
    # Set BREAK_TEST=true in the workflow dispatch input to force a failure.
    import os

    should_break = os.getenv("BREAK_TEST", "false").lower() == "true"
    assert not should_break, "Intentional failure: BREAK_TEST=true"
