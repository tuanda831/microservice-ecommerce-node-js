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
- [x] Elastic search
- [ ] Redis

## Search Engine:
- [x] Elastic Search
- [ ] Solr
- [ ] Algolia
- [ ] MongoDB

## Cache: 
- [x] memcache
- [ ] Redis

## Mornitoring: 
- [x] ELK, ~~Datadog~~, ~~newrelic~~ 
- [x] Promithius
- [x] Grafana
- [x] Promithius's Alertmanager integrate to email and slack

## Backup: 
- [ ] DB Replica delay 1 day compage to the master.
- [ ] Daily cronjob dump DB, zip, encrypt and store in S3