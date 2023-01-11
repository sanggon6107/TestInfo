from PyEnum import *
from dataclasses import dataclass, field


@dataclass
class TestInfo :
    num_site : list[int] = field(default_factory=list[int])
    pc       : list = field(default_factory=list)
    site     : list = field(default_factory=list)
    

    def __post_init__(self) -> None :
        cls = type(self)
        if not hasattr(cls, "_post_init") :
            
            for test in TESTER :
                match (test) :
                    case TESTER.TESTER1 :
                        self.num_site.append(4)
                        self.pc.append(['TESTER1_1','TESTER1_2'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4'])
                    
                    case TESTER.TESTER2 :
                        self.num_site.append(5)
                        self.pc.append(['TESTER2_1','TESTER2_2', 'TESTER2_3'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5'])

                    case TESTER.TESTER3 :
                        self.num_site.append(8)
                        self.pc.append(['TESTER3_1','TESTER3_2', 'TESTER3_3', 'TESTER3_4'])
                        self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5', 'SITE6', 'SITE7', 'SITE8'])

            cls._post_init = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__' :
    test_info = TestInfo()
    test_info2 = TestInfo()
