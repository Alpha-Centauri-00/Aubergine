from lib2to3.pgen2.token import LEFTSHIFT
from robot.running import TestSuiteBuilder
from robot.model import SuiteVisitor
from tkinter import LEFT, TOP, tix as Tix
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
        self.cl.pack(side=LEFT,ipadx=100,ipady=75)
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.setstatus("CL1", "off")

        builder = TestSuiteBuilder()
        all_test_suites = TestCasesFinder.all_robot_files()
        
        for test_suite in all_test_suites:
            Test_case = builder.build(test_suite)
            finder = TestCasesFinder()
            Test_case.visit(finder)
            self.cl.hlist.add(f"CL1.({Test_case})", text=Test_case)
            self.cl.setstatus(f"CL1.({Test_case})", "off")
            for x in finder.tests:
                self.cl.hlist.add(f"CL1.({Test_case}).{x}", text=x)
                self.cl.setstatus(f"CL1.({Test_case}).{x}", "off")
         
        
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