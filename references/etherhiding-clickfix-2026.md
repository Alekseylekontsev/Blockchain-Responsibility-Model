---
title: EtherHiding / ClickFix — Blockchain as Abuse-Resilient Delivery Infrastructure
status: research-reference
date: 2026-09-06
---

# EtherHiding / ClickFix — Blockchain as Abuse-Resilient Delivery Infrastructure

## Why this matters to BRM

Recent ClickFix campaigns show that a public blockchain can be used as part of malicious delivery and command-resolution infrastructure. The security significance is not that the blockchain itself is compromised, but that durable public state and widely available read access can be repurposed as a resilient coordination or payload-distribution substrate.

This is a useful BRM case because responsibility and remediation capabilities are split across several layers and actors. The actor that writes harmful state, the network that preserves it, the RPC/indexing layer that exposes it, the compromised website that references it, and the endpoint that ultimately executes attacker-controlled content are distinct components with different control rights.

## Observed pattern

Defensive abstraction:

`Compromised interface -> On-chain reference/state -> Public read infrastructure -> Off-chain delivery/execution path -> Victim impact`

The case demonstrates a control asymmetry:

`ability to publish durable state != ability to remove that state != ability to prevent downstream use`

A public ledger may make historical state difficult or impossible for any single participant to delete, while meaningful mitigations can still exist at other layers such as interfaces, RPC gateways, indexing services, client software, endpoint controls, abuse monitoring, and incident response.

## BRM implications

1. **Persistence is a responsibility-relevant property.** The model should record whether a component allows deletion, rollback, filtering, suppression, de-indexing, or only compensating controls downstream.
2. **Takedown capability must be decomposed.** `Delete`, `censor new writes`, `block access`, `de-index`, `warn`, `filter interpretation`, and `contain downstream execution` are different control rights and may belong to different actors.
3. **Immutability does not eliminate response duties.** When deletion is unavailable, the responsibility model should identify who can reduce reachability, interpretability, or harmful downstream effects and who owns the residual risk.
4. **Infrastructure neutrality does not answer allocation.** BRM should not infer legal liability from technical participation alone; it should map factual control, activity, authority, economic benefit, jurisdiction, and feasible response mechanisms.
5. **Security analysis must be end-to-end.** Treating the blockchain, website, RPC provider, smart contract, or endpoint in isolation misses the actual abuse path.

## Candidate BRM pattern

### Abuse-Resilience and Remediation Mapping

`Harmful state/effect -> Persistence property -> Exposure path -> Available control rights -> Mitigation owner -> Residual exposure -> Evidence`

Key invariants:

- `state persistence != authorization of its use`
- `cannot delete != cannot mitigate`
- `network participation != end-to-end responsibility`
- `technical neutrality claim != completed responsibility analysis`
- `takedown authority != incident responsibility`

## Source handling

Primary intake source supplied for review:

- BleepingComputer, 5 Sep 2026: **Over 5,400 hacked sites serve ClickFix payloads stored on the blockchain**
  - https://www.bleepingcomputer.com/news/security/over-5-400-hacked-sites-serve-clickfix-payloads-stored-on-the-blockchain/

Supporting defensive research:

- Israel National Digital Agency, Aug 2026: **Malware-On-The-Blockchain: How Attackers Build Infrastructure That Can't Be Taken Down**
  - https://govextra.gov.il/national-digital-agency/cyber/research/malware-on-the-blockchain/
- Cribl SecOps, Aug 2026: **EtherHiding malware campaign on the blockchain**
  - https://cribl.io/blog/cribl-secops-uncovers-etherhiding-malware-campaign-on-the-blockchain/
- FileScan Threat Labs, Jul/Aug 2026: **Tracing ClickFix Chain to a Live EtherHiding Resolution**
  - https://blog.filescan.io/posts/clickfix-etherhiding-chain/
- HHS HC3, Oct 2024: **ClickFix Attacks** sector alert, documenting earlier use of blockchain/smart contracts in ClickFix delivery chains.
  - https://www.hhs.gov/sites/default/files/clickfix-attacks-sector-alert-tlpclear.pdf

## Claim boundary

This reference is threat-model and responsibility-allocation evidence. It does not imply that validators, RPC providers, protocol developers, or other infrastructure participants are automatically legally responsible for malicious content or downstream execution. Any legal or regulatory conclusion must be derived separately from actor, activity, control, jurisdiction, knowledge, applicable law, and effective date.
