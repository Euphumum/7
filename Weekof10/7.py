# Stating who knows binary and who doesn't
x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s," % (binary, doNot)

print(x)
print(y)

print("I said: %r " % x)
print("I also said: '%s'," % y)
# stating whether or  ot the joke was funny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
# There is two strings creating one whole line when they are added together.
w = "This is the left side of ..."
e = "a string with a right side"

print(w + e)

# More stuff 10-8

print("Mary had a little lamb")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4,))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why did I use %r instead of %s?
# We have been using %r instead of %s because that's what we used our code with.

# Time for some strange stuff in the world of printing...

days ="Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMarch\nApril\nMay\nJune\nJuly\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# What if I didn't like Jan being listed on the line with the rest of the
# text and away from the months? How could I fix that.

# More escaping

tabbycat = "\tI'm tabbed in."
persiancat = "I'm split\non time."
backlashcat = "I'm \\ a \\ cat."
taskcat = """
I'll make a list:
\t*Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabbycat)
print(persiancat)
print(backlashcat)
print(taskcat)

# Escape seq          What does it do

# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N(name)
# \r
# \t
# \uxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh

# It allows for coding of multiple lines and tasks in one set of code,


# What's the following do:
# while True:
#      for i in(("/","-","|","\\","|")
#      print(%s\r" %i,end ='')

# Can you replace *** with '''?\

# Asking questions

age = input("How old are you?")
height = input("How tall are you ?")

print("So, you really $r old and %r tall? Wow..." % (age,height))






















