# encoding: utf-8
import pytest

import ckan.tests.factories as factories
import ckan.tests.helpers as helpers
from ckan import model
from ckan.lib.helpers import url_for


@pytest.mark.usefixtures('clean_db', 'clean_index')
@pytest.mark.ckan_config('ckan.plugins', 'saml2auth')
class TestBlueprint(object):

    def test_user_register_disabled_by_default(self, app):
        url = url_for("user.register")
        response = app.get(url=url)
        assert 403 == response.status_code

        assert u'This resource is forbidden' \
               u' by the system administrator. ' \
               u'Only SSO through SAML2 authorization ' \
               u'is available at this moment.' in response

    def test_internal_user_login_disabled_by_deafult(self, app):
        url = url_for("user.login")
        response = app.get(url=url)
        assert 403 == response.status_code

        assert u'This resource is forbidden' \
               u' by the system administrator. ' \
               u'Only SSO through SAML2 authorization ' \
               u'is available at this moment.' in response

    # @pytest.mark.ckan_config(u'ckanext.saml2auth.enable_ckan_internal_login', 'true')
    # def test_user_register_enabled(self, monkeypatch, make_app, ckan_config):
    #     monkeypatch.setitem(ckan_config, u'ckanext.saml2auth.enable_ckan_internal_login', True)
    #     url = url_for("user.register")
    #     app = make_app()
    #     response = app.get(url=url)
    #     assert 200 == response.status_code

    # def test_saml2_login(self, app):
    #     url = url_for("saml2auth.saml2login")
    #     response = app.get(url=url)
    #     assert 302 == response.status_code
