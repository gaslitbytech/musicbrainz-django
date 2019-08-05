from social_core.backends.oauth import BaseOAuth2

"""
Proudly copied from https://musicbrainz.org/doc/Development/OAuth2

Authorization request
The authorization sequence starts by redirecting the user to the authorization endpoint with a set of query string parameters describing the authorization request. The endpoint is located at https://musicbrainz.org/oauth2/authorize and is only accessible over HTTPS. HTTP connections are refused.

The following set of query string parameters is supported by the MusicBrainz authentication endpoint:

response_type
Must be always set to code.
client_id
Client ID assigned to your application. You can find it on the website in your list of registered applications.
redirect_uri
URL where clients should be redirected after authorization. This must match exactly the URL you entered when registering your application. Desktop applications can use either urn:ietf:wg:oauth:2.0:oob or http://localhost with a custom port.
scope
Space delimited list of scopes the application requests. See below for a list of all available scopes.
state (optional)
Any string the application wants passed back after authorization. For example, this can be a CSRF token from your application. This parameter is optional, but strongly recommended.
There are two extra parameters applicable only to web server applications:

access_type (optional)
Indicates if your application needs to access the API when the user is not present at the browser. This parameter defaults to online. If your application needs to refresh access tokens when the user is not present at the browser, then use offline. This will result in your application obtaining a refresh token the first time your application exchanges an authorization code for a user.
approval_prompt (optional)
Indicates if the user should be re-prompted for consent. The default is auto, so a given user should only see the consent page for a given set of scopes the first time through the sequence. If the value is force, then the user sees a consent page even if they have previously given consent to your application for a given set of scopes.
For example, a complete authorization request from a web application requesting permissions to read the user's private tags and ratings would look like this:

https://musicbrainz.org/oauth2/authorize?
  response_type=code&
  client_id=uTuPnUfMRQPx8HBnHf22eg&
  redirect_uri=http%3A%2F%2Fwww.example.com.com%2Fauth2callback&
  scope=tag%20rating&
  state=1351449443
The response to the authorization request will be sent to the URL indicated in the redirect_uri parameter. The authorization endpoint will redirect the user to this URL with a set of specific query string parameters indicating the result. If the user does not approve the request or there is a problem with the request, it will return an error describing the problem. Otherwise it will return an authorization code that can be exchanged for an access token by the token endpoint.

In case of an error, the response will look like this:
"""

class MusicBrainzOAuth2(BaseOAuth2):
    """MusicBrainz OAuth2 authentication backend"""
    name = 'musicbrainz'
    AUTHORIZATION_URL = 'https://musicbrainz.org/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://musicbrainz.org/oauth2/token'
    SCOPE_SEPARATOR = ' '
    EXTRA_DATA = [
        # ('id', 'id'),
        # ('expires', 'expires')
    ]

    DEFAULT_SCOPE = ['profile', 'collection']

    # github
    # def get_user_details(self, response):
    #     """Return user details from GitHub account"""
    #     return {'username': response.get('login'),
    #             'email': response.get('email') or '',
    #             'first_name': response.get('name')}

    # def user_data(self, access_token, *args, **kwargs):
    #     """Loads user data from service"""
    #     url = 'https://api.github.com/user?' + urlencode({
    #         'access_token': access_token
    #     })
    #     return self.get_json(url)
