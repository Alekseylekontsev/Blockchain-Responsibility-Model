---
title: Abuse-Resilience and Remediation Pattern
status: draft
version: 0.1
document_type: pattern
updated: 2026-09-06
---

# Abuse-Resilience and Remediation Pattern

> **Status: Draft v0.1.** This pattern extends BRM analysis for systems where durable or decentralized infrastructure can preserve harmful or unwanted state while no single actor has end-to-end removal authority.

## Purpose

BRM already records component, actor, control right, activity, jurisdiction, and lifecycle event. This pattern makes one additional property explicit: **remediation authority can be fragmented even when persistence is strong**.

The relevant analysis is not simply whether content or state is immutable. It is which actors can affect each stage of the harmful-use path and what mitigations remain feasible when direct deletion is unavailable.

## Pattern

`Harmful state/effect -> Persistence property -> Exposure path -> Available control rights -> Mitigation owner -> Residual exposure -> Evidence`

For each relevant component, distinguish at least:

- authority to create or publish state;
- authority to modify future behavior or parameters;
- authority to delete or roll back state, if any;
- authority to censor or refuse new writes, if any;
- authority to mediate reads or access;
- authority to index, de-index, classify, warn, or filter;
- authority to change client interpretation or defaults;
- authority to contain downstream execution or use;
- incident, legal, risk, control, and evidence ownership.

## Core invariants

- `ability to publish durable state != ability to remove that state`
- `cannot delete != cannot mitigate`
- `state persistence != authorization of its use`
- `network participation != end-to-end responsibility`
- `takedown authority != incident responsibility`
- `technical neutrality claim != completed responsibility analysis`

## BRM allocation rule

When a harmful or prohibited use relies on a durable blockchain component, do not stop analysis at the actor who cannot delete historical state. Continue across the exposure path and allocate feasible mitigation and evidence duties to actors that actually control interfaces, gateways, indexing, client behavior, operational response, or downstream systems.

Conversely, do not infer legal accountability merely because an actor technically participates in network operation. Legal and regulatory conclusions still require the BRM combination of factual control, performed activity, authority, economic benefit, jurisdiction, applicable law, and evidence.

## Example use case: EtherHiding / ClickFix

The 2026 EtherHiding/ClickFix reporting provides a concrete threat-model example in which on-chain state is used as part of resilient malicious delivery infrastructure. The useful BRM lesson is the **control asymmetry**, not the malware implementation detail.

See [EtherHiding / ClickFix — Blockchain as Abuse-Resilient Delivery Infrastructure](../references/etherhiding-clickfix-2026.md).
