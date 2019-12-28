by. korea1782
```python
#function
def grade(average):
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def printFrame():
    print(" Student            Name    Midterm   Final   Average   Grade")
    print("-------------------------------------------------------------------")

def printendFrame():
    print("-------------------------------------------------------------------")
    print("Enter: show, search, search(name,grade), change(score,name), add, remove, quit ")

def show():
    member.sort(key=lambda x: x[4], reverse=True)
    printFrame()
    for i in member:
        print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
    printendFrame()

def search():
    searchId = int(input("Student ID: "))
    temp = []
    for i in member:
        if searchId == i[0]:
            data = "%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5])
            temp.append(data)
            break
    if len(temp) != 0:
        printFrame()
        print(data)
        printendFrame()
    else:
        print("NO SUCH PERSON.")

def searchname():
    searchName = input("Student Name: ").replace(" ", "").lower()
    temp = []
    for i in member:
        if searchName == i[1].replace(" ","").lower():
            data = "%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5])
            temp.append(data)
    if len(temp) != 0:
        printFrame()
        for i in range(len(temp)):
            print(temp[i])
        printendFrame()
    else:
        print("NO SUCH PERSON.")

def changescore():
    search = int(input("Student ID: "))
    temp = False
    for i in member:
        if search == i[0]:
            temp = True
            score = input("Mid/Final? ").lower()
            if score == 'mid':
                mscore = int(input("Input new score: "))
                if mscore < 0 or mscore > 100:
                    print("잘못 입력하셨습니다.")
                    break
                else:
                    printFrame()
                    print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                    print("Score changed.")
                    i[2] = mscore
                    changeAve = float((i[2] + i[3]) / 2)
                    i[4] = changeAve
                    i[5] = grade(changeAve)
                    print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                    printendFrame()
                    break
            elif score == 'final':
                fscore = int(input("Input new score: "))
                if fscore < 0 or fscore > 100:
                    print("잘못 입력하셨습니다.")
                    break
                else:
                    printFrame()
                    print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                    print("Score changed.")
                    i[3] = fscore
                    changeAve = float((i[2] + i[3]) / 2)
                    i[4] = changeAve
                    i[5] = grade(changeAve)
                    print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                    printendFrame()
                    break
            else:
                print("잘못 입력하셨습니다.")
                break
    if temp == False:
        print("NO SUCH PERSON.")

def changename():
    changeName = input("Student ID or Name: ")
    temp = False
    if changeName.isdigit() == True:
        changeName = int(changeName)
        for i in member:
            if changeName == i[0]:
                temp = True
                name = input("Input new name: ")
                printFrame()
                print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                print("Name changed.")
                i[1] = name
                print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                printendFrame()
                break
    else:
        changeName = changeName.replace(" ","").lower()
        for i in member:
            if changeName == i[1].replace(" ","").lower():
                temp = True
                name = input("Input new name: ")
                printFrame()
                print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                print("Name changed.")
                i[1] = name
                print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                printendFrame()
                break
    if temp == False:
        print("NO SUCH PERSON.")

def add():
    addId = int(input("Student ID: "))
    temp = True
    for i in member:
        if addId == i[0]:
            temp = False
            print("ALREADY EXISTS.")
            break
    if temp == True:
        addName = input("Name: ")
        addMid = int(input("Midterm Score: "))
        while True:
            if addMid < 0 or addMid > 100:
                print("다시 입력하세요.")
                continue
        addFin = int(input("Final Score: "))
        while True:
            if addFin < 0 or addFin > 100:
                print("다시 입력하세요.")
                continue
        print("Student added.")
        addAverage = float((addMid + addFin) / 2)
        member.append([addId, addName, addMid, addFin, addAverage, grade(addAverage)])

def searchgrade():
    searchgrade = input("Grade to search: ").upper()
    tempSearch = []
    for i in member:
        if searchgrade == 'A' or searchgrade == 'B' or searchgrade == 'C' or searchgrade == 'D' or searchgrade == 'F':
            if searchgrade == i[5]:
                tempSearch.append(i)
        else:
            print("잘못 입력하셨습니다.")
            break
    if len(tempSearch) != 0:
        printFrame()
        for i in tempSearch:
            print("%8d %15s %8d %8d %8.1f %6s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
        printendFrame()
    else:
        print("NO RESULTS.")

def remove():
    temp = False
    if len(member) != 0:
        removeId = int(input("StudentID: "))
        for i in range(len(member)):
            if removeId == member[i][0]:
                del member[i]
                print("Student removed.")
                temp = True
                break
        if temp == False:
            print("NO SUCH PERSON.")
    else:
        print("List is empty.")

def quit():
    saveData = input("Save data?[yes/no] ").lower()
    temp = False
    if saveData == 'yes':
        member.sort(key=lambda x: x[4], reverse=True)
        fw = open(input("File name: "), "w")
        for i in member:
            data = "%d\t%s\t%d\t%d\n" % (i[0], i[1], i[2], i[3])
            fw.write(data)
        fw.close()
        temp = True
    elif saveData == 'no':
        temp = True
    else:
        print("잘못 입력하셨습니다.")
    return temp

# Main
fr =open("students.txt", "r")
a = fr.readlines()
member = []
for i in a:
    temp = i.split('\t')
    temp[0], temp[2], temp[3] = int(temp[0]), int(temp[2]), int(temp[3].strip())
    average = float((temp[2]+temp[3])/2)
    temp.append(average)
    temp.append(grade(average))
    member.append(temp)
show()

while True:
    cmd = input("# ").replace(" ", "").lower()
    if cmd == "show":
        show()
    elif cmd == "search":
        search()
    elif cmd == "searchname":
        searchname()
    elif cmd == "changescore":
        changescore()
    elif cmd == "changename":
        changename()
    elif cmd == "add":
        add()
    elif cmd == "searchgrade":
        searchgrade()
    elif cmd == "remove":
        remove()
    elif cmd == "quit":
        temp = quit()
        if temp == True:
            fr.close()
            break
    else:
        continue
```
