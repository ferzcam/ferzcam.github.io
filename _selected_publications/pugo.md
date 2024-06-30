---
title: "Predicting protein functions using positive-unlabeled ranking with ontology-based priors"
collection: publications
permalink: /publication/pugo
authors: 'Fernando Zhapa-Camacho, Zhenwei Tang, Maxat Kulmanov, Robert Hoehndorf'
date: 'Jun 2024'
venue: 'ISMB 2024'
venueurl: 'https://www.iscb.org/ismb2024/home'
paperurl: 'https://doi.org/10.1093/bioinformatics/btae237'
codeurl: 'https://github.com/bio-ontology-research-group/pu-go'
pubicon: 'pugo'
---

Automated protein function prediction is a crucial and widely studied
problem in bioinformatics. Computationally, protein function is a
multilabel classification problem where only positive samples are
defined and there is a large number of unlabeled annotations. Most
existing methods rely on the assumption that the unlabeled set of
protein function annotations are negatives, inducing the false
negative issue, where potential positive samples are trained as
negatives.  We introduce a novel approach named PU-GO, wherein we
address function prediction as a positive-unlabeled ranking
problem. We apply empirical risk minimization, i.e., we minimize the
classification risk of a classifier where class priors are obtained
from the Gene Ontology hierarchical structure. We show that our
approach is more robust than other state-of-the-art methods on
similarity-based and time-based benchmark datasets. Data and code are
available at https: //github.com/bio-ontology-research-group/PU-GO.
