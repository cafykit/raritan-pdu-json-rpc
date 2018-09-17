class Utils(object):

    @staticmethod
    def indent(string, indent):
        return "\n".join([(" " * indent) + l for l in string.splitlines()])

    @staticmethod
    def rprint(object):
    	if isinstance(object, str):
            return str(object)
    	try:
            return '[\n' + ",\n".join(Utils.indent(str(x), 4) for x in object) + '\n' + Utils.indent(']', 4)
    	except TypeError: # fallback
            return str(object)
