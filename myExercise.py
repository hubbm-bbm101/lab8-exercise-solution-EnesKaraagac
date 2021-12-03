import sys
with open(sys.argv[1]) as data:
    data_dict, data_List = {}, [x.split(":") for x in data.read().splitlines()]
    for archive in data_List:
        data_dict[archive[0]] = str(archive[1])
    for inpt in sys.argv[2].split(","):
        try:
            print(f"Name: {inpt}, University: {data_dict[inpt]}")
        except:
            print(f"No record '{inpt}' was found")





