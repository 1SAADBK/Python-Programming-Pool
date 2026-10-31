from typing import Any, Protocol
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
                if not isinstance(item, dict):
                    return False
                else:
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVexport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        line = ",".join(item[1] for item in data)
        print(line)


class JSONexport():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        parts = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("{" + ", ".join(parts) + "}")


class DataStream():
    def __init__(self) -> None:
        self.regi_proc: list = []
        self.process_stats: dict = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.regi_proc.append(proc)
        self.process_stats[type(proc).__name__] = 0

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            ingested = 0
            for proc in self.regi_proc:
                if proc.validate(item):
                    proc.ingest(item)
                    if isinstance(item, list):
                        self.process_stats[type(proc).__name__] += len(item)
                    else:
                        self.process_stats[type(proc).__name__] += 1
                    ingested = 1
                    break
            if not ingested:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.regi_proc) == 0:
            print("No processor found, no data")
        else:
            for proc in self.regi_proc:
                proc_type = type(proc).__name__
                display = proc_type.replace("Processor", " Processor")
                total = self.process_stats[proc_type]
                remaining = len(proc._data)
                print(f"{display}: total {total} items processed,"
                      f" remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.regi_proc:
            lst = []
            try:
                for i in range(nb):
                    lst.append(proc.output())
            except IndexError:
                pass
            if lst:
                plugin.process_output(lst)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Processors")
    num_pro = NumericProcessor()
    txt_pro = TextProcessor()
    log_pro = LogProcessor()
    data_stream.register_processor(num_pro)
    data_stream.register_processor(txt_pro)
    data_stream.register_processor(log_pro)
    batch_one = ['Hello world', [3.14, -1, 2.71],
                 [{'log_level': 'WARNING',
                   'log_message': 'Telnet access! Use ssh instead'},
                  {'log_level': 'INFO',
                   'log_message': 'User wil is connected'}],
                 1337,
                 ['Hi', 'five']
                 ]
    print(f"\nSend first batch of data on stream: {batch_one}\n")
    data_stream.process_stream(batch_one)
    data_stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVexport())
    print()
    data_stream.print_processors_stats()
    batch_two = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                 [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                  {'log_level': 'NOTICE',
                   'log_message': 'Certificate expires in 10 days'}],
                 [32, 1337, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data {batch_two}\n")
    data_stream.process_stream(batch_two)
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONexport())
    print()
    data_stream.print_processors_stats()
