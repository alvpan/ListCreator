import pprint
from itertools import combinations, permutations
import math
from tqdm import tqdm

print("Welcome to ListCreator!\n")
mode = input("Please choose a mode (c=custom/b=basic): ")

def CreateTxt(permutations_list):
    file_name = input("Save .txt file as: ")
    file_path = input("Choose file path: ")
    file = open(''f'{file_path}/'f'{file_name}.txt','w')
    for c in permutations_list:
        file.write(c+"\n")
    file.close()
    print("File ", file_name, ".txt was saved at: ", file_path)

#Basic
if(mode=='b'):
    basic_list = ['Target', 'Partner', 'Father', 'Mother', 'Child']
    BigList = []
    answer = 'y'
    for i in range(len(basic_list)):
        name=surname=middle=alias=birth=day=month=year=pet=0
        if(i>0):
            print("Add",basic_list[i],"creds (y/n)?: ", end="")
            answer = input()
        if(answer=='y' or i==0):
            print(basic_list[i],"Name: ", end="")
            name = input()
            print(basic_list[i], "Surname: ", end="")
            surname = input()
            print(basic_list[i], "Middle Name: ", end="")
            middle = input()
            print(basic_list[i], "Alias: ", end="")
            alias = input()
            print(basic_list[i], "Pet: ", end="")
            pet = input()
            print(basic_list[i], "Birth Date (DDMMYYYY): ", end="")
            birth = input()
            if(birth!=0):
                day = int(str(birth)[:2])
                month = int(str(birth)[2:4])
                year = int(str(birth)[4:])
            BigList.extend((name, surname, middle, alias, pet, birth, day, month, year))

    #delete empty space
    BigList = [i for i in BigList if(i != 0)]
    for i in range(len(BigList)):
        BigList[i] = str(BigList[i])
    BigList = list(dict.fromkeys(BigList))

    #lowercase
    Lower = [' 'for i in range(len(BigList))]
    for i in range(len(BigList)):
        Lower[i] = BigList[i].lower()

    #all lists together
    ListsCombined = Lower + BigList
    UniqueList = list(dict.fromkeys(ListsCombined))

    #permutations
    permutations2 = ["".join(a) for a in permutations(UniqueList, 2)]
    permutations3 = ["".join(a) for a in permutations(UniqueList, 3)]
    permutations4 = ["".join(a) for a in permutations(UniqueList, 4)]
    permutations = permutations2 + permutations3 + permutations4
    permutations = list(dict.fromkeys(permutations))
    final = []
    permutations = [file for file in permutations if len(set(file)) >= 8]
    for i in range(len(permutations)):
        if(len(permutations[i])<=14):final.append(permutations[i])       
    permutations = final
    print(len(permutations), " Strings Created.")
    CreateTxt(permutations)


#Custom
def CollectCredentials():
    add = 'y'
    counter = 0
    custom_names = []
    custom_surnames = []
    custom_middles = []
    custom_aliases = []
    custom_births = []
    date_lists = []
    while(add=='y'):
        title = input("\nTitle (optional): ")
        print("--- Subject",counter,title,"---")
        n = input("Name: ")
        custom_names.append(n)
        s = input("Surname: ")
        custom_surnames.append(s)
        m = input("Middle Name: ")
        custom_middles.append(m)
        a = input("Alias: ")
        custom_aliases.append(a)
        b = input("Birth Date (DDMMYYYY): ")
        custom_births.append(b)
        if(b!=0):
            day = int(str(b)[:2])
            month = int(str(b)[2:4])
            year = int(str(b)[4:])
            date_lists.extend((day, month, year))
        add = input("\nAdd another Subject (y/n)?: ")
        if(add=='y'):
            counter+=1
    BigList = custom_names + custom_surnames + custom_middles + custom_aliases + custom_births + date_lists
    BigList = [i for i in BigList if(i != '')]
    BigList = list(map(str, BigList))
    return(BigList)

def GetStarters(BigList):
    StartersList = [' 'for i in range(len(BigList))]
    starters = input("Use Starting Letters (y/n)?: ")
    if(starters=='y'):
        for i in range(len(BigList)):
            StartersList[i] = BigList[i][0:1]
    return(StartersList)

def LowerCase(BigList):
    Lower = [' 'for i in range(len(BigList))]
    lower = input("UPPER CASE + lower case (y/n)?: ")
    if(lower=='y'):
        for i in range(0,len(BigList)):
            Lower[i] = BigList[i].lower()
    return(Lower)

def Reverse(BigList):
    ReverseBigList = [' 'for i in range(len(BigList))]
    reverse = input("Use String Reversal(=lasreveR) (y/n)?: ")
    if(reverse=='y'):
        for i in range(len(BigList)):
            ReverseBigList[i] = BigList[i][::-1]
    return(ReverseBigList)

def Permutate(UniqueList):
    unique_strings = len(UniqueList)
    repeat = 'y'
    max_perms = 2
    permutations_list = []
    while(repeat=='y'):
        max_perms = int(input("Max Permutation Size (2-4 recommended): "))
        num_of_perms = 0
        for i in range(2,max_perms):
            num_of_perms += int((math.factorial(unique_strings))/math.factorial(unique_strings-i)) 
        print("\n!!!WARNING!!!: This will produce --->",num_of_perms,"<--- permutations!") 
        #choose x individual SMALLEST strings, combine them and show the length in chars.
        UniqueList.sort(key=len)
        min_string_list = UniqueList[:max_perms]
        min_string_length = len(''.join(min_string_list))
        print("MIN string length is: ",min_string_length," characters long.")
        #choose x individual BIGGEST strings, combine them and show the length in chars.
        UniqueList.sort(reverse=True, key=len)
        max_string_list = UniqueList[:max_perms]
        max_string_length = len(''.join(max_string_list))
        print("MAX string length is: ",max_string_length," characters long.")
        repeat = input("Change permutation Size (y/n)?:")
    for i in tqdm(range(0,max_perms), total=max_perms, desc="Generating Permutations..."):
        permutations_list+=["".join(a) for a in permutations(UniqueList, i)]
    return(permutations_list)

def ResizeListContents(permutations_list):
    minimum = int(input("Minimum String Length: "))
    maximum = int(input("Maximum String Length: "))
    #set mimimum
    permutations_list = [file for file in permutations_list if len(set(file)) >= minimum]
    #set maximum
    final = []
    for i in range(len(permutations_list)):
        if(len(permutations_list[i]) <= maximum):final.append(permutations_list[i])       
    print()
    print("AFTER FILTERS: ",len(permutations_list), " Strings Created.")
    return(final)

if(mode=='c'):

    ListsCombined = CollectCredentials()
    ListsCombined += GetStarters(ListsCombined)
    ListsCombined += LowerCase(ListsCombined) 
    ListsCombined += Reverse(ListsCombined)

    UniqueList = list(dict.fromkeys(ListsCombined))
    UniqueList = [i for i in UniqueList if(i != ' ')]
    unique_strings = len(UniqueList)
    print(unique_strings," Unique Strings.")

    permutations_list = Permutate(UniqueList)
    permutations_list = ResizeListContents(permutations_list)
    CreateTxt(permutations_list)


#comments and tidy up 
#add (syllables maybe in custom mode)
#break up working blocks in different files

