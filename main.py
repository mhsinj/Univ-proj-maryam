import itertools
import math
#test for commit
#main file of project
######################
#Part number one for moneer - banner and inputs to ask user what type of list number,numbers with letters , num,letters, special characters 




##################################
#part number 2 for yousef - function if it  is just numbers








######################################
#Part 3 for najeeb-  function of numbers with letters







######################################
#Part 4 (me)- function of numbers with letters with special characters 







######################################
#Part 5 for haroon- function to save the output to file 









######################################
#Part 6 (me)- Create Random listwith letters numbers and special characters #











#########################################
#part 7 (me)- feauter of pdf
def mix():
    names = input("Enter names => ").split(",")
    years = input("Enter years => ").split(",")

    names = [n.strip().lower() for n in names if n.strip()]
    years = [y.strip() for y in years if y.strip()]
    symbols = [ "_", "", "@"]
    templates = [
        "{name}{year}",
        "{name}_{year}",
        "{name}{symbol}{year}"
    ]

    leet = {
        "a": ["a", "@"],
        "e": ["e", "3"],
        "i": ["i", "1"],
        "o": ["o", "0"],
        "s": ["s", "$"],
    }

    max_words = 10000
    max_length = 14
    min_entropy = 2.5


######################################
#Part 8-  Main function  

def main():
    print("main function...")


main()