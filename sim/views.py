import asyncio
import random

from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

messages = ["asdfasdf"]

async def sse_stream(request):
    """
    Sends server-sent events to the client.
    """
    async def event_stream():
        while True:
            if len(messages) > 0:
                yield f'data: {messages.pop()}\n\n'
            else:
                await asyncio.sleep(1)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def index(request):
    return render(request, 'sse.html')

@csrf_exempt
def message(request):
    messages.append(request.body)
    return JsonResponse({})
