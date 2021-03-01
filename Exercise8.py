formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Sleep in horse barn pony,",
	"Dog starts nap,",
	"Only little Djonny",
	"Don't want to sleep."
))