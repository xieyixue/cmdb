from django.shortcuts import render
from django.shortcuts import HttpResponse

from web_models import models
import json
# Create your views here.
def create_server(request):
    '''
    data ={"data":{
        "hostname":"hostname1",
        "ip":"127.0.0.1",
        "cpu_slot_count":2,
        "memory_slot_count":2,
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
    if request.method == "POST":
        data = request.POST.get("data","")
        #print(data)
        data = json.loads(data)
        print(data)
        server_info = data

        hostname = server_info["hostname"]
        ip = server_info["ip"]
        memory_slot_count = server_info["memory_slot_count"]
        cpu_slot_count = server_info["cpu_slot_count"]


        cpus = server_info["cpus"]
        interfaces = server_info["interfaces"]
        memorys = server_info["memorys"]
        server_info.pop("cpus")
        server_info.pop("interfaces")
        server_info.pop("memorys")

        server_obj = models.Server.objects.filter(hostname=hostname)
        server_count = server_obj.count()

        if server_count == 0:
            server = models.Server(**server_info)
            server.save()
        else:
            print server_count

        for cpu_info in cpus:
            print cpu_info["id"]
            cpu_obj = models.Cpu.objects.filter(**cpu_info)
            cpu_count = cpu_obj.count()
            if cpu_count ==0:
                cpu_insert = models.Cpu(**cpu_info)
                cpu_insert.save()
                cpu_obj = models.Cpu.objects.filter(**cpu_info)
            else:
                pass
            server_obj.cpu_info_id = 2
            server_obj.save()

        for memory_info in memorys:
            memory_obj = models.Memory.objects.filter(**memory_info)
            memory_count = memory_obj.count()
            print memory_count,'ss'
            if memory_count == 0:
                memory_insert = models.Memory(**memory_info)
                memory_insert.save()
                memory_obj = models.Memory.objects.filter(**memory_info)
            #server_obj.memory = memory_obj
            print server_obj.memory.get()
            server_obj.memory.add(memory_obj)
        result = json.dumps(data)
    else:
        result = "Plase POST data"
    return HttpResponse(result)