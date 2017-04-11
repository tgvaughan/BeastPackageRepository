# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from submit.models import BeastPackage

def index(request):
    template = loader.get_template("packages/index.html")
    return HttpResponse(template.render({'beast_packages': BeastPackage.objects.all()}, request))

def xml(request):
    res = "<packages>\n"

    for o in BeastPackage.objects.all():
        res += """\n<package name="{name}" version="{version}"
         url="{url}"
         projectURL="{projectURL}"
         description="{description}" />\n""".format(name=o.name,
        version=o.version, url=o.url, projectURL=o.project_url, description=o.description)

    res += "</packages>\n"

    return HttpResponse(res)
