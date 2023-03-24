import SubModule                                                  #1
from SubModule import testTheModuleCalling                        #2
import SubModule as sub                                           #3
from SubModule import checkNumberIsPosOrNeg as addNameForPrint    #4

testTheModuleCalling("John")                   #2
sub.testTheModuleCalling("Alex")               #3
addNameForPrint()                              #4
SubModule.checkNumberIsPosOrNeg()              #1
print(__name__)

addName=SubModule.testTheModuleCalling
addName("Jasim")