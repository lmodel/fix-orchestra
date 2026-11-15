---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-orchestra`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
sources:
  - id: site
    resource: website/site.toml
    title: the site's address, title and redirects
  - resource: website/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:36:42Z"
status: draft
---

# Documentation site

The site redirects the retired mkdocs site's `/about` and `/elements` addresses to its own pages.[^site]

[^site]: website/site.toml, the site's address, title and redirects
