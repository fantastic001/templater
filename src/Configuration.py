import configparser
from .TemplateSource import TemplateSource
from .sources import * 

class Configuration:

    SOURCE_CLASSES = [
        DirectoryTemplateSource
    ]

    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def list_sources(self):
        res = []
        sources = []
        try:
            sources = self.config["DEFAULT"]["sources"].split(" ")
        except KeyError:
            return []
        for source in sources:
            if source.strip() == "":
                continue
            src_config = self.config["source:%s" % source]
            for src_class in self.SOURCE_CLASSES:
                if src_class.deserialize(src_config) is not None:
                    res.append(src_class.deserialize(src_config))
        return res

    def add_source(self, name, source: TemplateSource):
        if "sources" not in self.config["DEFAULT"]:
            self.config["DEFAULT"] = {"sources": ""}
        self.config["DEFAULT"]["sources"] = "%s %s" % (self.config["DEFAULT"]["sources"].strip(), name)
        self.config["source:%s" % name] = source.serialize()
        self.save()

    def save(self):
        with open(self.path, "w") as f:
            self.config.write(f)
