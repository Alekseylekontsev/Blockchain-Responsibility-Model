# How to Use the Blockchain Responsibility Model

The Blockchain Responsibility Model (BRM) is a practical framework for identifying who is responsible for what in a blockchain or distributed-ledger ecosystem. It connects technical architecture, factual control, regulated activities, legal accountability, risk ownership, controls, and evidence.

BRM is designed for multidisciplinary teams working across Legal, Compliance, Risk, Security, Privacy, Engineering, Product, Internal Audit, and external assurance.

> **BRM does not provide regulatory approval or replace legal advice.** It helps an organization produce a consistent, traceable, and evidence-based explanation of its system for authorisation, regulatory dialogue, conformity assessment, due diligence, and ongoing supervision.

## What BRM helps you do

Use BRM to:

- define the real boundary of a blockchain-enabled product or service;
- identify legal entities, technical actors, third parties, and decentralized participants;
- document who holds design, upgrade, emergency, key, treasury, and operational powers;
- determine which activities may trigger regulatory obligations;
- test claims of decentralization against observable control and economic influence;
- allocate legal, risk, control, and evidence ownership;
- identify gaps between policies and the system's actual architecture;
- build a regulator-ready or client-ready evidence package;
- reassess responsibility after a material change, incident, fork, or governance decision.

## Typical use cases

| Use case | Primary output |
|---|---|
| MiCA CASP authorisation | Regulatory perimeter, governance and control record, obligation-to-evidence matrix |
| Token issuance or admission to trading | Token classification, issuer/offeror analysis, white-paper responsibility map |
| Regulatory sandbox or pre-application dialogue | Concise system brief, open legal questions, safeguards and evidence |
| DLT Pilot Regime application | Requested exemptions, risks, compensating controls, responsible owners |
| GDPR DPIA or Article 36 prior consultation | Processing map, controller allocation, data-flow safeguards, residual-risk record |
| CRA conformity assessment | Product boundary, manufacturer/steward role, secure-lifecycle and vulnerability evidence |
| DORA or NIS2 readiness | ICT responsibility, resilience, incident, outsourcing and supply-chain evidence |
| Institutional due diligence | Standardized architecture, custody, governance, security, privacy, and dependency pack |
| Material product or protocol change | Delta assessment showing new actors, powers, obligations, risks, and evidence |
| Incident, exploit, fork, or shutdown | Decision authority, response duties, communication, remediation, and evidence ownership |

## The BRM analysis formula

Analyze the system through seven connected dimensions:

> **Network Profile × Component × Actor × Control Right × Activity × Jurisdiction × Lifecycle Event**

Do not start by asking whether “blockchain” is regulated. Start with the actors, activities, and powers that exist in the actual operating model.

## Recommended workflow

### Step 1 — Define the decision and scope

Record the product, legal entities, jurisdictions, intended decision, assessment date, expected go-live date, exclusions, and assumptions. The output is a one-page system boundary statement.

### Step 2 — Select the network profile

Choose the closest profile and record hybrid characteristics:

- public permissionless L1;
- public L2 or rollup;
- permissioned consortium network;
- private enterprise DLT;
- appchain or sidechain;
- cross-chain protocol;
- dApp built on a third-party public network;
- hybrid on-chain/off-chain financial service.

A project may use more than one profile. For example, a custodial service may operate a centralized application and custody layer on top of a public L1 and third-party bridge.

### Step 3 — Map components and dependencies

Use the technical stack in the [Core Metamodel](standards/core-metamodel.md):

1. infrastructure;
2. client and core protocol;
3. consensus and network operation;
4. data availability and state;
5. interoperability and external data;
6. smart contracts and protocols;
7. wallets, identity, and custody;
8. application, interface, and off-chain services.

For each component, record its owner, operator, hosting location, dependencies, data handled, assets affected, and failure impact.

Include cloud platforms, RPC providers, sequencers, validators, bridges, oracles, indexers, custodians, identity providers, multisig services, frontend hosting, analytics, and critical open-source dependencies.

### Step 4 — Identify actors and factual control

List legal and technical actors separately. A DAO, foundation, software company, multisig committee, validator, frontend operator, and token holder may have different powers even when public communications treat them as one “community.”

