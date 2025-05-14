---
title: "An inductive, supervised approach for predicting gene--disease associations using phenotype ontologies"
collection: publications
permalink: /publication/inductive_gda
authors: 'Safana Bakheet, Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'May 2025'
arxiv: 'https://www.biorxiv.org/content/10.1101/2025.05.07.652682v1'
codeurl: 'https://github.com/bio-ontology-research-group/ISGDA'
---

**Motivation:** Predicting gene--disease associations (GDAs) is the problem to determine which gene is associated with a disease. The problem can be framed as a ranking problem where genes are ranked based on a set of phenotypes using a measure of phenotype similarity. When phenotypes are described using phenotype ontologies, ontology-based semantic similarity measures are used. Traditional semantic similarity measures use only the ontology taxonomy. Recent methods based on ontology embeddings compare phenotypes in latent space; these methods can use all ontology axioms as well as a supervised signal, but are inherently transductive, i.e., queries must already be known at the time of learning embeddings, and therefore these methods do not generalize to novel diseases (sets of phenotypes** at inference time. 

**Results:** We developed an inductive method for ranking genes based on a set of phenotypes. Our method first uses a graph projection to map axioms from phenotype ontologies to a graph structure, and then uses ontology embeddings to create latent representations of phenotypes. We use an explicit aggregation strategy to combine phenotype embeddings into representations of genes or diseases, allowing us to generalize to novel sets of phenotypes. We also develop a method to make the phenotype embeddings and the similarity measure task-specific by including a supervised signal from known gene--disease associations. We apply our method to mouse models of human disease and demonstrate that we can significantly improve over inductive baseline measures, and reach a performance similar to transductive methods for predicting gene--disease associations while being more general. 

**Availability and Implementation**: https://github.com/bio-ontology-research-group/ISGDA



