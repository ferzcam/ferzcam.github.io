---
title: "Fully Geometric Multi-Hop Reasoning on Knowledge Graphs with Transitive Relations"
collection: publications
permalink: /publication/geometre
authors:  Fernando Zhapa-Camacho, Robert Hoehndorf
date: 'May 2025'
arxiv: 'https://arxiv.org/abs/2505.12369'
codeurl: 'https://github.com/bio-ontology-research-group/GeometrE'
---

Geometric embedding methods have shown to be useful for multi-hop
reasoning on knowledge graphs by mapping entities and logical
operations to geometric regions and geometric transformations,
respectively. Geometric embeddings provide direct interpretability
framework for queries. However, current methods have only leveraged
the geometric construction of entities, failing to map logical
operations to geometric transformations and, instead, using neural
components to learn these operations. We introduce GeometrE, a
geometric embedding method for multi-hop reasoning, which does not
require learning the logical operations and enables full geometric
interpretability. Additionally, unlike previous methods, we introduce
a transitive loss function and show that it can preserve the logical
rule $\forall a,b,c : r(a,b) \land r(b,c) \to r(a,c)$ . Our
experiments show that GeometrE outperforms current state-of-the-art
methods on standard benchmark datasets.
