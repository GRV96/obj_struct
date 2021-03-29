from obj_struct import write_obj_struct


def repr_arg(an_arg):
	if isinstance(an_arg, str):
		return "'" + an_arg + "'"

	return str(an_arg)


class Ajxo: # "thing" in Esperanto
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return self.__class__.__name__ + "(" + repr_arg(self.a) + ", "\
			+ repr_arg(self.b) + ")"


structure = ( # tuple
	Ajxo(None, 2187),
	11,
	{ # set
		"abc",
		7.42,
		( # tuple
			"def",
			66,
			Ajxo(77, 5.6)),
		"xyz"},
	{ # dict
		(Ajxo("g", "h"), "u"): "something",
		"ghi": Ajxo(8, 9),
		},
	Ajxo([3, "p", 2.09], Ajxo("q", 1)),
	[ # list
		63485,
		{ # dict
			4: Ajxo(2, 2),
			Ajxo(19, 23): [ # list
				"i",
				"j",
				"k",
				"l"],
			"fr": "quelque chose"},
		3.4159])

write_obj_struct(structure, "result.txt")
