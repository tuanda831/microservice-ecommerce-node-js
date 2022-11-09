# Overview Architecture

## Services Map
![Service Map](service-map.drawio.png "Title")

## Tech Stacks

### Architech:
- Microservices
- CQRS (Command Query Responsibility Segregation)
- Event Sourcing

### Deployment Stacks
- [x] DNS and DDOS Protection with Cloudflare
- [x] Kubenates
- [x] GCP - Bigquery
- [x] GCP - Cloud Store
- [x] GCP - Cloud SQL
- [x] Security with OpenVPN
- [x] Ansible to Devops automation
- [x] Teraform to IaC
- [ ] Anthos (Multi-Cloud)
- [ ] AWS
- [ ] Azure
- [ ] Others

### Service's Communicate:

- [x] Event Sourcing (Temporal, ~~Kafka~~, ~~RabbitMQ~~, ~~Redis~~)
- [x] REST APIs
- [ ] gRPC
- [ ] Socket.IO

### Storage: 
- [x] PostgreSQL, ~~Mysql~~
- [x] Minio (Interface for AWS S3, Cloud Store - GCP, others...)
- [x] BigQuery
- [x] MemCache
- [ ] Solr ~~Elastic search~~
- [ ] Redis

## Search Engine:
- [ ] Elastic Search
- [x] Solr
- [ ] Algolia
- [ ] MongoDB

## Cache: 
- [x] memcache
- [ ] Redis

## Observability vs Monitoring: 
- [x] Grafana Loki, ~~ELK, Datadog, newrelic~~ 
- [x] Promithius
- [x] Grafana Tempo (Distributed tracing)
- [x] Grafana Oncall (Alertmanager integrate to email and slack)

## Backup: 
- [ ] DB Replica delay 1 day compage to the master.
- [ ] Daily cronjob dump DB, zip, encrypt and store in S3