---
type: Service
id: https://w3id.org/lmodel/fix-orchestra/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-orchestra`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
sources:
  - id: site
    resource: website/site.config.mjs
    title: REPO, SITE, BASE and REDIRECTS
  - resource: website/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:53:42Z"
status: draft
---

# Documentation site

The site redirects the retired mkdocs site's `/about` and `/elements` addresses to its own pages.[^site]

[^site]: website/site.config.mjs, REPO, SITE, BASE and REDIRECTS
