# stats-server
A tiny web server that collects and saves statistics on application usage.

Example:

``` curl -d '{"command":"get_account", "version":"1.0.5"}' -H "Content-Type: application/json" -X POST https://andli-stats-server.herokuapp.com/pymkm ```