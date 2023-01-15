from PyEnum import *
from dataclasses import dataclass, field, fields
import sys
import traceback


@dataclass(frozen=True)
class TestInfo :
    num_site            : list[int]  = field(default_factory=list[int])
    pc                  : list       = field(default_factory=list)
    site                : list       = field(default_factory=list)
    pgm                 : list       = field(default_factory=list)
    additional_cal_site : list       = field(default_factory=list)

    def __post_init__(self) -> None :
        cls = type(self)
        if hasattr(cls, "_post_init") : TestInfo.__ReturnSingletonError()

        for tester in TESTER :
            match (tester) :
                case TESTER.TESTER1 :
                    self.num_site.append(4)
                    self.pc.append(['TESTER1_1','TESTER1_2'])
                    self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4'])
                    self.pgm.append(['PGM1_1', 'PGM1_2', 'PGM1_3', 'PGM1_4'])
                    self.additional_cal_site.append(self.__SetAdditionalCalSite(tester, 'None'))

                case TESTER.TESTER2 :
                    self.num_site.append(5)
                    self.pc.append(['TESTER2_1','TESTER2_2', 'TESTER2_3'])
                    self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5'])
                    self.pgm.append(['PGM2_1', 'PGM2_2', 'PGM2_3', 'PGM2_4', 'PGM2_5'])
                    self.additional_cal_site.append(self.__SetAdditionalCalSite(tester, 'All'))

                case TESTER.TESTER3 :
                    self.num_site.append(8)
                    self.pc.append(['TESTER3_1','TESTER3_2', 'TESTER3_3', 'TESTER3_4'])
                    self.site.append(['SITE1', 'SITE2', 'SITE3', 'SITE4', 'SITE5', 'SITE6', 'SITE7', 'SITE8'])
                    self.pgm.append(['PGM3_1', 'PGM3_2', 'PGM3_3', 'PGM3_4', 'PGM3_5', 'PGM3_6', 'PGM3_7', 'PGM3_8'])
                    self.additional_cal_site.append(self.__SetAdditionalCalSite(tester, 0, 1, 5))

        if not self.__CheckDataLen() : self.__ReturnDataLenError()

        cls._post_init = True

    def __new__(cls, *args, **kwargs) :
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __CheckDataLen(self) -> bool :
        len_field = [len(getattr(self, field)) for field in self.__annotations__]

        if len(set(len_field)) != 1 : return False
        if False in [i == len(TESTER) for i in len_field] : return False
        return True
    
    def __SetAdditionalCalSite(self, tester, *argv) -> list :
        if argv == ('None', ) :
            try : return [False for _ in range(len(self.site[tester]))]
            except IndexError : self.__ReturnDataLenError()

        elif argv == ('All', ) :
            try : return [True for _ in range(len(self.site[tester]))]
            except IndexError : self.__ReturnDataLenError()
            
        elif all(isinstance(n, int) for n in argv) :
            try : return [i in argv for i in range(len(self.site[tester]))]
            except IndexError : self.__ReturnDataLenError()
        
        else :
            self.__ReturnArgError()

    def __ReturnDataLenError(self) :
        traceback.print_stack(limit=4)
        return sys.exit("Failed to initialize TestInfo. : The length of the fields in TestInfo doesn't match.")

    def __ReturnArgError(self) :
        traceback.print_stack(limit=4)
        return sys.exit(f"Failed to initialize TestInfo. : \'{sys._getframe(1).f_code.co_name}\' doesn't have appropriate parameters.")

    @classmethod
    def __ReturnSingletonError(cls) :
        traceback.print_stack(limit=4)
        return sys.exit("Failed to initialize Testinfo. : TestInfo re-instantiated")


if __name__ == '__main__' :
    test_info = TestInfo()
    print(test_info.num_site)
    test_info.num_site[TESTER.TESTER1]=100
    print(test_info.num_site)
    print(test_info.additional_cal_site[TESTER.TESTER3])