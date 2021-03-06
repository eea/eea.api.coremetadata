# -*- coding: utf-8 -*-
""" @metadata endpoint for Plone REST API """
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer

from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service

from .adapters.interfaces import ICoreMetadata


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class Metadata(object):
    """ Expandable service factory implementation """

    def __init__(self, context, request):
        self.context = context.aq_explicit
        self.request = request

    def __call__(self, *args, **kwargs):
        result = {
            "metadata": {
                "@id": "{}/@metadata".format(
                    self.context.absolute_url(),
                ),
            },
        }
        # Ignore expansion mechanism,
        # always show expanded results
        #
        # if not expand:
        #     return result

        core_metadata_adapter = ICoreMetadata(self.context)
        # pylint: disable=too-many-function-args
        items = core_metadata_adapter.render_metadata()

        result["metadata"]["items"] = items
        return result


class MetadataGet(Service):
    """ @metadata endpoint implementation """

    def reply(self):
        """ return the proper information in the API """
        service_factory = Metadata(self.context, self.request)
        return service_factory(expand=True)["metadata"]
