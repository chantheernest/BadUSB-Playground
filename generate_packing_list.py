from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
ws.title = "1-Week Packing List"

# ── Colour palette ──────────────────────────────────────────────────────────
HEADER_BG   = "1F3864"   # deep navy
HEADER_FG   = "FFFFFF"
CAT_COLORS  = [
    "2E75B6", "C55A11", "375623", "7030A0",
    "843C0C", "1F497D", "833C00", "4F6228",
    "17375E", "953735",
]
ROW_EVEN    = "DEEAF1"
ROW_ODD     = "FFFFFF"
DONE_FILL   = "E2EFDA"   # light green when ticked (visual guide only)

thin = Side(style="thin", color="BFBFBF")
med  = Side(style="medium", color="808080")
thin_border = Border(left=thin, right=thin, top=thin, bottom=thin)
cat_border  = Border(left=med,  right=med,  top=med,  bottom=med)

# ── Column widths ────────────────────────────────────────────────────────────
ws.column_dimensions["A"].width = 4    # checkbox tick col
ws.column_dimensions["B"].width = 32   # item name
ws.column_dimensions["C"].width = 12   # qty
ws.column_dimensions["D"].width = 36   # notes / tips

# ── Title row ────────────────────────────────────────────────────────────────
ws.merge_cells("A1:D1")
title_cell = ws["A1"]
title_cell.value = "✈  1-WEEK TRIP PACKING CHECKLIST"
title_cell.font      = Font(name="Calibri", bold=True, size=18, color=HEADER_FG)
title_cell.fill      = PatternFill("solid", fgColor=HEADER_BG)
title_cell.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 36

# Sub-title
ws.merge_cells("A2:D2")
sub = ws["A2"]
sub.value     = "Tick the □ column as you pack each item"
sub.font      = Font(name="Calibri", italic=True, size=11, color="595959")
sub.alignment = Alignment(horizontal="center", vertical="center")
sub.fill      = PatternFill("solid", fgColor="D9E2F3")
ws.row_dimensions[2].height = 20

# Column headers
ws.row_dimensions[3].height = 22
headers = ["✔", "Item", "Qty", "Notes / Tips"]
for col, h in enumerate(headers, 1):
    c = ws.cell(row=3, column=col, value=h)
    c.font      = Font(name="Calibri", bold=True, size=11, color=HEADER_FG)
    c.fill      = PatternFill("solid", fgColor="2F5496")
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border    = cat_border

