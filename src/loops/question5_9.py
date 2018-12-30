import sys
import math

initial_character = ord(input('Enter starting character:'))
end_character = ord(input('Enter ending character:'))

if (not(initial_character >= ord('A') and initial_character <= ord('Z'))) or (not(end_character >= ord('A') and end_character <= ord('Z'))):
    print('Invalid Character [A~Z]')
    sys.exit()

character_slab = ''

step = 1 if end_character >= initial_character else -1 #int(math.copysign(1, end_character - initial_character))
for i in range(0, end_character - initial_character + step, step):
    character_slab += chr(initial_character + i) + ' '

#i = 0
#while (initial_character + i <= end_character) or (initial_character - i >= end_character):
#    
#    if initial_character == end_character:
#        character_slab = chr(initial_character)
#        break
#    
#    if initial_character <= end_character:
#        character_slab += chr(initial_character + i) + ' '
#        i += 1
#    
#    else:
#        character_slab += chr(initial_character - i) + ' '
#        i += 1
#

for j in range(0, abs(initial_character - end_character) + 1):
    print(character_slab)

