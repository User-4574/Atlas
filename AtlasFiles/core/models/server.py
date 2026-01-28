import uuid
from django.db import models
"""
This module defines the models for servers, their environments, types, files, file logs, and related metadata.
"""

class ServerEnvironment(models.Model):
    """
    Server environments, like production, Q/A, development, etc.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class ServerType(models.Model):
    """
    Server type, like bare metal, virtual machine, container, etc.
    """
    type = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.type




class Server(models.Model):
    """"
    Server object to represent a physical or virtual servers
    """
    motherboard_uuid = models.UUIDField(unique=True)
    hostname = models.CharField(max_length=255, unique=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    environment = models.ForeignKey(
        ServerEnvironment,
        on_delete=models.PROTECT,
        related_name="systems",
    )
    type = models.ForeignKey(
        ServerType,
        on_delete=models.PROTECT,
        related_name="systems",
    )
    last_seen = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ["hostname"]

    def __str__(self):
        return self.hostname



class File(models.Model):
    """
    A file on a server that is being tracked.
    """
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="files",
    )
    file = models.CharField(max_length=2048)
    contents = models.TextField()
    checksum = models.CharField(max_length=64)  
    size = models.BigIntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.server.hostname}: {self.file}"
    

class FileLog(models.Model):
    """
    A log for file changes.
    """
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name="change_logs",
    )
    change_type = models.CharField(max_length=50)  # e.g., 'created', 'modified', 'deleted'
    checksum = models.CharField(max_length=64)  
    timestamp = models.DateTimeField(auto_now_add=True)
    contents = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.file.file} - {self.change_type} at {self.timestamp}"
    





class SearchPath(models.Model):
    """
    Paths for the client to search for files to check in. As search paths are found on servers, they are added here
    so they can be checked on other servers.
    """
    path = models.CharField(max_length=8136, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.path
    

class FileExclusion(models.Model):
    """
    Files or patterns to exclude from being tracked. To prevent credential leakage or other sensitive data.
    """
    pattern = models.CharField(max_length=1024, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.pattern