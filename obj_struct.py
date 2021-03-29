from pathlib import Path


_DLST = (dict, list, set, tuple)


def _make_tabs(n):
	return "\t" * n


def _obj_and_type_to_str(obj):
	return str(obj) + " " + str(type(obj))


def _obj_is_a_dlst(obj):
	return isinstance(obj, _DLST)


def write_obj_struct(struct, output_path):
	if isinstance(output_path, str):
		output_path = Path(output_path)

	elif isinstance(output_path, Path):
		raise TypeError("The given path must be an instance "
			+ "of str or Pathlib's class Path.")

	_write_obj_struct_rec(struct, output_path.open(mode="w"))


def _write_obj_struct_rec(obj_to_write, w_stream, indent=0):
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
				_write_obj_struct_rec(item, w_stream, indent)

			else:
				line += _obj_and_type_to_str(item)
				w_stream.write(line + "\n")

	elif isinstance(obj_to_write, dict):
		for key, value in obj_to_write.items():
			line = tabs + str(key) + ": "

			if _obj_is_a_dlst(value):
				line += str(type(value))
				w_stream.write(line + "\n")
				_write_obj_struct_rec(value, w_stream, indent)

			else:
				line += " " + _obj_and_type_to_str(value)
				w_stream.write(line + "\n")

	elif isinstance(obj_to_write, set):
		for item in obj_to_write:
			line = tabs

			if _obj_is_a_dlst(item):
				line += str(type(item))
				w_stream.write(line + "\n")
				_write_obj_struct_rec(item, w_stream, indent)

			else:
				line += _obj_and_type_to_str(item)
				w_stream.write(line + "\n")

	else:
		line = tabs + _obj_and_type_to_str(obj_to_write)
		w_stream.write(line + "\n")
