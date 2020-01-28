# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ulearn5.pypitest.testing import ULEARN5_PYPITEST_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ulearn5.pypitest is properly installed."""

    layer = ULEARN5_PYPITEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ulearn5.pypitest is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ulearn5.pypitest'))

    def test_browserlayer(self):
        """Test that IUlearn5PypitestLayer is registered."""
        from ulearn5.pypitest.interfaces import (
            IUlearn5PypitestLayer)
        from plone.browserlayer import utils
        self.assertIn(IUlearn5PypitestLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ULEARN5_PYPITEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ulearn5.pypitest'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ulearn5.pypitest is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ulearn5.pypitest'))

    def test_browserlayer_removed(self):
        """Test that IUlearn5PypitestLayer is removed."""
        from ulearn5.pypitest.interfaces import \
            IUlearn5PypitestLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IUlearn5PypitestLayer,
            utils.registered_layers(),
        )
