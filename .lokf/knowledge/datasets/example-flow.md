---
type: OrchestraFlowV10
id: https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/example-flow
title: The example venue's order flow
description: A v1.0 flow from the example repository, `OrderFlow`, which carries orders from the actor Trader to the actor Venue with recoverable delivery.
resource: tests/data/xml/v1.0-repository.xml
fixr_name: OrderFlow
fixr_source: Trader
fixr_destination: Venue
fixr_reliability: recoverable
isPartOf:
  - https://w3id.org/lmodel/fix-orchestra/knowledge/datasets/example-files
sources:
  - id: example
    resource: tests/data/xml/v1.0-repository.xml
    title: the flow OrderFlow
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# The example venue's order flow

The example repository declares the flow between its two actors, and the message `NewOrderSingle` names it.[^example]

[^example]: tests/data/xml/v1.0-repository.xml, the flow OrderFlow
