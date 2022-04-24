from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
import logging

# iterate through the modules in the current package
package_dir = Path(__file__).resolve().parent
# print(package_dir)
formats_dict = {}
for (_, module_name, _) in iter_modules([package_dir]):
	# print(module_name)
	# import the module and iterate through its attributes
	# module = import_module(f"{__name__}.{module_name}")
	# module = import_module(f"{package_dir}.{module_name}")
	module = import_module(f"modules.formats.{module_name}")
	for attribute_name in dir(module):
		attribute = getattr(module, attribute_name)

		if isclass(attribute):
			# ignore any imports
			if not hasattr(attribute, "extension"):
				continue
			if attribute.extension is None:
				logging.debug(f"Missing extension on class {attribute_name} in file {module_name}")
				continue
			if not attribute.extension.startswith("."):
				logging.warning(f"Bad extension '{attribute.extension}' on class {attribute_name} in file {module_name}")
				continue
			formats_dict[attribute.extension] = attribute
			# print(attribute_name)
			# # Add the class to this package's variables
			# globals()[attribute_name] = attribute
# print(formats_dict)
