##The program will recieve 3 English words inputs from STDIN
##
##These three words will be read one at a time, in three separate line
##The first word should be changed like all vowels should be replaced by *
##The second word should be changed like all consonants should be replaced by @
##The third word should be changed like all char should be converted to upper case
##Then concatenate the three words and print them
##Other than these concatenated word, no other characters/string should or message should be written to STDOUT
##
##For example if you print how are you then output should be h*wa@eYOU.
##
##You can assume that input of each word will not exceed more than 5 chars


a = str(input())
b = str(input())
c = str(input())

v = ['a','e','i','o','u']
con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in a:
    if i in v:
        x = a.replace(i,'*')
for i in b:
    if i in con:
        y = b.replace(i,'@')
    else:
        y = b
z = c.upper()

print(x+y+z)

