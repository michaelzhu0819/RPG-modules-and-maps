# the function that generates the map
def Map():
    Map = [["end", "enemy", "enemy", "key"],
           ["supply", "nothing", "nothing", "enemy"],
           ["nothing", "start", "supply", "nothing"],
           ["nothing", "supply", "nothing", "enemy"]]

    print("\n*---------------------------------------*")
    for i in Map:
        print("|", end=" ")
        for j in i:
            print(j, end="")
            for k in range(8-len(j)):
                print(" ", end="")
            print("|", end=" ")
        print("\n*---------------------------------------*")
