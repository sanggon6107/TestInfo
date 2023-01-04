from enum import auto, IntEnum


class EnumFromZero(IntEnum) :
    def _generate_next_value_(name, start, count, last_values) :
        return count

    def __str__(self) :
        return self.name

    def __repr__(self) :
        return self.name

class TESTER(EnumFromZero) :
    TESTER1 = auto()
    TESTER2 = auto()
    TESTER3 = auto()


if __name__ == '__main__' :
    print([str(i) for i in TESTER])
    print(TESTER.TESTER1 == 0)
    print(TESTER.TESTER2 == 1)
    print(TESTER.TESTER3 == 2)