from django.db import models

# Create your models here.
class Server(models.Model):
    hostname=models.CharField(max_length=200)
    ip=models.GenericIPAddressField()
    cpu_slot_count=models.IntegerField(default=1)
    memory_slot_count=models.IntegerField(default=1)
    cpu=models.ForeignKey('Cpu')
    memory=models.ForeignKey('Memory')
    disk=models.ForeignKey('Disk')

    def __unicode__(self):
        return self.hostname

class Cpu(models.Model):
    cpu_speed=models.IntegerField(default=1)
    processor_cpu_count=models.IntegerField(default=1)

class Memory(models.Model):
    memory_size=models.IntegerField(default=1024)
    memory_speed=models.IntegerField(default=0000)

class Disk(models.Model):
    disk_type=models.CharField(max_length=200,default="SATA")
    disk_size=models.IntegerField(default=1024)
    disk_speed=models.IntegerField(default=5400)
