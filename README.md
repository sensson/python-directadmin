# python-directadmin

This is a Python interface to the DirectAdmin API.

# Usage

```
from directadmin.api import API

api = API(
  username='username',
  password='secure',
  server='https://1.2.3.4:2222',
)

resellers = api.cmd_api_show_resellers()
print(resellers)
```

# API

`API()` handles all connections, calls and responses. It accepts the following
parameters:

* `username`: the username that you use to login to DirectAdmin;
* `password`: the password belonging to the username;
* `server`: the server you're connecting to, including http(s) and the port;
* `debug`: a boolean to turn on debugging mode;
* `json`: a boolean to enable JSON output in the DirectAdmin API.

Although it supports the new JSON output DirectAdmin uses in its evolution
skin, this hasn't been added for all endpoints yet. JSON output is disabled
by default.

## Supported methods

The [API documentation](https://www.directadmin.com/api.html) has a list of all
available endpoints in DirectAdmin. All endpoints DirectAdmin provides are
supported, including future ones.

In the DirectAdmin documentation you will find endpoints such as:

* CMD_API_ACCOUNT_USER
* CMD_API_SHOW_USER_DOMAINS

And others.

These translate directly to methods of the API object. For example:

* CMD_API_ACCOUNT_USER is accessed via `api.cmd_api_account_user()`;
* CMD_API_SHOW_USER_DOMAINS is accessed via `api.cmd_api_show_user_domains()`.

Every method accepts the keywords as documented by DirectAdmin. To create a new
user you would use:

```
api.cmd_api_account_user(
  action='create',
  add='Submit',
  username='test',
  ...
)
```

## Impersonation

You can use `become()` to impersonate another user as an admin or reseller. For
example:

```
api = API(..)
api.become('username').cmd_api_databases(..)
```

`become()` will return a new instance of `API()`.

# Error handling

* `ResponseException` is raised when the API returns an unexpected response;
* `UnauthorizedException` is raised when your username or password is wrong.

Set `debug` to `True` when initializing the API object to get more information.

# Tests

Sorry, this code doesn't come with tests yet.
