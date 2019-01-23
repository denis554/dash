## [0.35.3] - 2019-01-23
## Fixed
- Asset blueprint takes routes prefix into it's static path. [#547](https://github.com/plotly/dash/pull/547)
- Asset url path no longer strip routes from requests. [#547](https://github.com/plotly/dash/pull/547)
- Remove print statement from PreventUpdate error handler. [#548](https://github.com/plotly/dash/pull/548)
- Removed ComponentRegistry dist cache [#524](https://github.com/plotly/dash/pull/524)

## Changed
- `assets_folder` argument now default to 'assets' [#547](https://github.com/plotly/dash/pull/547)
- The assets folder is now always relative to the given root path of `name` argument, the default of `__main__` will get the `cwd`. [#547](https://github.com/plotly/dash/pull/547)
- No longer coerce the name argument from the server if the server argument is provided. [#547](https://github.com/plotly/dash/pull/547)

## [0.35.2] - 2019-01-11
## Fixed
- Fix typo in some exception names [#522](https://github.com/plotly/dash/pull/522)

## 0.35.1 - 2018-12-27
### Fixed
- Always skip `dynamic` resources from index resources collection. [#518](https://github.com/plotly/dash/pull/518)

## 0.35.0 - 2018-12-18
## Added
- Experimental `--r-prefix` option to `dash-generate-components`, optionally generates R version of components and corresponding R package.  [#483](https://github.com/plotly/dash/pull/483)

## 0.34.0 - 2018-12-17
## Added
- `--ignore` option to `dash-generate-components`, default to `^_`. [#490](https://github.com/plotly/dash/pull/490)

## 0.33.0 - 2018-12-10
## Added
- Added specific Dash exception types to replace generic exceptions (InvalidIndexException, DependencyException, ResourceException) [#487](https://github.com/plotly/dash/pull/487)

## 0.32.2 - 2018-12-09
## Fixed
- Fix typo in missing events/inputs error message [#485](https://github.com/plotly/dash/pull/485)

## 0.32.1 - 2018-12-07
## Changed
- Muted dash related missing props docstring from extract-meta warnings [#484](https://github.com/plotly/dash/pull/484)

## 0.32.0 - 2018-12-07
## Added
- Support for .map file extension and dynamic (on demand) loading [#478](https://github.com/plotly/dash/pull/478)

## 0.31.1 - 2018-11-29
## Fixed
- Fix `_imports_.py` indentation generation. [#473](https://github.com/plotly/dash/pull/473/files)

## 0.31.0 - 2018-11-29
## Added
- Combined `extract-meta` and python component files generation in a cli [#451](https://github.com/plotly/dash/pull/451)

## 0.30.0 - 2018-11-14
## Added
- Hot reload from the browser [#362](https://github.com/plotly/dash/pull/362)
- Silence routes logging with `dev_tools_silence_routes_logging`.

## 0.29.0 - 2018-11-06
## Added
- Added component namespaces registry, collect the resources needed by component library when they are imported instead of crawling the layout. [#444](https://github.com/plotly/dash/pull/444)

## 0.28.7 - 2018-11-05
## Fixed
- Component generation now uses the same prop name black list in all supported Python versions. Closes [#361](https://github.com/plotly/dash/issues/361). [#450](https://github.com/plotly/dash/pull/450)

## 0.28.6 - 2018-11-05
## Fixed
- `Dash.registered_paths` changed to a `collections.defaultdict(set)`, was appending the same package paths on every index. [#443](https://github.com/plotly/dash/pull/443)

## 0.28.5 - 2018-10-18
## Fixed
- Replace windows endline when generating the components classes docstring [#431](https://github.com/plotly/dash/pull/431)

## 0.28.4 - 2018-10-18
## Fixed
- The `Component.traverse()` and `Component.traverse_with_paths()` methods now work correctly for components with `children` of type `tuple` (before, this only worked for `list`s). [#430](https://github.com/plotly/dash/pull/430)

## 0.28.3 - 2018-10-17
## Fixed
- Fix http-equiv typo [#418](https://github.com/plotly/dash/pull/418)

## 0.28.2 - 2018-10-05
## Added
- Moved `add_url` function definition out of `Dash.__init__` [#377](https://github.com/plotly/dash/pull/377)

## 0.28.1 - 2018-09-26
## Fixed
- Missing favicon package_data from setup.py [#407](https://github.com/plotly/dash/pull/407)

## 0.28.0 - 2018-09-26
## Added
- Default favicon for dash apps. [#406](https://github.com/plotly/dash/pull/406#issuecomment-424821743)
- Bust the cache of the assets favicon.

## Fixed
- Remove the first and last blank lines from the HTML index string. [#403](https://github.com/plotly/dash/pull/403)

## 0.27.0 - 2018-09-20
## Added
- Added support for serving dev bundles from the components suite, enable with `app.run_server(dev_tools_serve_dev_bundles=True)` [#369](https://github.com/plotly/dash/pull/369)

## Fixed
- Use HTML5 syntax for the meta tag [#350](https://github.com/plotly/dash/pull/350)

## 0.26.6 - 2018-09-19
## Fixed
- Added `Cache-Control` headers to files served by `Dash.serve_component_suites`. [#387](https://github.com/plotly/dash/pull/387)
- Added time modified query string to collected components suites resources.
- Added `InvalidResourceError`. [#393](https://github.com/plotly/dash/pull/393)
- Added a flask errorhandler to catch `InvalidResourceError` from `serve_component_suites` and return a 404.

## 0.26.5 - 2018-09-10
## Fixed
- Fix `get_asset_url` with a different `assets_url_path`. [#374](https://github.com/plotly/dash/pull/374)

## 0.26.4 - 2018-08-28
## Fixed
- Set `url_base_pathname` to `None` in `Dash.__init__`. Fix [#364](https://github.com/plotly/dash/issues/364)

## 0.26.3 - 2018-08-27
## Fixed
- Prefix assets files with `requests_pathname_prefix`. [#351](https://github.com/plotly/dash/pull/351)

## Added
- `Dash.get_asset_url` will give the prefixed url for the asset file.

## 0.26.2 - 2018-08-26
## Fixed
- Only create the assets blueprint once for app that provide the same flask instance to multiple dash instance. [#343](https://github.com/plotly/dash/pull/343)

## 0.26.1 - 2018-08-26
## Fixed
- Fix bug in `_validate_layout` which would not let a user set `app.layout` to be a function that returns a layout [(fixes #334)](https://github.com/plotly/dash/issues/334). [#336](https://github.com/plotly/dash/pull/336)

## 0.26.0 - 2018-08-20
## Added
- Added `assets_ignore` init keyword, regex filter for the assets files. [#318](https://github.com/plotly/dash/pull/318)

## 0.25.1 - 2018-08-20
## Fixed
- Ensure CSS/JS external resources are loaded before the assets. [#335](https://github.com/plotly/dash/pull/335)

## 0.25.0 - 2018-08-14
## Added
- Take configs values from init or environ variables (Prefixed with `DASH_`). [#322](https://github.com/plotly/dash/pull/322)

## Fixed
- Take `requests_pathname_prefix` config when creating scripts tags.
- `requests/routes_pathname_prefix` must starts and end with `/`.
- `requests_pathname_prefix` must ends with `routes_pathname_prefix`. If you supplied both `requests` and `routes` pathname before this update, make sure `requests_pathname_prefix` ends with the same value as `routes_pathname_prefix`.
- `url_base_pathname` set both `requests/routes` pathname, cannot supply it with either `requests` or `routes` pathname prefixes.


## 0.24.2 - 2018-08-13
## Fixed
- Disallow duplicate component ids in the initial layout. [#320](https://github.com/plotly/dash/pull/320)

## 0.24.1 - 2018-08-10
## Fixed
- Fixed bug in 0.23.1 where importing Dash components with no props would result in an error. (Fixes [#321](https://github.com/plotly/dash/issues/321)).
- Fixed bug in 0.23.1 where importing components with arguments that are python keywords could cause an error. In particular, this fixes `dash-html-components` while using Python 3.7.

## 0.24.0 - 2018-08-10
## Added
- Add a modified time query string to the assets included in the index in order to bust the cache. [#319](https://github.com/plotly/dash/pull/309)


## 0.23.1 - 2018-08-02
## Added
- Add ie-compat meta tag to the index by default. [#316](https://github.com/plotly/dash/pull/316)
- Add `external_script` and `external_css` keywords to dash `__init__`. [#305](https://github.com/plotly/dash/pull/305)
- Dash components are now generated at build-time and then imported rather than generated when a module is imported. This should reduce the time it takes to import Dash component libraries, and makes Dash compatible with IDEs.

## 0.22.1 - 2018-08-01
## Fixed
- Raise a more informative error if a non JSON serializable value is returned from a callback [#273](https://github.com/plotly/dash/pull/273)

## 0.22.0 - 2018-07-25
## Added
- Assets files & index customization [#286](https://github.com/plotly/dash/pull/286)
- Raise an error if there is no layout present when the server is running [#294](https://github.com/plotly/dash/pull/294)


## 0.21.1 - 2018-04-10
## Added
- `aria-*` and `data-*` attributes are now supported in all dash html components. (#40)
- These new keywords can be added using a dictionary expansion, e.g. `html.Div(id="my-div", **{"data-toggle": "toggled", "aria-toggled": "true"})`

## 0.21.0 - 2018-02-21
## Added
- #207 Dash now supports React components that use [Flow](https://flow.org/en/docs/react/).
    To support Flow, `component_loader` now has the following behavior to create docstrings
    as determined in discussion in [#187](https://github.com/plotly/dash/issues/187):
        1. If a Dash component has `PropTypes`-generated typing, the docstring uses the `PropTypes`, _regardless of whether the component also has Flow types (current behavior)._
        2. Otherwise if a Dash component has Flow types but _not `PropTypes`_, the docstring now uses the objects generated by `react-docgen` from the Flow types.

## 0.20.0 - 2018-01-19
## Added
- `exceptions.PreventUpdate` can be raised inside a callback to elegantly prevent
the callback from updating the app. See https://community.plot.ly/t/improving-handling-of-aborted-callbacks/7536/2 for context
and #190 for the PR.

## Changed
- Many pylint style fixes.
  See #163, #164, #165, #166, #167, #168, #169, #172, #173, #181, #185, #186, #193
- New integration test framework #184
- Submodules are now imported into the `dash` namespace for better IDE completion #174

# 0.19.0 - 2017-10-16
## Changed
- 🔒  CSRF protection measures were removed as CSRF style attacks are not relevant
to Dash apps. Dash's API uses `POST` requests with content type
`application/json` which are not susceptible to unwanted requests from 3rd
party sites. See https://github.com/plotly/dash/issues/141 for more.
- 🔒  Setting `app.server.secret_key` is no longer required since CSRF protection was
removed. Setting `app.server.secret_key` was difficult to document and
a very common source of confusion, so it's great that users won't get bitten
by this anymore :tada:

# 0.18.3 - 2017-09-08
## Added
- `app.config` is now a `dict` instead of a class. You can set config variables with
  `app.config['suppress_callback_exceptions'] = True` now. The previous class-based
  syntax (e.g. `app.config.suppress_callback_exceptions`) has been maintained for
  backwards compatibility

## Fixed
- 0.18.2 introduced a bug that removed the ability for dash to serve the app on
  any route besides `/`. This has been fixed.
- 0.18.0 introduced a bug with the new config variables when used in a multi-app setting.
  These variables would be shared across apps. This issue has been fixed.
  Originally reported in https://community.plot.ly/t/flask-endpoint-error/5691/7
- The config setting `supress_callback_exceptions` has been renamed to
  `suppress_callback_exceptions`. Previously, `suppress` was spelled wrong.
  The original config variable is kept for backwards compatibility.

# 0.18.3rc1 - 2017-09-08
The prerelease for 0.18.3

# 0.18.2 - 2017-09-07
## Added
- 🔧 Added an `endpoint` to each of the URLs to allow for multiple routes (https://github.com/plotly/dash/pull/70)

# 0.18.1 - 2017-09-07
## Fixed
- 🐛 If `app.layout` was supplied a function, then it used to be called excessively. Now it is called just once on startup and just once on page load. https://github.com/plotly/dash/pull/128

# 0.18.0 - 2017-09-07
## Changed
- 🔒  Removes the `/static/` folder and endpoint that is implicitly initialized by flask. This is too implicit for my comfort level: I worry that users will not be aware that their files in their `static` folder are accessible
- ⚡️  Removes all API calls to the Plotly API (https://api.plot.ly/), the authentication endpoints and decorators, and the associated `filename`, `sharing` and `app_url` arguments. This was never documented or officially supported and authentication has been moved to the [`dash-auth` package](https://github.com/plotly/dash-auth)
- ✏️ Sorts the prop names in the exception messages (#107)

## Added
- 🔧 Add two new `config` variables: `routes_pathname_prefix` and `requests_pathname_prefix` to provide more flexibility for API routing when Dash apps are run behind proxy servers. `routes_pathname_prefix` is a prefix applied to the backend routes and `requests_pathname_prefix` prefixed in requests made by Dash's front-end. `dash-renderer==0.8.0rc3` uses these endpoints.
- 🔧 Added id to KeyError exception in components (#112)


## Fixed
- ✏️  Fix a typo in an exception
- 🔧 Replaced all illegal characters in environment variable

##🔧 Maintenance
- 📝  Update README.md
- ✅  Fix CircleCI tests. Note that the [`dash-renderer`](https://github.com/plotly/dash-renderer) contains the bulk of the integration tests.
- 💄 Flake8 fixes and tests (fixes #99 )
- ✨ Added this CHANGELOG.md

# 0.17.3 - 2017-06-22
✨ This is the initial open-source release of Dash