# ── Packing data ─────────────────────────────────────────────────────────────
# Format: (category_name, [(item, qty, notes), ...])
sections = [
    ("👗  CLOTHING", [
        ("T-Shirts (casual)",                 "5",  "Pack a mix of colours"),
        ("Jeans",                             "2",  "1 dark, 1 light/neutral"),
        ("Going-out dress",                   "1",  "With matching accessories"),
        ("Smart/casual trousers or skirt",    "1",  "Versatile for dinners"),
        ("Shorts or lightweight pants",       "1",  "For warm-weather days"),
        ("Cardigan / light jacket",           "1",  "Planes & AC restaurants are cold"),
        ("Swimwear / bikini",                 "1",  "Even if no beach – hotel pool"),
        ("Activewear / gym outfit",           "1",  "If you plan any workouts"),
        ("Underwear",                         "7",  "1 per day + 1 spare"),
        ("Bras (regular)",                    "3",  "Include 1 strapless for dress"),
        ("Sports bra",                        "1",  "For gym or active days"),
        ("Socks",                             "7",  "1 per day; pack ankle & regular"),
        ("Sleeping clothes / pyjamas",        "2",  "Top + bottoms or 2 sets"),
        ("Slippers / flip-flops (indoor)",    "1",  "Essential for hotel floors"),
    ]),
    ("👠  FOOTWEAR", [
        ("Everyday walking shoes / trainers", "1",  "Broken in – NO new shoes"),
        ("Dress shoes / heels / smart flats", "1",  "For going-out dress"),
        ("Sandals / thongs",                  "1",  "Lightweight summer option"),
        ("Slippers (indoor / hotel)",         "1",  "Already listed above – verify"),
    ]),
    ("💄  MAKEUP & BEAUTY", [
        ("Foundation or BB/CC cream",         "1",  "Travel-size if possible"),
        ("Concealer",                         "1",  ""),
        ("Setting powder",                    "1",  ""),
        ("Setting spray",                     "1",  "Keeps makeup in heat"),
        ("Blush / bronzer / highlighter",     "1",  "Palette saves space"),
        ("Eyeshadow palette",                 "1",  "Neutral + bold shades"),
        ("Eyeliner (pencil or liquid)",       "1",  ""),
        ("Mascara",                           "1",  "Waterproof recommended"),
        ("Eyebrow pencil / gel",              "1",  ""),
        ("Lipstick / lip gloss",              "2",  "Day shade + evening shade"),
        ("Makeup brushes & sponge",           "1 set", "Travel roll-up case"),
        ("Makeup remover wipes",              "1 pk","Double as quick face refresh"),
        ("Makeup remover / micellar water",   "1",  "100 ml travel size"),
        ("False lashes + glue",               "1",  "Optional – for going-out nights"),
        ("Makeup bag / organiser",            "1",  "Waterproof inner lining ideal"),
    ]),
    ("🧴  TOILETRIES & SKINCARE", [
        ("Toothbrush",                        "1",  "Pack travel case to protect"),
        ("Toothpaste",                        "1",  "100 ml travel size"),
        ("Dental floss",                      "1",  ""),
        ("Mouthwash",                         "1",  "Travel-size bottle"),
        ("Shampoo",                           "1",  "100 ml or solid bar"),
        ("Conditioner",                       "1",  "100 ml or conditioner bar"),
        ("Body wash / soap",                  "1",  "Solid bar is TSA-friendly"),
        ("Face wash / cleanser",              "1",  ""),
        ("Moisturiser / face cream",          "1",  "Day + night if different"),
        ("Sunscreen SPF 50+",                 "1",  "Face & body; top up daily"),
        ("Eye cream",                         "1",  "Optional"),
        ("Toner / face mist",                 "1",  "Hydration on flights"),
        ("Serum / treatment",                 "1",  "Your regular routine"),
        ("Lip balm",                          "1",  "SPF version is a bonus"),
        ("Deodorant / antiperspirant",        "1",  "Roll-on or stick"),
        ("Perfume / body spray",              "1",  "Decant into travel atomiser"),
        ("Razor & extra blades",              "1",  "Or epilator"),
        ("Shaving cream / gel",               "1",  ""),
        ("Hair brush / comb",                 "1",  ""),
        ("Hair ties & bobby pins",            "1 pk",""),
        ("Dry shampoo",                       "1",  "Game-changer for busy days"),
        ("Hair styling product",              "1",  "Your usual: oil, serum, etc."),
        ("Travel hair dryer / diffuser",      "1",  "Check voltage if abroad"),
        ("Hair straightener / curler",        "1",  "Dual-voltage preferred"),
        ("Cotton pads & cotton buds",         "1 pk",""),
        ("Nail file & nail clippers",         "1",  ""),
        ("Nail polish (base + colour)",       "1",  "Optional"),
        ("Feminine hygiene products",         "7+", "Always bring more than needed"),
        ("Toilet paper / travel tissue",      "1 pk","Essential for unknown venues"),
        ("Hand sanitiser",                    "1",  "60%+ alcohol"),
        ("Travel towel (microfibre)",         "1",  "Some hotels charge for extras"),
        ("Shower cap",                        "1",  ""),
    ]),
    ("💊  MEDICATION & HEALTH", [
        ("Prescription medication",           "8+ days' supply", "Carry in original packaging"),
        ("Pain reliever (paracetamol/ibu)",   "1 pack",  "Headaches, fever"),
        ("Antihistamines",                    "1 pack",  "Allergies or insect reactions"),
        ("Anti-diarrhoeal (Imodium etc.)",    "1 pack",  "New food = upset stomach"),
        ("Antacid / indigestion relief",      "1 pack",  "Unfamiliar cuisine"),
        ("Nausea / motion-sickness tablets",  "1 pack",  "Flights, buses, boats"),
        ("Cold & flu tablets",                "1 pack",  "Just-in-case"),
        ("Throat lozenges",                   "1 pack",  "Dry AC air on flights"),
        ("Eye drops (lubricating)",           "1",       "Dry eyes on long flights"),
        ("Insect repellent",                  "1",       "DEET or picaridin"),
        ("Hydrocortisone cream",              "1",       "Bites, rashes, itching"),
        ("Antiseptic cream / spray",          "1",       "Small cuts & scrapes"),
        ("Plasters / band-aids (assorted)",   "1 pk",    ""),
        ("Rehydration sachets (ORS)",         "3",       "Heat, diarrhoea, hangover"),
        ("Vitamins / supplements",            "7 days",  "Your usual routine"),
        ("Face masks (disposable)",           "5",       "Crowded transport"),
        ("Small first-aid kit",               "1",       "Tweezers, scissors, gauze"),
        ("Doctor's letter for medication",    "1 copy",  "For customs if needed"),
    ]),
    ("📱  ELECTRONICS", [
        ("iPhone / Android Phone #1",         "1",  "Your primary device"),
        ("Phone #2",                          "1",  "Secondary / work phone"),
        ("Phone #3",                          "1",  "3rd device / backup"),
        ("iPad",                              "1",  "Entertainment + productivity"),
        ("Android Tablet",                    "1",  ""),
        ("Phone chargers (matching cables)",  "3",  "One per phone; label them"),
        ("iPad charger + USB-C cable",        "1",  ""),
        ("Tablet charger + cable",            "1",  ""),
        ("Portable power bank (20 000 mAh)",  "1",  "Check airline mAh limits"),
        ("Power bank charging cable",         "1",  ""),
        ("Multi-port USB charging hub",       "1",  "Charge everything from 1 outlet"),
        ("Universal travel adapter",          "1",  "Multi-region plug essential"),
        ("Surge protector (portable)",        "1",  "Protect devices from voltage spikes"),
        ("Wireless earbuds / AirPods",        "1",  "With charging case"),
        ("Over-ear headphones",               "1",  "Noise-cancelling for flights"),
        ("Laptop / MacBook",                  "1",  "If needed for work"),
        ("Laptop charger",                    "1",  ""),
        ("Camera + memory cards",             "1",  "If not using phone camera"),
        ("Camera charger / batteries",        "1",  ""),
        ("USB-C hub / dongle",                "1",  "Extra ports for laptop"),
        ("Cable organiser / pouch",           "1",  "Keep cables tangle-free"),
        ("Screen cleaner cloth",              "1",  "For all screens"),
        ("Phone mount / ring holder",         "1",  ""),
        ("Waterproof phone pouch",            "1",  "Beach, pool, rain"),
    ]),
    ("🎒  BAGS & LUGGAGE", [
        ("Main suitcase / rolling luggage",   "1",  "Check airline size/weight limits"),
        ("Day backpack",                      "1",  "For day trips & carry-on"),
        ("Handbag / clutch",                  "1",  "For going-out evenings"),
        ("Packing cubes (set)",               "1 set","Organise by category"),
        ("Laundry bag / mesh zip bag",        "1",  "Separate dirty from clean"),
        ("Reusable shopping bag (foldable)",  "1",  "Beach, market, groceries"),
        ("Toiletry/clear liquid bag (1 L)",   "1",  "TSA airport security"),
        ("Luggage lock",                      "2",  "TSA-approved"),
        ("Luggage tag with contact info",     "1",  ""),
        ("Luggage scale (handheld)",          "1",  "Avoid overweight fees"),
    ]),
    ("📄  TRAVEL DOCUMENTS & MONEY", [
        ("Passport (valid 6+ months)",        "1",  "Check expiry NOW"),
        ("National ID / driver's licence",    "1",  ""),
        ("Visa / e-visa printout",            "1",  "If required"),
        ("Flight tickets / boarding passes",  "1",  "Printed + on phone"),
        ("Hotel / accommodation booking",     "1",  "Confirmation printed"),
        ("Travel insurance documents",        "1",  "Policy number accessible"),
        ("Emergency contact list",            "1",  "Separate from phone"),
        ("Credit card (notify bank)",         "1",  "Primary travel card"),
        ("Debit card",                        "1",  "Backup card"),
        ("Cash (local currency)",             "–",  "Small denominations handy"),
        ("USD / EUR as backup currency",      "–",  "Widely accepted globally"),
        ("Photocopies of all documents",      "1 set","Store separately from originals"),
        ("Digital copies (cloud / email)",    "1",  "Google Drive or email to self"),
    ]),
    ("😴  COMFORT & SLEEP", [
        ("Travel pillow (neck)",              "1",  "Inflatable saves space"),
        ("Eye mask",                          "1",  "For flights & bright hotel rooms"),
        ("Ear plugs",                         "1 pk",""),
        ("Noise-cancelling earplugs",         "1",  "Or use headphones"),
        ("Lightweight blanket / travel wrap", "1",  "Cold flights & AC rooms"),
        ("Melatonin / sleep aid",             "1",  "Jet-lag support"),
        ("White-noise app (phone)",           "–",  "Download before travelling"),
    ]),
    ("🍎  SNACKS & MISC", [
        ("Reusable water bottle",             "1",  "Empty through security, refill after"),
        ("Travel snacks (nuts, bars, etc.)",  "1 bag","For flights & long journeys"),
        ("Chewing gum / mints",               "1 pk","Ear pressure during flights"),
        ("Collapsible umbrella",              "1",  "Even if sunny season – be prepared"),
        ("Sunglasses",                        "1",  "UV400 or polarised"),
        ("Hat / cap",                         "1",  "Sun protection"),
        ("Belt",                              "1",  "For jeans"),
        ("Jewellery / accessories",           "–",  "Earrings, necklace, bracelets"),
        ("Watch",                             "1",  "Or use phone"),
        ("Book / e-reader / Kindle",          "1",  "Flights & lazy mornings"),
        ("Notepad & pen",                     "1",  "Customs forms, random notes"),
        ("Ziplock bags (assorted sizes)",     "1 pk","Leakproof, snacks, wet items"),
        ("Travel laundry detergent sachets",  "3",  "Hand-wash essentials mid-trip"),
        ("Stain remover pen",                 "1",  "Spills happen"),
        ("Sewing kit (mini)",                 "1",  "Button, quick hem fix"),
        ("Safety pins",                       "5",  "Wardrobe emergencies"),
        ("Superglue (tiny)",                  "1",  "Shoe sole, broken strap"),
        ("Mini torch / flashlight",           "1",  "Power outages, night walks"),
        ("Reusable straw",                    "1",  "Optional – eco-friendly"),
        ("Portable door lock / alarm",        "1",  "Solo travel safety"),
        ("Pepper spray / personal alarm",     "1",  "Check destination legality"),
    ]),
]

