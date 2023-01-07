from PyEnum import *
from dataclasses import dataclass, field


@dataclass
class TestInfo :
    tester : list[str] = field(default_factory=list)
    site   : list[str] = field(default_factory=list)

    def __post_init__(self) -> None :
        self.tester = ['' for _ in range(len(TESTER))]
        self.site   = ['' for _ in range(len(TESTER))]

if __name__ == '__main__' :
    test_info = TestInfo()