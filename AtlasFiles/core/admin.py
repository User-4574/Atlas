#Basic
from django.contrib import admin

# Module Admin Imports
####### Server Module Admin Imports #######
from .adminModules.server import ServerAdmin
from .adminModules.server import ServerEnvironmentAdmin
from .adminModules.server import ServerTypeAdmin
from .adminModules.server import FileAdmin
from .adminModules.server import FileLogAdmin
from .adminModules.server import SearchPathAdmin
from .adminModules.server import FileExclusionAdmin


####### Site headers #######
admin.site.site_header = "Atlas Administration"
admin.site.site_title = "Atlas Admin Portal"
admin.site.index_title = "Welcome to Atlas Admin Portal"
# admin.site.site_url = ""

