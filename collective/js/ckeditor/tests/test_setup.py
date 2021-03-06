import unittest2 as unittest
from collective.js.ckeditor.tests import base
from plone.browserlayer import utils

class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_jsregistry(self):
        registry = self.portal.portal_javascripts
        resource = registry.getResource("++resource++collective.js.ckeditor/ckeditor.js")
        self.assertTrue(resource is not None)


class TestUninstall(base.IntegrationTestCase):
    """Test if the addon uninstall well"""

    def setUp(self):
        super(TestUninstall, self).setUp()
        qi = self.portal['portal_quickinstaller']
        qi.uninstallProducts(products=['collective.js.ckeditor'])

    def test_jsregistry(self):
        registry = self.portal.portal_javascripts
        resource = registry.getResource("++resource++collective.js.ckeditor/ckeditor.js")
        self.assertTrue(resource is None)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)