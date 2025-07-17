from dataclasses import dataclass
from typing import Optional


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
class FullProgram:
    program: str

    def find_all_instances_of(self, operation: str) -> list[TwoItemsOperation]:
        instances = []
        program = str(self.program)
        while program.find(operation) >= 0:
            idx = program.find(operation)
            program = program[idx+len(operation):]
            two_items_operation = TwoItemsOperation()
            item = ItemOperation()
            while program:
                print(program, item, two_items_operation)
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



if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        full_program = FullProgram(program="".join(handle.readlines()))
        ops = full_program.find_all_instances_of("mul")
        final_v = sum([e.item1.value * e.item2.value for e in ops])
        print(final_v)

