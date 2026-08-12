# ERC-20 Quickstart

This example shows the smallest useful BRM assessment: one token transfer, one actor, one control right, and verifiable evidence fields. It is illustrative and not legal advice.

## Apply it

1. Identify the token contract, chain ID, sender, recipient, and transaction hash.
2. Identify who controls the relevant signing key and who operates the wallet or frontend.
3. Record the activity as `transfer`, the lifecycle event as `operate`, and the applicable jurisdiction.
4. Map the signer to the operational-control and evidence-owner roles only when the evidence supports that conclusion.
5. Preserve the transaction receipt, block metadata, contract address, and collection timestamp using the [evidence-integrity guide](../../GUIDES/evidence-integrity.md).

The example intentionally distinguishes observable execution evidence from legal conclusions: a transaction proves execution, not the identity, authority, or legal responsibility of the signer.
