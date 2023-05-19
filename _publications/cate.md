---
title: "CatE: Embedding ALC ontologies using category-theoretical semantics"
collection: publications
permalink: /publication/cate
authors: 'Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'May 2023'
arxiv: 'https://arxiv.org/abs/2305.07163'
codeurl: 'https://github.com/bio-ontology-research-group/catE'
citation: 'cate'
---

 

Machine learning with Semantic Web ontologies follows several strategies, 
one of which involves projecting ontologies into graph
structures and applying graph embeddings or graph-based machine
learning methods to the resulting graphs. Several methods have been
developed that project ontology axioms into graphs. However, these
methods are limited in the type of axioms they can project (totality),
whether they are invertible (injectivity), and how they exploit
semantic information. These limitations restrict the kind of tasks to
which they can be applied. Category-theoretical semantics of logic
languages formalizes interpretations using categories instead of sets,
and categories have a graph-like structure. We developed CatE, which
uses the category-theoretical formulation of the semantics of the
Description Logic $\mathcal{ALC}$ to generate a graph representation for ontology
axioms. The CatE projection is total and injective, and therefore
overcomes limitations of other graph-based ontology embedding methods
which are generally not invertible. We apply CatE to a number of
different tasks, including deductive and inductive reasoning, and we
demonstrate that CatE improves over state of the art ontology
embedding methods. Furthermore, we show that CatE can also outperform
model-theoretic ontology embedding methods in machine learning tasks
in the biomedical domain.

