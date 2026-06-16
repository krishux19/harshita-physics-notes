import streamlit as st
from pathlib import Path
import re

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Harshita Physics Notes",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.block-container{
    max-width:1100px;
    padding-top:2rem;
}

section[data-testid="stSidebar"] {
    width: 320px !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# CHAPTERS
# =====================================================

CHAPTERS = {

    "📏 Units and Measurement":
    "github_notes_deploy/study/physics/cs11ch1/notes_output.md",

    "➡️ Motion in a Straight Line":
    "github_notes_deploy/study/physics/cs11ch2/notes_output.md",

    "🛩️ Motion in a Plane":
    "github_notes_deploy/study/physics/cs11ch3/notes_output.md",

    "⚖️ Laws of Motion":
    "github_notes_deploy/study/physics/cs11ch4/notes_output.md",

    "⚡ Work Energy and Power":
    "github_notes_deploy/study/physics/cs11ch5/notes_output.md",

    "🔄 System of Particles and Rotational Motion":
    "github_notes_deploy/study/physics/cs11ch6/notes_output.md",

    "🌍 Gravitation":
    "github_notes_deploy/study/physics/cs11ch7/notes_output.md",
}

# =====================================================
# HEADER
# =====================================================

st.title("📘 Physics Notes")

st.caption(
    "For Harshita ❤️"
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

selected_chapter = st.sidebar.radio(
    "Select Chapter",
    list(CHAPTERS.keys())
)

NOTES_PATH = CHAPTERS[selected_chapter]

# =====================================================
# LOAD NOTES
# =====================================================

try:

    with open(
        NOTES_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        notes = f.read()

    st.subheader(selected_chapter)

    # =================================================
    # SECTION PARSER
    # =================================================

    sections = re.split(
        r"\n# ",
        notes
    )

    emoji_map = {

        "CHAPTER OVERVIEW": "📖",

        "BEGINNER EXPLANATION": "📚",

        "COMPLETE CONCEPT NOTES": "🧠",

        "NCERT GOLDEN LINES": "⭐",

        "FORMULA SHEET": "📝",

        "DERIVATIONS AND LOGIC": "📐",

        "NEET HIGH-YIELD CONCEPTS": "🎯",

        "CONCEPTUAL TRAPS": "⚠️",

        "MEMORY BOOSTERS": "🧩",

        "CHAPTER REVISION SHEET": "📋",

        "1-DAY REVISION VERSION": "🔥",

        "TOP 25 NEET QUESTIONS": "❓",

        "PYQ PREDICTION AREAS": "🎯",

        "FINAL TAKEAWAYS": "✅"
    }

    parsed_sections = []

    for section in sections:

        if not section.strip():
            continue

        title = section.split(
            "\n",
            1
        )[0].replace(
            "#",
            ""
        ).strip()

        body = ""

        if "\n" in section:

            body = section.split(
                "\n",
                1
            )[1]

        parsed_sections.append(
            (
                title,
                body
            )
        )

    # =================================================
    # QUICK NAV
    # =================================================

    st.markdown("### 📚 Quick Navigation")

    cols = st.columns(4)

    for idx, (title, _) in enumerate(parsed_sections):

        icon = emoji_map.get(
            title.upper(),
            "📄"
        )

        cols[idx % 4].markdown(
            f"- {icon} {title}"
        )

    st.divider()

    # =================================================
    # RENDER SECTIONS
    # =================================================

    for title, body in parsed_sections:

        icon = emoji_map.get(
            title.upper(),
            "📄"
        )

        default_open = (
            title.upper()
            in [
                "CHAPTER OVERVIEW",
                "FORMULA SHEET",
                "1-DAY REVISION VERSION"
            ]
        )

        with st.expander(
            f"{icon} {title}",
            expanded=default_open
        ):
            st.markdown(body)

except Exception as e:

    st.error(
        f"Unable to load notes: {e}"
    )
