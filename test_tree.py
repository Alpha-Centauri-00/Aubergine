from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
import glob


class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)
    
    
    def get_all_files(self):
        self.files = glob.glob("*.robot")
        self.contacts = []
        for n in self.files:
            self.contacts = []
            #print(contacts.append((f'{n}')))
            #print(n)
            self.contacts.append(n)
            print(self.contacts)
        
        
finder = TestCasesFinder()
builder = TestSuiteBuilder()
listy = finder.get_all_files()


testsuite = builder.build("01_robot-file.robot")
testsuite.visit(finder)

#testy = TestCasesFinder
#testy.get_all_files()
print(*finder.tests)    


# for x in all_names:
    
    
#     builder = TestSuiteBuilder()
    
#     testsuite = builder.build(x)
#     testsuite.visit(finder)

# #testy = TestCasesFinder
# #testy.get_all_files()
#     print(*finder.tests)