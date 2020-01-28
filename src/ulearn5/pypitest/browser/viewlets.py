# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface

from ulearn5.theme.browser.viewlets import viewletHeaderUlearn
from ulearn5.pypitest.interfaces import IUlearn5PypitestLayer

grok.context(Interface)


class viewletHeaderUlearnPypitest(viewletHeaderUlearn):
    grok.name('pypitest.header')
    grok.template('header')
    grok.viewletmanager(IPortalHeader)
    grok.layer(IUlearn5PypitestLayer)
