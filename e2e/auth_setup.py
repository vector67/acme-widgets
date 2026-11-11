from typing import Protocol


class Field(Protocol):
    def fill(self, text: str) -> None: ...
    def clear(self) -> None: ...


class LoginPage(Protocol):
    username: Field
    password: Field

    def submit(self) -> bool: ...


def log_in(page: LoginPage, username: str, secret: str, attempts: int = 3) -> bool:
    password_input = page.password
    for _ in range(attempts):
        page.username.fill(username)
        password_input.fill(secret)
        if page.submit():
            return True
        password_input.clear()
    return False
