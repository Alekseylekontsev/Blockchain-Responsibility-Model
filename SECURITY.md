# Security and adversarial model

BRM is a governance and evidence framework, not a security guarantee. Each assessment must document the system boundary, assumptions, attacker capabilities, and residual risk.

## Threats to assess

| Threat | Responsibility question | Typical safeguards and evidence |
|---|---|---|
| Privileged key compromise | Who can pause, upgrade, drain, or change configuration? | Multisig policy, signer review, hardware-backed keys, rotation records, transaction logs |
| Collusion or threshold failure | Can a threshold group act together against users or governance? | Independent signers, timelocks, quorum analysis, conflict declarations, governance history |
| Sybil or delegated-voting capture | Who controls effective voting power rather than nominal token ownership? | Delegation analysis, concentration metrics, snapshot exports, proposal and vote records |
| Oracle manipulation | Who selects, operates, or can influence the data source? | Source diversity, deviation limits, circuit breakers, oracle updates, incident records |
| Frontend or RPC substitution | Can users be routed to altered code or data? | Reproducible builds, deployment hashes, domain/DNS controls, provider inventory, release attestations |
| Supply-chain compromise | Which dependency maintainer or build system can affect execution? | SBOM, pinned versions, review approvals, signed releases, vulnerability records |
| Availability or censorship failure | Who can stop inclusion, settlement, or access? | Operator/validator map, fallback paths, recovery tests, outage and escalation records |

## Scope rule

BRM covers factual control, performed activity, legal and regulatory accountability, risk ownership, controls, and evidence ownership. It does not decide legal liability, replace threat modeling, or establish that a protocol is decentralized merely because no single key is visible.

## Assessment method

For each material threat, record attacker capability, affected component, attack path, control owner, evidence owner, residual risk, acceptance authority, and reassessment trigger. Treat off-chain coordination, economic influence, and privileged fallback powers as control signals.
