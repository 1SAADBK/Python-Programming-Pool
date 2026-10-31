from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available to output")
        oldest_data = self._data.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, oldest_data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            valid = 1
            for item in data:
                if (not isinstance(item, int | float)
                        or isinstance(item, bool)):
                    valid = 0
            if valid:
                return True
            return False
        elif isinstance(data, int | float) and not isinstance(data, bool):
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, int | float):
            self._data.append(str(data))
        else:
            for item in data:
                self._data.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            valid = 1
            for item in data:
                if not isinstance(item, str):
                    valid = 0
            if valid:
                return True
        if isinstance(data, str):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, str):
            self._data.append(data)
        else:
            for item in data:
                self._data.append(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key in data:
                if not isinstance(key, str) or not isinstance(data[key], str):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                for key in item:
                    if (not isinstance(key, str)
                            or not isinstance(item[key], str)):
                        return False
            return True
        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def log_transform(log_data: dict[str, str]) -> str:
            if "log_level" in log_data and "log_message" in log_data:
                return f"{log_data["log_level"]}: {log_data["log_message"]}"
            return str(log_data)
        if isinstance(data, list):
            for item in data:
                self._data.append(log_transform(item))
        else:
            self._data.append(log_transform(data))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num_processor = NumericProcessor()
    print(f" Trying to validate input '1337': {num_processor.validate(1337)}")
    print(" Trying to validate input 'Hello'"
          f": {num_processor.validate('hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_processor.ingest('foo')
    except Exception as e:
        print(f" Got exception: {e}")
    num_list: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_list}")
    if num_processor.validate(num_list):
        num_processor.ingest(num_list)
    print(" Extracting 3 values...")
    for i in range(3):
        rank, value = num_processor.output()
        print(f" Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    txt = TextProcessor()
    print(f" Trying to validate input '1337': {txt.validate(1337)}")
    txt_list = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {txt_list}")
    print(" Extracting 1 value...")
    txt.ingest(txt_list)
    rank, value = txt.output()
    print(f" Text value {rank}: {value}")
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f" Trying to validate input 'Hello': {log.validate('hello')}")
    dict_list = [{'log_level': 'NOTICE',
                  'log_message': 'Connection to server'},
                 {'log_level': 'ERROR',
                  'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {dict_list}")
    log.ingest(dict_list)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f" Log entry {rank}: {value}")
