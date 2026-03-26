# UC-0A — Complaint Classifier

**Framework:** R.I.C.E · CRAFT
**Done with your facilitator**

---

## Scenario

The City Operations team receives hundreds of complaints per week.
An AI classifier reads each complaint and outputs a category, priority,
reason, and flag. The output feeds the Director's dashboard every Monday.

A naive prompt produces a classifier that invents category names, misses
urgent complaints involving children and injuries, and gives confident
answers on genuinely ambiguous inputs.

---

## The Five Failure Modes

| # | Failure Mode | What it looks like |
|---|---|---|
| 1 | **Taxonomy drift** | Same complaint type gets different category names across rows |
| 2 | **Severity blindness** | "Child fell near school" → Priority: Standard |
| 3 | **Missing justification** | No reason field in output |
| 4 | **Hallucinated sub-categories** | AI outputs "Pedestrian Safety Incident" — not in schema |
| 5 | **False confidence on ambiguity** | Ambiguous complaint classified confidently without NEEDS_REVIEW |

---

## Classification Schema

| Field | Allowed values |
|---|---|
| `category` | Pothole · Flooding · Streetlight · Waste · Noise · Road Damage · Heritage Damage · Heat Hazard · Drain Blockage · Other |
| `priority` | Urgent · Standard · Low |
| `reason` | One sentence citing specific words from the description |
| `flag` | NEEDS_REVIEW or blank |

**Severity keywords — must trigger Urgent:**
`injury` · `child` · `school` · `hospital` · `ambulance` · `fire` · `hazard` · `fell` · `collapse`

---

## Enforcement Rules Your agents.md Must Include

1. Category must be exactly one value from the allowed list. No variations.
2. Priority must be Urgent if description contains any severity keyword.
3. Every output row must include a reason field citing specific words from the description.
4. If category cannot be determined confidently — output `category: Other` and `flag: NEEDS_REVIEW`.
5. Never invent category names outside the allowed list.

---

## Skills to Define in skills.md

### `classify_complaint`
- Input: one complaint row (dict with description, location fields)
- Output: dict with category, priority, reason, flag
- Error handling: vague/short descriptions → Other + NEEDS_REVIEW

### `batch_classify`
- Input: path to test CSV file
- Output: path to results CSV file
- Error handling: malformed rows logged and skipped, processing continues

---

## Input File

```
data/city-test-files/test_[your-city].csv
```

Choose the file matching your city: pune / hyderabad / kolkata / ahmedabad

## Output File

```
uc-0a/results_[your-city].csv
```

## Run Command

```bash
cd uc-0a
python3 classifier.py --input ../data/city-test-files/test_pune.csv \
                      --output results_pune.csv
```

---

## CRAFT Commit Formula

```
UC-0A Fix [failure mode]: [why it failed] → [what you changed]
```

Examples:
```
UC-0A Fix severity blindness: no keywords in enforcement → added injury/child/school/hospital triggers
UC-0A Fix taxonomy drift: no fixed enum → restricted category to allowed list only
```
