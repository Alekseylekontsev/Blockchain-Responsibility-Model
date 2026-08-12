---
title: EU Regulation to Standards Crosswalk
status: implementation-reference
as_of: 2026-08-10
---

# EU Regulation to Standards Crosswalk

> Standards support implementation and evidence; they do not determine legal scope, replace MiCA authorisation, CRA conformity, or regulator-specific duties, or prove compliance by themselves.

| Implementation domain | EU overlays | BRM owners/evidence | Supporting standards and guidance |
|---|---|---|---|
| Governance and risk | MiCA, CRA, DORA, NIS2, GDPR | Legal accountable, risk/control/evidence owners; scope decision, risk register, approvals | ISO/IEC 27001:2022 + Amd 1:2024; ISO/IEC 27005:2022; ISO 31000:2018; ISO/TS 23635:2022 |
| Blockchain architecture and roles | All | Design/change/operational authority; architecture, actor and dependency records | ISO 23257:2022; ISO/TS 23258:2021; ISO 22739:2024; ISO/TR 6277:2025 |
| Secure product/software lifecycle | CRA; NIS2; DORA | Manufacturer/design/control/evidence owners; threat model, secure SDLC, test and release records | ISO/IEC 27034 series; ISO/IEC 27002:2022; ISO/IEC 30111:2019; ISO/IEC 29147:2018; emerging ISO 24875 series for smart-contract security |
| Vulnerability disclosure and handling | CRA; NIS2; DORA | PSIRT, incident/control/evidence owners; intake, triage, remediation, advisory, reporting | ISO/IEC 29147:2018; ISO/IEC 30111:2019 (edition 3 is under development); ENISA/CSIRT reporting guidance |
| Incident and crisis management | CRA; DORA; NIS2; GDPR | Incident commander, regulatory accountable, evidence owner; classification, timeline, notification, recovery | ISO/IEC 27035 series; ISO 22301:2019; ISO/IEC 27001/27002; DORA RTS/ITS and NIS2 national channels |
| Business continuity and operational resilience | DORA; NIS2; CRA support obligations | Operational/risk owners; BIA, continuity, backup, recovery, exit and test evidence | ISO 22301:2019; ISO/IEC 27031:2025; ISO/IEC 20000-1:2018; DORA RTS/ITS |
| ICT and supply-chain risk | DORA; NIS2; CRA | Vendor, dependency, concentration and exit owners; contracts, register, reviews, SBOM | ISO/IEC 27036 series; ISO/IEC 27001/27002; ISO/IEC 19770-1:2017; ENISA NIS2 Guidance v1.0 |
| Privacy management and DPIA | GDPR; Data Act | Controller/joint controller/processor, DPO, privacy risk/evidence owners; ROPA, DPIA, notices, rights | ISO/IEC 27701:2025; ISO/IEC 29100:2024; ISO/IEC 29134:2023; ISO/IEC 27555:2021; EDPB Guidelines 02/2025 v2 |
| Cloud privacy and processing | GDPR; DORA; NIS2; Data Act | Controller/processor and ICT third-party owners; contract, location, transfer and exit evidence | ISO/IEC 27017:2015; ISO/IEC 27018:2025; ISO/IEC 27701:2025; ISO/IEC 20000-1:2018 |
| Smart contracts and data sharing | Data Act; GDPR; CRA; MiCA | Vendor/deployer, design/change/emergency/data owners; agreement, access, termination, audit trail | Data Act Article 36; ISO/TR 23455:2019; ISO/DTS 18126.2 (draft); ISO 24875 series (draft); published editions only as normative references |
| Interoperability and data portability | Data Act; MiCA operational context | Design and dependency owners; schemas, interfaces, switching and portability tests | ISO/TS 23516:2026; ISO/TR 6277:2025; applicable European harmonised standards/common specifications when published |
| Custody and key management | MiCA; DORA; GDPR | Custodian, key/privilege owner, risk/evidence owner; ceremonies, access, recovery, segregation | ISO/TR 23576:2020; ISO/IEC 11770 series; ISO/IEC 27002:2022; relevant financial-sector rules |
| Privacy certification assurance | GDPR | PIMS accountable and assurance provider; audit scope and certificate | ISO/IEC 27701:2025; ISO/IEC 27706:2025. A certificate supports assurance but is not automatically an Article 42 GDPR certification. |

## Use rules

1. Pin the exact edition and amendment in every BRM control record.
2. Distinguish published standards from AWI/WD/CD/DIS/DTS projects.
3. Map each legal duty to a responsible actor, enforceable control, evidence item, and reporting clock; do not map only to a standard clause.
4. Treat CRA harmonised standards, DORA RTS/ITS, NIS2 implementing rules/national measures, and Data Act common specifications as separate controlled sources when published.
5. Keep full ISO/IEC texts only in licensed private storage. This public repository stores identifiers, status, official links, and non-substitutive implementation mappings.

## Official catalogues

- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001)
- [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html)
- [ISO/IEC 27701:2025](https://www.iso.org/standard/27701)
- [ISO/IEC 29147:2018](https://www.iso.org/standard/72311.html)
- [ISO/IEC 30111:2019](https://www.iso.org/standard/69725.html)
- [ISO/TC 307 work programme](https://www.iso.org/committee/6266604/x/catalogue/)
- [ENISA NIS2 Technical Implementation Guidance](https://www.enisa.europa.eu/publications/nis2-technical-implementation-guidance)
