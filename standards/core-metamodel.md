---
title: Blockchain Responsibility Model — Core Metamodel
acronym: BRM
status: draft
version: 0.1
document_type: metamodel
updated: 2026-08-10
---

# Blockchain Responsibility Model — Core Metamodel

> **Status: Draft v0.1.** This document defines the initial structure of the Blockchain Responsibility Model (BRM). It is a working model, not legal advice, a certification scheme, or an assertion that a named actor is liable in a particular jurisdiction.

## 1. Purpose

BRM is a control- and activity-based metamodel for allocating technical, operational, legal, risk, and assurance responsibilities across heterogeneous blockchain and DLT ecosystems.

It addresses a recurring accountability gap: technical decentralization, open-source contribution, a DAO label, or the absence of a single system owner does not by itself identify who designs, controls, changes, benefits from, assures, or answers for a blockchain-based service.

The model uses the following analytical expression:

> **Network Profile × Component × Actor × Control Right × Activity × Jurisdiction × Lifecycle Event**

No single dimension is sufficient. Responsibility is derived from the combined facts of the system and must be reassessed when control, activity, jurisdiction, or system state changes.

## 2. Core principles

1. **Substance over labels.** Allocate responsibility according to factual control, performed activity, decision power, and economic benefit—not only legal title, governance branding, or claims of decentralization.
2. **Component-level attribution.** Assess each component and processing activity separately. Different actors may be accountable for different parts of the same service.
3. **Authority creates duty.** Design, operational, upgrade, emergency, and key-management powers create corresponding duties even when the powers are rarely exercised.
4. **Activity defines regulatory perimeter.** Licensing and compliance obligations usually attach to a person and activity rather than to “the blockchain” as an abstract technology.
5. **Responsibility cannot disappear.** Outsourcing, automation, open-source publication, DAO voting, or a multi-party arrangement may distribute responsibility but must not create an unowned duty.
6. **Shared control requires explicit allocation.** Joint, sequential, or overlapping control must be documented, including decision boundaries and escalation paths.
7. **Assurance follows risk.** Evidence, testing, monitoring, audit, and incident duties must follow the risk owner and the actor able to implement or enforce controls.
8. **Allocation is event-sensitive.** Forks, upgrades, exploits, insolvency, key compromise, governance capture, and shutdown may change the responsible actor.

## 3. Four-plane model

BRM separates four kinds of concerns that are often mixed in a single architecture diagram or RACI matrix.

### 3.1 Technical stack

| ID | Layer | Typical components |
|---|---|---|
| T1 | Physical & Cloud Infrastructure | Compute, hosting, data centers, HSM, network connectivity, DDoS protection |
| T2 | Client & Core Protocol | Client software, P2P protocol, execution environment, protocol parameters |
| T3 | Consensus & Network Operation | Validators, miners, staking pools, sequencers, provers, builders, finality mechanisms |
| T4 | Data Availability & State | Ledger storage, archive nodes, DA layers, indexing, off-chain and decentralized storage |
| T5 | Interoperability & External Data | Bridges, relayers, cross-chain messaging, oracles, price feeds |
| T6 | Smart Contracts & Protocols | Token, DeFi, governance and upgrade contracts; proxies; admin functions |
| T7 | Wallet, Identity & Custody | Wallets, MPC, account abstraction, recovery, custody, identity and KYC services |
| T8 | Application, Interface & Off-chain Services | Web/mobile UI, API, RPC, backend, analytics, routing, notification and support services |

A product may use several instances of a layer and several independent companies may control components inside the same layer.

### 3.2 Control planes

Control planes cut across the technical stack:

- governance and voting;
- protocol and parameter changes;
- software release and upgrade authority;
- emergency pause, rollback, censorship, recovery, or shutdown powers;
- private keys, multisig, MPC, timelocks, and privileged identities;
- treasury and reserve management;
- token issuance, distribution, incentives, fees, MEV, staking rewards, and slashing;
- vendor and dependency selection;
- admission, permissioning, and user-access rules.

The **Economic & Incentive Plane** is explicit because fees, voting concentration, treasury control, and benefit flows can reveal effective influence that architecture diagrams miss.

### 3.3 Regulatory overlays

Compliance is not a single technical layer. The relevant overlay is selected by activity, asset/service classification, actor, user location, and jurisdiction.

| Domain | Example questions |
|---|---|
| Asset and service classification | What is issued or provided, and under which legal category? |
| Authorization | Is registration, licensing, notification, or regulatory approval required? |
| AML/CFT and sanctions | Who onboards, screens, monitors, blocks, reports, and retains evidence? |
| Travel Rule | Who is the obligated originator/beneficiary service provider? |
| Issuance and disclosures | Who is issuer, offeror, promoter, admission sponsor, or disclosure owner? |
| Market integrity | Who monitors manipulation, conflicts, insider information, and governance abuse? |
| Custody and client assets | Who controls keys, segregation, reserves, redemption, and recovery? |
| Consumer protection | Who owns disclosures, suitability, complaints, user warnings, and redress? |
| Privacy and data governance | Who determines purposes/means, acts as controller/processor, and handles rights and transfers? |
| Cybersecurity and resilience | Who manages security controls, continuity, testing, incidents, and regulatory reporting? |
| Outsourcing and third parties | Who performs due diligence, contracting, concentration analysis, and ongoing oversight? |
| Tax, accounting, and records | Who calculates, reports, reconciles, retains, and produces records? |
| IP and open source | Who owns or licenses code, content, trademarks, and dependencies? |

