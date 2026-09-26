# -*- coding: utf-8 -*-
"""P4-E label table — governed display labels for every category, series, lane, unit, event and state value that a
SIGNATURE or CORE_ANALYTICAL chart prints (independent verification V-D5).

Each entry: (namespace, raw value as it appears in the governed row, UI id, English label, Arabic label).
The labels become 04 'Governed interface copy' rows (Master-first, p4e_execute.py); the namespace -> raw -> UI id map
becomes the display_labels block of the visual design contract controlled input. English keeps the governed row's
meaning; where the raw value is a code or an enumeration, the English label states it in words. Arabic is authored by
the Lead in the product's register and has not been certified by an outside native editor.
"""

LABELS = [
    # Findex groups (25_FINDEX_BASELINE.group)
    ("findex_group", "total", "UI-VIS-CAT-FINDEX-TOTAL", "All adults (ages 15+)", "جميع البالغين (15 سنة فأكثر)"),
    ("findex_group", "female", "UI-VIS-CAT-FINDEX-FEMALE", "Women", "النساء"),
    ("findex_group", "male", "UI-VIS-CAT-FINDEX-MALE", "Men", "الرجال"),
    ("findex_group", "poorest 40%", "UI-VIS-CAT-FINDEX-POOREST40", "Adults in the poorest 40% of households", "البالغون في أفقر 40% من الأسر"),
    ("findex_group", "richest 60%", "UI-VIS-CAT-FINDEX-RICHEST60", "Adults in the richest 60% of households", "البالغون في أغنى 60% من الأسر"),
    ("findex_group", "primary education or less", "UI-VIS-CAT-FINDEX-PRIMARY-EDU", "Adults with primary education or less",
     "البالغون الحاصلون على تعليم ابتدائي أو أقل"),
    # publication vintages (23_REMITTANCES.series_vintage)
    ("series", "CBY_ANNUAL_REPORT_2024", "UI-VIS-CAT-SERIES-CBY-AR2024", "CBY Annual Report 2024", "التقرير السنوي للبنك المركزي 2024"),
    ("series", "CBY_ANNUAL_REPORT_2025", "UI-VIS-CAT-SERIES-CBY-AR2025", "CBY Annual Report 2025", "التقرير السنوي للبنك المركزي 2025"),
    ("series", "2025_ARTICLE_IV_STAFF_REPORT", "UI-VIS-CAT-SERIES-IMF-AIV2025", "IMF 2025 Article IV staff report",
     "تقرير خبراء صندوق النقد الدولي لمشاورات المادة الرابعة 2025"),
    ("series", "2025_ARTICLE_IV_SUPPLEMENTARY_REVISION", "UI-VIS-CAT-SERIES-IMF-AIV2025-SUPP", "IMF 2025 Article IV supplement (revised values)",
     "ملحق مشاورات المادة الرابعة 2025 لصندوق النقد الدولي (قيم معدّلة)"),
    # units
    ("unit", "USD million", "UI-VIS-UNIT-USD-MILLION", "USD million", "مليون دولار أمريكي"),
    ("unit", "count", "UI-VIS-UNIT-COUNT", "Number", "العدد"),
    ("unit", "percent of population ages 15+", "UI-VIS-UNIT-PCT-ADULTS", "% of adults (ages 15+)", "% من البالغين (15 سنة فأكثر)"),
    ("unit", "percent of send amount", "UI-VIS-UNIT-PCT-SEND", "% of the amount sent", "% من المبلغ المرسل"),
    ("unit", "percent", "UI-VIS-UNIT-PCT", "Percent", "نسبة مئوية"),
    ("unit", "percentage points", "UI-VIS-UNIT-PP", "Percentage points", "نقاط مئوية"),
    ("unit", "source-listed rows", "UI-VIS-UNIT-SOURCE-ROWS", "Rows listed in the source", "صفوف مدرجة في المصدر"),
    ("unit", "e-wallets", "UI-VIS-UNIT-EWALLETS", "E-wallets", "محافظ إلكترونية"),
    ("unit", "licensed e-wallets", "UI-VIS-UNIT-LICENSED-EWALLETS", "Licensed e-wallets", "محافظ إلكترونية مرخصة"),
    ("unit", "event participants", "UI-VIS-UNIT-EVENT-PARTICIPANTS", "Event participants", "مشاركون في الفعالية"),
    ("unit", "project-defined access points", "UI-VIS-UNIT-PROJECT-ACCESS-POINTS", "Access points as defined by the project",
     "نقاط وصول وفق تعريف المشروع"),
    ("unit", "borrowers", "UI-VIS-UNIT-BORROWERS", "Number of borrowers", "عدد المقترضين"),
    ("unit", "savers", "UI-VIS-UNIT-SAVERS", "Number of savers", "عدد المدخرين"),
    ("unit", "YER million", "UI-VIS-UNIT-YER-MILLION", "YER million (nominal)", "مليون ريال يمني (اسمية)"),
    # remittance corridors and send amounts (23_REMITTANCES)
    ("corridor", "Saudi Arabia", "UI-VIS-CAT-CORRIDOR-SA", "Saudi Arabia", "المملكة العربية السعودية"),
    ("corridor", "United Arab Emirates", "UI-VIS-CAT-CORRIDOR-AE", "United Arab Emirates", "الإمارات العربية المتحدة"),
    ("amount_sent", "200", "UI-VIS-CAT-AMOUNT-200", "USD 200 sent", "إرسال 200 دولار أمريكي"),
    ("amount_sent", "500", "UI-VIS-CAT-AMOUNT-500", "USD 500 sent", "إرسال 500 دولار أمريكي"),
    # payment objects (17_INDICATOR_LIBRARY names)
    ("payment_object", "IND-0001", "UI-VIS-CAT-PAY-CARDS", "Payment cards", "بطاقات الدفع"),
    ("payment_object", "IND-0002", "UI-VIS-CAT-PAY-POS-TERMINALS", "POS terminals", "أجهزة نقاط البيع"),
    ("payment_object", "IND-0003", "UI-VIS-CAT-PAY-POS-TRANSACTIONS", "POS transactions", "معاملات نقاط البيع"),
    ("payment_object", "IND-0006", "UI-VIS-CAT-PAY-ATMS", "ATMs", "أجهزة الصراف الآلي"),
    ("payment_object", "IND-0010", "UI-VIS-CAT-PAY-EWALLETS", "E-wallets", "المحافظ الإلكترونية"),
    ("payment_object", "IND-0011", "UI-VIS-CAT-PAY-EWALLET-SUBSCRIBERS", "E-wallet subscribers", "مشتركو المحافظ الإلكترونية"),
    ("payment_object", "IND-0017", "UI-VIS-CAT-PAY-ACCOUNTS", "Accounts", "الحسابات"),
    # firm finance (21_FIRM_FINANCE)
    ("firm_finance", "Formal establishments reporting a line of credit", "UI-VIS-CAT-FIRM-CREDIT-LINE",
     "Formal establishments reporting a line of credit", "المنشآت الرسمية التي أفادت بامتلاك خط ائتمان"),
    ("firm_finance", "Private commercial banks", "UI-VIS-CAT-FIRM-LOAN-PRIVATE-BANKS", "Private commercial banks", "البنوك التجارية الخاصة"),
    ("firm_finance", "State-owned bank/government agency", "UI-VIS-CAT-FIRM-LOAN-STATE", "State-owned bank or government agency",
     "بنك مملوك للدولة أو جهة حكومية"),
    ("firm_finance", "Non-bank financial institution / microfinance", "UI-VIS-CAT-FIRM-LOAN-NONBANK",
     "Non-bank financial institution or microfinance provider", "مؤسسة مالية غير مصرفية أو مقدم تمويل أصغر"),
    ("firm_finance", "Other non-financial institution", "UI-VIS-CAT-FIRM-LOAN-OTHER", "Other non-financial institution", "مؤسسة أخرى غير مالية"),
    ("firm_challenge", "Business challenge: Electricity", "UI-VIS-CAT-FIRM-CH-ELECTRICITY", "Electricity", "الكهرباء"),
    ("firm_challenge", "Business challenge: Fuel shortages", "UI-VIS-CAT-FIRM-CH-FUEL", "Fuel shortages", "نقص الوقود"),
    ("firm_challenge", "Business challenge: Transport/road blockade", "UI-VIS-CAT-FIRM-CH-TRANSPORT", "Transport or road blockades",
     "صعوبات النقل أو إغلاق الطرق"),
    ("firm_challenge", "Business challenge: Tax administration/rates", "UI-VIS-CAT-FIRM-CH-TAX", "Tax administration or tax rates",
     "الإدارة الضريبية أو معدلات الضرائب"),
    ("firm_challenge", "Business challenge: Political instability", "UI-VIS-CAT-FIRM-CH-POLITICAL", "Political instability", "عدم الاستقرار السياسي"),
    ("firm_challenge", "Business challenge: Access to finance", "UI-VIS-CAT-FIRM-CH-FINANCE", "Access to finance", "الوصول إلى التمويل"),
    ("firm_challenge", "Business challenge: Siege", "UI-VIS-CAT-FIRM-CH-SIEGE", "Siege", "الحصار"),
    ("firm_challenge", "Business challenge: Informal competitor practices", "UI-VIS-CAT-FIRM-CH-INFORMAL", "Practices of informal competitors",
     "ممارسات المنافسين غير الرسميين"),
    # microfinance lanes (24_MFI)
    ("mfi_lane", "borrowers", "UI-VIS-CAT-MFI-BORROWERS", "Borrowers", "المقترضون"),
    ("mfi_lane", "savers", "UI-VIS-CAT-MFI-SAVERS", "Savers", "المدخرون"),
    ("mfi_lane", "portfolio", "UI-VIS-CAT-MFI-PORTFOLIO", "Loan portfolio", "محفظة القروض"),
    # reform and payment-architecture events (22 reforms_regulation.event)
    ("event", "Unified domestic transfer network", "UI-VIS-CAT-EVT-UNIFIED-NETWORK", "Unified domestic transfer network",
     "الشبكة الموحدة للحوالات المحلية"),
    ("event", "FMIIP starts", "UI-VIS-CAT-EVT-FMIIP-START", "FMIIP starts", "بدء مشروع FMIIP"),
    ("event", "FMIIP approved", "UI-VIS-CAT-EVT-FMIIP-APPROVAL", "FMIIP approved", "الموافقة على مشروع FMIIP"),
    ("event", "Fast Payment System", "UI-VIS-CAT-EVT-FPS", "Fast Payment System", "نظام الدفع السريع"),
    ("event", "RTGS + CBY core banking", "UI-VIS-CAT-EVT-RTGS-CORE", "RTGS and CBY core banking",
     "نظام التسوية الإجمالية الفورية والنظام المصرفي الأساسي للبنك المركزي"),
    ("event", "Access-point database and usage support", "UI-VIS-CAT-EVT-ACCESS-DB", "Access-point database and usage support",
     "قاعدة بيانات نقاط الوصول ودعم الاستخدام"),
    ("event", "Unified network as main transfer channel", "UI-VIS-CAT-EVT-NETWORK-MAIN", "Unified network as the main transfer channel",
     "الشبكة الموحدة قناةً رئيسية للحوالات"),
    ("event", "National QR + e-wallet interconnection + FPS operator participation", "UI-VIS-CAT-EVT-QR-INTEROP",
     "National QR code, e-wallet interconnection and operator participation in the Fast Payment System",
     "رمز الاستجابة السريعة الوطني وربط المحافظ الإلكترونية ومشاركة المشغلين في نظام الدفع السريع"),
    ("event", "Digital-payment exhibition and unified-network activity signal", "UI-VIS-CAT-EVT-EXHIBITION",
     "Digital-payment exhibition and a signal of unified-network activity", "معرض المدفوعات الرقمية ومؤشر على نشاط الشبكة الموحدة"),
    ("event", "Restructuring, capital increase and broader bank shareholder base", "UI-VIS-CAT-EVT-NETWORK-COMPANY",
     "Restructuring, capital increase and a broader base of bank shareholders", "إعادة الهيكلة وزيادة رأس المال وتوسيع قاعدة البنوك المساهمة"),
    ("event", "Founding assembly of Yemen Payments and Clearing Company", "UI-VIS-CAT-EVT-YPCC-FOUNDING",
     "Founding assembly of the Yemen Payments and Clearing Company", "الجمعية التأسيسية لشركة اليمن للمدفوعات والمقاصة"),
    ("event", "First YPCC board meeting", "UI-VIS-CAT-EVT-YPCC-BOARD", "First board meeting of the Yemen Payments and Clearing Company",
     "أول اجتماع لمجلس إدارة شركة اليمن للمدفوعات والمقاصة"),
    # issuing authority
    ("authority", "Central Bank of Yemen — Aden", "UI-VIS-CAT-AUTH-CBY-ADEN", "Central Bank of Yemen — Aden", "البنك المركزي اليمني — عدن"),
    # provider observability (20 providers_data)
    ("provider_class", "BANKS_ALL_TYPES", "UI-VIS-CAT-PRV-CLASS-BANKS", "Banks (all types)", "البنوك بجميع أنواعها"),
    ("provider_class", "EXCHANGE_COMPANIES_ESTABLISHMENTS_AND_REMITTANCE_AGENTS", "UI-VIS-CAT-PRV-CLASS-EXCHANGE",
     "Exchange companies, exchange establishments and remittance agents", "شركات الصرافة ومنشآتها ووكلاء الحوالات"),
    ("provider_class", "E_WALLETS_OR_E_MONEY_SERVICES_AS_CBY_REPORTED", "UI-VIS-CAT-PRV-CLASS-EWALLETS",
     "E-wallets or e-money services, as reported by the CBY", "المحافظ الإلكترونية أو خدمات النقود الإلكترونية كما يوردها البنك المركزي"),
    ("provider_class", "NON_BANK_MICROFINANCE_INSTITUTIONS_AND_PROGRAMMES", "UI-VIS-CAT-PRV-CLASS-MFI",
     "Non-bank microfinance institutions and programmes", "مؤسسات وبرامج التمويل الأصغر غير المصرفية"),
    ("provider_count_state", "PRIMARY_CURRENT_LIST_VERIFIED", "UI-VIS-CAT-PRV-COUNT-CURRENT-LIST", "Count from the current official list",
     "عدد مأخوذ من القائمة الرسمية الحالية"),
    ("provider_count_state", "SOURCE_LISTED_ROWS__98_COMPANIES__225_ESTABLISHMENTS__106_REMITTANCE_AGENTS", "UI-VIS-CAT-PRV-COUNT-LISTED-ROWS",
     "Rows listed in the source, by category (companies, establishments, remittance agents)",
     "صفوف مدرجة في المصدر حسب الفئة (شركات ومنشآت ووكلاء حوالات)"),
    ("provider_count_state", "MULTIPLE_PRIMARY_DATED_COUNTS_WITH_DIFFERENT_WORDING", "UI-VIS-CAT-PRV-COUNT-SEVERAL",
     "Several dated official counts, worded differently", "عدة أعداد رسمية مؤرخة بصياغات مختلفة"),
    ("provider_count_state", "MEMBERSHIP_PAGES_ONLY", "UI-VIS-CAT-PRV-COUNT-MEMBERSHIP", "Network membership pages only", "صفحات عضوية الشبكة فقط"),
    ("provider_named_state", "COMPLETE_FOR_SOURCE_LIST", "UI-VIS-CAT-PRV-NAMED-COMPLETE", "Names complete for the source list",
     "الأسماء مكتملة لقائمة المصدر"),
    ("provider_named_state", "COMPLETE_CATEGORY_COUNTS__ROW_LEVEL_NAMES_NOT_YET_NORMALIZED_IN_PROVIDER_MASTER", "UI-VIS-CAT-PRV-NAMED-COUNTS-ONLY",
     "Category counts complete; names not yet normalised row by row", "أعداد الفئات مكتملة، ولم تُوحَّد الأسماء صفًا بصف بعد"),
    ("provider_named_state", "POSITIVE_NAMES_NOT_CONTROLLED", "UI-VIS-CAT-PRV-NAMED-NONE", "No controlled list of licensed names",
     "لا توجد قائمة مضبوطة بأسماء الجهات المرخصة"),
    ("provider_named_state", "PARTIAL_NETWORK_MEMBERSHIP_NOT_REGULATORY_UNIVERSE", "UI-VIS-CAT-PRV-NAMED-PARTIAL",
     "Partial network membership, not the regulated universe", "عضوية جزئية في الشبكة، وليست المجموعة الخاضعة للتنظيم"),
    ("provider_event_overlay", "NO_BANK_STATUS_EVENT_OVERLAY_APPLIED_IN_THIS_UNIT", "UI-VIS-CAT-PRV-EVENTS-NONE-APPLIED",
     "No bank status events applied", "لم تُطبَّق أحداث تتعلق بوضع البنوك"),
    ("provider_event_overlay", "SELECTED_2026_STATUS_OVERLAY__LATER_SUSPENSION_CLOSURE_EVENTS_MUST_NOT_BE_SUBTRACTED_MECHANICALLY",
     "UI-VIS-CAT-PRV-EVENTS-SELECTED-2026", "Selected 2026 status events shown; they are not subtracted from the list",
     "تُعرض أحداث وضع مختارة لعام 2026، ولا تُطرح من القائمة"),
    ("provider_event_overlay", "2024_NEGATIVE_AUTHORITY + 72_WALLET_COUNT_RECON__NO_POSITIVE_CURRENT_STATUS_LEDGER",
     "UI-VIS-CAT-PRV-EVENTS-WALLETS", "2024 list of unlicensed names and dated wallet counts; no current register of licensed status",
     "قائمة 2024 بالأسماء غير المرخصة وأعداد مؤرخة للمحافظ، ولا يوجد سجل حالي للوضع الترخيصي"),
    ("provider_event_overlay", "NONE", "UI-VIS-CAT-PRV-EVENTS-NONE", "None", "لا يوجد"),
    ("provider_limit", "List presence proves licensing/listing only; operation is not inferred.", "UI-VIS-CAT-PRV-LIMIT-BANKS",
     "List presence establishes licensing or listing only; operation is not inferred.",
     "الظهور في القائمة يثبت الترخيص أو الإدراج فقط، ولا يُستنتج منه التشغيل."),
    ("provider_limit", "429 is the arithmetic sum of source-listed rows across three classes, not a deduplicated unique-provider or "
     "currently operating-provider count.", "UI-VIS-CAT-PRV-LIMIT-EXCHANGE",
     "429 is the arithmetic sum of rows listed in the source across three classes, not a count of unique providers or of providers "
     "operating now.",
     "الرقم 429 مجموع حسابي لصفوف مدرجة في المصدر عبر ثلاث فئات، وليس عددًا لمقدمي خدمات فريدين ولا لمقدمي خدمات عاملين حاليًا."),
    ("provider_limit", "Official objects report 7 e-wallets (2024 Q3), 9 e-wallets (2025 H1), 8 licensed e-wallets (2025-09-10), and >9 "
     "event participants (2026-01-22). Preserve separately; named positive current wallet/PSP universe remains open.",
     "UI-VIS-CAT-PRV-LIMIT-EWALLETS",
     "Official sources report 7 e-wallets (2024 Q3), 9 e-wallets (2025 H1), 8 licensed e-wallets (2025-09-10) and more than 9 event "
     "participants (2026-01-22). The counts stay separate; a named current list of licensed wallets and payment service providers "
     "remains open.",
     "تورد المصادر الرسمية 7 محافظ إلكترونية (الربع الثالث 2024)، و9 محافظ (النصف الأول 2025)، و8 محافظ مرخصة (2025-09-10)، "
     "وأكثر من 9 مشاركين في فعالية (2026-01-22). وتبقى هذه الأعداد منفصلة، ولا تزال القائمة الحالية المسماة للمحافظ ومقدمي خدمات "
     "الدفع المرخصين مفتوحة."),
    ("provider_limit", "YMN membership presence is not licence or operation verification and is not a complete national universe.",
     "UI-VIS-CAT-PRV-LIMIT-MFI", "Membership of the YMN network does not verify a licence or operation and is not a complete national universe.",
     "العضوية في شبكة YMN لا تثبت الترخيص أو التشغيل، وليست مجموعة وطنية مكتملة."),
    ("provider_event_class", "E_WALLET_OR_ELECTRONIC_PAYMENT_SERVICE", "UI-VIS-CAT-PRV-EVCLASS-EWALLET", "E-wallet or electronic payment service",
     "محفظة إلكترونية أو خدمة دفع إلكتروني"),
    ("provider_event_class", "EXCHANGE_COMPANY_OR_ESTABLISHMENT", "UI-VIS-CAT-PRV-EVCLASS-COMPANY-OR-EST", "Exchange company or establishment",
     "شركة أو منشأة صرافة"),
    ("provider_event_class", "EXCHANGE_ESTABLISHMENT_AND_REMITTANCE_AGENT", "UI-VIS-CAT-PRV-EVCLASS-EST-AGENT",
     "Exchange establishment and remittance agent", "منشأة صرافة ووكيل حوالات"),
    ("provider_event_class", "EXCHANGE_COMPANY_ESTABLISHMENT_AND_REMITTANCE_AGENTS", "UI-VIS-CAT-PRV-EVCLASS-COMPANY-EST-AGENTS",
     "Exchange company, establishment and remittance agents", "شركة صرافة ومنشأة صرافة ووكلاء حوالات"),
    ("provider_event_class", "EXCHANGE_BRANCH", "UI-VIS-CAT-PRV-EVCLASS-BRANCH", "Exchange branch", "فرع صرافة"),
    ("provider_event_class", "EXCHANGE_ESTABLISHMENT", "UI-VIS-CAT-PRV-EVCLASS-ESTABLISHMENT", "Exchange establishment", "منشأة صرافة"),
    ("provider_event_class", "REMITTANCE_AGENT", "UI-VIS-CAT-PRV-EVCLASS-AGENT", "Remittance agent", "وكيل حوالات"),
    ("provider_event_class", "EXCHANGE_COMPANY", "UI-VIS-CAT-PRV-EVCLASS-COMPANY", "Exchange company", "شركة صرافة"),
    ("provider_event_class", "EXCHANGE_COMPANY_ESTABLISHMENTS_AND_REMITTANCE_AGENT", "UI-VIS-CAT-PRV-EVCLASS-COMPANY-ESTS-AGENT",
     "Exchange company establishments and remittance agent", "منشآت شركة صرافة ووكيل حوالات"),
    ("provider_status", "PROHIBITED_DEALING__UNLICENSED_AS_SOURCE_DATED", "UI-VIS-CAT-PRV-STATUS-PROHIBITED",
     "Dealing prohibited — unlicensed on the source date", "يُحظر التعامل — غير مرخص في تاريخ المصدر"),
    ("provider_status", "LICENCE_SUSPENSION_AND_CLOSURE_EVENT", "UI-VIS-CAT-PRV-STATUS-SUSPENDED", "Licence suspended and closure ordered",
     "إيقاف الترخيص والأمر بالإغلاق"),
    ("provider_status", "LICENCE_WITHDRAWAL_EVENT", "UI-VIS-CAT-PRV-STATUS-WITHDRAWN", "Licence withdrawn", "سحب الترخيص"),
    ("provider_status", "UNLICENSED_AS_NAMED_IN_SOURCE_ON_SOURCE_DATE", "UI-VIS-CAT-PRV-STATUS-NAMED-UNLICENSED",
     "Named as unlicensed on the source date", "مسمّى غير مرخص في تاريخ المصدر"),
    ("provider_status", "PRIMARY_ADMINISTRATIVE_COUNT", "UI-VIS-CAT-PRV-STATUS-ADMIN-COUNT", "Official administrative count", "عدد إداري رسمي"),
    ("provider_status", "PRIMARY_OFFICIAL_DATED_LICENSING_STATEMENT", "UI-VIS-CAT-PRV-STATUS-LICENSING-STATEMENT",
     "Official dated statement on licensing", "بيان رسمي مؤرخ بشأن الترخيص"),
    ("provider_status", "PRIMARY_OFFICIAL_EVENT_PARTICIPATION", "UI-VIS-CAT-PRV-STATUS-EVENT-PARTICIPATION",
     "Official record of participation in an event", "سجل رسمي للمشاركة في فعالية"),
]

# further raw spellings of an already governed label (no new interface copy)
ALIASES = [
    ("unit", "YER_million", "UI-VIS-UNIT-YER-MILLION"),     # 19_PAYMENTS_DATA POS value unit (nominal)
]

# grammar addition used by the target/result contract
BASELINE = ("UI-VIS-BASELINE", "Baseline — the starting value the project reports", "خط الأساس — القيمة الابتدائية التي يوردها المشروع")


def namespaces():
    out = {}
    for ns, raw, uid, _en, _ar in LABELS:
        out.setdefault(ns, {})
        if raw in out[ns]:
            raise ValueError(f"duplicate label for {ns}={raw!r}")
        out[ns][raw] = uid
    known = {x[2] for x in LABELS}
    for ns, raw, uid in ALIASES:
        if uid not in known or raw in out.setdefault(ns, {}):
            raise ValueError(f"alias {ns}={raw!r} -> {uid} is not valid")
        out[ns][raw] = uid
    ids = [x[2] for x in LABELS] + [BASELINE[0]]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate UI id in the label table")
    return out
