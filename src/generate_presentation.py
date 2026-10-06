"""
Script to generate a professional, publication-grade 12-slide PowerPoint presentation
for the India Tourism Analytics & Econometric Pipeline (2022-2026).
"""
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank layout

    # Color Palette definitions
    C_NAVY_DARK = RGBColor(11, 19, 43)      # #0B132B
    C_NAVY_CARD = RGBColor(28, 37, 65)      # #1C2541
    C_BG_LIGHT  = RGBColor(248, 250, 252)   # #F8FAFC
    C_CARD_BG   = RGBColor(255, 255, 255)   # #FFFFFF
    C_BORDER    = RGBColor(203, 213, 225)   # #CBD5E1
    C_TEXT_MAIN = RGBColor(15, 23, 42)      # #0F172A
    C_TEXT_MUTED= RGBColor(71, 85, 105)     # #475569
    C_TEAL      = RGBColor(13, 148, 136)    # #0D9488
    C_BLUE      = RGBColor(37, 99, 235)     # #2563EB
    C_AMBER     = RGBColor(217, 119, 6)     # #D97706
    C_WHITE     = RGBColor(255, 255, 255)

    def set_slide_background(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, category_tag, slide_title, slide_number):
        # Category Tag Pill
        tag_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(3.2), Inches(0.32))
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = C_TEAL
        tag_box.line.color.rgb = C_TEAL
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_tag = tf_tag.paragraphs[0]
        p_tag.alignment = PP_ALIGN.CENTER
        p_tag.text = category_tag.upper()
        p_tag.font.name = "Calibri"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_WHITE

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(10.5), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = slide_title
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT_MAIN

        # Slide Number Tracker
        num_box = slide.shapes.add_textbox(Inches(11.3), Inches(0.4), Inches(1.3), Inches(0.4))
        tf_num = num_box.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.text = f"{slide_number:02d} / 12"
        p_num.font.name = "Calibri"
        p_num.font.size = Pt(13)
        p_num.font.bold = True
        p_num.font.color.rgb = C_TEAL

        # Separator line
        sep = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.02))
        sep.fill.solid()
        sep.fill.fore_color.rgb = C_BORDER
        sep.line.fill.background()

    def add_card(slide, left, top, width, height, title="", title_color=C_TEXT_MAIN, bg_color=C_CARD_BG, border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.45))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = "Calibri"
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = title_color
        return card

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1, C_NAVY_DARK)

    # Decorative header banner
    accent_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(2.8), Inches(0.35))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = C_AMBER
    accent_bar.line.fill.background()
    p_bar = accent_bar.text_frame.paragraphs[0]
    p_bar.text = "ACADEMIC CAPSTONE PROJECT"
    p_bar.alignment = PP_ALIGN.CENTER
    p_bar.font.name = "Calibri"
    p_bar.font.size = Pt(11)
    p_bar.font.bold = True
    p_bar.font.color.rgb = C_WHITE

    # Title & Subtitle text
    t_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(1.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "India Tourism Analytics & Econometric Pipeline"
    p1.font.name = "Calibri"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "End-to-End Data Engineering, Exploratory Profiling & Econometric Modeling (2022–2026)"
    p2.font.name = "Calibri"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_before = Pt(8)

    # Card 1: Project Metadata
    meta_card = add_card(slide1, Inches(0.8), Inches(3.4), Inches(5.6), Inches(3.3), 
                         title="PROJECT INFORMATION", title_color=C_AMBER, bg_color=C_NAVY_CARD, border_color=RGBColor(51, 65, 85))
    tb_meta = slide1.shapes.add_textbox(Inches(1.0), Inches(4.0), Inches(5.2), Inches(2.5))
    tf_meta = tb_meta.text_frame
    tf_meta.word_wrap = True
    
    meta_items = [
        ("Industry Domain:", "Tourism & Hospitality / Civil Aviation"),
        ("Focus Areas:", "District Footfall, Hospitality Infrastructure, Gateways"),
        ("Data Pipeline:", "Multi-Departmental Integration (MoT, NIDHI, ASI, AAI)"),
        ("Tools:", "Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy"),
        ("Deliverables:", "Jupyter Pipeline, Visual Dashboards, Executive PDF")
    ]
    for i, (label, val) in enumerate(meta_items):
        p = tf_meta.paragraphs[0] if i == 0 else tf_meta.add_paragraph()
        r1 = p.add_run()
        r1.text = f"{label} "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = RGBColor(226, 232, 240)
        r2 = p.add_run()
        r2.text = val
        r2.font.size = Pt(12)
        r2.font.color.rgb = RGBColor(148, 163, 184)
        p.space_after = Pt(6)

    # Card 2: Student & Academic Profile
    auth_card = add_card(slide1, Inches(6.8), Inches(3.4), Inches(5.7), Inches(3.3), 
                         title="CANDIDATE INFORMATION", title_color=C_TEAL, bg_color=C_NAVY_CARD, border_color=RGBColor(51, 65, 85))
    tb_auth = slide1.shapes.add_textbox(Inches(7.0), Inches(4.0), Inches(5.3), Inches(2.5))
    tf_auth = tb_auth.text_frame
    tf_auth.word_wrap = True
    
    auth_items = [
        ("Student Name:", "Thillai valavan A S"),
        ("Student ID:", "AF05309210"),
        ("Organization:", "Anudip Foundation"),
        ("Program / Course:", "Artificial Intelligence & Machine Learning (AIML)"),
        ("Batch Code:", "ANP-D7444")
    ]
    for i, (label, val) in enumerate(auth_items):
        p = tf_auth.paragraphs[0] if i == 0 else tf_auth.add_paragraph()
        r1 = p.add_run()
        r1.text = f"{label} "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = RGBColor(226, 232, 240)
        r2 = p.add_run()
        r2.text = val
        r2.font.size = Pt(12)
        r2.font.color.rgb = RGBColor(52, 211, 153) if "Thillai" in val else RGBColor(148, 163, 184)
        p.space_after = Pt(6)

    # =========================================================================
    # SLIDE 2: Industry Overview
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2, C_BG_LIGHT)
    add_header(slide2, "Industry Landscape", "Industry Overview: Indian Tourism, Hospitality & Civil Aviation", 2)

    col_w = Inches(3.64)
    h_cards = Inches(5.3)

    # Card 1: Selected Industry & Macro Scale
    add_card(slide2, Inches(0.8), Inches(1.6), col_w, h_cards, "1. Industry Scale & Ecosystem", C_BLUE)
    tb2_1 = slide2.shapes.add_textbox(Inches(1.0), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf2_1 = tb2_1.text_frame
    tf2_1.word_wrap = True
    bullets2_1 = [
        ("National Economic Pillar: ", "Contributes ~6.8% to India's GDP and supports over 40 million direct and indirect livelihoods across diverse supply chains."),
        ("Multi-Tier Ecosystem: ", "Encompasses domestic pilgrimage circuits, heritage monuments, eco-reserves, classified hotels, and civil aviation corridors."),
        ("Post-Pandemic Rebound: ", "Exhibits strong double-digit recovery in foreign tourist arrivals (FTAs) and domestic tourist visits (DTVs) through 2026.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets2_1):
        p = tf2_1.paragraphs[0] if i == 0 else tf2_1.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(12)

    # Card 2: Importance of Data Analysis
    add_card(slide2, Inches(4.84), Inches(1.6), col_w, h_cards, "2. Role of Data Analytics", C_TEAL)
    tb2_2 = slide2.shapes.add_textbox(Inches(5.04), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf2_2 = tb2_2.text_frame
    tf2_2.word_wrap = True
    bullets2_2 = [
        ("Evidence-Based Planning: ", "Shifts tourism administration from historical intuition to real-time, empirical demand forecasting and resource allocation."),
        ("Capacity Smoothing: ", "Enables hoteliers and civil aviation operators to mitigate extreme seasonal fluctuations and airport congestion."),
        ("Foreign Exchange Maximization: ", "Identifies high-velocity source geographies to optimize international marketing spend and visa facilitation policies.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets2_2):
        p = tf2_2.paragraphs[0] if i == 0 else tf2_2.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(12)

    # Card 3: Strategic Opportunities (2022-2026)
    add_card(slide2, Inches(8.88), Inches(1.6), col_w, h_cards, "3. Emerging Dynamics (2022–2026)", C_AMBER)
    tb2_3 = slide2.shapes.add_textbox(Inches(9.08), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf2_3 = tb2_3.text_frame
    tf2_3.word_wrap = True
    bullets2_3 = [
        ("Niche Circuit Expansion: ", "Rapid surge in Nature/Eco-tourism, wellness travel, and heritage trails surpassing classical golden triangle routes."),
        ("Aviation Gateway Transformation: ", "Secondary gateways (Cochin, Trivandrum, Ahmedabad) emerging as vital international diaspora and leisure conduits."),
        ("Hospitality Diversification: ", "Rise of classified homestays and boutique eco-lodges alongside classical star hotels, reshaping regional tariff spreads.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets2_3):
        p = tf2_3.paragraphs[0] if i == 0 else tf2_3.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(12)

    # =========================================================================
    # SLIDE 3: Problem Statement
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3, C_BG_LIGHT)
    add_header(slide3, "Problem Diagnostic", "Problem Statement: Infrastructure & Geographical Asymmetries", 3)

    add_card(slide3, Inches(0.8), Inches(1.6), col_w, h_cards, "1. Real-World Industry Problem", RGBColor(220, 38, 38))
    tb3_1 = slide3.shapes.add_textbox(Inches(1.0), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf3_1 = tb3_1.text_frame
    tf3_1.word_wrap = True
    bullets3_1 = [
        ("Severe Geographical Concentration: ", "Over 55% of inbound foreign tourist footfall is concentrated into a small handful of metropolitan gateways, leaving emerging high-potential districts under-monetized."),
        ("Infrastructure Mismatch: ", "Severe disconnect between rapid footfall spikes and certified hotel room capacities (NIDHI), leading to severe lodging deficits during peak festival seasons."),
        ("Departmental Data Fragmentation: ", "Visitor data (MoT), hotel units (NIDHI), monuments (ASI), and airport movements (AAI) reside in isolated silos with zero relational linkage.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets3_1):
        p = tf3_1.paragraphs[0] if i == 0 else tf3_1.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(10)

    add_card(slide3, Inches(4.84), Inches(1.6), col_w, h_cards, "2. Why the Problem is Critical", C_AMBER)
    tb3_2 = slide3.shapes.add_textbox(Inches(5.04), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf3_2 = tb3_2.text_frame
    tf3_2.word_wrap = True
    bullets3_2 = [
        ("Capital Misallocation: ", "State and central tourism budgets are frequently committed to saturated hubs rather than high-return emerging eco-circuits."),
        ("Forex Revenue Leakage: ", "Inability to retain high-spending international travelers results in truncated lengths of stay and lost revenue."),
        ("Tourist Dissatisfaction: ", "Infrastructure bottlenecks lead to elevated tourist complaints, degraded satisfaction scores, and weakened revisit intent (low NPS).")
    ]
    for i, (b_title, b_desc) in enumerate(bullets3_2):
        p = tf3_2.paragraphs[0] if i == 0 else tf3_2.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(12)

    add_card(slide3, Inches(8.88), Inches(1.6), col_w, h_cards, "3. Who is Affected?", C_BLUE)
    tb3_3 = slide3.shapes.add_textbox(Inches(9.08), Inches(2.2), col_w - Inches(0.4), h_cards - Inches(0.8))
    tf3_3 = tb3_3.text_frame
    tf3_3.word_wrap = True
    bullets3_3 = [
        ("Ministry of Tourism & State Boards: ", "Lack cross-domain analytical intelligence to design targeted regional incentive packages and marketing drives."),
        ("Hoteliers & Hospitality Investors: ", "Risk under-building or over-building room inventory without data on seasonal demand and localized tariff spreads."),
        ("Aviation & Transit Operators: ", "Face uneven passenger load distributions and bottlenecked international transit corridors."),
        ("Domestic & International Tourists: ", "Suffer from price gouging, lack of standardized lodging, and inadequate destination services.")
    ]
    for i, (b_title, b_desc) in enumerate(bullets3_3):
        p = tf3_3.paragraphs[0] if i == 0 else tf3_3.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + b_title; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_desc; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(8)

    # =========================================================================
    # SLIDE 4: Project Objectives
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4, C_BG_LIGHT)
    add_header(slide4, "Project Goals", "Project Objectives: Core Scientific & Analytical Aims", 4)

    obj_w = Inches(5.66)
    obj_h = Inches(2.45)
    
    # 4 distinct objective cards
    objs = [
        ("1. Multi-Departmental Data Harmonization", 
         "Ingest, audit, clean, and relationally merge heterogeneous datasets spanning 474 districts, 1,650 hotels, 1,200 monuments, 2,500 exit surveys, and 40 airport gateways into a single unified analytical data model.",
         C_BLUE, Inches(0.8), Inches(1.6)),
        ("2. Inbound Footfall & Destination Density Profiling", 
         "Isolate high-density foreign visitor districts versus aggregate domestic tourist engines to establish targeted destination prioritization for state infrastructure grants.",
         C_TEAL, Inches(6.86), Inches(1.6)),
        ("3. Econometric Spending Velocity & NPS Modeling", 
         "Evaluate foreign tourist daily expenditure across global source continents, assessing its correlation with visitor experience ratings, dwell times, and Net Promoter Sentiment.",
         C_AMBER, Inches(0.8), Inches(4.35)),
        ("4. Aviation Gateway & Hospitality Infrastructure Audit", 
         "Quantify post-COVID civil aviation traffic recovery trajectories and profile room tariff dispersions across 7 lodging formats to benchmark private-sector capacity alignment.",
         RGBColor(147, 51, 234), Inches(6.86), Inches(4.35))
    ]
    for title, desc, color, left, top in objs:
        add_card(slide4, left, top, obj_w, obj_h, title, color)
        tb = slide4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.65), obj_w - Inches(0.4), obj_h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_MUTED
        p.line_spacing = 1.25

    # =========================================================================
    # SLIDE 5: Proposed Solution & Analysis Questions
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5, C_BG_LIGHT)
    add_header(slide5, "Technical Blueprint", "Proposed Solution & Key Data Analysis Questions", 5)

    # Left Column: Proposed Solution (w: 5.2)
    add_card(slide5, Inches(0.8), Inches(1.6), Inches(5.2), Inches(5.3), "Proposed Solution: Python Data Pipeline", C_BLUE)
    tb5_sol = slide5.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(4.8), Inches(4.5))
    tf5_sol = tb5_sol.text_frame
    tf5_sol.word_wrap = True
    sol_bullets = [
        ("Automated Python Architecture: ", "Build an end-to-end reproducible pipeline combining modular Jupyter notebooks and automated CLI data processing modules."),
        ("Domain-Aware Engineering: ", "Implement statistically sound imputation (modal pincodes, bounded medians) and structural zero logic without synthetic distortions."),
        ("Relational Harmonization: ", "Produce a unified cross-domain district master profile linking demand metrics (footfall) directly to supply metrics (rooms, monuments, flights)."),
        ("Econometric Dashboarding: ", "Generate publication-grade 300 DPI visualizations and tabular executive summaries for senior policymakers.")
    ]
    for i, (b_t, b_d) in enumerate(sol_bullets):
        p = tf5_sol.paragraphs[0] if i == 0 else tf5_sol.add_paragraph()
        r1 = p.add_run(); r1.text = "✓ " + b_t; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = b_d; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(10)

    # Right Column: Analysis Questions (w: 6.2)
    add_card(slide5, Inches(6.3), Inches(1.6), Inches(6.233), Inches(5.3), "5 Core Analysis Questions Addressed", C_TEAL)
    tb5_q = slide5.shapes.add_textbox(Inches(6.5), Inches(2.2), Inches(5.8), Inches(4.5))
    tf5_q = tb5_q.text_frame
    tf5_q.word_wrap = True
    questions = [
        ("Q1: Destination Density", "Which specific districts exhibit the highest foreign visitor density relative to domestic volume, requiring internationalization amenities?"),
        ("Q2: Category Performance", "How do distinct tourism segments (Nature/Eco, Beach, Heritage, Religious) compare in visitor volumes and tourist dwell times?"),
        ("Q3: Spend vs Satisfaction", "How do tourist spending velocity and satisfaction (NPS) correlate across source continents?"),
        ("Q4: Gateway Exposure", "Which civil aviation gateways handle primary domestic loads, and which carry the highest international exposure ratios?"),
        ("Q5: Tariff Spreads", "What are the entry and peak room tariff spreads across different accommodation categories (Heritage, Star, Resorts, Homestays)?")
    ]
    for i, (q_t, q_d) in enumerate(questions):
        p = tf5_q.paragraphs[0] if i == 0 else tf5_q.add_paragraph()
        r1 = p.add_run(); r1.text = f"{q_t}: "; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEAL
        r2 = p.add_run(); r2.text = q_d; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(8)

    # =========================================================================
    # SLIDE 6: Dataset Information
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6, C_BG_LIGHT)
    add_header(slide6, "Data Catalog", "Dataset Information: Multi-Domain Data Architecture", 6)

    # Left: Dataset Overview Card
    add_card(slide6, Inches(0.8), Inches(1.6), Inches(4.8), Inches(5.3), "Master Architecture Specifications", C_BLUE)
    tb6_info = slide6.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(4.4), Inches(4.5))
    tf6_info = tb6_info.text_frame
    tf6_info.word_wrap = True
    ds_specs = [
        ("Dataset Collection:", "India Tourism Multi-Domain Master Dataset (2022–2026)"),
        ("Primary Sources:", "Ministry of Tourism (MoT), NIDHI, ASI, BOI, DGCA/AAI"),
        ("Format & Layout:", "Structured CSV files (Raw & Cleaned architectures)"),
        ("Coverage Scope:", "474 Districts, 1,650 Hospitality Units, 1,200 Monuments, 2,500 Survey Respondents, 40 Airports"),
        ("Key Dimension Features:", "District_City, State_UT, Year, Category, Star_Classification, Airport_Code, Origin_Country"),
        ("Key Metric Features:", "Domestic_Visitors, Foreign_Visitors, Total_Rooms, Min_Tariff_INR, Total_Spend_USD, NPS")
    ]
    for i, (label, val) in enumerate(ds_specs):
        p = tf6_info.paragraphs[0] if i == 0 else tf6_info.add_paragraph()
        r1 = p.add_run(); r1.text = f"• {label}\n  "; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = val; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(6)

    # Right: Sub-dataset Inventory Cards
    add_card(slide6, Inches(5.8), Inches(1.6), Inches(6.733), Inches(5.3), "Integrated Sub-Datasets & Scale", C_TEAL)
    tb6_grid = slide6.shapes.add_textbox(Inches(6.0), Inches(2.2), Inches(6.3), Inches(4.5))
    tf6_grid = tb6_grid.text_frame
    tf6_grid.word_wrap = True
    datasets = [
        ("1. District Footfall Dataset", "2,380 Rows × 8 Columns", "474 Districts across 5 years (2022–2026) capturing domestic & foreign footfalls."),
        ("2. NIDHI Hospitality Registry", "1,650 Rows × 14 Columns", "Classified hotel units, star ratings, room capacities, audit scores, and room tariffs."),
        ("3. ASI Protected Monuments", "1,200 Rows × 10 Columns", "Centrally protected national monuments, UNESCO status, and ticketed visitor tallies."),
        ("4. Inbound Exit Survey Microdata", "2,500 Rows × 12 Columns", "International airport exit surveys: dwell nights, spending USD, satisfaction ratings."),
        ("5. Civil Aviation Monthly Traffic", "2,400 Rows × 9 Columns", "40 domestic & international gateways across 60 monthly periods (AAI/DGCA)."),
        ("6. Unified Master Profile (2026)", "474 Rows × 18 Columns", "Cross-domain merged profile uniting footfall, hotel supply, and heritage sites.")
    ]
    for i, (d_name, d_dim, d_desc) in enumerate(datasets):
        p = tf6_grid.paragraphs[0] if i == 0 else tf6_grid.add_paragraph()
        r1 = p.add_run(); r1.text = f"[{d_dim}] "; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_TEAL
        r2 = p.add_run(); r2.text = f"{d_name}: "; r2.font.bold = True; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MAIN
        r3 = p.add_run(); r3.text = d_desc; r3.font.size = Pt(10); r3.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(5)

    # =========================================================================
    # SLIDE 7: Data Collection & Understanding
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7, C_BG_LIGHT)
    add_header(slide7, "Stage 1: Exploration", "Data Collection & Understanding: Schema & Integrity Audit", 7)

    # Left: Explanation (w: 5.4)
    add_card(slide7, Inches(0.8), Inches(1.6), Inches(5.4), Inches(5.3), "Collection & Structural Audit", C_BLUE)
    tb7 = slide7.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.0), Inches(4.5))
    tf7 = tb7.text_frame
    tf7.word_wrap = True
    audits = [
        ("Automated Collection: ", "Ingested tabular bulletins from the Ministry of Tourism, NIDHI hotel databases, and civil aviation reports."),
        ("Data Type Heterogeneity: ", "Identified mixed schemas: integer visitor counts, floating-point tariff currencies, multi-level categorical labels, and temporal month-year dates."),
        ("Missing Value Diagnosis: ", "Discovered 12.4% missing foreign visitors in remote non-border districts and unrecorded pincodes in regional hotel listings."),
        ("Zero Duplicate Verification: ", "Executed duplicate audit across composite primary keys [District_City, Year] and [Airport_Code, Date]; confirmed 0 duplicate records (100% unique keys).")
    ]
    for i, (a_t, a_d) in enumerate(audits):
        p = tf7.paragraphs[0] if i == 0 else tf7.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + a_t; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = a_d; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(10)

    # Right: Screenshot card
    add_card(slide7, Inches(6.5), Inches(1.6), Inches(6.033), Inches(5.3), "Jupyter Notebook Inspection Console", C_TEAL)
    img7_path = "results/cards/01_data_understanding.png"
    if os.path.exists(img7_path):
        slide7.shapes.add_picture(img7_path, Inches(6.65), Inches(2.2), Inches(5.733), Inches(4.5))

    # =========================================================================
    # SLIDE 8: Data Cleaning & Transformation
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8, C_BG_LIGHT)
    add_header(slide8, "Stage 2: Preparation", "Data Cleaning & Transformation: Imputation & Feature Engineering", 8)

    # Left: Explanation (w: 5.4)
    add_card(slide8, Inches(0.8), Inches(1.6), Inches(5.4), Inches(5.3), "Cleaning & Transformation Pipeline", C_TEAL)
    tb8 = slide8.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.0), Inches(4.5))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    cleanings = [
        ("Nullable Int64 Casting: ", "Cast numeric count columns with missing values to Pandas nullable Int64 (Foreign_Visitors, Complaints), preventing float truncation."),
        ("Hierarchical Mode Imputation: ", "Imputed missing hotel pincodes using group-level modal pincode of the corresponding District_City; unresolved assigned 'Unknown'."),
        ("Domain Categorical Handling: ", "Assigned 'Unclassified' to 342 non-graded lodging units; imputed Audit_Quality_Score via category median with a boolean missing indicator flag."),
        ("Structural Zero Fallbacks: ", "Assigned ₹0 to non-ticketed ASI monuments; imputed 0 international movements for domestic regional airfields."),
        ("Engineered Features: ", "Derived Spend_Velocity_USD (Spend/Nights), Foreign_Visitor_Ratio, Hotel_Density_Per_100k, and Tariff_Spread_INR.")
    ]
    for i, (c_t, c_d) in enumerate(cleanings):
        p = tf8.paragraphs[0] if i == 0 else tf8.add_paragraph()
        r1 = p.add_run(); r1.text = "✓ " + c_t; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = c_d; r2.font.size = Pt(10); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(7)

    # Right: Screenshot card
    add_card(slide8, Inches(6.5), Inches(1.6), Inches(6.033), Inches(5.3), "Jupyter Notebook Transformation Code", C_BLUE)
    img8_path = "results/cards/02_data_cleaning.png"
    if os.path.exists(img8_path):
        slide8.shapes.add_picture(img8_path, Inches(6.65), Inches(2.2), Inches(5.733), Inches(4.5))

    # =========================================================================
    # SLIDE 9: Exploratory Data Analysis (EDA)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9, C_BG_LIGHT)
    add_header(slide9, "Stage 3: Discovery", "Exploratory Data Analysis (EDA): Statistical Findings & Groupings", 9)

    # Left: Explanation (w: 5.4)
    add_card(slide9, Inches(0.8), Inches(1.6), Inches(5.4), Inches(5.3), "Core EDA Statistical Discoveries", C_AMBER)
    tb9 = slide9.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.0), Inches(4.5))
    tf9 = tb9.text_frame
    tf9.word_wrap = True
    eda_findings = [
        ("Extreme Skewness in Foreign Inflow: ", "Top 10 districts capture >55% of total foreign footfall. Metropolitan hubs (Chennai, Jaipur) lead absolute volume, but coastal/heritage nodes (Ernakulam 20.08%, Puri 14.99%) lead in foreign density."),
        ("Eco & Nature Tourism Superiority: ", "Nature / Eco-tourism achieves the highest average foreign arrivals (42,150/district) and longest dwell time (3.0 days), outperforming classical heritage circuits."),
        ("High-Yield Regional Source Markets: ", "Travelers from Oceania ($257.7/day) and the Americas ($224.5/day) produce the highest foreign exchange velocity."),
        ("Aviation Gateway Polarization: ", "Delhi (DEL) and Mumbai (BOM) drive passenger throughput, but Cochin (48.4%) and Trivandrum (46.0%) exhibit highest international exposure ratios.")
    ]
    for i, (e_t, e_d) in enumerate(eda_findings):
        p = tf9.paragraphs[0] if i == 0 else tf9.add_paragraph()
        r1 = p.add_run(); r1.text = "• " + e_t; r1.font.bold = True; r1.font.size = Pt(11); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = e_d; r2.font.size = Pt(11); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(10)

    # Right: Screenshot card
    add_card(slide9, Inches(6.5), Inches(1.6), Inches(6.033), Inches(5.3), "Jupyter Notebook Econometric Aggregations", C_TEAL)
    img9_path = "results/cards/03_eda_summary.png"
    if os.path.exists(img9_path):
        slide9.shapes.add_picture(img9_path, Inches(6.65), Inches(2.2), Inches(5.733), Inches(4.5))

    # =========================================================================
    # SLIDE 10: Data Visualization
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10, C_BG_LIGHT)
    add_header(slide10, "Stage 4: Dashboards", "Data Visualization: Key Analytical Dashboards & Insights", 10)

    # 2 prominent side-by-side visualization cards with full breakdown:
    # Chart Name -> Purpose -> What the chart shows -> Key Insight
    card_w10 = Inches(5.766)
    
    # Left: Inbound Spend vs Experience
    add_card(slide10, Inches(0.8), Inches(1.6), card_w10, Inches(5.3), "Inbound Spend vs Experience & Satisfaction", C_BLUE)
    img10_left = "results/plots/02_inbound_spend_vs_experience.png"
    if os.path.exists(img10_left):
        slide10.shapes.add_picture(img10_left, Inches(1.0), Inches(2.15), card_w10 - Inches(0.4), Inches(2.45))
    
    tb10_l = slide10.shapes.add_textbox(Inches(1.0), Inches(4.65), card_w10 - Inches(0.4), Inches(2.1))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True
    v_left = [
        ("Chart Name: ", "Inbound Spend vs. Experience Rating & Net Promoter Sentiment"),
        ("Purpose: ", "Evaluate foreign exchange velocity and visitor satisfaction across world regions."),
        ("What it shows: ", "Scatter plot of trip expenditure (USD) vs satisfaction (1–10) grouped by source continent."),
        ("Key Insight: ", "Oceania ($257.7/day) and Americas ($224.5/day) lead in yield; South Asian (31.9%) and US visitors record highest NPS.")
    ]
    for i, (lbl, val) in enumerate(v_left):
        p = tf10_l.paragraphs[0] if i == 0 else tf10_l.add_paragraph()
        r1 = p.add_run(); r1.text = lbl; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_BLUE
        r2 = p.add_run(); r2.text = val; r2.font.size = Pt(10); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(2)

    # Right: Monthly Airport Passenger Movements
    add_card(slide10, Inches(6.766), Inches(1.6), card_w10, Inches(5.3), "Monthly Airport Passenger Traffic Evolution", C_TEAL)
    img10_right = "results/plots/01_monthly_airport_passenger_movements.png"
    if os.path.exists(img10_right):
        slide10.shapes.add_picture(img10_right, Inches(6.966), Inches(2.15), card_w10 - Inches(0.4), Inches(2.45))
        
    tb10_r = slide10.shapes.add_textbox(Inches(6.966), Inches(4.65), card_w10 - Inches(0.4), Inches(2.1))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True
    v_right = [
        ("Chart Name: ", "Monthly Airport Passenger Movements Trajectory (2022–2026)"),
        ("Purpose: ", "Track civil aviation recovery curves and domestic vs international traffic volumes."),
        ("What it shows: ", "Multi-year monthly passenger curves across 40 primary aviation hubs."),
        ("Key Insight: ", "Delhi (DEL) & Mumbai (BOM) absorb total volume; Cochin (48.4%) & Trivandrum (46.0%) lead international exposure.")
    ]
    for i, (lbl, val) in enumerate(v_right):
        p = tf10_r.paragraphs[0] if i == 0 else tf10_r.add_paragraph()
        r1 = p.add_run(); r1.text = lbl; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_TEAL
        r2 = p.add_run(); r2.text = val; r2.font.size = Pt(10); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(2)

    # =========================================================================
    # SLIDE 11: Key Insights & Recommendations
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11, C_BG_LIGHT)
    add_header(slide11, "Strategic Roadmap", "Key Insights & Practical Policy Recommendations", 11)

    half_w = Inches(5.766)

    # Left: Key Insights
    add_card(slide11, Inches(0.8), Inches(1.6), half_w, Inches(5.3), "Empirical Insights from Analysis", C_BLUE)
    tb11_ins = slide11.shapes.add_textbox(Inches(1.0), Inches(2.2), half_w - Inches(0.4), Inches(4.5))
    tf11_ins = tb11_ins.text_frame
    tf11_ins.word_wrap = True
    insights = [
        ("1. Foreign Density Asymmetry: ", "Ernakulam (20.08%) and Puri (14.99%) lead in foreign tourist density despite lower overall volume than metros like Delhi."),
        ("2. Nature/Eco Outperformance: ", "Eco-tourism achieves 42,150 foreign visitors/district and longest dwell time (3.0 days), generating superior local value."),
        ("3. High-Yield Source Markets: ", "Oceania ($257.7/day) and North America ($224.5/day) produce the highest spending velocity; South Asian tourists record highest NPS (31.9%)."),
        ("4. Southern Gateway Exposure: ", "Cochin (48.4%) and Trivandrum (46.0%) serve as critical international diaspora and leisure conduits."),
        ("5. Alternative Lodging Value: ", "Homestays (₹1,500–₹3,000) sustain high audit scores (75.7/100), providing accessible regional capacity without luxury overheads.")
    ]
    for i, (t, d) in enumerate(insights):
        p = tf11_ins.paragraphs[0] if i == 0 else tf11_ins.add_paragraph()
        r1 = p.add_run(); r1.text = t; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = d; r2.font.size = Pt(10); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(6)

    # Right: Recommendations
    add_card(slide11, Inches(6.766), Inches(1.6), half_w, Inches(5.3), "Actionable Industry Recommendations", C_TEAL)
    tb11_rec = slide11.shapes.add_textbox(Inches(6.966), Inches(2.2), half_w - Inches(0.4), Inches(4.5))
    tf11_rec = tb11_rec.text_frame
    tf11_rec.word_wrap = True
    recommendations = [
        ("1. Targeted Inbound Amenities: ", "Deploy dedicated multi-lingual tourist assistance desks, foreign exchange kiosks, and digital payments in high-density nodes (Ernakulam, Puri)."),
        ("2. Expand Eco & Nature Circuits: ", "Incentivize certified eco-resorts and guided nature trails along eco-corridors to capture long dwell times and high spending."),
        ("3. Prioritize High-Velocity Source Markets: ", "Focus Ministry of Tourism marketing and fast-track electronic visa processing on Oceania and North America."),
        ("4. Upgrade Southern Aviation Gateways: ", "Expand customs clearance lanes and international transfer lounges at Cochin (COK) and Thiruvananthapuram (TRV)."),
        ("5. Standardize Alternative Lodging: ", "Broaden NIDHI accreditation, hygiene certification, and hospitality skill training for homestays and eco-lodges.")
    ]
    for i, (t, d) in enumerate(recommendations):
        p = tf11_rec.paragraphs[0] if i == 0 else tf11_rec.add_paragraph()
        r1 = p.add_run(); r1.text = t; r1.font.bold = True; r1.font.size = Pt(10); r1.font.color.rgb = C_TEXT_MAIN
        r2 = p.add_run(); r2.text = d; r2.font.size = Pt(10); r2.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(6)

    # =========================================================================
    # SLIDE 12: Conclusion & Future Scope
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12, C_BG_LIGHT)
    add_header(slide12, "Executive Wrap-Up", "Project Conclusion & Future Horizons", 12)

    c_box_w = Inches(5.66)
    c_box_h = Inches(2.45)
    
    conclusions = [
        ("1. What Was Achieved",
         "Successfully designed and executed an end-to-end Python data pipeline harmonizing 5 departmental datasets across 474 districts, generating 100% clean data models and 5 publication-ready visual dashboards.",
         C_BLUE, Inches(0.8), Inches(1.6)),
        ("2. Addressing the Industry Problem",
         "Replaced fragmented intuition with empirical cross-domain intelligence, pinpointing foreign visitor concentration nodes, accommodation bottlenecks, and aviation load dynamics.",
         C_TEAL, Inches(6.86), Inches(1.6)),
        ("3. Practical Stakeholder Value",
         "Delivers concrete roadmap for state tourism boards to optimize budget allocation, hoteliers to calibrate room inventory, and airport authorities to expand transit capacity.",
         C_AMBER, Inches(0.8), Inches(4.35)),
        ("4. Future Scope & Improvements",
         "Implement predictive machine learning models (ARIMA / Prophet / XGBoost) for seasonal footfall forecasting; incorporate natural language sentiment analysis on tourist reviews; deploy interactive web GIS dashboards.",
         RGBColor(147, 51, 234), Inches(6.86), Inches(4.35))
    ]
    for title, desc, color, left, top in conclusions:
        add_card(slide12, left, top, c_box_w, c_box_h, title, color)
        tb = slide12.shapes.add_textbox(left + Inches(0.2), top + Inches(0.65), c_box_w - Inches(0.4), c_box_h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.name = "Calibri"
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_MUTED
        p.line_spacing = 1.25

    # Save presentations
    output_path = "results/India_Tourism_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to {output_path}")

    # Also save as India_Tourism_Project_Report.pptx for consistency
    alt_path = "results/India_Tourism_Project_Report.pptx"
    prs.save(alt_path)
    print(f"Presentation successfully saved to {alt_path}")

if __name__ == "__main__":
    build_presentation()
