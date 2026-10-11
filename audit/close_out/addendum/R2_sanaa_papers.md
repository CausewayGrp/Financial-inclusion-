# R2: Sana'a Center / DeepRoot papers S1 and S2 (duplicates, S1 regulatory history, CBY Circular No. 11 of 2014)

Retrieval date: 2026-10-11 (05:39 to 05:54 UTC). Tools: curl, poppler `pdfinfo`/`pdftotext`/`pdftoppm`, page images read visually where the text layer was unreliable (figures, Arabic, scans). Python only with `python3 -I`, scripts outside the download folder.
Downloads: `scratchpad/addendum/dl/r2/` (sub-folders `cby/`, `sec/`).
Page numbers: S1 and S2 printed page numbers equal the PDF page index (S1 page 2 shows "2"; S2 page 3 shows "3"). Quotes are copied from the PDF text layer. Where a word was broken at a line-end hyphen, the printed hyphen is restored (for example "CBY-Sana’a", "cash-in", "Al-Amal"). Curly apostrophes are as printed.

---

## 0. Findings first

1. **S1: the two copies are byte-identical.** SHA-256 `35bf57cb…6abe` for both. One record, two locators.
2. **S2: the two copies differ in bytes but are the same document.** They have the same title, date, author line, 16 pages and body text. Only the cover (page 1) differs: title capitalisation and the "prepared by" sentence. The DeepRoot copy is an earlier build (PDF created 19 Sep 2024); the Sana'a copy is later (24 Sep 2024). One record, two locators, with the cover difference noted.
3. **Authorship as printed.** Both papers say "By: The Sana’a Center Economic Unit" (S1) or "By The Sana’a Center Economic Unit" (S2). The Sana'a Center web pages credit **Wadhah Al-Awlaqi** as author of both papers (byline and citation text), which does not match the PDFs. The words "joint initiative" appear in neither PDF.
4. **Dates.** S1: the Sana'a page shows **7 March 2022**, the DeepRoot page shows **2022-03-11**, and the PDF prints only "March 2022". S2: the cover prints "Date: September 23, 2024" and both web pages give 23 September 2024, but every running footer on pages 2–15 of S2 reads "Rethinking Yemen’s Economy | March 2024".
5. **"Publisher: DeepRoot Consulting" misstates both papers.** Each says it was prepared by the Sana'a Center for Strategic Studies, in coordination with DeepRoot Consulting and CARPO, within Rethinking Yemen's Economy. S2's own citation line names all three institutions. DeepRoot is a project partner and a mirror host, not the sole publisher.
6. **S1 regulatory history.** The paper confirms (a): "Circular No. 11 of 2014", issued "In late 2014" (Figure 1 date: "DEC 11, 2014"), set up a bank-led model. It confirms (b) with an exact date: a **March 2020** CBY-Sana’a directive, decree or decision opened e-rial licensing to non-bank institutions. It confirms (c): the paper says CBY-Aden was "holding to the prewar legal framework" and "sticking to the bank-led model created prior to the conflict". S1 refers to **no** later Aden instructions, from 2023 or any other year. The paper dates from March 2022.
7. **S1 is internally inconsistent on its central framing.** Pages 5 and 23 say a banks-only regime "was the legal framework/practice prior to 2014". Page 11 says "Prior to 2014, there was no clear regulatory framework". Pages 12–13 say the bank-led model was created by Circular No. 11 in late 2014. There are also at least 10 number or date conflicts (§6). This supports taking no numbers from S1.
8. **Primary source.** No public copy of CBY Circular No. 11 of 2014 was found. Evidence that it exists, and its official Arabic title, come from Article 13 of the CBY-Sana’a Governor's Decision No. (1) of 2020, of which a scan was read: "المنشور رقم (11) لسنة 2014م بشأن القواعد التنظيمية لتقديم خدمات النقود الالكترونية عبر الهاتف المحمول بواسطة البنوك". That decision states that it does **not** repeal the circular. The key "who may provide" sentence was found only in a secondary source, an Institute of Banking Studies (Sana'a) study of 2020: "No one is allowed to provide electronic money service via mobile phone except through a licensed bank."
9. **Context for the time bound (not from S1).** CBY-Aden later issued "التعليمات المنظمة لأعمال مقدمي خدمات الدفع و/أو مشغلي/مديري أنظمة الدفع" (Ref. 720/CBY/2022, 14/9/2022). It defines payment service providers as **non-bank** financial institutions licensed by the CBY. Any website statement that CBY-Aden kept the bank-only framework must therefore be bounded to the paper's date (March 2022).

---

## 1. Files retrieved (2026-10-11)

