from abc import ABC, abstractmethod
from typing import Any
stream: list[Any] = ['Hello world',
                     [3.14, -1, 2.71],
                     [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
                     42,
                     ['High', 'five']]
stream1: list[Any] = ['Hello world',
                     [3.14, -1, 2.71],
                     [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
                     42,
                     ['High', 'five']]

class DataProcessor(ABC):
    def __init__(self):
        self.data: list[Any] = []
        self.index = 0

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
            self.data.extend(data)
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


class Datastream:
    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for value in stream:
            for processor in self.processors:
                if processor.validate(value):
                    processor.ingest(value)
                    stream.remove(value)
        for lasting_value in stream:
            print(f"DataStream error - Can't process element in stream: {lasting_value}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processors found, no data")
            return
        for processor in self.processors:
            if type(processor) is NumericProcessor:
                print(f"Numeric Processor: total {len(processor.data)}", end="")
                print(f" items processed, remaining {len(stream)} on processor")
            if type(processor) is TextProcessor:
                print(f"Text Processor: total {len(processor.data)}", end="")
                print(f" items processed, remaining {len(stream)} on processor")
            if type(processor) is LogProcessor:
                print(f"Log Processor: total {len(processor.data)}", end="")
                print(f" items processed, remaining {len(stream)} on processor")


def third_test() -> None:
    third_stream = Datastream()
    print("Registering Others Processors")
    print("")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    third_stream.register_processor(num_proc)
    third_stream.register_processor(text_proc)
    third_stream.register_processor(log_proc)
    print("Send the same batch again")
    third_stream.process_stream(stream1)
    third_stream.print_processors_stats()


def second_test() -> None:
    second_stream = Datastream()
    print("Registering Numeric Processor")
    print("")
    nume_proc = NumericProcessor()
    second_stream.register_processor(nume_proc)
    print(f"Send first batch of data on stream: {stream}")
    second_stream.process_stream(stream)
    second_stream.print_processors_stats()


def first_test() -> None:
    first_stream = Datastream()
    first_stream.print_processors_stats()


def manage_data_stream() -> None:
    first_test()
    print("")
    second_test()
    print("")
    third_test()


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("")
    print("Initialize Data Stream...")
    manage_data_stream()


if __name__ == "__main__":
    main()
