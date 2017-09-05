# Unreleased
## Changed
- 🔒  Removes the `/static/` folder and endpoint that is implicitly initialized by flask. This is too implicit for my comfort level: I worry that users will not be aware that their files in their `static` folder are accessible
- ⚡️  Removes all API calls to the Plotly API (https://api.plot.ly/), the authentication endpoints and decorators, and the associated `filename`, `sharing` and `app_url` arguments. This was never documented or officially supported and authentication has been moved to the [`dash-auth` package](https://github.com/plotly/dash-auth)

## Added
- 🔧  Add two new `config` variables: `routes_pathname_prefix` and `requests_pathname_prefix` to provide more flexibility for API routing when Dash apps are run behind proxy servers. `routes_pathname_prefix` is a prefix applied to the backend routes and `requests_pathname_prefix` prefixed in requests made by Dash's front-end. `dash-renderer==0.8.0rc3` uses these endpoints.

## Fixed
- ✏️  Fix a typo in an exception

## Maintenance
- 📝  Update README.md
- ✅  Fix CircleCI tests. Note that the the [`dash-renderer`](https://github.com/plotly/dash-renderer) contains the bulk of the integration tests.
- 💄 Flake8 fixes and tests (fixes #99 )
- ✨ Added this CHANGELOG.md

# 0.17.3
✨ This is the initial open-source release of Dash
