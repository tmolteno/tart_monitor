# TART_monitor

Author: Tim Molteno

Basic Monitoring Service for TART telescopes

## Client

This runs on each tart as a microservice. Sends a ping with its basic info to the server at regular intervals (1 minute). This will cause a callback to the /api/v1/info endpoint. 


## Server

Runs inside the tailnet, listening on a host tart-monitor

API:

/tart/list GET list of running TARTS and their status
/tart/update PUT tell of a new TART. This causes a callback on the /api/v1/info endpoint.

