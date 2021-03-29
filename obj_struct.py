_DLST = (dict, list, set, tuple)


_STREAM_WRITING_MODES = ("a", "a+", "r+", "w", "w+")


def _make_tabs(n):
	return "\t" * n


def _obj_and_type_to_str(obj):
	return str(obj) + " " + str(type(obj))


def _obj_is_a_dlst(obj):
	return isinstance(obj, _DLST)


def write_obj_struct(struct, w_stream, write_types=False):

	if w_stream.mode not in _STREAM_WRITING_MODES:
		raise ValueError("The stream's mode must be "
			+ "\"a\", \"a+\", \"r+\", \"w\" or \"w+\".")

	obj_str_fnc = _obj_and_type_to_str if write_types else str

	if _obj_is_a_dlst(struct):
		w_stream.write(str(type(struct)) + "\n")
		indent = 1

	else:
		indent = 0

	_write_obj_struct_rec(struct, w_stream, indent, obj_str_fnc)


def _write_obj_struct_rec(obj_to_write, w_stream, indent, obj_str_fnc):
	tabs = _make_tabs(indent)
	indent += 1

	if isinstance(obj_to_write, (list, tuple)):
		length = len(obj_to_write)

		for i in range(length):
			item = obj_to_write[i]
			line = tabs + "[" + str(i) + "]: "

			if _obj_is_a_dlst(item):
				line += str(type(item))
				w_stream.write(line + "\n")
				_write_obj_struct_rec(item, w_stream, indent, obj_str_fnc)

			else:
				line += obj_str_fnc(item)
				w_stream.write(line + "\n")

	elif isinstance(obj_to_write, dict):
		for key, value in obj_to_write.items():
			line = tabs + str(key) + ": "

			if _obj_is_a_dlst(value):
				line += str(type(value))
				w_stream.write(line + "\n")
				_write_obj_struct_rec(value, w_stream, indent, obj_str_fnc)

			else:
				line += obj_str_fnc(value)
				w_stream.write(line + "\n")

	elif isinstance(obj_to_write, set):
		for item in obj_to_write:
			line = tabs

			if _obj_is_a_dlst(item):
				line += str(type(item))
				w_stream.write(line + "\n")
				_write_obj_struct_rec(item, w_stream, indent, obj_str_fnc)

			else:
				line += obj_str_fnc(item)
				w_stream.write(line + "\n")

	else:
		line = tabs + obj_str_fnc(obj_to_write)
		w_stream.write(line + "\n")
