import raritan.rpc

class ValueObject(object):
    def __init__(self):
        pass

    @staticmethod
    def decode(json, agent):
        if not json:
            return None
        class_ = raritan.rpc.TypeInfo.decode(json['type'])
        obj = class_.decode(json['value'], agent)
        return obj

    @staticmethod
    def encode(obj):
      json = {}
      json['type'] = obj.idlType
      json['value'] = obj.encode()
      return json

    def __str__(self):
        elements = self.listElements()
        l = max([len(e) for e in elements])
        pretty = "\n".join([
            raritan.rpc.Utils.indent("* %-*s = %s" % (l, e, raritan.rpc.Utils.rprint(getattr(self, e))), 4) for e in elements
        ])
        return "%s:\n%s" % (raritan.rpc.TypeInfo.typeBaseName(self.idlType), pretty)

    def __eq__(self, other):
        return (other != None and self.idlType == other.idlType and
                all([getattr(self, e) == getattr(other, e) for e in self.listElements()]))

