#!/usr/bin/python3.4
#HW1Q2
#Olympic Figure Skating score calculator
#Python 3.4

short_program=[21,32,28,24,29]
free_skating=[24,28,19,23,24]

print("Short program scores: ", short_program)
print("Free skating scores: ", free_skating)
# The spread of scores for a component is given by: (max - min)/(average of remaining scores)

ssorted=(sorted(short_program))
fsorted=(sorted(free_skating))

def spread(program):
    max_val=program[-1]
    min_val=program[0]
    program.pop(0)
    program.pop(-1)
    print("Total score for the program is", sum(program))
    sumdiv = len(program)
    maxx = sum(program)
    avgg=maxx/sumdiv
    spreadd= (max_val-min_val)/avgg
    return spreadd

#Spread of the short program is 0.407407407407
#Spread of the free skating is 0.38028169014

print("The spread of the short program is",spread(ssorted))
print("The spread of the free skating is", spread(fsorted))
print("The total score for the competitor", (spread(fsorted)+spread(ssorted)))

"""
Short program scores 21 32 28 24 29
Free skating scores 24 28 19 23 24
Spread of the short program is 0.407407407407
Spread of the free skating is 0.380281690141
Total score for the short program is 81
Total score for the free skating is 71
The total score for the competitor is 152
"""
