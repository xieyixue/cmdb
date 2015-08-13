#!/usr/bin/env python
#-*-coding:utf-8-*-
from django.shortcuts import render
from django.shortcuts import HttpResponse

from web_models import models
import json
# Create your views here.
def create_server(request):
    '''
    data ={"data":{
        "hostname":"hostname1",
        "server_sn":"9781cc98-17eb-4e51-ad4e-fa60e1d549be",
        "manufactory":"dell",
        "manage_ip":"192.168.2.200",
        "cpu_count":4,
        "cpu_physical_count":2,
        "first_mac":"00:16:3e:00:1d:cc",
        "memory_slot_count":2,
         }
        }
        "cpus":[{
            "id":1,
            "cpu_speed":1.5,
            "processor_cpu_count":2
            }
        ],
        "interfaces":[{
            "ipaddr":"192.168.10.1.1",
            "netmask":"255.255.255.0",
            "mac":"00:30:48:DA:D1:E5"
            },
            {
            "ipaddr":"192.168.10.1.2",
            "netmask":"255.255.255.0",
            "mac":"00:30:48:DA:D1:E6"
            }
        ],
        "memorys":[{
            "memory_speed":1300,
            "memory_size":4000
            },
            {
            "memory_speed":1301,
            "memory_size":4000
        }
        ]
     }
    }
    '''


    '''
    {
    "hostname": "c1.text.com",
    "sn": "9781cc98-17eb-4e51-ad4e-fa60e1d549be",
    "manufactory": "dell",
    "manage_ip": "192.168.2.200",
    "cpu_count": 4,
    "cpu_physical_count": 2,
    "first_mac": "00:16:3e:00:1d:cc"

}
    '''
    if request.method == "POST":
        data = request.POST.get("data","")
        data = json.loads(data)
        server_info = data

        hostname = server_info["hostname"]
        ip = server_info["manage_ip"]
        cpu_physical_count = server_info["cpu_physical_count"]
        cpu_count = server_info["cpu_count"]


        server_obj = models.Server.objects.filter(hostname=hostname)
        server_count = server_obj.count()

        if server_count == 0:
            #device_type_obj = models.DeviceType.(name=u'服务器')
            ##device_type_obj.save()
            #device_status_obj = models.Status.(name=u'线下')

            Asset_obj = models.Asset.objects.filter(device_type_id=1,device_status_id=1)
            #Asset_obj.device_status = device_status_obj
            #Asset_obj.device_type = device_type_obj
            #Asset_obj = models.Asset(device_status=device_status_obj,device_type=device_type_obj)

            server = models.Server(asset=Asset_obj,**server_info)
            server.save()
        else:
            print server_count


        result = json.dumps(data)
    else:
        result = "Plase POST data"
    return HttpResponse(result)