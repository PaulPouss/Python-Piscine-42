from abc import ABC, abstractmethod
from typing import Any
lst_numb: list[Any] = [88, 87, 36, 2, 8]
lst_text: list[Any] = [['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]]


class DataProcessor(ABC):
    def __init__(self):
        self.data: list[Any] = []
        self.index: int = 0

    def output(self) -> tuple[int, str]:
        if self.index < len(self.data):
            self.index += 1
            return (self.index - 1, self.data[self.index - 1])
        else:
            raise IndexError

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if type(data) is list[int] | list[float]:
            for numb in data:
                self.data.append(numb)
        else:
            self.data.append(data)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for value in data:
                if not isinstance(value, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if type(data) is list[str]:
            for ptr in data:
                self.data.append(ptr)
        else:
            self.data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, list):
            for value in data:
                if not isinstance(value, dict):
                    return False
            return True
        return False

    def ingest(self, data: dict[Any, Any] | list[dict[Any, Any]]) -> None:
        if isinstance(data, list):
            self.data.extend(data)
        else:
            self.data.append(data)


def test_numeric() -> None:
    print("Testing Numeric Processor...")
    number_list = NumericProcessor()
    for i in lst_text:
        print(f"Trying to validate input'{i}': ", end="")
        print(number_list.validate(i))
        if number_list.validate(i):
            number_list.ingest(i)
        else:
            print(f"Test invalid ingestion osf string '{i}' ", end="")
            print("without prior validation:")
            print("Got exception: Improper numeric data")
    if number_list.validate(lst_numb):
        number_list.ingest(lst_numb)
    for i in range(len(number_list.data)):
        tpl: tuple[int, str] = number_list.output()
        print(f"Numeric value {tpl[0]}: {tpl[1]}")


def test_log() -> None:
    print("Testing log Processor...")
    log_list = LogProcessor()
    for i in lst_text:
        print(f"Trying to validate input'{i}': ", end="")
        print(log_list.validate(i))
        if log_list.validate(i):
            log_list.ingest(i)
        else:
            print(f"Test invalid ingestion osf string '{i}' ", end="")
            print("without prior validation:")
            print("Got exception: Improper log data")
    for i in range(len(log_list.data)):
        tpl: tuple[int, str] = log_list.output()
        print(f"Text value {tpl[0]}: {tpl[1]}")


def test_text() -> None:
    print("Testing Text Processor...")
    text_list = TextProcessor()
    for i in lst_text:
        print(f"Trying to validate input'{i}': ", end="")
        print(text_list.validate(i))
        if text_list.validate(i):
            text_list.ingest(i)
        else:
            print(f"Test invalid ingestion osf string '{i}' ", end="")
            print("without prior validation:")
            print("Got exception: Improper text data")
    for i in range(len(text_list.data)):
        tpl: tuple[int, str] = text_list.output()
        print(f"Text value {tpl[0]}: {tpl[1]}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    test_numeric()
    test_text()
    test_log()


if __name__ == "__main__":
    main()