| ID | URL | Bytes | SHA-256 | Notes |
|---|---|---|---|---|
| S1-SC-PDF | https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_En.pdf (the "Read the full white paper" / "Download PDF" link on https://sanaacenter.org/publications/policy-research/16974) | 841,204 | `35bf57cb523803be31cd909e2748041978646a5cec15b4be43128ddb46dd6abe` | 43 pages (pdfinfo); InDesign 17.1; CreationDate 2022-03-06 14:41:20 UTC; server Last-Modified Sun, 06 Mar 2022 22:12:53 GMT |
| S1-DR-PDF | https://deeproot.consulting/en/publications/73/download | 841,204 | `35bf57cb523803be31cd909e2748041978646a5cec15b4be43128ddb46dd6abe` | **Identical bytes.** Content-Disposition filename "CHALLENGES AND PROSPECTS FOR ELECTRONIC MONEY_En.pdf"; server Last-Modified Wed, 24 Jan 2024 19:03:13 GMT (re-upload of the same bytes) |
| S1-SC-AR | https://sanaacenter.org/files/Rethinking_Yemens_Economy_No10_Ar.pdf | 961,533 | `8e5602a27366ee9924a1596c3c0178c244a07ac8fac32033e341a0431f43b177` | Arabic edition, 42 pages, created 2022-03-06; its page numbers differ from the English edition |
| S2-SC-PDF | https://sanaacenter.org/files/Enhancing_the_Role_of_Microfinance_Banks_for_Sustainable_Impact_in_Yemen_en.pdf (linked from https://sanaacenter.org/publications/policy-research/23418) | 405,030 | `f580a688e8da06214d12c6c2f707541bffd9e25d46e8427931916c2019d2c8f0` | 16 pages; InDesign 19.5; CreationDate 2024-09-24 08:47:00 UTC; Last-Modified Wed, 25 Sep 2024 07:19:40 GMT |
| S2-DR-PDF | https://deeproot.consulting/en/publications/83/download | 405,751 | `9a33fd9ff3e3e787a6951e637ad2b8651ac907be32e0b70ce4140054ac90a2dc` | 16 pages; CreationDate 2024-09-19 08:55:57 UTC; Last-Modified Mon, 23 Sep 2024 10:42:38 GMT. **Different bytes** |
| S1-SC-page | https://sanaacenter.org/publications/policy-research/16974 | 163,179 | `ffbae4c3…92e5c`¹ | |
| S1-DR-page | https://deeproot.consulting/en/publications/challenges-and-prospects-for-electronic-money-and-payment-systems-in-yemen | 36,580 | `2aa91490…2b80`¹ | |
| S2-SC-page | https://sanaacenter.org/publications/policy-research/23418 | 238,759 | `dcd34b10…a46c`¹ | |
| S2-DR-page | https://deeproot.consulting/en/publications/enhancing-the-role-of-microfinance-banks-for-sustainable-impact-in-yemen | 39,996 | `67817d16…e5c`¹ | |

¹ The HTML pages are dynamic: they carry view counters and "trending" lists, so their hashes are not stable identifiers. Full hashes of the HTML files:
- S1-SC-page `ffbae4c3642f569509095140ac6ce120935cd8796627edf828df522fac0b2ee7`
- S1-DR-page `2aa91490dcac6806cce7a7646ce1e72ffce496fa03c96d1b6cd3ed00da9b3e80`
- S2-SC-page `dcd34b1081bbe64cc6f7204a042333406783cf2c032cdd406bf88845aebaa46c`
- S2-DR-page `67817d16a292a15c1169044392e32e81327ff4e4314c20ec0ec68b9036292e5c`

Files retrieved for task 4 are listed in §7.

---

## 2. S1 duplicate check: "Challenges and Prospects for Electronic Money and Payment Systems in Yemen"

**Verdict: the same document. The bytes are identical (same SHA-256 and same size), so every item below is identical by construction.**

| Item | Sana'a Center copy | DeepRoot copy |
|---|---|---|
| Title (cover, p.1) | "CHALLENGES AND PROSPECTS FOR ELECTRONIC MONEY AND PAYMENT SYSTEMS IN YEMEN" | identical |
| Author line (p.1 and p.2) | "By: The Sana’a Center Economic Unit" | identical |
| Date printed (p.1, p.2, all footers) | "March 2022"; footer "Rethinking Yemen’s Economy \| March 2022" | identical |
| Pages | 43 (printed pages 2–40 numbered; p.41 a plain dark page; p.42 "PREVIOUS PUBLICATIONS"; p.43 back cover)² | identical |
| First paragraph (p.5) | "Yemen has a heavily cash-based economy with low levels of financial inclusion. The country’s formal banking sector is highly underdeveloped, undercapitalized and concentrated in urban areas, leaving it inaccessible for the majority of the Yemeni population. …" | identical |
| Last paragraph (p.40) | "To unleash the potential of mobile money, regulators must create an open and level playing field that allows both banks and non-bank providers to offer mobile money services, … Increased outreach to hard to reach rural areas and overall financial system liquidity would be welcomed by humanitarian actors that seek to make secure cash transfers to beneficiaries in rural areas." | identical |

² `file(1)` reports "17 page(s)", which comes from a partial page tree in this linearised PDF. `pdfinfo` and the full text extraction both give 43 pages. Use 43.

**Authorship and series, verbatim:**
- Cover (p.1): "By: The Sana’a Center Economic Unit" / "March 2022". The cover logo reads "RETHINKING YEMEN’S ECONOMY".
- Inside cover (p.2): "This white paper was prepared by the Sana’a Center for Strategic Studies, in coordination with the project partners DeepRoot Consulting and CARPO – Center for Applied Research in Partnership with the Orient."
- p.2: "Note: This document has been produced with the financial assistance of the European Union and the Embassy of the Kingdom of the Netherlands to Yemen. The recommendations expressed within this document are the personal opinions of the author(s) only, and do not represent the views of the Sana’a Center for Strategic Studies, DeepRoot Consulting, CARPO - Center for Applied Research in Partnership with the Orient, or any other persons or organizations with whom the participants may be otherwise affiliated. …" The page also carries the mark "Co-funded by the European Union".
- Series line (running footer, every numbered page): "Rethinking Yemen’s Economy | March 2022".
- Back cover (p.43): "The project is implemented by CARPO – Center for Applied Research in Partnership with the Orient, DeepRoot Consulting and the Sana’a Center for Strategic Studies. It is funded by the European Union and the Embassy of the Kingdom of the Netherlands to Yemen." Also: "Contact: Sana’a Center for Strategic Studies, Haddah Street, Sana’a, Yemen | Email: info@devchampions.org".
- No series number is printed in S1. The Sana'a file name contains "No10", but that is **NOT VERIFIED** as an official RYE white-paper number. S1 has no "Please cite as" line.

**Dates on the web pages:**
- Sana'a Center page: the visible date is "March 7, 2022". `article:published_time` and JSON-LD `datePublished` are "2022-03-07T11:00:48+00:00". The page's "Cite This" text reads: "Wadhah Al-Awlaqi, “Challenges and Prospects for Electronic Money and Payment Systems in Yemen”, Sana’a Center for Strategic Studies, 7 March, 2022, available at: https://sanaacenter.org/publications/policy-research/16974". The page credits "Wadhah Al-Awlaqi" (Chief Economist) as author; the meta author is "Sana'a Center". The page's tag is "Rethinking Yemen's Economy".
- DeepRoot page: the visible date is "2022-03-11", shown twice. No author is shown. The page reproduces the Executive Summary text verbatim.
- **Answer: 7 March 2022 is the Sana'a Center page date; 11 March 2022 is the DeepRoot page date.** The PDF itself prints only "March 2022". Its internal creation timestamp is 2022-03-06 UTC, and the Sana'a server copy was last modified 2022-03-06 22:12:53 GMT.
- Use "March 2022" as the document date. Record 7 March 2022 as the date of first web publication, at the Sana'a Center.

**Authorship discrepancy:** the PDF says "The Sana’a Center Economic Unit"; the Sana'a web page credits Wadhah Al-Awlaqi. The PDF should take precedence for attribution. Whether Al-Awlaqi led the Economic Unit's drafting is **NOT VERIFIED**, because the PDF names no individual.

---

## 3. S2 duplicate check: "Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen"

**Verdict: the same document with a different cover build.** The bytes differ: `f580a688…c8f0` (Sana'a) against `9a33fd9f…a2dc` (DeepRoot). The full text was compared, both raw and with layout, and every page was rendered at 40 dpi and compared pixel by pixel. **Pages 2–16 are pixel-identical.** Page 1 differs in two places only:

| Item | Sana'a Center copy | DeepRoot copy |
|---|---|---|
| Title on cover (p.1) | "ENHANCING THE ROLE OF MICROFINANCE BANKS FOR SUSTAINABLE IMPACT IN YEMEN" (upper case) | "Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen" (title case) |
| Preparation line (p.1, verbatim) | "This policy brief was prepared by Sana’a Center in coordination with its project partners, the DeepRoot Consulting and the Center for Applied Research in Partnership with the Orient (CARPO), as part of the Rethinking Yemen’s Economy initiative." | "This policy brief was prepared by the Sana’a Center for Strategic Studies in coordination with the project partners, DeepRoot Consulting and CARPO – Center for Applied Research in Partnership with the Orient. It is informed by input from the Development Champions Forum." |
| Series / number / date (p.1) | "POLICY BRIEF" … "No: 29" … "Date: September 23, 2024" | identical |
| Author line (p.1) | "By The Sana’a Center Economic Unit" | identical |
| Citation line (p.1) | "Please cite as: Sana’a Center Economic Unit, “Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen,” Rethinking Yemen’s Economy, RYE Policy Brief 29, Sana’a Center for Strategic Studies, DeepRoot Consulting, and CARPO, September 2024. Available at: https://devchampions.org/publications/policy-brief/Enhancing_the_Role_of_Microfinance_Banks_for_Sustainable_Impact_in_Yemen" | identical |
| Pages | 16 | 16 |
| First paragraph (p.1, Executive Summary) | "Yemen’s microfinance sector is undergoing a radical transformation. Despite initial success in empowering small businesses, the ongoing conflict has exposed deep vulnerabilities. …" | identical |
| Last paragraph (p.16, back cover) | "The Rethinking Yemen’s Economy (RYE) Initiative and its associated Development Champions Forum aim to contribute to … The RYE initiative is implemented by DeepRoot Consulting, the Sana’a Center for Strategic Studies, and CARPO – Center for Applied Research in Partnership with the Orient. It is funded by the European Union." | identical |
| Last body paragraph (p.15) | "Develop a system to monitor MFBs’ impact on financial inclusion, poverty reduction, and rural development." | identical |
| Running footer (pp.2–15) | "Rethinking Yemen’s Economy \| March 2024" (14 occurrences) | identical |
| Back cover contact (p.16) | "Contact: Sana’a Center for Strategic Studies, Haddah Street, Sana’a, Yemen \| Email: info@sanaacenter.org" | identical |

**Dates:**
- Printed cover date: "Date: September 23, 2024".
- Running footers: "March 2024". This internal inconsistency is in both copies; it is probably a template carry-over, but that is **NOT VERIFIED**.
- Sana'a page: visible "September 23, 2024"; `article:published_time` 2024-09-23T11:35:52+00:00; `dateModified` 2024-09-23T15:06:48+00:00. Its "Cite This" text reads: "Wadhah Al-Awlaqi, “Enhancing the Role of Microfinance Banks for Sustainable Impact in Yemen”, Sana’a Center for Strategic Studies, 23 September, 2024, …". The byline is "Wadhah Al-Awlaqi".
- DeepRoot page: "2024-09-23"; "Authors: Sana’a Center Economic Unit".

**Web page against PDF:** the Sana'a S2 web page text says the RYE initiative "is funded by the European Union and the Embassy of the Kingdom of the Netherlands to Yemen". The S2 PDF (p.16) says only "It is funded by the European Union."

**Content note:** S2 contains no statement about e-money or mobile-money regulation. A search for "e-money", "electronic money", "mobile money" and "wallet" found nothing. The only hits for "mobile" or "FinTech" are recommendations on pp.1 and 15. S2 names the authorities as "The government-affiliated CBY-Aden" and "The CBY-Sana’a, affiliated with the Houthi (Ansar Allah) authorities since September 2016" (p.5), and also "the rival CBYs" and "the fractured CBY in Sana’a and Aden".

---

## 4. Does "Publisher: DeepRoot Consulting" misstate it?

**Yes, for both papers.**
- S1 p.2: "This white paper was prepared by the Sana’a Center for Strategic Studies, in coordination with the project partners DeepRoot Consulting and CARPO …"; the contact on p.43 is the Sana'a Center.
- S2 p.1 citation line: "Rethinking Yemen’s Economy, RYE Policy Brief 29, Sana’a Center for Strategic Studies, DeepRoot Consulting, and CARPO".

DeepRoot is one of three implementing partners of the RYE initiative and hosts a mirror copy. Its pages do not call it the publisher; the S2 DeepRoot page lists "Authors: Sana’a Center Economic Unit".

Suggested record wording:
- **Author:** Sana’a Center Economic Unit.
- **Publisher:** Sana’a Center for Strategic Studies, in coordination with DeepRoot Consulting and CARPO (Rethinking Yemen’s Economy initiative).
- **For S2, the paper's own form:** "Sana’a Center for Strategic Studies, DeepRoot Consulting, and CARPO".

The phrase "joint initiative" is not printed in either PDF; do not quote it as if it were.

---

## 5. S1 regulatory history: verbatim, with pages

**Number and year the paper gives:**
- "Circular No. 11 of 2014" (pp.12, 19, 23, 24, 27; fn 48, 50, 55).
- "CBY Circular No. (11) of 2014" (Figure 1, p.13).
- "Circular No. 11 (2014)" (p.19).
- Issue timing: "In late 2014" (p.12). The Figure 1 timeline is dated "DEC 11, 2014" (p.13; read from the rendered image).

### (a) The bank-led model under Circular No. 11 of 2014

- p.5 (Executive Summary): "Broadly speaking, e-money adoption around the globe has been accompanied by three types of regulatory environments: highly, moderately and minimally regulated markets. In Yemen, a highly regulated market – which grants the right to provide e-money services only to banks – was the legal framework prior to 2014, though in practice adoption remained minimal."
- p.11: "Prior to 2014, there was no clear regulatory framework to govern the provision of electronic financial services in Yemen."
- p.12: "In late 2014, the CBY issued Circular No. 11 of 2014 to enable the establishment of a bank-led model to provide electronic money services, with support from USAID, the World Bank, the Consultative Group to Assist the Poor (CGAP) and the Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ). The model was informed by a nearly two-year review process and discussions with the private sector.[15] The 2014 circular determined the basic regulatory and supervisory aspects for electronic mobile money services – e.g. license requirements and technical capacities as well as duties and responsibilities of envisioned actors and the bank-oriented providers of such services. It allowed for licensed banks to contract or outsource the provision of electronic mobile money services to telecommunications companies and agents, while holding banks ultimately responsible for the actions of these entities."
- p.12: "Both sets of internationally backed reforms were cut short by the onset of conflict in Yemen. No implementation plan was developed or carried out for Circular No. 11 due to the country’s widening political divisions."
- p.13 (Figure 1, image text): "DEC 11, 2014 / Launch / CBY Circular No. (11) of 2014 endorses bank-led model for e-money services, laying out basic regulatory and supervisory aspects for mobile e-money service." Source line: "Sources: CBY, World Bank".
- p.19: "The CBY-Sana’a decree in March 2020 contradicted CBY Circular No. 11 of 2014, which restricted the provision of e-rial services to banks operating in Yemen."
- p.19: "While the bank-oriented model involved a limited number of actors – banks holding trust accounts and issuing e-rials; mobile network operators contracted to deliver network services; and agents available on the ground to manage electronic money services on behalf of banks – the new model gives additional financial institutions the right to obtain a license to contract a third party to manage agent networks delivering e-money services."
- pp.19–20: "In addition, the March 2020 decree set no maximum limit on the amount of e-money one financial institution could issue, overriding the regulation in Circular No. 11 (2014) that mandated that a bank was only allowed to issue electronic money up to 15 percent of its paid capital and statutory reserves (by law in Yemen, a commercial bank has to put up YR6 billion in capital to be licensed to operate)."
- p.23: "In Yemen, a highly regulated market – which grants the right to provide e-money services only to banks – was the legal practice prior to 2014. Indeed, the regulatory framework outlined under Circular No. 11 of 2014 established a conservative and narrow model, allowing banks to issue and manage electronic money either directly or through agents, by acting as the intermediary financial channel to open e-money accounts and facilitate cash-in and cash-out services. Under this model, clients and recipients were required to have a bank account to conduct e-money services such as e-payments, balance inquiries and transfers between accounts. The distinguishing facet of this model is that banks are the main legal providers of e-money services while other potential actors, such as mobile phone companies or financial services companies, are secondary players. These secondary players work on behalf of authorized banks either as agents, to deliver cash-in and cash-out services, or to provide the mobile network services essential to operate e-money transactions. The mobile network operator’s participation would be limited to providing the data transfer services, while the banks offer individual accounts and organize the infrastructure such as cash-in/cash-out payments through ATMs, branches, or an agent network. The bank-led model created prior to the conflict in Yemen saw a slow service growth as it limits competition and scope for innovators to access unbanked populations.[45]"
- p.24: "As noted, Circular No. 11 of 2014 stipulated that the total amount of e-rials in each bank’s e-wallet must be the equivalent of physically deposited rial notes, and the total value of the e-wallet cannot exceed 15 percent of a bank’s paid-in capital and legal reserve.[48]"
- p.24, fn 48: "According to Circular No. 11 of 2014, a licensed bank is not allowed to issue electronic money exceeding 15 percent of its paid-up capital and the statutory reserve, except with prior approval from CBY. The obligatory value of the e-rial issued by the e-wallet should equal 100 percent of the accumulated trust (pool) account in the bank."
- p.27: "Individuals without an e-money account can only receive money in cash according to transaction ceilings dictated by Circular No. 11 of 2014: YR30,000 per financial transaction and YR50,000 for total transactions per day, while the maximum e-rial balance per person cannot exceed YR300,000.[55]"
- p.28: "The use of e-rials across the country since 2016 under the bank-led model has been restricted to financial transfers among held accounts, capped cash-in or cash-out transactions, and to a minimal extent the payment of cell phone, internet, electricity, and water bills, which can be made easily via GAPPs branches or money exchange outlets."
- **Source trace for (a).** S1's citations for the circular's content (fn 15, 50, 55) point to John Owens, "Central Bank of Yemen issues new mobile banking regulations," AFI, 7 March 2015. I retrieved that post (§7). It does **not** state the circular number, the 15 percent cap, the transaction ceilings or the KYC tiers. Fn 55 also gives a mismatched URL (http://beta.wenet-ye.com/en/about). The 15 percent cap and the "licensed bank only" rule do appear in the IBS (Sana'a) 2020 study (§7).

### (b) CBY-Sana’a moving to non-bank provision after the split, and from when

The date the paper gives is **March 2020**. The instrument is variously called a "circular" (p.10), "directive" (p.18), "decree" (p.19), and "Decision no. 1 of the Central Bank Governor" (fn 34). It is dated "March 11, 20202" [sic] in fn 7 and "March 8, 2020" in fn 34; see §6.

- p.5: "The Yemeni conflict escalated in 2015, and by 2016 the CBY was fragmented across frontlines, with rivaling branches vying for dominance in Aden and Sana’a – affiliated with the internationally recognized government and the Houthi authorities, respectively. In the years following, the CBY-Sana’a has increasingly taken steps to establish a minimally regulated, nonbank led model for e-money services, which the CBY-Aden has opposed, holding to the prewar legal framework."
- p.10: "However, to date there is no ratified legal framework formalizing the operations of electronic payment service providers, other than the circular issued by CBY Sana’a in March 2020 intended to regulate such services.[7]"
- p.15: "President Abdo Rabbu Mansour Hadi ordered the relocation of the CBY headquarters from Sana’a to Aden in September 2016, leaving the central bank fragmented between the two cities.[19]"
- p.18: "During 2020, the Houthi authorities finalized a number of measures to reform the previously established legal framework associated with the provision of e-money services. Such measures would, of course, only pertain to areas under Houthi control. In early 2020, CBY-Sana’a established a Payments System Department (PSD) within its organizational structure to develop national e-payment institutional capacity and its functional framework, and to supervise the newly envisioned e-rial payment system."
- p.18: "In March 2020, CBY-Sana’a issued a new directive that expanded the scope of the type of financial service providers eligible to obtain a license to offer e-rial services.[34] The directive paved the way for non-bank institutions such as money exchange companies, traders and non-financial institutions to be granted permission to offer e-rial services.[35] CBY-Aden challenged the legality of this directive, while senior banking officials warned of the potential repercussions.[36] (More on this below.)"
- p.19: "The new Houthi legal framework created an opportunity for less regulated actors – such as money exchange companies, traders and other non-bank institutions – to obtain licenses from CBY-Sana’a to perform e-money issuance and e-payment management services previously reserved for banks."
- p.19: "… the new model gives additional financial institutions the right to obtain a license to contract a third party to manage agent networks delivering e-money services. These financial institutions are then permitted to receive physical cash liquidity in exchange for e-rial balances and manage e-payment services."
- p.20: "The decree also created payment instruments outside the mobile phone app, such as prepaid cards and other fintech tools."
- p.30: "While CBY-Sana’a issued an initial e-money license to ONE Cash in July 2020, CBY-Aden has not yet accepted its request to obtain the license. (Despite receiving the final license in early 2022 from the CBY-Sana’a, as of this writing ONE Cash is yet to launch operations in Houthi-controlled areas.)"
- p.35: "Two distinct models have been created out of the two competing central bank branches: a recently created non-bank model in Houthi-controlled areas and CBY-Aden sticking to the bank-led model created prior to the conflict."
- **Primary check of the March 2020 instrument** (scan read, pages 1–3 and 45 of 45; see §7). It is "قرار محافظ البنك المركزي رقم (1) لسنة 2020م بشأن القواعد التنظيمية لتقديم المؤسسات المالية خدمات الدفع الإلكترونية عبر الهاتف المحمول". The decision is dated 2020/03/08 and its cover letter 2020/03/11. Article 2 defines "الشركة المرخصة" as a public or limited-liability shareholding company licensed to carry on electronic payment service activities under the decision. **Article 13 states that the decision does not repeal Circular No. (11) of 2014.** S1's wording on p.19, "contradicted", is the paper's characterisation; the decision itself states coexistence. Neither the "contradicted" reading nor the decision's coexistence wording should be presented as settled fact without attribution.

### (c) CBY-Aden keeping the pre-war framework; later Aden instructions

- p.5: "… which the CBY-Aden has opposed, holding to the prewar legal framework."
- p.18: "CBY-Aden challenged the legality of this directive, while senior banking officials warned of the potential repercussions.[36]" Fn 36 cites "“Cautionary statement [AR],” CBY-Aden statement, April 2020, https://www.cby-ye.com/2020/04/…". That URL returned HTTP 500 on 2026-10-11.
- p.20: "In January 2020, CBY-Aden warned Yemeni banks and money exchange firms against adhering to the Houthi ban on new rial banknotes and dealing in the e-rial. The CBY-Aden stated that the CBY-Sana’a circular was issued by an illegal entity, outside the legal framework of the banking sector, and would lead to loss of trust in cash. On September 21, 2020, the CBY-Aden issued a circular decrying Houthi authorities’ efforts to establish an e-money model and process real-time clearing settlements for interbank payment transactions outside the legal framework of the banking sector." No footnote is attached to the 21 September 2020 circular.
- p.20: "Over the last two years, CBY-Aden has conducted several consultations with the World Bank, the Arab Monetary Fund (AMF), USAID, and other international development donors to develop a payment system infrastructure. The technical support offered by these bodies has included institutional capacity building; this resulted in the establishment of the CBY-Aden’s own Payment Systems Department (PSD)."
- p.35: "… and CBY-Aden sticking to the bank-led model created prior to the conflict."
- p.38: "° Strengthen the institutional and governance structure of the national payment system and the Payment Systems Department (PSD), established in mid-2020 inside CBY, …"
- p.38 (recommendation): "° Refrain from supporting developments in e-money services that are outside of the current legal framework in Yemen."
- **Later Aden instructions: none in S1.** The PDF contains no "2023" and no "instruction". S1 is dated March 2022, so its CBY-Aden statements describe the situation up to that date only. For instruments found outside the paper, see §8.
- For balance, S1's own long-term recommendations (pp.39–40) favour "a gradual shift to a non-bank led model for e-currency issuance" (p.39) and "an open and level playing field that allows both banks and non-bank providers to offer mobile money services" (p.40). Over the short term (pp.37–38), they urge regulators not to make unilateral changes and urge donors to stay within the current legal framework.

### Naming the paper uses for the two authorities (English S1)

- **Sana'a branch:**
  - "CBY-Sana’a" ×25; "CBY Sana’a" ×1 (p.10); "CBY-Sanaa" ×1 (p.8); "Central Bank of Yemen (Sana’a)" (fn 7); "Central Bank of Yemen – Sana’a" (fn 34).
  - Paired with "the Houthi authorities" ×17, "de facto Houthi authorities" ×2, "the Houthis" ×2 and the "Houthi-affiliated National Salvage Government (NSG)".
- **Aden branch:**
  - "CBY-Aden" ×24; "the CBY in Aden" ×1 (p.38).
  - Paired with "the internationally recognized Yemeni government" ×3 and "internationally recognized government" ×1.
- **Both branches together:**
  - "rivaling branches vying for dominance in Aden and Sana’a" (p.5);
  - "two competing central bank branches" (p.35);
  - "the fragmented CBYs in Sana’a and Aden" (p.37);
  - "the CBY branches" (p.37);
  - p.23: "the central bank on one side (Sana’a) is dominant domestically, the central bank on the other (Aden) is the sole holder of international legitimacy".
- "CBY" with no branch is used for the pre-split bank, and also for the 2015–2019 licences (p.8, p.24).

**Arabic edition of S1, for the bilingual record** (transcribed from page images, kashida removed):
- AR p.4 (= EN p.5): "في اليمن، اتسم الإطار القانوني السائد قبل عام 2014 بسوق شديدة التنظيم -والتي تمنح الحق في تقديم الخدمات الإلكترونية للبنوك فقط- رغم أن التطبيق ظل محدودًا من الناحية العملية. تصاعدت حدة الصراع اليمني عام 2015، وبحلول 2016 كان البنك المركزي اليمني منقسمًا عبر خطوط المواجهة، مع تنافس فرعي عدن وصنعاء على الهيمنة، الفرع التابع للحكومة المعترف بها دوليًا والآخر التابع لسلطات الحوثيين، على التوالي. في السنوات التالية، اتخذ البنك المركزي في صنعاء خطوات تصعيدية لتأسيس نموذج غير مصرفي محدود التنظيم لتقديم الخدمات المالية الإلكترونية، وهو ما عارضه البنك المركزي في عدن، متمسكًا بالإطار القانوني لما قبل الحرب."
- AR p.11 (= EN p.12): "أواخر عام 2014، أصدر البنك المركزي اليمني التعميم رقم 11 لعام 2014 لتمكين إنشاء نموذج قائم على البنوك لتوفير خدمات النقود الإلكترونية، بدعم من الوكالة الأمريكية للتنمية الدولية، والبنك الدولي، والمجموعة الاستشارية لمساعدة الفقراء (سيجاب)، والوكالة الألمانية للتعاون الدولي." Also: "سمح التعميم للبنوك المرخصة بالتعاقد مع شركات الاتصالات والوكلاء أو الاستعانة بمصادر خارجية لتوفير خدمات النقود الإلكترونية عبر الهاتف المحمول، وفي الوقت ذاته حمل التعميم البنوك المسؤولية النهائية عن تصرفات هذه الكيانات."
- AR p.18 (= EN p.19): "جاء قرار البنك المركزي اليمني في صنعاء الصادر في مارس/آذار 2020 مناقضًا لتعميم البنك المركزي اليمني رقم 11 لسنة 2014 الذي منح البنوك العاملة في اليمن حصريًا دون غيرها حق تقديم خدمات الريال الإلكتروني. أوجد الإطار القانوني الجديد الذي فرضه الحوثيون فرصة للجهات الفاعلة الأقل تنظيمًا -مثل شركات الصرافة والتجار وغير ذلك من المؤسسات غير المصرفية- للحصول على تراخيص منه لإصدار النقود الإلكترونية وتقديم خدمات إدارة المدفوعات الإلكترونية."
- Naming in the Arabic edition: "البنك المركزي في صنعاء" / "البنك المركزي في عدن" and "البنك المركزي اليمني في صنعاء".
- Note that "increasingly taken steps" in the English edition is rendered "خطوات تصعيدية" (escalating steps) in the Arabic.
- The Arabic text layer has lam-alef and ligature errors. Other Arabic passages are **NOT VERIFIED** and need visual transcription before public use.

---

## 6. S1 internal consistency (reason for taking no numbers from S1)

| # | Conflict | Location A (verbatim) | Location B (verbatim) |
|---|---|---|---|
| 1 | Account holders, end-2019 | p.7: "By 2019, 3 million Yemenis (10 percent of the population) held at least one bank account, of which 27 percent were electronic money, or ‘e-money’, accounts." | p.25: "As stated above, almost 2.9 million Yemenis (approximately 10 percent of the population) owned at least one bank account by the end of 2019" |
| 2 | Number of e-money provider banks "as of this writing" | p.8: four banks licensed by "the CBY" and CAC Bank by "the CBY-Sana’a" (2015–2019), plus "In January 2021, the CBY-Sanaa gave licenses to two additional banks, Shamil Bank of Yemen and Bahrain (SBYB) and International Bank of Yemen (IBY)", making 7. p.19 adds that in Q1 2021 "More financial institutions were also permitted to provide customers with e-rials, such as IBY, SBYB, One and Tamkeen." | p.27: "The integration of the e-wallets held by these five banks is limited. As of this writing …"; p.32: "any of the five banks offering mobile banking and e-wallet services" |
| 3 | WeNet participant banks | p.27: "between the five participant banks that have been recently connected to the financial switch interbank network led by YFSC under the business identity and brand, WeNet" | p.30: "WeNet started to process instant money transfers among the six participant banks subscribing to its network: Yemen Bank for Reconstruction and Development, Yemen Kuwait Bank, Shamil Bank of Yemen and Bahrain, Saba Islamic Bank, Islamic Bank of Yemen for Finance and Investment, and CAC Bank." Only two of the six are among the five e-wallet banks. |
| 4 | ONE Cash licensing date | p.19: Q1 2021, institutions "permitted to provide customers with e-rials, such as … One and Tamkeen" | p.30: "initial e-money license to ONE Cash in July 2020 … final license in early 2022 … yet to launch operations" |
| 5 | Date of the March 2020 CBY-Sana’a instrument (same yemen-yba.com URL in both footnotes) | p.10 fn 7: "Central Bank of Yemen (Sana’a), March 11, 20202" [sic] | p.18 fn 34: "“Decision no. 1 of the Central Bank Governor”, … Central Bank of Yemen – Sana’a, March 8, 2020". The primary scan shows the decision dated 2020/03/08 and its cover letter 2020/03/11, so both dates exist in the source; the paper does not explain which is which. |
| 6 | Year of the "December 18" circular | p.17: "On December 18, 2019, CBY-Sana’a issued a circular expanding the ban on new rial banknotes" | p.17 fn 30: "Per a copy of the December 18, 2020 CBY-Sana’a circular shared with the Sana’a Center." |
| 7 | Year GAPPS launched its EFT/e-rial scheme | p.13, Figure 1 (image): "JAN 10, 2000 / Electronic Fund Transfer (EFT) / Government-owned Post Office launchs an electronic fund transfer (EFT) system e-rial project to settle limited utility bills." | p.13 text: "One of first electronic payment/e-money schemes was rolled out via the government-run GAPPS[16] in 2002, in the form of an EFT system to settle some utility bills." |
| 8 | Regime before 2014 (framing, not a number) | p.5: "a highly regulated market – which grants the right to provide e-money services only to banks – was the legal framework prior to 2014"; p.23 "… was the legal practice prior to 2014" | p.11: "Prior to 2014, there was no clear regulatory framework to govern the provision of electronic financial services in Yemen."; p.12: the bank-led model was established by the late-2014 circular |
| 9 | E-money issued against e-money payments | p.25: "The total amount of e-money issued from 2016 to 2019) amounted to YR115 billion, while in 2019 alone some YR75 billion was issued." | p.28 fn 57: "The total value of e-money payments each year from 2016 to 2019 was: In 2016 YR101,685,663; in 2017 YR11,393,123,266; in 2018, YR 31,243,779,947; in 2019, YR118,905,021,167." 2019 payments alone (YR118.9 bn) exceed the stated four-year issuance (YR115 bn); the four-year payments total is YR161.64 bn. These are different measures, so this is not strictly an arithmetic contradiction, but the paper does not reconcile them. |
| 10 | Composition of e-rial use | p.28: "In 2018, transfers among electronic money and banking accounts as well as cash-in and cash-out transactions represented 95 percent of the electronic money transactions (of which 9 percent was cash-out payments), while the value of financial transactions conducted to disburse electricity, cell phone, and internet bills, and carry out commodity purchases only represented 1 percent." | p.29, Figure 4 "Payments Using E-rials in Yemen, 2016 - 2019" (image): Cash Withdrawl 59%, Invoices Payment (cellphone and internet) 26%, Online Purchasing 13%, Invoices Payment for other utilities (unlabelled slice). The period and base differ, but cash-out at 9% against 59%, and bills plus purchases at 1% against about 39% or more, cannot be reconciled from the paper. |
| 11 | Law citation | p.11: "The first CBY framework to be issued post-unification, Law No. 14 of 2000, was designed to regulate the CBY’s functions" | p.24 fn 49: "Article (12): Law No. (38) of 1998, Central Bank of Yemen". The preamble of the CBY-Sana’a 2020 decision lists Law (38) of 1998 as "بشأن البنوك" (Banks Law). |
| 12 | YKB's platform name | p.18: Dec 2019 circular platforms include "Quality Connect, jointly owned by Yemen Kuwait Bank (YKB), Swaid & Sons for Exchange, and Al Akwaa Exchange" | p.27, Figure 3: "YKB (Floosak)"; p.29 describes Quality Connect as "a company created to perform similar roles" to the YFSC switch |

Attribution ambiguity (not a number conflict):
- p.8 and p.24 say "the CBY" licensed four banks in 2015–2019.
- Fn 46 dates those licences as Al-Kuraimi 2015, Tadhamon 2016, Al-Amal 2017, and "the Bank of Yemen and Kuwait" and CAC Bank 2018.
- The CBY headquarters moved in September 2016 (p.15), so the paper does not say which branch issued the 2017–2018 licences.

Checked and internally consistent:
- Figure 3 totals (p.27) sum correctly: agents 2626+26+391+238+90 = 3,371; points of sale 7,620+2,222+5,071+1,547+116 = 16,576; branches 132+50+17+15+28 = 242.
- Al-Kuraimi's 80% share appears on both p.26 text and Figure 2.
- 18 banks = 4+4+8+2 (p.11).
- The p.28 claim of "just 1 percent of the total YR4.35 trillion" matches fn 57 only if the 2016–2018 three-year total (YR42.74 bn) is read against one year's average. That reading is ambiguous and not counted as a conflict.

---

## 7. Primary source: CBY Circular No. 11 of 2014

**Result: no public copy of the circular text found (NOT VERIFIED).** The circular's existence, number, year and official Arabic title are confirmed by an official CBY-Sana’a instrument. Its content is described in secondary sources.

**Where I looked (2026-10-11):**
1. **cby-ye.com** (CBY Head Office, Aden):
   - home page;
   - `/publicationsandcirculars` pages 1–2, which list all 15 items (IDs 143–157: capital, liquidity, credit information, internal control, BCP and similar); none concerns mobile or e-money;
   - `/rulesandregulations` (7 laws: amended CBY law, Banks, Exchange, Public Debt, Islamic Banks, AML/CFT, Deposit Insurance); no circular;
   - all 74 Arabic news index pages (662 items, IDs 1–975), title-filtered for e-money, mobile, wallet, payment, circular and 2014: no 2014 circular;
   - `/files/6240256ea92fd.pdf`, a 2022 Payment Systems Department profile. It says the CBY "كلف … فريق من الخبراء بإعداد القواعد التنظيمية اللازمة لمزودي خدمات الدفع والمحافظ الإلكترونية" and does not cite Circular 11.
2. **english.cby-ye.com**: home, `/rulesandregulations`, `/publicationsandcirculars` (same 15 items), and all 20 news index pages (177 items). No 2014 circular.
3. **centralbank.gov.ye / www.centralbank.gov.ye** (CBY-Sana’a): unreachable. HTTPS gave connection reset, HTTP gave 503, and WebFetch gave 503. **NOT VERIFIED.** S1's fn 49 used http://centralbank.gov.ye/App_Upload/law38a.pdf, which suggests an older document store there.
4. **Wayback Machine** (web.archive.org CDX for centralbank.gov.ye/App_Upload/*): blocked from this environment (proxy tunnel closed; WebFetch refused). **NOT VERIFIED.**
5. **Web searches:**
   - "Central Bank of Yemen Circular No. 11 2014 mobile banking regulations";
   - "Central Bank of Yemen issues new mobile banking regulations" Owens;
   - "Circular No. 11" Yemen 2014 mobile money USAID Chemonics;
   - an extended search on Yemen 2014 mobile financial services regulations;
   - Arabic: "البنك المركزي اليمني منشور رقم 11 لسنة 2014 خدمات الدفع عبر الهاتف المحمول", "منشور رقم (11) لسنة 2014" البنك المركزي, "القواعد التنظيمية لتقديم خدمات النقود الإلكترونية عبر الهاتف المحمول بواسطة البنوك 2014", and site:cby-ye.com terms.
   None returned the circular text.
6. **pdf.usaid.gov/pdf_docs/PA00MT1H.pdf** (Chemonics for USAID, Dec 2016, cited by S1): download failed (proxy CONNECT 502). **NOT VERIFIED** whether it reproduces the circular.

**Best available evidence:**
- **Official mention (primary, CBY-Sana’a).** Governor's Decision No. (1) of 2020, scan hosted by the Yemen Banks Association (Sana'a):
  - URL: http://www.yemen-yba.com/wp-content/uploads/2020/03/قرار-محافظ-البنك-المركزي-لقواعد-التنظيمية-لتقديم-المؤسسات-المالية-خدمات-الدفع-الالكتروني-عبر-الهاتف-المحمول-1.pdf
  - 45 pages, 12,965,505 bytes, SHA-256 `977a56a2757741f73109607d4169adc67d06fdd8328d09286e8b8afb178e363c`.
  - Cover letter (Banking Supervision Sector, Sana'a) dated 2020/03/11; decision dated 2020/03/08.
  - Article 13 (p.45, read from the image): "مادة (13): لا يلغي هذا القرار أحكام المنشور رقم (11) لسنة 2014م بشأن القواعد التنظيمية لتقديم خدمات النقود الالكترونية عبر الهاتف المحمول بواسطة البنوك."
  - YBA news page https://yemen-yba.com/7623/ ("بتاريخ: 2020/03/19", SHA-256 `af1c8b1a…0188`) states the same.
  - So the circular's official designation is **"المنشور رقم (11) لسنة 2014م"**, on regulatory rules for providing e-money services via mobile phone **by banks**. The issuer is the Central Bank of Yemen (pre-split, unified), and the date is given by S1 as 11 December 2014 (Figure 1) and by AFI as "On 11 December 2014". The issue date is **NOT VERIFIED** from a primary source.
- **Key "who may provide" sentence (secondary).** Abdulghani Mohamed AlSamawi, Bilquis Ahmed Al-Fosail, Saleh Zaid Al-Hada and Amal Ahmed Al-Dubaili, "Electronic Payment Services in Yemen, Challenges and Opportunities", Institute of Banking Studies (Sana'a), English edition.
  - URL: https://findevgateway.org/sites/default/files/publications/submissions/78206/%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%20%D8%A8%D8%B9%D8%AF%20%D8%A7%D9%84%D8%AA%D8%B9%D8%AF%D9%8A%D9%842.pdf
  - 107 pages, SHA-256 `6136ca78aa130429404e9d3972f1c5cd714ccc17b4157bb70b6eb4e8f986ba8b`.
  - Printed p.25 (PDF p.33): "although the circular has limited the permission to provide electronic money services through licensed banks only, but the licensed bank is allowed to contract or outsource this service to telecommunications companies and agents without prejudice to the bank’s responsibility for all service provision responsibilities … 1. No one is allowed to provide electronic money service via mobile phone except through a licensed bank. 2. The licensed bank is permitted to contract with another party such as telecommunications companies and agents to provide electronic money service via mobile phone. 3. The licensed bank is not entitled to issue electronic money that exceeds 15% of the paid-up capital and the legal reserve without the prior approval of the Central Bank."
  - Printed p.6 (PDF p.14): "it issued at the end of 2014 Circular No. 11 of 2014 regarding the regulatory rules for electronic money services via mobile phone to regulate the issuance and management of electronic money, which was limited to banks, as five wallets were licensed through banks from the date of the publication. … the Central Bank recently issued Resolution No. 1 of 2020 … according to which non-bank financial institutions established for this purpose are allowed to provide electronic money services".
  - Note: IBS is a CBY-Sana’a-affiliated institute. Printed p.1 is a "Central Bank Governor's Speech".
- **AFI blog (secondary, cited by S1).** John Owens, "Central Bank of Yemen issues new mobile banking regulations", Alliance for Financial Inclusion, 7 March 2015.
  - URL: https://www.afi-global.org/opinion/central-bank-of-yemen-issues-new-mobile-banking-regulations/ (SHA-256 of the HTML `f218ca1f…4000`).
  - Verbatim: "On 11 December 2014, the Central Bank of Yemen (CBY) issued new mobile banking regulations following an almost two-year process of reviews and discussions with the private sector and support from USAID, the World Bank, the Consultative Group to Assist the Poor (CGAP) and Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ)."
  - Also: "By allowing and providing the enabling environment for banks and mobile network operators to work together, CBY sees their new regulation as a tremendous opportunity to safely and soundly expand true banking services and deeper financial inclusion access much more rapidly than either player could provide on their own."
  - The post gives no circular number and no link to the text.

---

## 8. Later CBY-Aden instruments found during the search (context; NOT in S1)

These matter only for bounding any statement. S1 (March 2022) says CBY-Aden held to the pre-war bank-led framework; later Aden instruments exist.

- **14/9/2022: payment service provider instructions.**
  - Title (p.1): "التعليمات المنظمة لأعمال مقدمي خدمات الدفع و/أو مشغلي /مديري أنظمة الدفع". Ref. 720/CBY/2022, dated 14/9/2022, Central Bank of Yemen, Head Office – Aden.
  - Announced in news item https://cby-ye.com/news/376 (2022-09-21, "اللائحة والتعليمات المنظمة لمقدمي أنظمة الدفع (وثيقة)"), which states the instructions were issued "بدعم فني مقدم من البنك الدولي والوكالة الأمريكية للتنمية (USAID)".
  - File: https://cby-ye.com/files/632b0c240dc11.pdf, 33-page scan, SHA-256 `8d15745560805a8d4764fe20ff0201812ec7e2b3e96c37780fbbcc113d59af71`.
  - Read pp.1–5 only, transcribed from the images:
    - p.2: "مقدمي خدمات الدفع: المؤسسات المالية غير البنكية المخول والمسموح لها من قبل البنك المركزي بتقديم خدمات الدفع لتمكين عمليات الإيداع والسحب من الحسابات كدفع المعاملات التي تنطوي على تحويل الأموال وإصدار أو إدارة أدوات الدفع."
    - p.4: "لا يجوز لأي شخص في الجمهورية العمل كمقدم لخدمات الدفع و/أو مشغل/مدير لنظام الدفع بدون الحصول على ترخيص بذلك ساري المفعول صادر من البنك المركزي بموجب هذه التعليمات."
    - p.5: money-exchange institutions may not apply unless they convert entirely. The minimum paid-up capital reads as 500 million YR for a payment service provider and 750 million YR for a payment system operator; read from the image, verify before use.
  - Whether these instructions authorise non-banks to issue e-money specifically, and whether they mention Circular 11/2014, is **NOT VERIFIED** (pp.6–33 unread).
- **18/12/2023: e-KYC instructions.** CBY-Aden news https://cby-ye.com/news/619, "البنك المركزي يصدر تعليمات تنظيم اجراءات اعرف عميلك الكترونياً (وثيقة)", file /files/65806fe2b3757.pdf. Not opened. **NOT VERIFIED** for content.
- **26/06/2024: circular on unlicensed wallets.** Circular No. CBY/L/282/2024, Banking Supervision Sector, Aden (https://cby-ye.com/files/667c32dabd223.pdf, SHA-256 `07f8edf8abf3cd81399387917c8bb3b18255a807adbf31772898fe3fa549c385`; news https://cby-ye.com/news/703 and https://english.cby-ye.com/news/181).
  - Subject: "حظر التعامل مع الكيانات والمحافظ وخدمات الدفع الالكتروني غير المرخصة". It lists 12 named wallets or entities.
  - Legal basis cited: Law (14) of 2000 on the CBY as amended, Law (40) of 2006 on payment systems and electronic financial and banking operations, AML/CFT Law (1) of 2010, and "تعليمات البنك المركزي التنظيمية ذات الصلة".
  - It does not name Circular 11/2014.

---

## 9. NOT VERIFIED (with reason)

- The text of CBY Circular No. (11) of 2014. No public copy was found; the CBY-Sana’a site and the Wayback Machine were unreachable; the USAID/Chemonics 2016 report failed to download.
- Its exact issue date of 11 December 2014. This comes only from S1 Figure 1 and AFI; there is no primary copy.
- Whether "No10" in the Sana'a file name is S1's official RYE series number. It is not printed in the PDF.
- Whether Wadhah Al-Awlaqi authored either paper. Only the Sana'a web pages say so; the PDFs say "Sana’a Center Economic Unit".
- The CBY-Sana’a Decision No. 1/2020 beyond pages 1–3 and 45 of 45.
- The CBY-Aden PSP instructions of 2022 beyond pages 1–5 of 33, and the e-KYC instructions of 2023 (not opened).
- Arabic S1 passages other than the three transcribed in §5. The text layer has ligature errors.
- The unlabelled slice in Figure 4 (p.29).
- Other mirrors not examined: devchampions.org and carpo-bonn.org pages for S1.

---

## 10. Draft bounded statement (suggestion only; for the steward to adapt)

> According to a March 2022 white paper by the Sana’a Center Economic Unit (Rethinking Yemen’s Economy; Sana’a Center for Strategic Studies with DeepRoot Consulting and CARPO), CBY Circular No. 11 of 2014 set up a bank-led model for mobile e-money. The paper reports that in March 2020 the Sana’a-based branch of the central bank opened e-money licensing to non-bank institutions, and that the Aden-based branch, as of the paper’s writing, held to the pre-war bank-led framework.

Sources: S1 pp.5, 12, 18–19, 35; Arabic edition pp.4, 11, 18. Take no numbers from S1 (§6). If the statement goes beyond March 2022, note that CBY-Aden issued instructions for non-bank payment service providers on 14 September 2022 (§8).
