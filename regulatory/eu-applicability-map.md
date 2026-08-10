---
title: EU Regulatory Applicability Map for Blockchain and DLT
status: current-reference
version: 0.1
as_of: 2026-08-10
jurisdiction: European Union
---

# EU Regulatory Applicability Map for Blockchain and DLT

> Applicability aid for BRM, not legal advice. It does not replace an actor-, activity-, product-, Member-State-, and facts-specific assessment.

## 1. The short version

| Instrument | Trigger | Usually attaches to | Blockchain-specific reality check |
|---|---|---|---|
| CRA — Regulation (EU) 2024/2847 | A product with digital elements is made available on the EU market in commercial activity | Manufacturer; importer/distributor duties; special role for open-source software stewards | A network or protocol is not automatically a product. Commercial wallets, node clients, appliances, SDKs, and dApp software may be in scope depending on supply model. FOSS outside commercial activity is excluded, but commercial stewardship can create duties. |
| DORA — Regulation (EU) 2022/2554 | An entity is a listed EU financial entity, including an authorised MiCA CASP, or supplies ICT services into its regulated ICT chain | Financial entity; contractual ICT third-party provider; designated critical provider | A validator, DAO, protocol, or VASP is not automatically in scope. ESMA confirms transitional VASPs not yet authorised under MiCA are not DORA CASPs until authorised. |
| NIS2 — Directive (EU) 2022/2555 | An entity meets national transposition criteria for an Annex I/II sector, size rule, or special inclusion | Essential/important entity and management body | “Blockchain company” is not a listed category. Cloud, data-centre, CDN, DNS, trust-service, MSP/MSSP, marketplace, energy, finance, health, or other covered operations can bring the operator into scope. |
| Data Act — Regulation (EU) 2023/2854 | The actor/data relationship falls within connected-product data access, B2B/B2G data sharing, cloud switching, or interoperability rules | Data holder/user/recipient; data-processing provider; data-space participant; vendor/deployer of a covered smart contract | Article 36 does not regulate every smart contract. It applies to smart contracts used for automated execution of a data-sharing agreement in the Data Act context. |
| GDPR — Regulation (EU) 2016/679 | Personal data are processed and territorial scope is met | Controller, joint controllers, processor, and other actors for their own processing | Public keys, transaction metadata, payloads, revocation data, and off-chain linkages can be personal data. Roles follow factual purposes, means, and influence—not the label “decentralised”. |

## 2. Decision path

1. **Define the unit.** Name the legal entity/collective, product, component, service, users, countries, and lifecycle phase.
2. **Classify activity before technology.** Is the actor supplying software/hardware, operating infrastructure, providing ICT or financial services, sharing data, or processing personal data?
3. **Record factual control.** Who designs, deploys, upgrades, pauses, holds keys, selects dependencies, routes transactions, earns fees, and communicates with users?
4. **Apply overlays independently.** Product law (CRA), entity/sector resilience (DORA/NIS2), data economy (Data Act), and personal-data law (GDPR) can overlap.
5. **Resolve lex-specialis and national law.** DORA can be sector-specific cybersecurity law relative to NIS2 for equivalent requirements; NIS2 duties arise through Member-State transposition.
6. **Allocate controls and evidence.** No duty should be assigned to an actor lacking authority, enforceable dependency, or documented escalation.

## 3. Actor and component mapping

Legend: **Y** likely/direct when the trigger is met; **C** conditional; **N** not by this role alone.

| BRM actor/component | CRA | DORA | NIS2 | Data Act | GDPR | Primary allocation questions |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Core protocol/client commercial manufacturer | Y/C | N/C | C | C | C | Who places client/SDK on market and controls releases, vulnerabilities, support, and conformity evidence? |
| Non-commercial FOSS contributor | N/C | N | N | N/C | C | Is contribution outside commercial activity? Does the actor determine purposes/means of processing? |
| Open-source software steward | Y/C | C | C | C | C | Is there systematic support of FOSS intended for commercial activity? Who coordinates vulnerability handling? |
| Cloud/hosting/data-centre/CDN provider | C | C/Y | Y/C | C/Y | C/Y | Covered NIS2 infrastructure or DORA ICT service? Controller or processor for which processing? |
| Validator/miner/node operator | C | C | C | N/C | C | Product or service? Covered sector? Which personal data are replicated or observed? |
| L2 sequencer/prover/DA operator | C | C | C | C | C | Who controls ordering, availability, forced exit, upgrades, recovery, and service commitments? |
| Oracle/bridge/relayer/RPC/indexer | C | C | C | C | C/Y | Product, ICT service, covered entity, data intermediary, or controller/processor? Who can suspend/correct? |
| Smart-contract developer/vendor | C | C | C | Y/C | C/Y | Commercially supplied product? Specifically executes a data-sharing agreement? Who controls deployment/upgrades? |
| DAO/foundation/protocol governance | C | C | C | C | C/Y | Identify wrapper and factual influence: proposals, voting, multisig, treasury, fees, frontend, emergency powers. |
| Wallet software provider | Y/C | C | C | C | C/Y | Product status, custody, remote processing, telemetry, recovery, support, and security updates. |
| Custodian/exchange/authorised MiCA CASP | C | Y | C | C | Y/C | DORA governance, ICT risk/testing/incidents, third-party register/contracts, client-data roles. |
| Transitional VASP not authorised under MiCA | C | N as CASP until authorised | C | C | Y/C | ESMA Q&A 2364: transitional permission does not make it an authorised MiCA CASP for DORA. |
| Bank/investment firm/FMI using DLT | C | Y | C/lex specialis | C | Y/C | Allocate DLT dependencies into ICT risk, testing, continuity, incidents, outsourcing, and concentration controls. |
| dApp/frontend/API operator | Y/C | C | C | C | Y/C | Software supply, hosting, routing/defaults, personal data, user notices, and dependency risk. |
| Private user | N | N | N | C | Usually household exemption | Separate personal activity from professional/commercial operation or activity for others. |

