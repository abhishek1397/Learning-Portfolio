# Core research terms

## Construct, definition, variable
- Construct: A theoretical concept you intend to study (e.g., “research impact,” “job satisfaction”). Measured indirectly via variables.
- Definition (operational): The precise, study-ready way you will observe/measure a construct (e.g., “impact measured by citations in Scopus in 4 years”).
- Variable: A measurable attribute that can vary (e.g., citation count, article type). Types: independent, dependent, control, categorical, continuous. These are general research-method terms; you’ll use Scopus metrics (below) as variables for evaluation.

Quick check: Can you give one construct you care about in your field and suggest ONE measurable variable for it?

# Types of journals and indexing (Scopus context)
- Scopus is a large, curated abstract and citation database covering journals, conference series, and book series selected by an independent Content Selection and Advisory Board (CSAB).[1][2]
- Each journal has a Scopus “Source” page with journal-level metrics: CiteScore, SJR, SNIP, coverage, subject areas, publisher, ISSN/e-ISSN, percent articles cited, percent reviews, and more.[3][4]
- Indexing in Scopus signals visibility and minimum quality/selection criteria enforced by CSAB (policies are transparent and updated; new titles may be eligible earlier than before, but still require publication history).[5][6]

Quick check: Where in Scopus would you look up a journal’s coverage and SNIP?

# Journal metrics in Scopus (with formulas where available)

## CiteScore (journal-level)
- What it is: A family of indicators based on 4-year windows, available on Scopus for active titles, with annual values and a monthly Tracker. Includes peer‑reviewed documents: articles, reviews, conference papers, data papers, and book chapters.[7][3]
- Definition (current methodology): “Citations received in four years to documents published in those four years, divided by the number of documents published in those four years.”[8]
- Formula (per Scopus/LibGuides summary):
  CiteScore = (Citations in years t−3…t to documents published in years t−3…t) / (Number of documents published in years t−3…t).[8][3]
- Notes: Updated method since 2020; provides rank and percentile within subject categories.[3][8]

## SJR: SCImago Journal Rank
- What it is: A prestige-weighted citation metric; citations from higher-SJR journals count more. Conceptually similar to PageRank and computed iteratively on a journal citation network.[4][3]
- Formal model: SJR assigns prestige based on citations, weighting by the citing journal’s SJR; computed via an iterative process with damping constants (e.g., d ≈ 0.85) until convergence.[9][10]
- Indicative equation elements (from SCImago technical note): SJR_i depends on citations from j to i divided by j’s total references, scaled by constants d and e, iterated to convergence; an average prestige-per-article variant SJRQ divides SJR by article count in the citation window.[9]

## SNIP: Source-Normalized Impact per Paper
- What it is: Field‑normalized citation impact; weights each citation by the “citation potential” of the journal’s subject field so fields with lower citation density give higher weight per citation.[8][3]
- Use: Compare journals across fields because it normalizes for field-specific citation behavior.[4]

## h-index (author- or journal-level as displayed in Scopus)
- Definition: A unit has h-index = h if it has h items each cited ≥ h times. Scopus computes and shows it for authors and sometimes sources in profiles.[3]

## Other useful journal page indicators in Scopus
- CiteScore rank and percentile, total citations in year, total documents in year, percent not cited, percent reviews.[8][3]

Quick check: If Journal A gets 2,400 citations in 2021–2024 to 800 docs published 2021–2024, what is its CiteScore for 2024?

# High‑value/reputed publishers (in Scopus coverage)
- Scopus indexes content from 7,000+ publishers worldwide, including major academic houses such as Elsevier, Springer Nature, Wiley, Taylor & Francis, SAGE, IEEE, ACS, etc., subject to CSAB selection policies. Selection does not equal endorsement of every title; titles are periodically reviewed and may be discontinued if standards lapse.[2][11][5]

Quick check: Why is “publisher reputation” not enough to choose a journal without checking its specific Source page?

# Journal finder / suggestion using Scopus
- Scopus “Sources” allows you to search and compare by title, ISSN, publisher, or subject area, then view Source Details with metrics (CiteScore, SJR, SNIP) to judge fit and impact.[4][3][8]
- Workflow you can use now:
  1) From Scopus, open Sources and filter by your subject area.
  2) Sort by CiteScore or SJR, then open 3–5 candidate Source pages.
  3) Read “Aims & Scope” on the publisher site from the Source page to confirm fit.
  4) Check acceptance of your article type (original article, review, data paper, etc.) and open access options.

Quick check: Which metric would you rely on to fairly compare journals across different fields, and why?

# When and where to publish (Scopus-aligned guidance)
- Where: Choose Scopus‑indexed journals whose scope matches your manuscript; examine CiteScore/SJR/SNIP, rank/percentile, percent reviews, and recent article topics on the Source page.[3][4][8]
- When: Submit when your study is methodologically complete, analysis is reproducible, and the target journal’s recent issues show receptivity to your topic; Scopus Source trend lines (CiteScore trend/Tracker) can indicate current momentum.[3]
- New journals: Policy changes allow earlier submissions for indexing consideration by CSAB once sufficient publication history exists, but quality screening persists.[6]

Quick check: Name two Source-page signals you’d check before selecting a journal for your paper.

# Types of publication (as recognized in Scopus coverage)
- Scopus covers peer‑reviewed serial content and various document types; common types include: Article, Review, Conference paper, Data paper, Editorial, Erratum, Book chapter, Article‑in‑Press, among others (classification by Scopus editorial team).[12][13]
- These types appear in journal and document records and influence what counts toward metrics (e.g., CiteScore includes articles, reviews, conference papers, data papers, and book chapters).[12][3]

Quick check: Which of these counts in CiteScore: Editorials, Book chapters? (Hint: check inclusions above.)

# Peer review: models and steps
- Models used by journals indexed in Scopus vary by publisher/journal; common models include: single‑anonymized (reviewer hidden), double‑anonymized (both hidden), open review (identities known), and variants; Elsevier summarizes pros/cons and guidance for reviewers.[14][15]
- Typical steps: Editor triage → desk decision → external peer review → revision cycles → accept/reject → production; reviewers evaluate novelty, methods, results, and ethics (publishers provide reviewer guides).[16][14]

Quick check: If a journal uses double‑anonymized review, what information is hidden from whom?

# Key formulas and how to use them
- CiteScore (year t):
  CiteScore_t = (Citations in t to documents published in t−3…t) / (Documents published in t−3…t).[8][3]
- h-index: Largest h such that at least h items each have ≥ h citations (as displayed in Scopus profiles).[3]
- SJR: Computed iteratively on the journal citation network with damping (d ≈ 0.85) and prestige transfer proportional to references; final SJR and size‑independent prestige per article (SJRQ) reported by SCImago; no simple hand calculation in practice.[10][9]
- SNIP: Field‑normalized—weights each citation by field citation potential; calculated by CWTS and displayed in Scopus; used to compare across fields.[4][8][3]

# Exam tips (Scopus-aware)
- If asked “Which metric fairly compares across fields?” answer: SNIP (field‑normalized).[4]
- If asked “Which metric reflects prestige of citing sources?” answer: SJR (prestige-weighted).[4][3]
- If asked “Which uses a 4‑year window including articles, reviews, conference papers, data papers, book chapters?” answer: CiteScore.[3]
- Remember: Check a journal’s Scopus Source page for up‑to‑date coverage, metrics, and rank/percentile before deciding where to submit.[4][3]



[53](https://linkinghub.elsevier.com/retrieve/pii/S2341287923001333)
[54](https://blog.scopus.com/scopus-institutional-profile-wizard-user-interface-redesign/)
