docker run \
    -p 9090:9090 \
    -v prometheus.yml:/etc/prometheus \
    --rm \
    -d \
    prom/prometheus:v2.31.0

docker run \
    -d \
    --name=grafana \
    -p 3000:3000 \
    --rm grafana/grafana-enterprise:8.2.3-ubuntu