from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
from tkinter import tix as Tix
import glob

class TestCasesFinder(SuiteVisitor):
    def __init__(self):
        self.tests = []

    def visit_test(self, test):
        self.tests.append(test)

    def all_robot_files():
        files = glob.glob("*.robot")
        contacts = []
        for n in files:
            contacts.append((f'{n}'))
        return contacts

# builder = TestSuiteBuilder()
# all_test_suites = TestCasesFinder.all_robot_files()
# #print(all_test_suites)
# for test_suite in all_test_suites:
#     testsuite = builder.build(test_suite)
#     finder = TestCasesFinder()
#     testsuite.visit(finder)

#     print(type(finder.tests))


class View(object):
    def __init__(self, root):
        self.root = root
        self.makeCheckList()

    def get_test_suites():
        files = glob.glob("*.robot")
        contacts = []
        for n in files:
            contacts.append((f'{n}'))
        #return contacts
        
        contacts[:] = [s.replace('.robot', ' ') for s in contacts]
        return contacts
    
    

    def makeCheckList(self):
        self.cl = Tix.CheckList(self.root, browsecmd=self.selectItem)
        self.cl.pack()
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.setstatus("CL1", "off")
        
        name = View.get_test_suites()
        builder = TestSuiteBuilder()
        all_test_suites = TestCasesFinder.all_robot_files()
        #print(all_test_suites)
        for test_suite in all_test_suites:
            testsuite = builder.build(test_suite)
            finder = TestCasesFinder()
            testsuite.visit(finder)

            print(finder.tests)
        for test_suits in name:
            self.cl.hlist.add(f"CL1.({test_suits})", text=test_suits)
            self.cl.setstatus(f"CL1.({test_suits})", "off")
            for x in finder.tests:
                self.cl.hlist.add(f"CL1.({test_suits}).{x}", text=x)
                self.cl.setstatus(f"CL1.({test_suits}).{x}", "off")

        
        #self.cl.hlist.add("CL1.item2", text=View.get_test_suites())
        #self.cl.setstatus("CL1.item2", "off")
            
        
        self.cl.autosetmode()

    def selectItem(self, item):
        print(item, self.cl.getstatus(item))
        


def main():
    root = Tix.Tk()
    view = View(root)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    main()