For each component, identify:

- Design Authority;
- Implementation Responsibility;
- Operational Control;
- Change or Upgrade Authority;
- Emergency Authority;
- Key or Privilege Custodian;
- Economic Beneficiary;
- Legal or Regulatory Accountable;
- Risk Owner;
- Control Owner;
- Evidence Owner;
- Assurance Provider;
- User or Counterparty Duty Owner.

Document observable facts: admin keys, multisig thresholds, repository permissions, deployment rights, pause functions, governance delegation, treasury access, fee flows, voting concentration, contractual rights, and practical ability to influence another actor.

### Step 5 — Map activities before regulations

Describe what each actor actually does. Examples include:

- issuing, offering, or seeking admission to trading of a token;
- custody or administration of crypto-assets;
- exchange, brokerage, transfer, execution, or order routing;
- operation of a trading platform;
- staking, lending, payment, or redemption services;
- manufacturing or commercially supplying software with digital elements;
- providing managed ICT or critical infrastructure services;
- determining the purposes and essential means of personal-data processing;
- deploying a smart contract to execute a data-sharing agreement.

Only after this activity map is complete should the team assess legal applicability.

### Step 6 — Apply regulatory overlays

Use the [EU Regulatory Applicability Map](regulatory/eu-applicability-map.md) to assess MiCA, CRA, DORA, NIS2, the Data Act, and GDPR.

For every regime, record one of four conclusions:

- **In scope** — the actor and activity meet the applicable conditions;
- **Out of scope** — supported by a documented legal and factual rationale;
- **Conditional** — applicability depends on a fact, threshold, classification, or regulatory interpretation;
- **Unresolved** — external counsel or regulator clarification is required.

Record the applicable legal entity, activity, jurisdiction, effective date, legal source, responsible reviewer, and approval date. Do not assign an entire regulation to the blockchain system without identifying the regulated person and activity.

### Step 7 — Link obligations to controls and evidence

Build a traceability chain for each material obligation:

> **Requirement → Actor → Control right → Risk → Control → Evidence → Owner → Reviewer → Date**

Good evidence should demonstrate both design and operation. Examples include governance approvals, architecture and data-flow diagrams, key-ceremony records, deployment logs, access reviews, SBOMs, vulnerability records, reconciliation records, recovery tests, outsourcing monitoring, DPIAs, complaints, white papers, code reviews, penetration tests, and control attestations.

Use the [EU Regulation to Standards Crosswalk](references/eu-regulation-standards-crosswalk.md) to identify supporting standards. A certification or standard may support assurance, but it does not by itself prove legal compliance.

### Step 8 — Resolve gaps and prepare the dossier

Classify findings as:

- missing accountable actor;
- authority without legal responsibility;
- responsibility without effective authority;
- undocumented dependency;
- control design gap;
- operating-evidence gap;
- conflicting legal and technical descriptions;
- unresolved regulatory interpretation;
- unacceptable residual risk.

Create remediation owners and due dates. Escalate any obligation that no actor can technically or legally perform. Then assemble the relevant output pack.

## Minimum viable assessment

For an early product or initial legal review, start with five artifacts:

1. **system-boundary.md** — product, entities, jurisdictions, assumptions, and exclusions;
2. **architecture-and-data-flows.md** — components, dependencies, asset and personal-data flows;
3. **actor-control-register.yaml** — actors and factual powers;
4. **regulatory-perimeter.md** — in/out/conditional/unresolved conclusions with rationale;
5. **obligation-evidence-matrix.csv** — requirements, controls, evidence, owners, and gaps.

This lightweight assessment is enough to expose most responsibility conflicts before detailed policy drafting.

## Full Regulatory Readiness Pack

For authorisation, sandbox participation, prior consultation, conformity assessment, or institutional due diligence, add:

