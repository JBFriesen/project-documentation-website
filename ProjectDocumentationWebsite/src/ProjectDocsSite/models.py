from django.conf import settings
from django.db import models


class ProjectType(models.Model):
    """The ProjectType model contains the base model data for each project type such as the type name,
    allowed entry types and amounts, allowed status and contrib_status settings for this project type, and the 
    link to the templates for how this project type should be displayed."""
    type_code = models.CharField(max_length=5, primary_key=True)
    type_name = models.CharField(max_length=25, unique=True)
    allowed_entries_string = models.TextField()
    allowed_status_string = models.TextField()
    allowed_contrib_status_string = models.TextField()
    preview_temp = models.CharField(max_length=50)
    view_temp = models.CharField(max_length=50)
    edit_temp = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name
    
    def allowed_entries_dict(self):
        """Converts the allowed_entries_string field to a dict object and returns it."""
        return string_to_dict(self.allowed_entries_string)
    
    def allowed_status_list(self):
        """Converts the allowed_status_string field to a list and returns it."""
        return string_to_list(self.allowed_status_string)
    
    def allowed_contrib_status_list(self):
        """Converts the allowed_contrib_status_string to a list object and returns it."""
        return string_to_list(self.allowed_contrib_status_string)


class EntryType(models.Model):
    """The EntryType model defines the entry_type name, the required data for this entry type,
    if it can have a update entry, and the templates for displaying each view."""
    type_code = models.CharField(max_length=5, primary_key=True)
    type_name = models.CharField(max_length=25, unique=True)
    required_data_dict_string = models.TextField()
    update_bool = models.BooleanField()
    preview_temp = models.CharField(max_length=50)
    view_temp = models.CharField(max_length=50)
    edit_temp = models.CharField(max_length=50)
    update_preview_temp = models.CharField(max_length=50)
    update_view_temp = models.CharField(max_length=50)
    update_edit_temp = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name
    
    def required_data_dict_dict(self):
        """Converts the required_data_dict_string field to a dict object and returns it."""
        return string_to_dict(self.required_data_dict_string)
  

class Project(models.Model):
    """The Project model is where project specific statuses, creation date, 
    type, and the creator userId are stored"""
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateField()
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    status = models.CharField(max_lenght=50)          # tells if the project in pending,finished,etc
    contrib_status = models.CharField(max_length=50)  # tells if and how the organization contributed to the project
    
    def __str__(self):
        return self.name
    
    
class Entry(models.Model):
    """The Entry model is where individual entry data is stored"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateField()
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry_type = models.ForeignKey(EntryType, on_delete=models.CASCADE)
    note = models.TextField()
    data_list_string = models.TextField() # a csv list of key:value pairs eg. "key:value,key1:value1"
    
    def __str__(self):
        return "%s-#%s" % (self.entry_type, self.id)
    
    def data_list_dict(self):
        """Converts the data_list_string field to a dict object and returns it."""
        return string_to_dict(self.data_list_string)


class UserInfo(models.Model):
    """Contains custom info for each user such as the user status, etc."""
    user_object = models.OneToOneField(settings.AUTH_USER_MODEL)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_object.name
    
 
    
def string_to_dict(d_string):
    """Converts the string to a dict object when the string is formatted as 'key1:value1,key2:value2' etc."""
    data_dict = {}
    for i in d_string.split(','):
        temp = i.split(':')
        data_dict[temp[0]] = temp[1]
    return data_dict

def string_to_list(d_string):
    """Converts the string to a list object by splitting a the commas."""
    return d_string.split(',')
    
        