Certification and audit provide assurance; they do not replace a required license or transfer regulatory accountability.

### 3.4 Assurance plane

The assurance plane includes:

- threat modeling and risk assessment;
- architecture and economic-security review;
- code review, testing, fuzzing, invariant testing, and formal verification;
- external smart-contract and infrastructure audits;
- build provenance and deployment verification;
- control monitoring, observability, and anomaly detection;
- dependency, vendor, and concentration-risk monitoring;
- evidence collection and retention;
- control attestations and certifications;
- incident detection, notification, investigation, recovery, and lessons learned;
- periodic reassessment following material changes.

## 4. Network profiles

The same metamodel is instantiated differently for each profile:

| ID | Network profile | Distinguishing responsibility questions |
|---|---|---|
| N1 | Public permissionless L1 | Client diversity, validator concentration, forks, foundation/core-developer influence |
| N2 | Public L2 / rollup | Sequencer, prover, bridge, DA, upgrade keys, forced exit and inherited L1 dependencies |
| N3 | Permissioned consortium network | Membership, consortium governance, node obligations, shared controller and exit rules |
| N4 | Private enterprise DLT | Enterprise ownership, outsourcing, operator access, internal control and vendor allocation |
| N5 | Appchain / sidechain | Validator set, bridge trust, upgrade authority, inherited security and economic incentives |
| N6 | Cross-chain protocol | Source/destination assumptions, relayers, message verification, bridge custody and recovery |
| N7 | dApp on a third-party network | Smart contracts, frontend, admin keys, wallet/RPC dependencies and network risk acceptance |
| N8 | Hybrid on-chain/off-chain financial service | Custody, backend decisioning, legal entity, client relationship, reconciliation and redress |

Profiles are templates, not conclusions. A concrete system may combine several profiles.

## 5. Actor classes

BRM does not assume that one legal entity owns an end-to-end system. Relevant actors may include:

- protocol founders, core developers, maintainers, and open-source contributors;
- foundations, legal wrappers, associations, DAOs, delegates, councils, and token holders;
- infrastructure, cloud, node, validator, sequencer, prover, builder, and staking operators;
- bridge, oracle, relayer, DA, indexer, RPC, API, and storage providers;
- smart-contract deployers, protocol teams, multisig signers, guardians, and treasury managers;
- wallet, custody, identity, KYC, exchange, broker, payment, lending, and staking providers;
- frontend operators, mobile publishers, integrators, aggregators, and support providers;
- users, institutional clients, liquidity providers, and governance participants;
- auditors, certification bodies, monitoring providers, insurers, and incident responders;
- regulators, courts, insolvency practitioners, and law-enforcement bodies where relevant.

An organization may occupy several actor classes; one actor class may be split across multiple organizations.

## 6. Responsibility dimensions

RACI may be used for a bounded operational process, but BRM requires distinct attribution fields:

| Dimension | Allocation question |
|---|---|
| Design Authority | Who defines architecture, requirements, trust assumptions, and acceptable behavior? |
| Implementation Responsibility | Who builds, configures, integrates, and verifies the component? |
| Operational Control | Who runs the component and controls its day-to-day behavior? |
| Change / Upgrade Authority | Who can change code, parameters, dependencies, membership, or configuration? |
| Emergency Authority | Who can pause, censor, rollback, recover, rotate, migrate, or shut down? |
| Key / Privilege Custodian | Who possesses or can activate privileged credentials or signing power? |
| Economic Beneficiary | Who receives fees, rewards, treasury value, appreciation, or another material benefit? |
| Legal / Regulatory Accountable | Who holds the authorization, client duty, reporting duty, or legal accountability? |
| Risk Owner | Who accepts, treats, transfers, or escalates residual risk? |
| Control Owner | Who designs and maintains the control that mitigates the risk? |
| Evidence Owner | Who produces, protects, retains, and provides evidence that the duty was performed? |
| Assurance Provider | Who independently tests or attests, without assuming management accountability? |
| User / Counterparty Duty Owner | Who communicates terms, risks, incidents, complaints, remedies, and exit options? |

Multiple values are allowed, but every allocation must state whether responsibility is exclusive, joint, shared, sequential, delegated, or inherited.

## 7. Allocation method

For every in-scope component or activity:

