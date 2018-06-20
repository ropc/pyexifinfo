import pyexifinfo as p
import csv
import asyncio

#tested with Pytest
#
#
# python logo (MIT)
import os
TESTSDIR = os.path.dirname(os.path.realpath(__file__))
image = TESTSDIR + '/python-logo-master-v3-TM.png'

def test_version_is_greater_than_8():
    """ test the version is greater than 8 """
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.ver())
    #transforming bytes to string
    a = a[0].decode('utf-8')
    #transform string to float
    a = float(a)
    assert a >= 8

def test_get_json():
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.get_json(image))
    assert len(a[0]) >= 25

def test_get_csv():
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.get_csv(image))
    assert a[0:10] == "SourceFile"

def test_get_xml():
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.get_xml(image))
    assert a[0:5] == "<?xml"

def test_get_fileType():
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.fileType(image))
    assert a.lower() == 'png'

def test_get_mimeType():
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(p.mimeType(image))
    assert a.lower() == 'image/png'
