# Blockchain Responsibility Model (BRM)

A control- and activity-based metamodel for allocating technical, operational, legal, risk, and assurance responsibilities across heterogeneous blockchain and distributed-ledger ecosystems.

> **Core proposition:** responsibility follows factual control, performed activity, decision authority, and economic benefit—not only technical layer, legal title, or a claim of decentralization.

## Repository status

This repository is under active development. Documents marked **Draft** capture working models and are not approved policy, legal advice, certification criteria, or normative requirements.

## Start here

- [Blockchain Responsibility Model — Core Metamodel](standards/core-metamodel.md) — the primary model: technical stack, control planes, regulatory overlays, assurance, network profiles, actor classes, control rights, and allocation rules. **Status: Draft v0.1.**
- [ISO/TC 307 Standards Landscape](references/iso-tc-307-landscape.md) — published baseline, active revisions, draft projects, and their intended use in BRM. **Status date: 2026-08-10.**
- [EU Regulatory Applicability Map](regulatory/eu-applicability-map.md) — actor/activity/component mapping for CRA, DORA, NIS2, Data Act, GDPR, and regulator interpretations. **Status date: 2026-08-10.**
- [EU Source Register](references/eu-source-register.yaml) and [Official Downloads Index](references/official-sources/README.md) — controlled versions, dates, direct official downloads, and source/licensing rules.
- [DeFi dApp Development Project Lifecycle](standards/defi-dapp-development-lifecycle.md) — original 11-stage lifecycle and RACI draft. It is retained as a lifecycle projection to be normalized against the core metamodel. **Status: Draft.**

## Model structure

BRM analyzes a system through:

> **Network Profile × Component × Actor × Control Right × Activity × Jurisdiction × Lifecycle Event**

It separates four planes:

1. **Technical stack:** infrastructure; client/core protocol; consensus/network operation; data availability/state; interoperability/oracles; smart contracts; wallets/identity/custody; application/interface/off-chain services.
2. **Control planes:** governance, upgrades, emergency powers, keys and privileges, treasury, and economic incentives.
3. **Regulatory overlays:** authorization, AML/CFT, issuance, market integrity, custody, consumer protection, privacy, resilience, outsourcing, tax, records, and IP.
4. **Assurance:** risk assessment, testing, audit, monitoring, evidence, certification, incident response, and reassessment.

## Responsibility dimensions

BRM extends beyond a single RACI assignment and records:

- Design Authority;
- Implementation Responsibility;
- Operational Control;
- Change / Upgrade Authority;
- Emergency Authority;
- Key / Privilege Custodian;
- Economic Beneficiary;
- Legal / Regulatory Accountable;
- Risk Owner;
- Control Owner;
- Evidence Owner;
- Assurance Provider;
- User / Counterparty Duty Owner.

## Source and draft handling

- Imported drafts retain their source and draft status.
- Published standards are pinned by identifier, edition, and status.
- ISO work items at AWI, WD, CD, DIS, DTS, or PRF stages are tracked as research inputs and are not represented as published requirements.
- Regulatory claims must be checked against the activity, actor, jurisdiction, and effective date.
- Model changes should preserve traceability from source to concept, allocation rule, control, and evidence.

## Roadmap

- canonical actor and component taxonomy;
- machine-readable YAML/JSON responsibility-record schema;
- network-profile templates;
- control-right and economic-influence assessment;
- jurisdictional regulatory-activity decision trees;
- assurance and evidence catalogue;
- worked examples for L1, L2, consortium DLT, cross-chain protocol, and hybrid DeFi;
- normalization of the lifecycle draft against BRM.
