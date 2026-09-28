# Annotation Guidelines
## NLP Bias Detector for Governance

### 1. Purpose

The purpose of this annotation framework is to identify
linguistic patterns in policy documents that may warrant
further human review for potential bias.

The annotation does NOT determine whether a policy is
objectively biased.

---

## 2. Annotation Categories

### Category 1: Loaded or Evaluative Language

Words or phrases that express strong judgment,
evaluation, or emotional characterization.

Examples:

- dangerous
- radical
- undeserving
- unfair
- problematic
- burden

Label:

LOADED_LANGUAGE

---

### Category 2: Stereotyping or Generalization

Statements that make broad claims about a group without
sufficient qualification.

Examples:

- "These people are unwilling to work."
- "Such communities are dependent on government support."

Label:

STEREOTYPING

---

### Category 3: Unequal or Group-Based Representation

Language that describes a social group in a way that may
create unequal or one-sided representation.

Examples:

- consistently describing one group negatively
- describing one group positively while another group is
  consistently described negatively

Label:

GROUP_REPRESENTATION

---

### Category 4: Strong Authority or Obligation

Language expressing strong requirements, commands, or
obligations.

Examples:

- must
- shall
- mandatory
- required

Label:

STRONG_MODALITY

Important:

Strong modality is NOT automatically bias.

It is recorded as a linguistic feature for further analysis.

---

### Category 5: Uncertainty or Hedging

Language expressing uncertainty or reduced confidence.

Examples:

- may
- might
- could
- possibly
- likely
- unlikely

Label:

UNCERTAINTY

Important:

Uncertainty is NOT automatically bias.

---

### Category 6: Neutral Language

The sentence does not contain an identifiable potential
bias indicator under the categories above.

Label:

NEUTRAL

---

## 3. Annotation Rules

### Rule 1

Annotate the sentence based on the actual language used.

Do not infer the author's intention.

### Rule 2

Do not label a sentence as biased simply because it
contains a negative word.

Example:

"The policy aims to reduce serious poverty."

The word "poverty" is negative in meaning, but this sentence
does not automatically indicate bias.

### Rule 3

Do not label "must", "shall", or "should" as bias by itself.

These words commonly occur in legislation and policy
documents.

### Rule 4

Consider the surrounding context whenever necessary.

A single word may have different meanings in different
contexts.

### Rule 5

If the evidence is unclear, use:

REVIEW

rather than forcing a binary decision.

---

## 4. Annotation Format

Each sentence should contain:

| Field | Description |
|---|---|
| sentence_id | Unique sentence number |
| sentence | Original sentence |
| indicator | Detected linguistic indicator |
| category | Annotation category |
| human_label | Human annotation |
| reason | Short explanation |
| reviewer | Person performing annotation |

---

## 5. Example

Sentence:

"The policy must protect vulnerable citizens."

Possible annotations:

Indicator:
vulnerable

Category:
LOADED_LANGUAGE

Human label:
REVIEW

Reason:
The term describes a group using an evaluative
characterization and requires contextual interpretation.

The word "must" should separately be recorded as:

Category:
STRONG_MODALITY

Human label:
NEUTRAL

Reason:
The word expresses a policy requirement and does not
independently demonstrate bias.

---

## 6. Research Principle

The system should identify potential linguistic indicators,
not make final judgments about whether a policy or institution
is biased.

Human review is required for contextual interpretation.
