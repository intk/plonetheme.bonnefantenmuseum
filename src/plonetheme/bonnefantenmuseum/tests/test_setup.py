# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.bonnefantenmuseum.testing import PLONETHEME_MODERNBASE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.bonnefantenmuseum is properly installed."""

    layer = PLONETHEME_MODERNBASE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.bonnefantenmuseum is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.bonnefantenmuseum'))

    def test_browserlayer(self):
        """Test that IPlonethemebonnefantenmuseumLayer is registered."""
        from plonetheme.bonnefantenmuseum.interfaces import (
            IPlonethemeModernBaseLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeModernBaseLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_MODERNBASE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.bonnefantenmuseum'])

    def test_product_uninstalled(self):
        """Test if plonetheme.bonnefantenmuseum is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.bonnefantenmuseum'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemebonnefantenmuseumLayer is removed."""
        from plonetheme.bonnefantenmuseum.interfaces import IPlonethemeModernBaseLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeModernBaseLayer, utils.registered_layers())
