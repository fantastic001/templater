
class TemplateSource:

    def get_templates(self):
        """
        Get all templates available in source as dictionary where key is unique 
        identifier of template in that source and value is either 
        TemplateFile or TemplateDirectory object.

        Returns: dict object as described above
        """
        raise NotImplementedError()
    
    def get_name(self):
        """
        Should return name of template source. 

        Returns: str 
        """
        raise NotImplementedError()
    
    def get_source(self):
        """
        Source is string representing human readable string of URL or similar
        where user can see actual location of repository.abs
        For instance, it can be folder path, ftp server URL etc...

        Returns: str
        """
        raise NotImplementedError()
    
    def serialize(self):
        """
        Should convert source representation to dict object such that it can be written 
        to JSON later on.abs

        Returns: dict
        """
        raise NotImplementedError()
    
    def deserialize(d):
        """
        Should read dictionary (given by parsing JSON data probably) and 
        create TemplateSource object. 
        If it cannot be created (for instance, metadata is not for given type), returns None

        Returns: dict or None
        """
        raise NotImplementedError()
    
    def get_template(self, name):
        """
        Tries to find template with given name. If it finds it, returns Template object or similar.
        If it fails, returns None. 
        
        Returns: template object or None
        """
        for k,v in self.get_templates().items():
            if k == name:
                return v 
        return None