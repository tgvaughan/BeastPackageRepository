# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage

import tempfile, shutil, zipfile
import xml.etree.ElementTree as ET

from submit.models import BeastPackage

def index(request):
    template = loader.get_template("submit/index.html")
    return HttpResponse(template.render({}, request))

def upload(request):
    package_file = request.FILES['package_file']
    fs = FileSystemStorage()
    filename = fs.save(package_file.name, package_file)

    pkgzip = zipfile.ZipFile(fs.path(filename), 'r')

    vfh = pkgzip.open("version.xml")
    root =  ET.parse(vfh).getroot()
    depends = root.findall("depends")

    print request.POST
    pkg = BeastPackage(name=root.attrib['name'],
            version=root.attrib['version'],
            description=request.POST['description'],
            url=fs.url(filename),
            project_url=request.POST['project_url'],
            email=request.POST['email'],
            doi=request.POST['doi'])
    pkg.save()

    return HttpResponse("thanks")
