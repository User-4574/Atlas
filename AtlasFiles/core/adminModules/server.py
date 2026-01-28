from django.contrib import admin
from core.models.server import FileExclusion
from core.models.server import ServerType
from core.models.server import Server
from core.models.server import ServerEnvironment
from core.models.server import File
from core.models.server import FileLog
from core.models.server import SearchPath

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    """
    Docstring for SystemAdmin
    """ 
    list_display = (
        "hostname",
        "environment",
        "ip_address",
        "active",
        "last_seen",
    )

    search_fields = (
        "hostname",
        "motherboard_uuid",
        "ip_address",
    )

    list_filter = (
        "environment",
        "active",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "last_seen",
    )

@admin.register(ServerEnvironment)
class ServerEnvironmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

@admin.register(ServerType)
class ServerTypeAdmin(admin.ModelAdmin):
    list_display = (
        "type",
        "created_at",
    )

    search_fields = (
        "type",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "server",
        "file",
        "checksum",
    )

    search_fields = (
        "file",
        "checksum",
    )

    # readonly_fields = (
    #     "server",
    #     "file",
    #     "checksum",
    # )

@admin.register(FileLog)
class FileLogAdmin(admin.ModelAdmin):
    list_display = (
        "file",
    )

    search_fields = (
        "file",
        "contents",
        "action",
        "creation_date",
        "last_modified_date",
        "timestamp",
    )

    # readonly_fields = (
    #     "contents",
    #     "creation_date",
    #     "last_modified_date",
    #     "timestamp",
    # )


@admin.register(SearchPath)
class SearchPathAdmin(admin.ModelAdmin):
    list_display = (
        "path",
        "description",
    )

    search_fields = (
        "path",
        "description",
    )


@admin.register(FileExclusion)
class FileExclusionAdmin(admin.ModelAdmin):
    list_display = (
        "pattern",
        "description",
    )

    search_fields = (
        "pattern",
        "description",
    )