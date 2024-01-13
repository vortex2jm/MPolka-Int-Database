from(bucket: "IntData")
  |> range(start: -2d)
  |> filter(fn: (r) => r._measurement == "Connectivity" and r._field == "latency" and r.port == "eth0")
