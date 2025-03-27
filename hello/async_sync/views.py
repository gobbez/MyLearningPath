import asyncio
import time
from django.http import HttpResponse
from libreria.helpers import log_colorato

def orario():
    return time.strftime('%H:%M:%S', time.localtime())

def task_sync():
    log_colorato(f"{orario()}: task sync begin")
    time.sleep(5)
    log_colorato(f"{orario()}: task sync run success")

def view_sync(request):
    log_colorato(f"{orario()}: sync begin")
    task_sync()
    log_colorato(f"{orario()}: sync return")
    return HttpResponse(f"{orario()}: Sync HTTP request")

async def task_async():
    log_colorato(f"{orario()}: task async begin")
    await asyncio.sleep(5)
    log_colorato(f"{orario()}: task async run success")

async def view_async(request):
    log_colorato(f"{orario()}: async begin")
    loop = asyncio.get_event_loop()
    loop.create_task(task_async())
    log_colorato(f"{orario()}: async return")
    return HttpResponse(f"{orario()}: async HTTP request")
