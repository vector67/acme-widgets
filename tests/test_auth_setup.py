import unittest

from e2e.auth_setup import log_in


class FakeField:
    def __init__(self) -> None:
        self.text = ""

    def fill(self, text: str) -> None:
        self.text += text

    def clear(self) -> None:
        self.text = ""


class FakePage:
    def __init__(self, fails: int) -> None:
        self.username = FakeField()
        self.password = FakeField()
        self.fails = fails

    def submit(self) -> bool:
        if self.fails:
            self.fails -= 1
            self.username.clear()
            return False
        return self.password.text == "s3cret"


class LogInTest(unittest.TestCase):
    def test_clears_the_password_before_trying_again(self) -> None:
        self.assertTrue(log_in(FakePage(fails=1), "octocat", "s3cret"))
