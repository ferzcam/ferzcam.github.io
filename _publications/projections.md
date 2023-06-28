---
title: "From axioms over graphs to vectors, and back again: evaluating the properties of graph-based ontology embeddings"
collection: publications
permalink: /publication/projections
authors: 'Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'March 2023'
venue: 'NeSy 2023'
venueurl: 'https://sites.google.com/view/nesy2023'
arxiv: 'https://arxiv.org/abs/2303.16519'
paperurl: 'https://www.cs.ox.ac.uk/isg/conferences/tmp-proceedings/NeSy2023/paper7.pdf'
codeurl: 'https://github.com/bio-ontology-research-group/ontology-graph-projections'
citation: 'projections'
---



Several approaches have been developed that generate embeddings for
Description Logic ontologies and use these embeddings in machine
learning. One approach of generating ontologies embeddings is by first
embedding the ontologies into a graph structure, i.e., introducing a
set of nodes and edges for named entities and logical axioms, and then
applying a graph embedding to embed the graph in ℝn. Methods that
embed ontologies in graphs (graph projections) have different formal
properties related to the type of axioms they can utilize, whether the
projections are invertible or not, and whether they can be applied to
asserted axioms or their deductive closure. We analyze, qualitatively
and quantitatively, several graph projection methods that have been
used to embed ontologies, and we demonstrate the effect of the
properties of graph projections on the performance of predicting
axioms from ontology embeddings. We find that there are substantial
differences between different projection methods, and both the
projection of axioms into nodes and edges as well ontological choices
in representing knowledge will impact the success of using ontology
embeddings to predict axioms.