| Artifact | Purpose |
|---|---|
| **responsibility-matrix.yaml** | Complete legal, risk, control, and evidence allocation |
| **third-party-dependencies.md** | Outsourcing, protocol, cloud, oracle, bridge, RPC, custody, and supply-chain dependencies |
| **decentralisation-assessment.md** | Evidence-based assessment of control, governance, fees, treasury, and concentration |
| **risk-and-control-register.yaml** | Risks, controls, residual risk, owners, treatment, and acceptance |
| **regulatory-questions.md** | Narrow, decision-ready questions for counsel, NCA, DPA, or sandbox |
| **material-change-delta.md** | Responsibility and applicability changes since the approved baseline |
| **submission-index.md** | Document versions, approvals, owners, evidence links, and submission status |

## How different teams should use BRM

### Legal and Compliance

Use BRM to qualify actors and activities, record the legal basis for scope conclusions, identify authorisation or notification requirements, and ensure that legal opinions match factual control.

### Engineering and Product

Validate component boundaries, dependencies, admin capabilities, upgrade paths, emergency mechanisms, key custody, data flows, and technical feasibility of regulatory commitments.

### Security, Privacy, and Risk

Map threats, processing operations, third-party risks, control objectives, residual risks, incident duties, and required assurance evidence to accountable owners.

### Internal Audit and Assurance

Test whether the declared responsibility model matches permissions, contracts, logs, governance records, operational practice, and retained evidence.

### Executive Management and Boards

Approve risk ownership, regulated operating model, critical outsourcing, unresolved interpretations, material changes, and residual risks that cannot be delegated.

## Using BRM with a regulator or external counsel

Do not send the entire repository without context. Prepare a concise decision package:

1. executive summary and requested decision;
2. system boundary and architecture;
3. actor and factual-control map;
4. regulatory-perimeter conclusions;
5. unresolved questions;
6. safeguards, controls, and residual risks;
7. evidence index and responsible contacts.

Ask narrow questions supported by facts. For example:

- Does the described frontend and transaction-routing activity constitute a crypto-asset service?
- Does the documented allocation of protocol and application decisions create joint controllership for the identified processing?
- Are the proposed compensating controls sufficient for the requested DLT Pilot exemption?
- Does the specified software distribution model make the entity a manufacturer or open-source software steward under the CRA?

This approach reduces iterative clarification because the legal question, architecture, control rights, and evidence are presented consistently.

## Reassessment triggers

Repeat the affected BRM steps when any of the following occurs:

- a new token, service, jurisdiction, customer type, or distribution channel;
- deployment on another L1, L2, bridge, or data-availability layer;
- a change to admin keys, multisig membership, voting, treasury, fees, or upgrade powers;
- addition or replacement of a custodian, oracle, RPC, sequencer, validator, cloud, or ICT provider;
- a protocol fork, exploit, insolvency, shutdown, or major incident;
- a new regulatory interpretation or applicable legal date;
- a material architecture, personal-data, outsourcing, or custody change.

Preserve the previous baseline and create a delta assessment rather than rewriting history.

## Source control and review rules

- Pin legal and standards references by identifier, edition, status, and effective date.
- Use [the source register](references/eu-source-register.yaml) for official EU sources.
- Treat draft standards and regulatory consultations as research inputs, not binding requirements.
- Record assumptions and uncertainty explicitly.
- Require Legal approval for regulatory conclusions and accountable management approval for residual risk.
- Retain evidence of who reviewed and approved each baseline.
- Keep confidential keys, personal data, client evidence, and privileged legal advice outside the public repository; link to controlled systems instead.

## Definition of done

A BRM assessment is ready for decision when:

- the system boundary and network profiles are approved;
- every critical component and dependency has an identified operator;
- all material control rights and economic beneficiaries are documented;
- regulated activities and jurisdictions are assessed;
- every applicable obligation has an accountable actor, control owner, and evidence owner;
- unresolved questions are explicit and assigned;
- responsibility-without-authority conflicts are remediated or accepted;
- the evidence index is complete and versioned;
- material residual risks are formally approved.

## Start here

1. Read the [Core Metamodel](standards/core-metamodel.md).
2. Select a network profile and create the five minimum viable assessment artifacts.
3. Apply the [EU Regulatory Applicability Map](regulatory/eu-applicability-map.md).
4. Build obligation-to-control-to-evidence traceability.
5. Review the package jointly with Legal, Compliance, Engineering, Security, Privacy, and Risk.
