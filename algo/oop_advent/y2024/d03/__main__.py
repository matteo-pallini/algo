import copy
import functools
from dataclasses import dataclass, field
from typing import Optional, Callable


@dataclass
class ItemOperation:
    value: Optional[int] = None
    _partial_item: str = ""

    def add(self, value: str) -> bool:
        try:
            int(value)
            if len(self._partial_item) < 3:
                self._partial_item += value
                self.value = int(self._partial_item)
                return True
            else:
                return False
        except ValueError:
            return False

    @property
    def complete(self):
        return len(self._partial_item) == 3


@dataclass
class TwoItemsOperation:
    item1: Optional[ItemOperation] = None
    item2: Optional[ItemOperation] = None

    @property
    def complete(self):
        return self.item1 is not None and self.item2 is not None

    def add_item(self, item) -> bool:
        if self.item1 is None:
            self.item1 = item
        elif self.item2 is None:
            self.item2 = item
        else:
            return self.complete
        return self.complete


@dataclass
class FullProgramRunner:
    program: str
    prefilters: list[Callable[[str], str]] = field(default_factory=lambda: [])

    def find_all_instances_of(self, operation: str) -> list[TwoItemsOperation]:
        instances = []
        program = copy.copy(self.program)
        for p in self.prefilters:
            program = p(program)
        print(program)
        while program.find(operation) >= 0:
            idx = program.find(operation)
            program = program[idx+len(operation):]
            two_items_operation = TwoItemsOperation()
            item = ItemOperation()
            while program:
                next_ch, program = program[0], program[1:]
                if next_ch == "(" and item.value is None and two_items_operation.item1 is None:
                    continue
                elif not item.complete and item.add(next_ch):
                    continue
                elif next_ch == "," and item.value is not None and not two_items_operation.complete:
                    two_items_operation.add_item(item)
                    item = ItemOperation()
                elif next_ch == ")" and item.value is not None and not two_items_operation.complete and two_items_operation.item1 is not None:
                    two_items_operation.add_item(item)
                    instances.append(two_items_operation)
                    break
                else:
                    break
        return instances


def filter_out(program: str, switch_on: str, switch_off: str) -> str:
    on = True
    filtered_program = ""
    while program:
        if on:
            idx = program.find(switch_off)
            if idx == -1:
                return filtered_program + program
            filtered_program += program[:idx]
            program = program[idx+len(switch_off):]
            on = False
        else:
            idx = program.find(switch_on)
            if idx == -1:
                return filtered_program
            program = program[idx + len(switch_on):]
            on = True
    return filtered_program




if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        full_program = "".join(handle.readlines())
        do_dont_prefilter = functools.partial(filter_out, switch_on="do()", switch_off="don't()")
        full_program_runner = FullProgramRunner(program=full_program, prefilters=[do_dont_prefilter])
        ops = full_program_runner.find_all_instances_of("mul")
        final_v = sum([e.item1.value * e.item2.value for e in ops])
        print(final_v)

