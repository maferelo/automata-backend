from app import wikipedia


def test_random_page_uses_given_language(_mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = _mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
