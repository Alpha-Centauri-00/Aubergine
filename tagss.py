
import glob

tagy_tag = []

def ListToStr_del_Brackets(list1):
    return str(list1).replace('[','').replace(']','')


def opining_robot_files():
    files = glob.glob("*.robot")
    contacts = []
    for n in files:
        contacts.append(n)
        with open(n,"r") as f:
            lines = f.readlines()
            res = []
            for line in lines:
                if "[Tags]" in line:
                    word = line.split()
                    word = list(dict.fromkeys(word))
                    tagy_tag.append(word)
    tagging = ListToStr_del_Brackets(tagy_tag)
    final_result = ','.join(set(tagging.split(',')))
    print(final_result)
    
opining_robot_files()
