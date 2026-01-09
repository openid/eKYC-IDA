# Delegated Authority for Digital Trust: Human and AI-Enabled Delegation, Consent, and Oversight #

## Scope ##
This technical standard defines frameworks, requirements, and best practices for verifying, assigning, managing, and revoking delegated authority within digital systems. It applies to all actors, humans and AI agents, who seek or are granted authority to act on behalf of others, whether the represented parties are individuals (children, adults), organisations, or automated systems, across domains including online services, SaaS platforms, healthcare and business process automation.
The aim is to ensure that this standard is designed to be modular and extendable, supporting both human-centered and fully automated use cases, and aligns with OpenID Foundation, Kantara UMA and ISO approaches for delegated authority and trust management in federated digital environments.

## The standard supports: ##
- **Verification of delegated authority chains**, including for complex relationships (legal guardianship, organisational structures, agency assignments, AI agent enablement).
- **Secure provisioning and deprovisioning of rights**, conditional and time-bound delegation, and interoperable logging/audit mechanisms for compliance and transparency.
- **Enabling both human and non-human delegates** (AI agents, bots) to act within defined scopes, subject to granular constraints (purpose, data access, transaction rights), and mandatory revocation.
- **Use in regulatory contexts**, such as the AI Act, GDPR, DORA, COPPA, DSA, Anti-Money Laundering, health and research participation, and more, where proof of authority and due diligence is critical.

## Core Use Cases ##
**Delegated authority involving children**, including:
- Parents, foster carers, or agency representatives acting for minors in both offline (established) and online safeguarding contexts. The latter are emerging and the subject of a policy framework which is being developed in alignment with and to complement this standard.
- Children in alternative care where legal guardianship may transfer due to changes in care pathways over time.​
- Teens or older minors participating in progressive assent scenarios (e.g., medical research or data consent), where consent may come from both legal guardian and mature minor, jointly or conditionally. (factor in Rune’s requirements)

