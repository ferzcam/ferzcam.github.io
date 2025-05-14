---
title: "Enhancing Geometric Ontology Embeddings for EL++ with Negative Sampling and Deductive Closure Filtering"
collection: publications
permalink: /publication/el_analysis
authors: 'Olga Mashkova, Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'Sep 2024'
venue: 'NeSy 2024'
venueurl: 'https://sites.google.com/view/nesy2024'
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-031-71167-1_18'
citation: 'el_analysis'
codeurl: 'https://github.com/bio-ontology-research-group/geometric_embeddings'
---

Ontology embeddings map classes, relations, and individuals in
ontologies into $\mathbb{R^n}$, and within $\mathbb{R^n}$ similarity
between entities can be computed or new axioms inferred. For
ontologies in the Description Logic $\mathcal{EL}^{++}$, several
embedding methods have been developed that explicitly generate models
of an ontology. However, these methods suffer from some limitations;
they do not distinguish between statements that are unprovable and
provably false, and therefore they may use entailed statements as
negatives. Furthermore, they do not utilize the deductive closure of
an ontology to identify statements that are inferred but not
asserted. We evaluated a set of embedding methods for
$\mathcal{EL}^{++}$ ontologies based on high-dimensional ball
representation of concept descriptions, incorporating several
modifications that aim to make use of the ontology deductive
closure. In particular, we designed novel negative losses that account
both for the deductive closure and different types of negatives. We
demonstrate that our embedding methods improve over the baseline
ontology embedding in the task of knowledge base or ontology
completion.
