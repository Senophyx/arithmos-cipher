from .encrypt import encrypt
from .decrypt import decrypt
from .utils import get_version

__title__ = "Arithmos Cipher"
__version__ = "2.0"
__authors__ = "LyQuid"
__license__ = "Apache License 2.0"
__copyright__ = "Copyright 2022-present LyQuid"


get_version = get_version()

if get_version == "offline":
    pass
else:
	if float(__version__) == float(str(get_version)):
		pass
	else:
		print(f"Warning! Your arithmos-cipher version is outdated! Latest version : {get_version()}")
