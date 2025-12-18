---
title: "LLM Agent Based Protein Function Prediction"
collection: publications
permalink: /publication/go-agent
authors: 'Fernando Zhapa-Camacho, Olga Mashkova, Robert Hoehndorf, Maxat Kulmanov'
date: 'Sep 2025'
venue: 'PSB 2026'
venueurl: 'https://psb.stanford.edu/'
codeurl: 'https://github.com/bio-ontology-research-group/go-agent'
paperurl: 'https://doi.org/10.1142/9789819824755_0036'
citation: 'go_agent'
---

Protein function prediction remains a fundamental challenge in
computational biology. Here, we present a Large Language Model
(LLM) agent-based system that improves protein function prediction performance
using knowledge-augmented reasoning and multi-source evidence synthesis.

Our approach integrates computational predictions with structured
protein metadata, scientific literature, and ontological knowledge
through a multi-stage reasoning process. An LLM agent equipped with
specialized tools progressively refines functional predictions by
querying constraints, cross-referencing evidence, and ensuring
biological plausibility. Furthermore, the system provides detailed
explanations for each prediction update, documenting the reasoning
process and evidence sources.

We evaluate our approach against established baseline methods across
three Gene Ontology sub-ontologies using four complementary metrics,
achieving superior performance in threshold-dependent measures,
attaining the lowest $S_{\min}$ scores across all ontologies and the
best $F_{\max}$ for Molecular Function and Cellular Component
ontologies.
We make our code publicly available at
\url{https://github.com/bio-ontology-research-group/go-agent}.


