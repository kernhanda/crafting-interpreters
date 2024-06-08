class LoxError(Exception):
    def __init__(self, line: int, err: str) -> None:
        super().__init__()
        self.line = line
        self.err = err

    def __str__(self) -> str:
        return f"Error at line {self.line}: {self.err}"


def error(line: int, message: str):
    report(line, "", message)


def report(line: int, where: str, message: str):
    print(f"[line {line}] Error {where}: {message}")
