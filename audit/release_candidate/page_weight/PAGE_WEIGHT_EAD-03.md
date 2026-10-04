# Cold page weight before and after the logo derivatives (EAD-03)

Release candidate, Part A G4 item 2 (`audit/release_candidate/INSTRUCTIONS.md`). Method: the EAD-10 method, unchanged —
`audit/final_integration/f7_measure_baseline.py` (`docs/SUSTAINABILITY_METHOD.md`): headless Chromium, a local static server
(no compression, no CDN), one representative page per route class in each language, cold = new context and empty cache,
bytes received on the wire. Raw measurements: `before_logo_derivatives.json` (the build at `7895694`, every surface loading
the 10,018,273-byte master) and `after_logo_derivatives.json` (the same build with the derivatives served). Both runs on
2 October 2026 in the same session; desktop viewport, device pixel ratio 1, so each page fetched the 1× files.

| Page (cold) | Before, bytes | After, bytes | Images before | Images after | Requests after |
|---|---:|---:|---:|---:|---:|
| `home:en` /en/ | 10,320,168 | 306,856 | 10,018,273 | 4,658 | 8 |
| `home:ar` /ar/ | 10,355,006 | 341,694 | 10,018,273 | 4,658 | 8 |
| `explore:en` /en/explore/ | 10,319,596 | 306,284 | 10,018,273 | 4,658 | 8 |
| `explore:ar` /ar/explore/ | 10,353,840 | 340,528 | 10,018,273 | 4,658 | 8 |
| `domain_answer:en` /en/people/ | 10,340,969 | 327,657 | 10,018,273 | 4,658 | 8 |
| `domain_answer:ar` /ar/people/ | 10,381,863 | 368,551 | 10,018,273 | 4,658 | 8 |
| `evidence_index:en` /en/evidence/ | 10,368,006 | 354,694 | 10,018,273 | 4,658 | 8 |
| `evidence_index:ar` /ar/evidence/ | 10,417,932 | 404,620 | 10,018,273 | 4,658 | 8 |
| `evidence_record:en` /en/evidence/CLM-001/ | 10,318,984 | 305,672 | 10,018,273 | 4,658 | 8 |
| `evidence_record:ar` /ar/evidence/CLM-001/ | 10,353,407 | 340,095 | 10,018,273 | 4,658 | 8 |
| `compare:en` /en/evidence/compare/ | 10,339,884 | 326,572 | 10,018,273 | 4,658 | 8 |
| `compare:ar` /ar/evidence/compare/ | 10,385,130 | 371,818 | 10,018,273 | 4,658 | 8 |
| `sources_directory:en` /en/data/ | 10,614,001 | 600,689 | 10,018,273 | 4,658 | 8 |
| `sources_directory:ar` /ar/data/ | 10,705,622 | 692,310 | 10,018,273 | 4,658 | 8 |
| `readings_index:en` /en/readings/ | 10,313,592 | 300,280 | 10,018,273 | 4,658 | 8 |
| `readings_index:ar` /ar/readings/ | 10,345,662 | 332,350 | 10,018,273 | 4,658 | 8 |
| `reading:en` /en/readings/same-year-different-number/ | 10,339,897 | 326,585 | 10,018,273 | 4,658 | 8 |
| `reading:ar` /ar/readings/same-year-different-number/ | 10,379,155 | 365,843 | 10,018,273 | 4,658 | 8 |
| `methodology:en` /en/methodology/ | 10,338,478 | 325,166 | 10,018,273 | 4,658 | 8 |
| `methodology:ar` /ar/methodology/ | 10,379,632 | 366,320 | 10,018,273 | 4,658 | 8 |
| `measurement:en` /en/measurement/ | 10,338,767 | 325,455 | 10,018,273 | 4,658 | 8 |
| `measurement:ar` /ar/measurement/ | 10,382,091 | 368,779 | 10,018,273 | 4,658 | 8 |
| `trust_about:en` /en/about/ | 10,312,679 | 299,367 | 10,018,273 | 4,658 | 8 |
| `trust_about:ar` /ar/about/ | 10,344,638 | 331,326 | 10,018,273 | 4,658 | 8 |

Range: before 10,312,679–10,705,622 bytes; after 299,367–692,310 bytes. The difference is the logo alone: HTML, CSS,
JavaScript and fonts are byte-identical between the two runs except the `<img>` markup. One more request per page than
before: the product bar and the institutional band now fetch their own size (two small files) where both drew the one master.

## The derivatives

Master `site-src/assets/CauseWay_Master_Logo.png`, unchanged, SHA-256 `5830163d50f9badbef3227ec44e7705548e2fcc8a06b2d6ae33d56ade60c6a90`. Pure Lanczos resamples
(no crop, filter, recolour, mask or matte), written and checked pixel for pixel by `scripts/logo_derivatives.py` (`--check`
in CI and CONTRIBUTING.md §5):

| File | px | bytes | SHA-256 |
|---|---:|---:|---|
| `CauseWay_logo_32.png` | 32 | 1,378 | `1bdf8396b7c98bac34b242dcb6e4f83638298ee8cb96c80ef8ed8e458c77a4d4` |
| `CauseWay_logo_40.png` | 40 | 1,809 | `3bf0597f227d1913c2e9c45d2bb41d9bd6b9319f84a615e2a0764cdf8e725644` |
| `CauseWay_logo_48.png` | 48 | 2,473 | `7a11034ab33fb6524eb5edbe60a8a37e82de29a14fa39a49c3a2bdc841d43b97` |
| `CauseWay_logo_64.png` | 64 | 3,646 | `8043014d4373a5a183bd8f3f46b035765bff9ab1576ff5373ce38c42993a7fa2` |
| `CauseWay_logo_72.png` | 72 | 4,366 | `d99a13e5bcdf1d57cbb63e9fcc64d856b6be42b507d4fc59afe38db753b7d9e0` |
| `CauseWay_logo_80.png` | 80 | 4,966 | `542fe4595ae4cc23eef7dd4fbac30fe1cd8467739fc1fdde4d3b377d7bf443d5` |
| `CauseWay_logo_96.png` | 96 | 6,479 | `9ed7bbf592e321a0b69e34d3ac36b7d1870e450df0f431f5290b2714b0f63178` |
| `CauseWay_logo_144.png` | 144 | 11,582 | `85310ecc96c316acb7040f895a0e48dee36c897911d85b460769c6c723253478` |

Total 36,699 bytes for all eight. Surfaces (`design/08_ASSET_MAP.md` §1): the product bar (40 px, 48 px
from 900 px; `srcset` of 40/48/80/96), the institutional band (40/80), the 404 head (48/96), print (the bar's image), the
export identity line (32/64). The social-image template keeps the master file, so the 286 governed social images stay
byte-identical (`scripts/social_images.py --check` CURRENT); it is rendered offline and never served to a reader.
No carbon figure is computed (the method forbids it before the host is known).
