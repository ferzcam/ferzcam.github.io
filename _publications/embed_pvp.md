---
title: "Prioritizing genomic variants through neuro-symbolic, knowledge-enhanced learning"
collection: publications
permalink: /publication/embedpvp
authors: 'Azza Althagafi, Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'Nov 2023'
arxiv: 'https://www.biorxiv.org/content/10.1101/2023.11.08.566179v1'
codeurl: 'https://github.com/bio-ontology-research-group/EmbedPVP'
citation: 'embedpvp'
---

 
**Motivation:** Whole-exome and genome sequencing have become common tools
in diagnosing patients with rare diseases. Despite their success, this
approach leaves many patients undiagnosed. A common argument is that
more disease variants still await discovery, or the novelty of disease
phenotypes results from a combination of variants in multiple
disease-related genes. Interpreting the phenotypic consequences of
genomic variants relies on information about gene functions, gene
expression, physiology, and other genomic features. Phenotype-based
methods to identify variants involved in genetic diseases combine
molecular features with prior knowledge about the phenotypic
consequences of altering gene functions. While phenotype-based methods
have been successfully applied to prioritizing variants, such methods
are based on known gene–disease or gene–phenotype associations as
training data and are applicable to genes that have phenotypes
associated, thereby limiting their scope. In addition, phenotypes are
not assigned uniformly by different clinicians, and phenotype-based
methods need to account for this variability.

**Results:** We developed
an Embedding-based Phenotype Variant Predictor (EmbedPVP**, a
computational method to prioritize variants involved in genetic
diseases by combining genomic information and clinical
phenotypes. EmbedPVP leverages a large amount of background knowledge
from human and model organisms about molecular mechanisms through
which abnormal phenotypes may arise. Specifically, EmbedPVP
incorporates phenotypes linked to genes, functions of gene products,
and the anatomical site of gene expression, and systematically relates
them to their phenotypic effects through neuro-symbolic,
knowledge-enhanced machine learning. We demonstrate EmbedPVP’s
efficacy on a large set of synthetic genomes and genomes matched with
clinical information.  

**Availability:** EmbedPVP and all evaluation
experiments are freely available at https://github.com/
bio-ontology-research-group/EmbedPVP.

