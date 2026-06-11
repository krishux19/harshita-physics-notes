import streamlit as st

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Units and Measurement",
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

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.title("📘 Units and Measurement")

st.caption(
    "For Harshita ❤️"
)

st.divider()

# =====================================================
# LOAD NOTES
# =====================================================

NOTES_PATH = (
    "github_notes_deploy/study/physics/"
    "cs11ch1-units_and_measurements/"
    "notes_output.md"
)

try:

    with open(
        NOTES_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        notes = f.read()

    with st.container(
        border=True
    ):
        st.markdown(notes)

except Exception as e:

    st.error(
        f"Unable to load notes: {e}"
    )
