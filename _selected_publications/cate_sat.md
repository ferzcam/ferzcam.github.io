---
title: "Lattice-Based ALC Ontology Embeddings With Saturation (Extended Version)"
collection: publications
permalink: /publication/cate_sat
authors: 'Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'Jun 2025'
venue: 'Neurosymbolic Artificial Intelligence'
venueurl: 'https://doi.org/10.1177/29498732251340186'
arxiv: 'https://arxiv.org/abs/2305.07163'
paperurl: 'https://doi.org/10.1177/29498732251340186'
codeurl: 'https://github.com/bio-ontology-research-group/catE'
citation: 'cate_sat'
pubicon: 'cate'
---

Generating vector representations (embeddings) of OWL ontologies is a
growing task due to its applications in predicting missing facts and
knowledge-enhanced learning in fields such as bioinformatics. The
underlying semantics of OWL ontologies is expressed using Description
Logics (DLs). Initial approaches to generate embeddings relied on
constructing a graph out of ontologies, neglecting the semantics of
the logic therein. Recent semantic-preserving embedding methods often
target lightweight DL languages like EL++, ignoring more expressive
information in ontologies. Although some approaches aim to embed more
descriptive DLs like ALC, those methods require the existence of
individuals, while many real-world ontologies are devoid of them. We
propose an ontology embedding method for the ALC DL language that
considers the lattice structure of concept descriptions. We use
connections between DL and Category Theory to materialize the lattice
structure and embed it using an order-preserving embedding method. We
show that our method outperforms state-of-the-art methods in several
knowledge base completion tasks. We make our code and data available
at https://github.com/bio-ontology-research-group/catE

