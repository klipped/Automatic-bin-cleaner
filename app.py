# make a project based on deleting files in a recycling bin

# this should be a automation type project

# 1.  make code that finds the recycle bin path
# 2. make code that sense when the bin has reached a certain amount of memory
# 3. make a app that sync buttons of the commands i want made
# 4. make this app runs when the desktop is turned on automatically


from pathlib import Path

def finding_recycle_bin():  
    for p in Path('C:\\Users\\').iterdir():
        if "Recycle Bin" in str(p):
            return p


def get_size(memory):
    return round(int(memory))


