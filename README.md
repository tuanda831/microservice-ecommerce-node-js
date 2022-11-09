<p align="center">
    <a href="#">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiJTzaR29x3TcQ9S3tKDaIdi_0KBjZLfr8FxvAGz3zfDuZhZJKvo_TE_vMiNSZhyQFdMk&usqp=CAU" height="100" alt="Inventory Service">
    </a>
</p>

<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/npm-v6.3.0-blue" alt="npm@6.3.0">
    </a>
    <img src="https://img.shields.io/badge/node-%3E%3D%2014.0.0-brightgreen" alt="node@>14.0.0">
    <img src="https://img.shields.io/badge/license-Apache2-blue.svg?style=flat" alt="Apache 2">
</p>

# [Microservice with Node JS](https://www.linkedin.com/in/tuando831/)

## Blueprints
The Blueprint is divided into several sections:

* [Overview Architecture](/docs/README.md)
* [API Gateway](https://github.com/tuanda831/api-gateway)
* [Users Service](docs/users/README.md)
* [Storefront Sites](/docs/storefront/README.md)
* [Search Service](https://github.com/tuanda831/search-service)
* [Data Warehouse Service](/docs/data-warehouse/README.md)
* [Inventory Service](https://github.com/tuanda831/inventory-service)
* [Customers Service](docs/customers/README.md)

## Contact points
You can find the member who can support you on the topics here:
* API Gateway: @tuanda831
* Users Service: @tuanda831
* Storefront Sites: @tuanda831
* Inventory Service: @tuanda831
* Customer Service: @tuanda831
* Search Service: @tuanda831
* Data Warehouse Service: @tuanda831

## Roadmap

- [x]  Design High-Level Solution
- [x]  Setup Dev Environment
- [x]  Implementing the Inventory Services
- [ ]  Implementing the Search Services
- [ ]  Implementing the API Gateway
- [ ]  Implementing the Storefront Sites
- [ ]  Implementing the Users Services
- [ ]  Implementing the Customers Services
- [ ]  Implementing the Data Warehouse Services
- [ ]  Setup CI Pipeline
- [ ]  Setup Infra to deployment and CD pipeline
- [ ]  Setup Mornitoring tools, ELK, Grafana and prometheus + alertmanager
- [ ]  Setup Database daily backup

## How to Up and Run Dev Environment
### Native Application Development

- Install python to run script pull source code from other services repo
- Install docker/docker-compose on the local machine

```bash
# Pull all service in one place to mock the dependancy
./prepare.py

# Up the dependant resources (DB, Search Engine...)
docker-compose up -d
```

### Access Resource in Local environment

1. Connect with PostgreSQL

    > Recommend [TablePlus](https://tableplus.com/), dbeaver

    ```
    POSTGRES_USER=dev_user
    POSTGRES_PASSWORD=dev_pass
    POSTGRES_DB=inventory_db (users_db...)
    ```

2. API Gateway URL: `http://localhost:8000`
    - Search Endpoint: `/storefront` (port: 8080)
    - Search Endpoint: `/admin` (port: 3000)
    - Users Endpoint: `/users` (port: 3001)
    - Inventory Endpoint: `/inventory` (port: 3002)
    - Search Endpoint: `/search` (port: 3003)
    - Search Endpoint: `/data-warehourse` (port: 3004)
    - Search Endpoint: `/customers` (port: 3005)

3. APIs Document (Swagger): http://localhost:8000/{service-slug}/docs

## How to access QA Environment

//TODO

## Contributing Guidelines

The main purpose of this document is to summary, Giving you an all in one page to explore the platform the contributing guidline will be detail in each Services. Below is some common guidelines which is apply across the teams.

### Commit message convention

Before committing code in this repository it is important to read the guidelines below.

Commit messages that apply the conventional commit pattern should be structured like this:

```
<type>(scope): <description>
```

where the structural elements of type, scope and description are meant to communicate intent of the commit content to
both humans and machine:

Must be one of the following:

* build: MR introduces changes to the build process
* ci: MR introduces changes to ci/cd pipelines
* docs: MR introduces changes to the documentation
* feat: MR introduces changes to an existing features or a new one
* fix: MR introduces changes that fix a reported bug
* perf: MR introduces changes that are related to performance
* refactor: MR introduces changes that neither fixes a bug nor adds/changes a feature
* style: MR introduces changes that formatting, naming, styling etc...
* test: MR introduces changes that add missing tests or correcting existing ones
* revert: MR reverts a previously merged commit

### Design Pattern and Convention
* Following SOLID
* Mostly, service code base following the Dependancy Injection pattern
* Generally, Source code structure will be following the [3 Layers architecture](https://medium.com/@deanrubin/the-three-layered-architecture-fe30cb0e4a6)