## 4. Instrument-specific allocation

### CRA

**Status on 2026-08-10:** in force. Vulnerability/incident reporting starts **2026-09-11**; main obligations apply **2027-12-11**. Commission guidance C(2026) 5252 and its annex were published 2026-07-27.

Map manufacturer/importer/distributor/OSS-steward role; product boundary and remote processing; risk assessment; secure development; vulnerability handling; SBOM and technical documentation; support period and updates; reporting; conformity assessment; substantial modification; and the evidence owner. Do not infer exclusion merely because software is open source, decentralised, supplied in finance, or deployed as a smart contract.

### DORA

**Status:** applicable since **2025-01-17**.

For an in-scope financial entity map management accountability; ICT assets and DLT dependencies; prevention/detection/recovery; incidents; resilience testing and TLPT; ICT third-party due diligence, contracts, register, concentration and exit risk. Critical-provider designation does not transfer the financial entity's accountability.

### NIS2

**Status:** transposition deadline **2024-10-17**; scope and enforcement must be checked in each national law.

Map Annex I/II service, size/special inclusion, establishment, jurisdiction, essential/important status, management duties, Article 21 measures, Article 23 reporting, Implementing Regulation (EU) 2024/2690 and ENISA guidance where applicable, plus DORA/sector-law overlap.

### Data Act

**Status:** generally applicable since **2025-09-12**.

Test connected-product/related-service duties; required data sharing; B2G exceptional need; cloud switching; data spaces; and Article 36. For Article 36 record the underlying data-sharing agreement, vendor/deployer, robustness/access control, safe termination/interruption, archiving/continuity, and consistency with the agreement. A generic smart contract is insufficient.

### GDPR and regulator interpretation

**Current primary interpretation:** final EDPB Guidelines 02/2025 v2, adopted **2026-07-07**. They supersede the consultation draft; AEPD was lead rapporteur.

Map per operation: on/off-chain personal data and linkability; controller/joint-controller/processor boundaries; purposes, necessity, legal basis, transparency, accuracy, minimisation, retention, rights; technology necessity; DPIA; transfers; off-chain data and on-chain proofs/commitments; correction/erasure/restriction/automated decisions/human intervention; contracts, security, key management, governance change, incident response, and evidence.

The 2018 CNIL paper remains useful historical engineering guidance. The AEPD public-administration guide has a blockchain chapter but is visibly marked **OBSOLETO**; it is not the current authority.

## 5. Overlap rules

| Overlap | BRM treatment |
|---|---|
| CRA + NIS2 | CRA governs product duties; NIS2 governs a covered entity's organisational/operational cybersecurity. Map manufacturer and operator separately. |
| CRA + DORA | DORA governs the financial entity and ICT chain; CRA may govern products supplied into it. Do not assume blanket exclusion. |
| DORA + NIS2 | Test NIS2 Article 4 and national implementation; record displaced and remaining requirements. |
| Data Act + GDPR | Data Act does not lower GDPR protection. Identify GDPR basis and roles; personal-data safeguards prevail on conflict. |
| Immutable ledger + GDPR rights | Difficulty is not exemption. Predesign off-chain deletion, key/witness destruction, restriction, correction, migration, and redress. |
| DAO/decentralisation + any instrument | Replace labels with evidence of control, activity, benefit, interface, keys, voting concentration, and legal relationships. |

## 6. Minimum evidence package

- legal entity/actor ID, BRM profile, and T1–T8 component boundary;
- product/service/activity and EU country/user scope;
- control-right and economic-benefit evidence;
- per-instrument decision: in / out / conditional / unresolved;
- cited article/guidance, assumptions, and decision date;
- accountable owner, risk owner, control owner, and evidence owner;
- implementation/reporting dates and national-law dependencies;
- reassessment triggers: authorisation, commercialisation, modification, jurisdiction, new data use, governance/key change, or incident.

## 7. Principal current sources

- [CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) and [Commission C(2026) 5252 guidance](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)
- [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) and [ESMA Q&A 2364](https://www.esma.europa.eu/publications-data/questions-answers/2364)
- [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) and [ENISA implementation guidance](https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance)
- [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) and [Commission explanation](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained)
- [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and [EDPB Guidelines 02/2025 final](https://www.edpb.europa.eu/documents/guideline/guidelines-on-processing-of-personal-data-through-blockchain-technologies_en)
- [European Blockchain Sandbox, 3rd Cohort](https://blockchain-observatory.ec.europa.eu/document/43771f62-e58b-4f64-9c45-d14c140edaaa_en)
- [CNIL Blockchain and GDPR](https://www.cnil.fr/en/blockchain-and-gdpr-solutions-responsible-use-blockchain-context-personal-data)
- [AEPD obsolete historical guide](https://www.aepd.es/guias/guia-tecnologias-admin-digital.pdf)

See the controlled [EU source register](../references/eu-source-register.yaml).
