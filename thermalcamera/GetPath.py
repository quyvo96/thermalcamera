import sys, os
path = ""


def module_path():
    encoding = sys.getfilesystemencoding()

    return os.path.dirname(bytes(__file__, encoding))
def get_path():
    path = str(module_path())
    path = path[2:-1]
    return path

	
	
