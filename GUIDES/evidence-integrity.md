# Evidence integrity guide

Responsibility claims should be reproducible without unnecessarily publishing personal data, secrets, or privileged legal material.

## Evidence record

For every material artifact record:

- stable evidence ID and description;
- source URI or controlled storage reference;
- collection timestamp in UTC;
- SHA-256 digest and byte size;
- media type, language, version, and superseded/current status;
- collector, reviewer, owner, and retention period;
- related actor, component, control right, activity, and lifecycle event.

## Blockchain evidence

For an on-chain claim preserve chain ID, network, transaction hash, block number, block hash, event signature, contract address, relevant log indices, and the verification date. A transaction hash proves inclusion in a particular network history; it does not by itself prove who controlled a key or why an action was taken.

## Stronger integrity patterns

- sign evidence manifests with an organization-controlled signing key;
- anchor a manifest digest on-chain or in an append-only store;
- use Merkle trees when many evidence items share one review cycle;
- preserve the original artifact and create derived redacted copies separately;
- store personal data and legal advice off-chain, using hashes or references in public records;
- document key custody, clock source, access controls, and verification procedure.

## Review rule

Evidence supports a responsibility allocation; it does not create one. Record uncertainty explicitly and never publish credentials, private keys, personal data, or confidential incident details.
