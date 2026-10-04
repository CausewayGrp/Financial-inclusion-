# Judgement — how decisions are made here

One page. The hard rules are in `AGENTS.md`; the change protocol is `CONTRIBUTING.md`. This page holds the judgement
that rules cannot: what to build, in what form, and when to stop.

1. **Four readers.** A citizen on a phone in Arabic, a journalist, a supervisor, a researcher. Every change answers:
   what can one of them do afterwards that they could not do before? No one-sentence answer, no build.
2. **The public value check.** User need → evidence already held → missing input → strongest truthful form → cost →
   what is lost if nothing is done. Before dropping something, look for a form of it that is true; before keeping
   something, look at how it could mislead when cropped or forwarded.
3. **Name the gap.** A content gap (the evidence cannot support more) is closed only by new evidence. An expression gap
   (the evidence supports more than the page says) is closed in the Master's copy. An implementation gap (the contract
   says it, the page does not) is closed in code. Fix at the layer that has the gap.
4. **Every blocker is a claim.** Ask what becomes false, unsafe or unverifiable if it is removed today. If nothing,
   resolve it through the authority that owns it. Never bypass a valid blocker; never keep a dead one for its name.
5. **Two lanes.** The release lane carries only release defects and release records; everything else is value-lane
   work on its own branch, reviewed on its own.
6. **Bound is not read.** A value tied to a source record is not a value seen in the source. Read the original (page,
   table, paragraph, series code) or say plainly that it has not been read. Dates are values.
7. **One fact, one place.** A number lives in the record whose sources give it. Another record names it by record ID,
   never copies it; otherwise the source trace lies.
8. **Presentation can create a claim.** Two numbers side by side read as a comparison, three rising points as a trend,
   a bold figure as the finding, a lone pair on Home as a ranking. Check what the arrangement says, not only the words.
9. **An alias broadens, never redefines.** A search alias may lead a reader to a record; it may not change what a word
   means on the site.
10. **Gates assert what a reader sees.** Test the rendered text, the drawn label, the visible table — not a class name
    — and give every gate a negative control that proves it still fails on its fault.
11. **Look before every push.** Open the changed pages at 390 px in Arabic and 1440 px in English. Gates prove rules;
    only looking proves the page.
