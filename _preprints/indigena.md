---
title: "INDIGENA: inductive prediction of disease-gene associations using phenotype ontologies"
collection: publications
permalink: /publication/indigena
authors: 'Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'Feb 2026'
arxiv: 'https://arxiv.org/abs/2602.01088'
codeurl: 'https://github.com/bio-ontology-research-group/indigena'
---

Motivation: Predicting gene-disease associations (GDAs) is the problem to determine which gene is associated with a disease. GDA prediction can be framed as a ranking problem where genes are ranked for a query disease, based on features such as phenotypic similarity. By describing phenotypes using phenotype ontologies, ontology-based semantic similarity measures can be used. However, traditional semantic similarity measures use only the ontology taxonomy. Recent methods based on ontology embeddings compare phenotypes in latent space; these methods can use all ontology axioms as well as a supervised signal, but are inherently transductive, i.e., query entities must already be known at the time of learning embeddings, and therefore these methods do not generalize to novel diseases (sets of phenotypes) at inference time.
Results: We developed INDIGENA, an inductive disease-gene association method for ranking genes based on a set of phenotypes. Our method first uses a graph projection to map axioms from phenotype ontologies to a graph structure, and then uses graph embeddings to create latent representations of phenotypes. We use an explicit aggregation strategy to combine phenotype embeddings into representations of genes or diseases, allowing us to generalize to novel sets of phenotypes. We also develop a method to make the phenotype embeddings and the similarity measure task-specific by including a supervised signal from known gene-disease associations. We apply our method to mouse models of human disease and demonstrate that we can significantly improve over the inductive semantic similarity baseline measures, and reach a performance similar to transductive methods for predicting gene-disease associations while being more general.
Availability and Implementation: https://github.com/bio-ontology-research-group/indigena



