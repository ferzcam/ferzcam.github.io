---
title: "A homotopy-type-theoretic generalization of neurosymbolic inference"
collection: publications
permalink: /publication/hott_nesy
authors: 'Fernando Zhapa-Camacho, Robert Hoehndorf'
date: 'Jun 2026'
arxiv: 'https://arxiv.org/abs/2606.17851'
codeurl: 'https://github.com/bio-ontology-research-group/hott-nesy'
citation: 'hott_nesy'
---

A wide range of neurosymbolic (NeSy) systems compute one functional: a
belief-weighted sum of a logical quantity over a space of σ-structures, of
which weighted model counting, fuzzy logic, and probabilistic logic are special
cases. This account is built on sets, and a set deliberately forgets two things
that are important for NeSy: when two σ-structures are the same up to a symmetry
of the theory, and how many distinct proofs witness a query. Replacing the
underlying sets by types, in the sense of homotopy type theory, preserves this
information, and turns this functional into a belief-weighted homotopy
cardinality, a notion of size that counts each object in inverse proportion to
its symmetries. We develop the framework from scratch for NeSy systems, prove a
conservativity theorem that recovers the classical functional when symmetries
are trivial, and show that the symmetry our framework exposes is exactly the one
behind reasoning shortcuts. The payoff is concrete: the shortcut-aware concept
posterior that recent methods reach by ensembling or expressive density
estimation is the only symmetry-invariant point of the confusion-set simplex,
computable in closed form by averaging a single model over the symmetry group.
On MNIST reasoning-shortcut benchmarks this single-model wrapper is better
calibrated than a diversity-trained ensemble, while leaving label accuracy and
identifiable concepts untouched.
