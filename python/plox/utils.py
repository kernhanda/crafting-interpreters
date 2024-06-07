class LoxError(Exception):
    def __init__(self) -> None:
        super().__init__()


def error(line: int, message: str):
    report(line, "", message)


def report(line: int, where: str, message: str):
    print(f"[line {line}] Error {where}: {message}")
