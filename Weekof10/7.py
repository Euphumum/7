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
