---
hide:
  - navigation
---

# GraphQL vs. REST vs. SQL vs. gRPC vs. OData vs. MongoDB

## GraphQL vs. REST
**GraphQL** is a query language that lets you query an API for specific data through a single endpoint.

**REST** is an API architectural style or design pattern that describes how APIs should be built. REST APIs typically have multiple endpoints and return a lot more data than necessary for users.

Consider GraphQL if you have complex schemas or need better performance on queries.

Consider REST if you want to build an API with structured querying for a large number of consumers, or resource based API.

## GraphQL vs. SQL
**GraphQL** is a flexible query language that uses a type system to efficiently return data with dynamic queries.

**SQL(structured query language)** is an older, more adopted language standard used specifically for tabular/relational database systems.

Consider GraphQL if you want your API to be built on a NoSQL database.

Consider SQL if you want a query language for managing relational database systems.

## GraphQL vs. gRPC
**GraphQL** is a specialized query language that does away with API versioning and provides predictable, single-point data access methods with fields and types.

**gRPC** is a Google-developed data exchange technology that uses a binary format for fast data delivery and streaming.

Consider GraphQL if you have multiple complex data sources or API architectures you want to aggregate to a single endpoint.

Consider gRPC if you want to have rapid communication between internal APIs such as microservices.

## GraphQL vs. OData
**GraphQL** is a query language that, by showing what queries are available in advance, lets you query only the data you need.

**OData** is a standardized protocol that defines best practices for building and using REST APIs.

Consider GraphQL for a specification with comparatively greater adoption and performance in the case of mobile APIs and newer technologies.

Consider OData for a more mature API with a lower barrier to entry that implements the required REST specifications. OData will also allow for a reasonable learning curve for your API consumers.

## GraphQL vs. MongoDB
**GraphQL** is an API query language and server-side runtime for executing queries with your existing code and data.

**MongoDB** is a popular NoSQL database that provides storage for unstructured data in a JSON-like format.

Consider GraphQL if you want to create a GraphQL API for an existing database system and use a built-in IDE to build and test queries.

Consider MongoDB if you're managing and delivering content/data that can require scaling. MongoDB and GraphQL can be used together.

## MongoDB vs. SQL
**MongoDB** is a NoSQL database that flexibly stores data using key-value pairs that can include nested key-value pairs or arrays.

**SQL** is a query language standard for relational databases. SQL databases are more rigid and store data in tables and rows.

Consider MongoDB if you want to store loosely structured or unstructured data.

Consider SQL if you want to store structured and/or transactional data where expected change or growth is minimal or non-existent.

## gRPC vs. REST
**gRPC** is a modern Remote procedure call framework that uses HTTP/2 and a data serializing method for increased performance with communication or storage applications.

**REST** is an architectural model for APIs to follow the HTTP request and response cycle. REST APIs typically use text-based (JSON or XML) formats for data.

Consider gRPC if you require efficient communication between microservices or cloud services.

Consider REST if want a widely used and supported API framework to work with human-readable data.

## OData vs. REST
**OData** is a web based protocol that defines best practices for building and using REST APIs.

**REST** is a widely adopted architectural style describing how APIs should be built.

Consider OData if you want to build a REST API while focusing on the functionality of the API. OData assists in implementing REST specifications.

Consider REST if would like to build custom APIs that do not strictly implement REST specifications.