1. **Select network profile(s).**
2. **Identify the component and technical layer.**
3. **Enumerate actors, including dependencies and privileged collectives.**
4. **Record factual control rights**, including indirect, emergency, economic, and governance influence.
5. **Identify performed activities** and applicable product/service classifications.
6. **Select jurisdictional overlays** for each actor, user group, and activity.
7. **Allocate responsibility dimensions** and state the allocation mode.
8. **Map risks, controls, evidence, and assurance.**
9. **Define lifecycle and crisis events** that trigger reassessment or transfer.
10. **Validate gaps and conflicts:** no duty may remain unowned; no actor may be named accountable without authority or enforceable recourse.

## 8. Minimum responsibility record

Each allocation should be machine-readable and contain at least:

| Field | Required content |
|---|---|
| record_id | Stable unique identifier |
| system / profile | System boundary and selected network profile |
| component_id / layer | Component and T1–T8 classification |
| actor_id / legal_entity | Technical actor and, where known, accountable person/entity |
| activity | Function actually performed |
| jurisdiction / user_scope | Applicable location and affected population |
| control_right | Nature, threshold, and technical mechanism of influence |
| responsibility_dimension | One or more dimensions from Section 6 |
| allocation_mode | Exclusive, joint, shared, sequential, delegated, or inherited |
| risk / control | Risk owned and control maintained |
| evidence | Evidence type, producer, repository, retention, and reviewer |
| dependencies | Upstream/downstream actors and inherited assumptions |
| trigger_event | Event requiring review, transfer, notification, or escalation |
| effective_period | Start, end, and review date |
| confidence / rationale | Evidence-backed reasoning and unresolved uncertainty |

## 9. Inheritance and escalation rules

1. **Inherited security is documented, not assumed.** A dApp inherits network properties but remains responsible for selecting the network, disclosing material dependencies, and controlling its own layers.
2. **Delegation does not equal transfer.** A delegating actor retains oversight unless law and enforceable agreement validly allocate otherwise.
3. **Privileged fallback overrides nominal decentralization.** Admin keys, guardians, emergency councils, upgrade committees, or hosted frontends must be visible in the allocation.
4. **Economic concentration is an escalation indicator.** Concentrated voting power, fees, MEV, stake, treasury, or token holdings trigger enhanced control and accountability analysis.
5. **Interface control matters.** A party that curates access, routes transactions, sets defaults, geoblocks, charges users, or provides support may have duties even without changing smart contracts.
6. **Unowned obligations escalate.** Any missing risk, control, evidence, incident, or regulatory owner is a governance defect requiring resolution before release or continued operation.
7. **Conflicting authority escalates.** Where an actor is accountable but lacks change or emergency authority, the gap must be closed through governance, contract, technical control, or explicit risk acceptance.
8. **Material events trigger reassessment.** At minimum: ownership or governance change, fork, upgrade, new jurisdiction, new regulated activity, exploit, key compromise, insolvency, major dependency change, or shutdown.

## 10. Relationship to lifecycle

Lifecycle is one projection of BRM, not the organizing model itself.

For each lifecycle stage—design, build, test, deploy, operate, respond, upgrade, and sunset—the responsibility record identifies:

- the affected component and network profile;
- the actor exercising each control right;
- the risk, legal, control, evidence, and assurance owner;
- the decision gate and required evidence;
- responsibility transfers or changes caused by the event.

The existing [DeFi dApp Development Project Lifecycle](defi-dapp-development-lifecycle.md) will be normalized against this metamodel in a later revision.

## 11. Initial source basis

BRM integrates concepts from existing architecture, governance, legal, privacy, and decentralization work. Its intended contribution is the unified responsibility-allocation method rather than a claim that its individual layers are novel.

- [ISO/TC 307 standards catalogue](https://www.iso.org/committee/6266604/x/catalogue/)
- [UNCITRAL Model Law on Automated Contracting and DLT-related materials](https://uncitral.un.org/)
- [NIST IR 8301: Blockchain Networks — Token Design and Management Overview](https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8301.pdf)
- [Governance challenges of blockchain and decentralized autonomous organizations](https://pure.tudelft.nl/ws/portalfiles/portal/85677186/IP_190154.pdf)
- [Taxonomy of centralization in public blockchain systems](https://arxiv.org/abs/2009.12542)
- [EDPB Guidelines 02/2025 on processing personal data through blockchain technologies](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-022025-processing-personal-data-through_en)
- [FATF guidance for virtual assets and VASPs](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html)
- [EU Markets in Crypto-assets Regulation (MiCA)](https://eur-lex.europa.eu/eli/reg/2023/1114/oj)

## 12. Planned profiles and artefacts

- canonical actor and component taxonomy;
- YAML/JSON responsibility-record schema;
- profile templates for N1–N8;
- control-right and economic-influence assessment;
- regulatory-activity decision trees by jurisdiction;
- responsibility matrices for normal operation and crisis events;
- evidence catalogue and assurance mapping;
- worked examples for an L1, L2, consortium DLT, cross-chain protocol, and hybrid DeFi service;
- normalization of the lifecycle draft against BRM.
