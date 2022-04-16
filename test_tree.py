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
            self.contacts.append(n)
            for i in n.split():
                self.finder = TestCasesFinder()
                self.builder = TestSuiteBuilder()
                self.testsuite = self.builder.build(str(i))
                self.testsuite.visit(self.finder)
                self.testname = self.finder.tests
                for d in self.testname:
                    print(n,d)
                    #return n,d
            
            
d = TestCasesFinder()
d.get_all_files()
        
