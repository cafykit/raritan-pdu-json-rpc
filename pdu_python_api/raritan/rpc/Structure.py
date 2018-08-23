import raritan.rpc

class Structure(object):
    def __str__(self):
        l = max([len(e) for e in self.elements])
        pretty = "\n".join([
            raritan.rpc.Utils.indent("* %-*s = %s" % (l, e, raritan.rpc.Utils.rprint(getattr(self, e))), 4) for e in self.elements
        ])
        return "%s:\n%s" % (raritan.rpc.TypeInfo.typeBaseName(self.idlType), pretty)

    def __eq__(self, other):
        return (other != None and self.idlType == other.idlType and
                all([getattr(self, e) == getattr(other, e) for e in self.elements]))
