from PyEnum import *
from dataclasses import dataclass, field
import sys


@dataclass(frozen=True)
class TestInfo :
    num_site : list[int] = field(default_factory=list[int])
    pc       : list      = field(default_factory=list)
    site     : list      = field(default_factory=list)
    pgm      : list      = field(default_factory=list)


    def __post_init__(self) -> None :
        cls = type(self)
        if not hasattr(cls, "_post_init") :
            for test in TESTER :
                match (test) :
                    case TESTER.TESTER1 :
                        self.num_site.append(4)
                        self.pc.append(['TESTER1_1','TESTER1_2'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4'])
                        self.pgm.append(['PGM1_1', 'PGM1_2', 'PGM1_3', 'PGM1_4'])
                    
                    case TESTER.TESTER2 :
                        self.num_site.append(5)
                        self.pc.append(['TESTER2_1','TESTER2_2', 'TESTER2_3'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5'])
                        self.pgm.append(['PGM2_1', 'PGM2_2', 'PGM2_3', 'PGM2_4', 'PGM2_5'])

                    case TESTER.TESTER3 :
                        self.num_site.append(8)
                        self.pc.append(['TESTER3_1','TESTER3_2', 'TESTER3_3', 'TESTER3_4'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5', 'SITE6', 'SITE7', 'SITE8'])
                        self.pgm.append(['PGM3_1', 'PGM3_2', 'PGM3_3', 'PGM3_4', 'PGM3_5', 'PGM3_6', 'PGM3_7', 'PGM3_8'])

            if not self.__CheckDataLen() :
                sys.exit("Failed to initialize TestInfo.")

            cls._post_init = True

    def __new__(cls, *args, **kwargs) :
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __CheckDataLen(self) -> bool :
        if not (len(self.num_site) == len(self.pc) == len(self.site) == len(self.pgm)) :
            return False
        return True

if __name__ == '__main__' :
    test_info = TestInfo()
    print(test_info.num_site)
    test_info.num_site[TESTER.TESTER1]=100
    print(test_info.num_site)