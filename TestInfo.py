from PyEnum import *
from dataclasses import dataclass, field


@dataclass
class TestInfo :
    tester : list[str] = field(default_factory=list)
    site   : list[str] = field(default_factory=list)

    def __post_init__(self) -> None :
        cls = type(self)
        if not hasattr(cls, "_post_init") :
            
            self.tester = ['' for _ in range(len(TESTER))]
            self.site   = ['' for _ in range(len(TESTER))]
            
            cls._post_init = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__' :
    test_info = TestInfo()
    test_info2 = TestInfo()
