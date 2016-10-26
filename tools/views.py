from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from models import Tool, ToolType

# Create your views here.

def toolsHome(request):
    tool_types = ToolType.objects.all()
    tools = Tool.objects.all().prefetch_related('types')
    context = { 'tools' : tools,
                'tool_types' : tool_types,
                'title' : 'Neurodata Tools'}
    return render(request, 'tools_home.html', context)

def toolPage(request, token):
    tool = get_object_or_404(Tool, token=token)

    context = {'tool' : tool,
               'title' : tool.longname }
    return render(request, 'tool_page.html', context)
