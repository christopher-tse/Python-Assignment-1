# open files for I/O
inputFile = open("input.txt", "r")
outputFile = open("output.html", "w")

# read in contents as strings each line
contents = inputFile.read().splitlines()

# join whole file to single string with " "
full = " ".join(contents)

# remove empty list items from whitespace
full = list(filter(None, full.split(" ")))

# reverse list to use .pop() later
full.reverse() 

# enable list printing for debug
print(full)

# define student class with input attributes
class Student:
    def __init__(self, ID, firstN, lastN, grade, effort):
        self.ID = ID
        self.firstN = firstN
        self.lastN = lastN
        self.grade = grade
        self.effort = effort

# set flag for ignoring city/state info
isJunk = True

# initialize empty list to place Students in
studentlist = [] 
while full:
    isJunk = True # set junk flag to true to check later
    
    # pop the next five items to create Student
    currID = full.pop()
    currfirstN = full.pop()
    currlastN = full.pop()
    currgrade = int(full.pop())
    curreffort = full.pop()

    # change effort from string to int for easier sorting later
    if curreffort == "L":
        curreffort = 0
    else:
        curreffort = 1

    # create new Student and append into list
    studentlist.append(Student(currID, currfirstN, currlastN, currgrade, curreffort))
    
    # if next item in input is number aka is ID and not city/state set flag to false and loop again
    if full[-1].isdigit():
        isJunk = False

    # if junk flag is true, pop until next item is ID
    while isJunk and full:
        full.pop()
        if full and full[-1].isdigit():
            isJunk = False

# sort student list by grade then effort, then put in descending order
studentlist.sort(key=lambda x: (x.grade, x.effort), reverse=True)


# predefine third and bottom values for cleaner for loops
third = (len(studentlist)//3) # floor(n/3)
bottom = -(-len(studentlist)//10) # ceil(n/10)

# set letter grades according to parameters given
for st in studentlist[0:third]:
    st.letter = "A"

for st in studentlist[third:2*third]:
    st.letter = "B"

for st in studentlist[-bottom:]:
    st.letter = "F"

for st in studentlist:
    
    # check if student has letter, if not set C or D depending on effort
    if not hasattr(st, "letter"):
        if st.effort == 1:
            st.letter = "C"
        else:
            st.letter = "D"

for st in studentlist:
    print(st.ID, st.firstN, st.lastN, st.grade)

# sort list again by last name, first name, and ID as specified in assignment
studentlist.sort(key=lambda x: (x.lastN, x.firstN, x.ID))

# print output to console
for st in studentlist:
    print(st.ID, st.firstN, st.lastN, st.letter)


# start writing HTML boilerplate and minimal styling to table formatting
outputFile.write("<!DOCTYPE html>")
outputFile.write("<html><head><title>Output</title><style>table{border-collapse:collapse} table,td{border:1px solid black; padding:15px; font-size: 16px; }</style></head><body>")
outputFile.write("<table>")

# for each student write the desired output to a column
for s in studentlist:
    outputFile.write("<tr>")
    outputFile.write("<td>" + s.ID  + "</td>")
    outputFile.write("<td>" + s.firstN  + "</td>")
    outputFile.write("<td>" + s.lastN  + "</td>")
    outputFile.write("<td>" + s.letter + "</td>")
    outputFile.write("</tr>") 

outputFile.write("</table></body></html>")

# close I/O
inputFile.close()
outputFile.close()
