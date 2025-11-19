thonfrom src.automation.validator import validate_email

def test_validate_email():
 assert validate_email("test@example.com") is True
 assert validate_email("bad-email") is False