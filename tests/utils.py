import re

REGISTRATION_VERIFY_RE = re.compile(
    "https://.*user_id=(?P<user_id>[^&amp;]*).*timestamp=(?P<timestamp>[^&amp]*).*signature=(?P<signature>.*)"
)
