import typing
import random


def gen_event() -> typing.Generator:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lst: list) -> typing.Generator:
    while len(lst) > 0:
        index = random.randrange(len(lst))
        item = lst.pop(index)
        yield item


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    lst = []
    for i in range(10):
        lst.append(next(stream))
    print(f"Built list of 10 events: {lst}")
    for event in consume_event(lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst}")
