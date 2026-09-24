---
title: W3C Threat Modeling and CRA — GDC 2026
status: research-input
classification: PROMOTE
architectural_delta: MAIN
source_date: 2026-09-18
reviewed: 2026-09-21
---

# W3C Threat Modeling and the CRA — GDC 2026

## Source

- W3C blog: https://www.w3.org/blog/2026/w3c-threat-modeling-and-the-cra-a-report-from-gdc-2026/
- W3C Threat Modeling Guide: https://www.w3.org/TR/threat-modeling-guide/
- W3C Threat Model for the Web: https://w3c.github.io/threat-model-web/
- W3C Threat Model for Decentralized Credentials: https://www.w3.org/TR/threat-model-decentralized-credentials/
- ETSI work item EN 304 617 is discussed by W3C as a draft European harmonised standard for browsers under the CRA.

## Classification

**PROMOTE / CRA / Threat Modeling / Responsibility Allocation / Standards Engineering**

Architectural delta promoted to **MAIN BRM**:

> Threat modeling precedes risk assessment. Responsibility must be derived not only from components and control rights, but also from data flows, trust boundaries, threat exposure, mitigation authority, security outcomes, and ownership of remaining threats.

## Why it matters to BRM

The W3C report describes threat modeling being integrated into the structure of draft ETSI EN 304 617 as a precursor to risk analysis and risk acceptance. The reported approach describes the product through components, data flows, and trust boundaries, then relates threats and applicable requirements to that model.

This reinforces BRM's component- and control-based allocation approach, while adding a missing explicit link between threat exposure and responsibility allocation.

BRM therefore records three additional responsibility dimensions:

1. **Threat Mitigation Authority** — who can technically, contractually, operationally, or through governance implement or enforce the selected response.
2. **Security Outcome Owner** — who remains accountable for the required security outcome even where implementation is delegated or distributed.
3. **Remaining Threat Owner** — who accepts, transfers, escalates, monitors, or reopens a threat that cannot be fully addressed.

The traceability chain is extended to:

> System boundary → Component → Data flow → Trust boundary → Asset / Stakeholder → Threat / Harm → Security outcome → Risk → Requirement → Actor / Control right → Threat response / Control → Evidence → Remaining threat / Acceptance.

## Blockchain-specific implication

Distributed systems frequently separate accountability from technical authority. Examples include a dApp that depends on an external bridge, an L2 that inherits L1 properties, a frontend that depends on an RPC provider, or an accountable legal entity that cannot directly patch a third-party protocol.

BRM must therefore distinguish:

- who is exposed to the threat;
- who is accountable for the security outcome;
- who can actually mitigate the threat;
- what enforceable dependency or escalation path exists;
- who owns the remaining threat when direct mitigation is unavailable.

A responsibility assignment is incomplete when an actor is named accountable but no mitigation authority, enforceable recourse, or explicit remaining-threat decision exists.

## Source-status caution

The W3C Threat Modeling Guide is a **W3C Group Note Draft**, not a W3C Recommendation and not a binding CRA requirement. The GDC article reports work on draft ETSI EN 304 617 for browsers. BRM uses these materials as architecture and standards-engineering research inputs; it does not generalise browser-specific draft language into a universal blockchain CRA obligation.
