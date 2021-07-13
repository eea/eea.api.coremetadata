# -*- coding: utf-8 -*-
""" Base metadata adapter for a Plone site """
from zope.component import adapter
from zope.interface import implementer

from plone import api
from plone.dexterity.content import CEILING_DATE
from plone.dexterity.content import FLOOR_DATE
from Products.CMFPlone.interfaces import IPloneSiteRoot

from .dexterity import BaseDexterityCoreMetadataAdapter
from .interfaces import ICoreMetadata


try:
    from Products.CMFPlone.utils import getSiteLogo
except ImportError:
    getSiteLogo = None


@implementer(ICoreMetadata)
@adapter(IPloneSiteRoot)
class PloneSiteCoreMetadataAdapter(BaseDexterityCoreMetadataAdapter):
    """This is the base core metadata adapter.
    When building a custom adapter for your content-type, just inherit
    from this, modify the relevant method and register the adapter for
    your content-type.
    """

    def title(self):
        """ see ICoreMetadata"""
        return self.context.Title()

    def abstract(self):
        """ see ICoreMetadata"""
        return self.context.Description()

    def description(self):
        """ see ICoreMetadata"""
        return self.context.Description()

    def creation_date(self):
        """ see ICoreMetadata"""
        return self.context.creation_date.ISO8601()

    def issued_date(self):
        """ see ICoreMetadata"""
        if self.context.effective and self.context.effective() != FLOOR_DATE:
            return self.context.effective().ISO8601()

        return None

    def expiration_date(self):
        """ see ICoreMetadata"""
        if self.context.expires and self.context.expires() != CEILING_DATE:
            return self.context.expires().ISO8601()

        return None

    def publisher(self):
        """ see ICoreMetadata"""
        return None

    def data_provenance(self):
        """ see ICoreMetadata"""
        return None

    def contributors(self):
        """ see ICoreMetadata"""
        return None

    def format(self):
        """ see ICoreMetadata"""
        return None

    def word_count(self):
        """ see ICoreMetadata"""
        return None

    def rights(self):
        """ see ICoreMetadata"""
        return None

    def depiction(self):
        """ see ICoreMetadata"""
        if getSiteLogo is not None:
            return getSiteLogo()
        else:
            return "{}/logo.png".format(api.portal.get().absolute_url())
