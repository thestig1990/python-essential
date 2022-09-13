
# 1st version
import greetings

greetings.greet("Yevhen")
greetings.greet("Max")
greetings.greet("Kate")

print("#"*22)


# 2nd version
import greetings as g

g.greet("Yevhen")
g.greet("Max")
g.greet("Kate")

print("#"*22)


# 3rd version
from greetings import greet

greet("Yevhen")
greet("Max")
greet("Kate")



