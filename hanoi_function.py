#Towers of Hanoi

def hanoi(n, Source, Destination, Temp) :
    """
Move a Tower of n discs of varying sizes
stacked in discreaasing size from bottom to top
at source.
It prints the moves to transfer the tower from
Source to destination
Using Temp
only one disc can be moved at a time taken from the top
At instance, a disc cannot be stacked on top of a disc smaller than it.
"""
    if n == 1 :
        print(f"Move disc {n} from {Source} to {Destination}")
    elif n > 1 :
        hanoi(n-1, Source, Temp, Destination)
        print(f"Move Disc {n} from {Source} to {Destination}")
        hanoi(n-1, Temp, Destination, Source)
    else :
        print("Number of disks must be positive integer")
    #end if
#end def
