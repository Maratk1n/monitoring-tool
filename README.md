# Monitoring tool

## Ports

The services in the app run on the following ports:

| Host Port | Service |
| - | - |
| 3000 | Grafana |
| 5000 | Receiver (Flask) |
| 127.0.0.1:8086 | InfluxDB |
| 127.0.0.1:8888 | Chronograf |

## Volumes

The app creates the following named volumes (one for each service) so data is not lost when the app is stopped:

* influxdb-storage
* chronograf-storage
* grafana-storage

## Database

The app creates a default InfluxDB database called `db0`.

## Data Sources

The app creates a Grafana data source called `InfluxDB` that's connected to the default IndfluxDB database (e.g. `db0`).

To provision additional data sources, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#datasources) and add a config file to `./grafana-provisioning/datasources/` before starting the app.

## Dashboards

Grafana uses dashboard which located at `./grafana-provisioning/dashboards/maple_farm.json`.

To provision additional dashboards, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#dashboards) and add a config file to `./grafana-provisioning/dashboards/` before starting the app.
