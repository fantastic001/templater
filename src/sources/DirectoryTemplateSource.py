from .. import *

import os 
import os.path

class DirectoryTemplateSource(TemplateSource):
    
    def __init__(self, path):
        self.path = path
    

    def get_templates(self):
        """
        Get all templates available in source as dictionary where key is unique 
        identifier of template in that source and value is either 
        TemplateFile or TemplateDirectory object.

        Returns: dict object as described above
        """
        res = {}
        for name in os.listdir(self.path):
            fullpath = os.path.join(self.path, name)
            if os.path.isfile(fullpath):
                continue
            else:
                for subdir in os.listdir(fullpath):
                    fullsubpath = os.path.join(fullpath, subdir)
                    if os.path.isdir(fullsubpath):
                        res["%s/%s" % (name, subdir)] = Template(fullsubpath)
        return res
    
    def get_name(self):
        """
        Should return name of template source. 

        Returns: str 
        """
        path = os.path.normcase(self.path)
        return os.path.split(path)[1]
    
    def get_source(self):
        """
        Source is string representing human readable string of URL or similar
        where user can see actual location of repository.abs
        For instance, it can be folder path, ftp server URL etc...

        Returns: str
        """
        return os.path.normpath(self.path)
    
    def serialize(self):
        """
        Should convert source representation to dict object such that it can be written 
        to JSON later on.abs

        Returns: dict
        """
        return {
            "type": "directory",
            "path": self.get_source()
        }
    
    def deserialize(d):
        """
        Should read dictionary (given by parsing JSON data probably) and 
        create TemplateSource object. 
        If it cannot be created (for instance, metadata is not for given type), returns None

        Returns: dict or None
        """
        return DirectoryTemplateSource(d["path"]) if d["type"] == "directory" else None