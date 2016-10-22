from urllib.parse import urljoin

from django.conf import settings
from social.backends.oauth import BaseOAuth2


class EXROAuth2(BaseOAuth2):
    name = 'exr'

    ID_KEY = 'id'
    ACCESS_TOKEN_METHOD = 'POST'

    AUTHORIZATION_URL = urljoin(
        settings.SOCIAL_AUTH_EXR_BASE_URL, '/oauth/authorize/')
    ACCESS_TOKEN_URL = urljoin(
        settings.SOCIAL_AUTH_EXR_BASE_URL, '/oauth/token/')
    REVOKE_TOKEN_URL = urljoin(
        settings.SOCIAL_AUTH_EXR_BASE_URL, '/oauth/revoke_token/')

    def get_user_details(self, response, *args, **kwargs):
        return {k: v for k, v in response.items()
                if k in ['username', 'email', 'first_name', 'last_name']}

    def user_data(self, access_token, *args, **kwargs):
        url = urljoin(self.setting('BASE_URL'), '/api/users/me/')
        return self.get_json(url, params={'access_token': access_token})
