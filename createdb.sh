docker run \
      --name influx_db -d \
      -p 8086:8086 \
      -v /home/vortex2jm/dev/python/mpolka-int-database/influxdb_volume:/var/lib/influxdb2 \
      influxdb:latest