**Delegated authority for AI agents:**
- AI systems acting for individuals or entities in online transactions, customer support, or data processing, bounded by explicit credentials, purpose limitations, and transparency requirements. Take into account https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/
- SaaS platforms or B2B ecosystems where an organisation delegates an AI agent to act under contractual or policy-based rules, with secure, auditable flows and instant revocation.
- Cross-context scenarios: where AI agents negotiate or execute on behalf of other AIs, organisations, or humans in a federated digital ecosystem. (take into accounts Eve M’s UMA protocol - https://docs.kantarainitiative.org/uma/rec-uma-core.html#rfc.section.1.3.4)

**Questions:** It was suggested at last week’s OIDF KYC meeting that we reference UMA protocol. Throughout the UMA protocol, all delegated access, claims collection, permission registration, and token revocation depend on the authorisation server as the policy and trust anchor between the resource owner, resource server, and requesting party

-------

OpenID Federation serves as a trust governance backbone by allowing AI agents to participate as verified entities within a federated ecosystem - see diagram which includes Authz Server: Raidiam's OpenID Federation implementation presented at Internet Identity Workshop (IIW),

![Screenshot 2025-12-17 at 20.32.02.png](https://bitbucket.org/repo/nkyb7qg/images/1642907569-Screenshot%202025-12-17%20at%2020.32.02.png)

- Agent registration - Each AI agent can be registered with signed metadata describing its capabilities, permissions, and compliance posture.
- Federated verification - Organizations can automatically verify external agents before granting access to internal or partner APIs.
- Policy enforcement - Federation operators define authentication methods, token policies, and even trust scores or isolation boundaries.

The result is a secure, interoperable marketplace where AI agents from different vendors can interact under shared, verifiable trust rules - paving the way for scalable and regulated AI ecosystems.
- For alternative care scenarios, we are focused on enabling third parties to verify legal guardianship (often still outside any digital UMA-compliant framework). Any move toward UMA-style digital delegation is a future (aspirational) direction, not immediate reality for child safeguarding systems, because of the sheer challenge of working with governments, funding, disparate non-uniform systems
We need to consider / include these caveats to ensure we map the desired architectural model for digital trust and delegation, but also ground our recommendations in current and near-future operational realities for child welfare and legal guardianship contexts.

------

## Terms and Definitions ##
- Delegator / Delegated Authority: ISO 37000:2021 (Governance of organizations—Guidance) acknowledges delegated authority as the practice where an entity empowers another to make decisions or take actions on its behalf, and stresses clarity in delegation for good governance.​
- Delegate: ISO Glossary defines a delegate as a person or entity nominated to represent or act on behalf of another, confirming the principle of explicit assignment and representation.​
- Delegated Authority Chain: The OpenID Foundation’s OpenID Federation draft specifies “delegation” as a claim representing the granting of authority from one entity to another, and discusses chains of delegation in federated trust and control contexts.​ https://openid.net/specs/openid-federation-1_0.html#name-terminology
- Progressive Assent/Consent (new term /definition): The Kantara Initiative’s UMA protocol and glossary introduces the concept of dynamic “scope” and the evolution of consent for access and action, supporting scenarios where authority aligns with evolving capacity or regulation.​
    - UMA enables resource owners (who may be individuals or their legally empowered agents) to set access policies for their resources and to define claims collection workflows (Sections 1 and 3 of the core spec), allowing for fine-grained access control, but the specifics of progressive or staged consent based on maturity, age, or circumstance are left to application-level policy, not directly defined in the protocol specification. (In the context of the delegated authority policy framework I am working on, we are currently mapping these)
- AI Agent: The OpenID Foundation, in whitepapers addressing agent native identity and delegated authority, discusses the assignment of authority to software agents (AI systems) and their subsequent fiduciary and operational responsibilities - see https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/
- Provisioning/Deprovisioning: ISO service management and delegation frameworks clarify that provisioning/deprovisioning are essential life-cycle events, requiring formal initiation, approval, logging, and revocation for compliance and auditability.​ (Covered in ISO 20000 is an international standard for IT Service Management (ITSM).
  - While not explicitly mentioning "delegation," ISO 20000's emphasis on defined processes, roles, and responsibilities inherently requires a structured approach to how tasks and decisions are executed. For instance:
    - Change Management: Delegating authority for approving high-risk changes.
    - Incident Management: Delegating resolution authority or escalation points.
    - Problem Management: Delegating investigation and root cause analysis responsibilities.
    - Service Level Management: Ensuring delegated responsibilities align with negotiated service levels.
  - Delegation Contribution: ISO 20000 ensures that any delegated authority is integrated into established service processes, documented, and contributes to the overall quality and reliability of IT services. It promotes accountability within the service delivery chain, where delegated tasks must still meet service objectives. (currently exploring the scope to extrapolate from these IT systems requirements to legal guardianship contexts in the supporting policy framework)
- Constraint Propagation: UMA and OpenID Federation standards support the persistent enforcement of scope and constraints set by the original delegator throughout all delegation chains, as part of the core claims and policy framework.​ 
  - Constraint propagation is handled within UMA through policy enforcement by the authorization server. Section 3.1 and 3.4 of the core spec detail how access scopes and authorization data are associated with tokens, and Section 2.3.3 of the trust obligations document specifies that the Resource Server Operator is obligated to respect and enforce the permissions set by the Authorization Server, thereby propagating constraints through every access and delegation.
    - Map current paper based and IT based operations in the absence of UMA in a children in alternative care contexts
- Revocation Mechanisms: Kantara UMA protocol details how authorization grants and permissions can be revoked at any time, with policy-driven enforcement and immediate effect.​
    - Specifically, UMA revocation is achieved through immediate or scheduled token invalidation, permission expiry, or policy change, and enforced by the resource server’s requirement to always validate the current status of a token with the authorisation server.

Neither "progressive assent/consent" nor "constraint propagation" appear as formal, explicitly labeled sections, in UMA or OIDF but their functional equivalents can be inferred from the authorisation, claim gathering, and permission management flows.

## Reference Standards and Normative Documents ##
This section lists the standards and specifications referenced in this document, including baseline protocols and relevant legal or regulatory instruments (“normative references”). Implementations must conform to these wherever cited.
- OAuth 2.0 (RFC 6749)
- UMA Core Protocol (Kantara Initiative)
- OpenID Connect / OpenID Federation
- ISO/IEC 29115 (Entity authentication assurance) - currently being updated - The standard was published in April 2013 and is currently under systematic review, with the status "International Standard to be revised" as of May 2024. A new working draft, ISO/IEC WD 29115.3, is under development and is intended to replace ISO/IEC 29115:2013. The standard is recognized internationally, with identical versions published by various national standards bodies, including NEN, BSI, CEI UNI, UNI CEI, INCITS, and PN. It is also referenced by other standards such as ISO/IEC 27001:2013, ISO/IEC 19792:2009, and ISO/IEC 29100:2011.
- AI Act, Digital Operational Resilience Act, GDPR, DSA, AML, COPPA (as applicable)

## Architecture and Roles ##
To be added - a description of the standard’s core architecture, including actors (delegators, delegates, authorization server, resource server, custodians, AI agents, etc.), their responsibilities, and how they interact in delegated authority workflows.

## Functional and Security Requirements ##
Detailed requirements for:
- Identity proofing and authentication of all roles.
- Credential issuance, storage, and management.
- Delegation and chaining of authority (including policy expression and inheritance).
- Consent management: collecting, storing, updating, and auditing consent/delegation records.
- Security properties: confidentiality, integrity, auditing, and non-repudiation.
- Lifecycle events: provisioning, usage, revocation, re-provisioning, logging.

## Protocol Flows and Interactions ##
Step-by-step interaction models covering core use cases (delegation setup, delegated transaction, revocation, consent updates, audit events, and error handling). 
Presents step-by-step message flows and sequences for:
- Granting delegated authority.
- Exercising delegated rights (e.g., acting for a child on a fintech /health tech platform, AI processing, or organisational authorisation).
- Revoking or updating delegated rights.
- Consent withdrawal and conflict resolution.
- Error or incident response handling.
We need to include diagrams and canonical message formats/references to protocols.

## Data Models and Schemas ##
Definitions of credentials, tokens, consent receipts, constraint expressions, and metadata needed to support interoperability (with examples).
- Data fields for roles, constraints, validity, source, and audit log references.
- Sample credential definition (e.g., JWT, Verifiable Credential, or schema-neutral JSON).
- How consent/authority is described, updated, and bound to domain-specific or cross-domain identifiers.

## Compliance and Conformance ##
Defines how implementers demonstrate compliance, including:
- Required behaviours and minimal test cases.
- Optional features (“may”/“should” vs. “must” normative language).
- Mappings to regulatory requirements (such as Article 8 GDPR, COPPA, AMLD, AI act, DSA transparency etc).
- Certification or attestation procedures.
  - Required tests and outcomes for implementers to claim conformance to the standard - Will OIDF develop /adapt 

## Use Cases and Implementation Guidance ##
Elaborated user journeys and domain-specific guidance showing how the standard is adapted across sectors (health, child protection, SaaS, B2B, IoT, etc.).
Expands on practical examples:
- Child and Parental Rights Protection: Delegated authority in parental, alternative care, or progressive assent settings.
- Corporate and SaaS environments: Delegation to human administrators or AI agents.
- AI agent autonomy, limits, revocation, and transparency in real-world automation.
- Cross-jurisdiction scenarios (federation and interoperability).

## Annexes ##
Glossary, 
threat model, 
implementation patterns, 
and possibly sample policies, configurations, or open-source reference implementations.
Each section will methodically build on the scope and definitions to ensure clarity, completeness, and actionable guidance for implementers and auditors.
