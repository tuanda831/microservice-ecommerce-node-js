# [iCommerce](https://i-commerce.com/)


## Blueprints
The Blueprint is divided into several sections:

* [Overview Architecture](/docs/README.md)
* [API Gateway](/api-gateway/README.md)
* [Storefront Sites](/storefront-service/README.md)
* [Search Service](/search-service/README.md)
* [DWH Service](/dwh-service/README.md)
* [Inventory Service](/inventory-service/README.md)
* [CRM Service](/crm-service/README.md)
* [User Service](/user-service/README.md)


## Contact points
You can find the member who can support you on the topics here:
* API Gateway: @tuanda831
* Storefront Sites: @tuanda831
* Search Service: @tuanda831
* DWH Service: @tuanda831
* Inventory Service: @tuanda831
* CRM Service: @tuanda831
* User Service: @tuanda831

## Roadmap

- [x]  Design High-Level Solution
- [ ]  Setup Dev Environment
- [ ]  Implementing the API Gateway
- [ ]  Implementing the Storefront Sites
- [ ]  Implementing the Search Services
- [ ]  Implementing the DWH Services
- [ ]  Implementing the Inventory Services
- [ ]  Implementing the Customers Services
- [ ]  Implementing the Users Services
- [ ]  Setup CI Pipeline
- [ ]  Setup Infra to deployment and CD pipeline
- [ ]  Setup Mornitoring tools, ELK, Grafana and prometheus + alertmanager
- [ ]  Setup Database daily backup

## How to Up and Run Dev Environment

//TODO

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

### Merging Branch Convention

//The master branch

//The stating branch

//The Task branch

### Design Pattern and Convention
* Following SOLID
* Mostly, service code base following the Dependancy Injection pattern
* Generally, Source code structure will be following the [3 Layers architecture](https://medium.com/@deanrubin/the-three-layered-architecture-fe30cb0e4a6)