# ── Write rows ────────────────────────────────────────────────────────────────
current_row = 4
color_idx   = 0

for cat_name, items in sections:
    # Category header
    cat_color = CAT_COLORS[color_idx % len(CAT_COLORS)]
    color_idx += 1

    ws.merge_cells(f"A{current_row}:D{current_row}")
    cat_cell = ws[f"A{current_row}"]
    cat_cell.value     = cat_name
    cat_cell.font      = Font(name="Calibri", bold=True, size=12, color="FFFFFF")
    cat_cell.fill      = PatternFill("solid", fgColor=cat_color)
    cat_cell.alignment = Alignment(horizontal="left", vertical="center",
                                   indent=1)
    cat_cell.border    = cat_border
    ws.row_dimensions[current_row].height = 22
    current_row += 1

    for idx, (item, qty, notes) in enumerate(items):
        fill_color = ROW_EVEN if idx % 2 == 0 else ROW_ODD
        row_fill   = PatternFill("solid", fgColor=fill_color)

        # Checkbox column (□)
        cb = ws.cell(row=current_row, column=1, value="□")
        cb.font      = Font(name="Calibri", size=14, color="595959")
        cb.alignment = Alignment(horizontal="center", vertical="center")
        cb.fill      = row_fill
        cb.border    = thin_border

        # Item name
        it = ws.cell(row=current_row, column=2, value=item)
        it.font      = Font(name="Calibri", size=11)
        it.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        it.fill      = row_fill
        it.border    = thin_border

        # Quantity
        qt = ws.cell(row=current_row, column=3, value=qty)
        qt.font      = Font(name="Calibri", size=11)
        qt.alignment = Alignment(horizontal="center", vertical="center")
        qt.fill      = row_fill
        qt.border    = thin_border

        # Notes
        nt = ws.cell(row=current_row, column=4, value=notes)
        nt.font      = Font(name="Calibri", size=10, color="404040", italic=bool(notes))
        nt.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        nt.fill      = row_fill
        nt.border    = thin_border

        ws.row_dimensions[current_row].height = 18
        current_row += 1

    # Spacer row
    ws.row_dimensions[current_row].height = 6
    current_row += 1

# ── Footer ────────────────────────────────────────────────────────────────────
ws.merge_cells(f"A{current_row}:D{current_row}")
footer = ws[f"A{current_row}"]
footer.value     = "✈  Safe travels! Tick □ → ✔ as you pack each item."
footer.font      = Font(name="Calibri", bold=True, size=11, color=HEADER_FG)
footer.fill      = PatternFill("solid", fgColor=HEADER_BG)
footer.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[current_row].height = 24

# ── Freeze top rows ───────────────────────────────────────────────────────────
ws.freeze_panes = "A4"

# ── Save ──────────────────────────────────────────────────────────────────────
out = "/home/user/BadUSB-Playground/1_Week_Packing_Checklist.xlsx"
wb.save(out)
print(f"Saved → {out}")
