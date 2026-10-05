---
title: When Law Executes Code — Executable Particularity and Stablecoin Execution Return
status: research-input
classification: PROMOTE
architectural_delta: MAIN-supporting
source_date: 2026-08-23
reviewed: 2026-10-04
---

# When Law Executes Code: The Particularity Problem in Stablecoin Seizure

## Source

- Matthew Ramírez, attorney, Holland & Hart LLP
- Paper date: 2026-08-23
- User-provided paper reviewed in full for BRM relevance.
- Primary legal anchors discussed by the paper include the U.S. GENIUS Act and federal forfeiture matters.
- No canonical public URL was supplied with the uploaded source; do not invent one.

## Classification

**PROMOTE / Legal-to-Code Translation / Stablecoin Controls / Execution Evidence / Responsibility Allocation / Auditability**

Architectural delta promoted as **MAIN-supporting BRM**:

> A legally authorized instruction and a technically successful blockchain action are different evidence objects. Responsibility requires a reviewable join from legal authority through mapping and approval to code execution, variance, and later legal/remedial state.

## Core contribution

The paper identifies a gap between legal commands expressed in legal objects and limits, and token contracts that accept technical parameters such as addresses, functions, amounts, networks, and permissions.

It introduces two useful constructs:

1. **Executable Particularity** — a decision rule for testing whether the boundaries of a lawful command survive technical mapping, approval, execution, and later property-state transitions.
2. **Stablecoin Execution Return (SER)** — a protected, tiered relational record that joins the legal command, property specification, issuer mapping and approvals, executed code action, variance, and subsequent legal/remedial states.

A transaction receipt alone proves that code executed. It does not prove that the legal command was mapped correctly or that institutional authority, property scope, timing, notice, challenge, custody, title, and remedy remained aligned.

## BRM delta

Extend the responsibility traceability chain for legally compelled or compliance-driven blockchain actions:

> Legal authority → Operative command → Property/object specification → Technical mapping → Decision roles → Approval/signing authority → Function and parameters → On-chain execution → Observed effect → Variance → Custody/title/notice/challenge/remedy state → Reviewer reproduction.

BRM should distinguish at least:

- **Authority Owner** — validates the legal or regulatory authority and operative terms.
- **Mapping Owner** — translates legal objects into token, chain, deployment, address/account, amount, timing, and technical effect.
- **Approval Owner** — authorizes the selected technical action and records decision roles.
- **Execution Owner** — invokes the function and records signers, threshold, transaction, block, time, and result.
- **Variance Owner** — determines whether execution was exact, overinclusive, underinclusive, delayed, failed, superseded, or presently unverifiable.
- **State/Remedy Owner** — maintains later distinctions among control, custody, title, notice, challenge, correction, release, forfeiture, remission, disbursement, and receipt.
- **Evidence/Return Owner** — preserves the joined episode and makes the appropriate evidence tier available to authorized reviewers.

## Responsibility invariants

- `technical_capability != legal_authority`
- `successful_transaction != conforming_execution`
- `legal_order != technical_mapping`
- `approval != execution`
- `control != custody != title`
- `transaction_receipt != complete_audit_evidence`
- `missing_evidence != proof_of_illegality`
- `later_success != proof_of_correct_contemporaneous_mapping`

## Evidence model

The paper's SER construct is useful because it keeps relationships explicit rather than relying on a generic case folder or chronology.

Minimum joined evidence should cover:

- command identity, issuing authority, legal verbs, deadline, exclusions, review route;
- token, chain, deployment, address/account, amount, units, measurement rule, destination, reversal terms;
- ambiguity treatment, third-party interests, decision roles, approvals, signing threshold;
- function, parameters, transaction, block, time, confirmation, resulting state;
- variance classification and rationale;
- later control, custody, title, notice, challenge, correction, release, forfeiture, remission, disbursement, and receipt states;
- stable episode identifier, timestamps, provenance links, retention rules, and role-based access.

## Privacy and security note

The proposed return is explicitly **protected and tiered**, not a public transparency dump. Different views may be appropriate for public, affected-party, regulator/court, and restricted investigative access.

This aligns with BRM's requirement to preserve evidence while minimizing unnecessary exposure of personal data, investigative material, or signing architecture.

## Scope caution

The paper is a legal/architecture research proposal based on a purposive set of U.S. stablecoin forfeiture matters. It does not establish an industry error rate, universal legal obligation, or global stablecoin-control standard.

BRM should therefore use Executable Particularity and SER as a reusable responsibility/evidence pattern, not as a claim that every jurisdiction requires this exact record structure.
