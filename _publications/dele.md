---
title: 'DELE: Deductive EL++ Embeddings for Knowledge Base Completion'
collection: publications
permalink: /publication/dele
authors: 'Olga Mashkova , Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'November 2024'
arxiv: https://arxiv.org/abs/2411.01574
codeurl: 'https://github.com/bio-ontology-research-group/DELE'
citation: dele
---

Ontology embeddings map classes, relations, and individuals in ontologies into Rn, and within Rn similarity between entities can be computed or new axioms inferred. For ontologies in the Description Logic EL++, several embedding methods have been developed that explicitly generate models of an ontology. However, these methods suffer from some limitations; they do not distinguish between statements that are unprovable and provably false, and therefore they may use entailed statements as negatives. Furthermore, they do not utilize the deductive closure of an ontology to identify statements that are inferred but not asserted. We evaluated a set of embedding methods for EL++ ontologies, incorporating several modifications that aim to make use of the ontology deductive closure. In particular, we designed novel negative losses that account both for the deductive closure and different types of negatives and formulated evaluation methods for knowledge base completion. We demonstrate that our embedding methods improve over the baseline ontology embedding in the task of knowledge base or ontology completion.
