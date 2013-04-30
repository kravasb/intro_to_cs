#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(number):
    x=1000000000
    tmp=number
    while x>=10:
        if int(tmp/x)>0:
            boo=int(tmp/x)
            print(get_line(boo))
            tmp=tmp-(x*boo)
            x=x/10

        else:
            print(get_line(0))
            x=x/10
    print(get_line(tmp))

def get_line(number):
    length=10
    result="|"
    i=0
    while i!=length:
        if i==(length-number):
            result=result+"   "
        if i<5:
            result=result+"0"
            i=i+1
        else:
            result=result+"*"
            i=i+1

    if len(result)<14:
        result=result+"   "
    result=result+"|"

    return result

print_abacus(555)

