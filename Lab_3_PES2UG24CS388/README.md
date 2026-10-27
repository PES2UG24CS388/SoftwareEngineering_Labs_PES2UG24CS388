
# Lab 3: Component Modelling & Architectural Pattern Selection

## Problem Statement
**Hospital Bed & ICU Allocation Dashboard System**

## Objective
To select and justify a suitable software architecture for the proposed system.

## Selected Architecture
**Layered Architecture**

The system is organized into three layers:

- **Presentation Layer:** Dashboard UI Component for hospital staff and administrators.
- **Business Layer:** Bed Allocation Manager, ICU Recommendation Engine, Authentication & Access Control, and Alert & Notification components.
- **Data Layer:** Bed & Patient Database Component for storing bed status, patient, and allocation data.

## Architecture Justification

### Reason 1: Separation of Concerns
The architecture separates allocation logic from the user interface and data storage. This allows bed allocation, ICU matching, and alerting rules to be modified independently of the dashboard UI and database schema.

### Reason 2: Suitability for a Centralized Deployment
The dashboard serves a single hospital's wards and ICU. Layered Architecture provides the required separation of concerns without the additional network latency, data-consistency challenges, and operational overhead associated with Microservices Architecture.

## Security Advantage
The Authentication & Access Control component and centralized Data Layer provide consistent enforcement of TLS encryption in transit, encryption at rest, and role-based access for authorized hospital staff, supporting **NFR-002**.

## Performance Benefit
The Bed & Patient Database Component supports performance optimizations such as indexing bed and ICU availability records and caching frequently requested queries. These optimizations help meet **NFR-001**, which requires current availability to load within 2 seconds under 500 concurrent users.

## Deliverables
- Architecture selection and justification
- Layered architecture design
- Component diagram

## Outcome
The system architecture is defined using a layered approach that separates presentation, business logic, and data storage. This provides a maintainable structure with consistent security enforcement and efficient bed and ICU availability lookups.
