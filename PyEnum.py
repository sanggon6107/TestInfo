from enum import auto, IntEnum


class TESTER(IntEnum) :
    def _generate_next_value_(name, start, count, last_values) :
        return count

    def __str__(self) :
        return self.name

    def __repr__(self) :
        return self.name

    TESTER1 = auto()
    TESTER2 = auto()
    TESTER3 = auto()
    
if __name__ == '__main__' :
    print(TESTER.TESTER1 < TESTER.TESTER2)