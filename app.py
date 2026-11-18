
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# SMARTSCAN AI - SIH 2026
# Educational simulation prototype
# ---------------------------------

st.set_page_config(
    page_title="SMARTSCAN AI",
    page_icon="📡",
    layout="wide"
)

# Styling

# ---------------------------------
# PROFESSIONAL SMARTSCAN AI THEME
# ---------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080f1e, #101b30);
    color: #e2e8f0;
}

[data-testid="stHeader"] {
    background: rgba(8, 15, 30, 0.85);
}

[data-testid="stSidebar"] {
    background: #101b30;
    border-right: 1px solid #263750;
}

[data-testid="stSidebar"] h1 {
    color: #38bdf8;
    font-size: 25px;
}

h1 {
    color: #38bdf8 !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #7dd3fc !important;
}

p, label, li {
    color: #cbd5e1;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #172b46, #102039);
    border: 1px solid #294765;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.2);
}

[data-testid="stMetricLabel"] {
    color: #94a3b8;
}

[data-testid="stMetricValue"] {
    color: #38bdf8;
    font-weight: 800;
}

div.stButton > button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #0369a1, #1d4ed8);
    border: 1px solid #38bdf8;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #294765;
    border-radius: 12px;
}

hr {
    border-color: #294765;
}

[data-testid="stDownloadButton"] button {
    background: #164e63;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# Sidebar

# ---------------------------------
# PROFESSIONAL SIDEBAR
# ---------------------------------

with st.sidebar:

    st.markdown("# 📡 SMARTSCAN")
    st.caption("AI INTELLIGENCE PLATFORM")
    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select Module",
        [
            "Dashboard",
            "Simulation",
            "Performance",
            "Workflow",
            "About"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### System Status")

    st.success("● Application Online")

    st.info(
        "Educational simulation environment\n\n"
        "Synthetic data only."
    )

    st.divider()

    st.markdown("### Project Information")
    st.caption("SIH 2026")
    st.caption("Team AetherX")
    st.caption("Version 2.0")


# Generate synthetic demonstration data
def generate_data(samples, seed):
    rng = np.random.default_rng(seed)

    bands = ["Band A", "Band B", "Band C", "Band D", "Band E"]

    activity = rng.integers(
        0, 2, size=(samples, len(bands))
    )

    frame = pd.DataFrame(
        activity,
        columns=bands
    )

    frame.index.name = "Observation"

    # Illustrative predictions, NOT a trained ML model
    truth = activity.flatten()
    predictions = truth.copy()

    noise = rng.random(len(predictions)) < 0.15
    predictions[noise] = 1 - predictions[noise]

    tp = np.sum((truth == 1) & (predictions == 1))
    fp = np.sum((truth == 0) & (predictions == 1))
    fn = np.sum((truth == 1) & (predictions == 0))

    detection = tp / max(tp + fn, 1)
    false_alarm = fp / max(fp + np.sum((truth == 0) & (predictions == 0)), 1)
    accuracy = np.mean(truth == predictions)

    return frame, detection, false_alarm, accuracy


# Sidebar controls
st.sidebar.subheader("Simulation Settings")

samples = st.sidebar.slider(
    "Number of observations",
    min_value=20,
    max_value=200,
    value=60,
    step=10
)

seed = st.sidebar.number_input(
    "Demo seed",
    min_value=1,
    max_value=9999,
    value=42
)

if st.sidebar.button("Generate New Demo", use_container_width=True):
    st.session_state["demo_seed"] = int(seed)

active_seed = st.session_state.get("demo_seed", 42)

data, detection, false_alarm, accuracy = generate_data(
    samples, active_seed
)

# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.title("📡 SMARTSCAN AI")
    st.subheader("Intelligent Adaptive Scan Scheduling")

    st.write(
        "A simulation-based research prototype for "
        "studying intelligent scheduling concepts."
    )

    st.success("Simulation Environment: Ready")

    c1, c2, c3 = st.columns(3)

    c1.metric("Virtual Bands", "5")
    c2.metric("Observations", samples)
    c3.metric("Environment", "Synthetic")

    st.divider()

    st.subheader("Project Overview")

    st.write("""
    SMARTSCAN AI explores how machine learning concepts
    can support adaptive scheduling research through
    a software-based simulated environment.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Proposed Technologies")
        st.write("- Python")
        st.write("- Streamlit")
        st.write("- NumPy")
        st.write("- Pandas")
        st.write("- Matplotlib")
        st.write("- Machine Learning (future module)")

    with col2:
        st.markdown("### Main Components")
        st.write("- Synthetic RF environment")
        st.write("- Virtual receiver representation")
        st.write("- Observation collection")
        st.write("- Scheduling research concept")
        st.write("- Performance evaluation")

    st.divider()
    st.caption("Team AetherX | Smart India Hackathon 2026")

# ---------------- SIMULATION ----------------

elif page == "Simulation":

    st.title("Synthetic Environment")

    st.write(
        "This page displays fictional activity data "
        "for five virtual bands. Values are generated "
        "for demonstration and are not real RF measurements."
    )

    st.subheader("Virtual Band Activity")

    fig, ax = plt.subplots(figsize=(11, 4))

    ax.imshow(
        data.T,
        aspect="auto",
        cmap="Blues",
        interpolation="nearest"
    )

    ax.set_yticks(range(5))
    ax.set_yticklabels(data.columns)
    ax.set_xlabel("Observation Number")
    ax.set_title("Synthetic Activity Matrix")

    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Activity Summary")

    activity_count = data.sum()

    st.bar_chart(activity_count)

    st.subheader("Sample Observation Data")
    st.dataframe(data.head(15), use_container_width=True)

    csv = data.to_csv().encode("utf-8")

    st.download_button(
        "Download Synthetic Data CSV",
        data=csv,
        file_name="smartscan_demo.csv",
        mime="text/csv"
    )

# ---------------- PERFORMANCE ----------------

elif page == "Performance":

    st.title("Performance Evaluation")

    st.write(
        "The following values are calculated from "
        "synthetic demonstration data. They are not "
        "validated results from a trained ML scheduler."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Probability of Detection",
        f"{detection * 100:.2f}%"
    )

    c2.metric(
        "Probability of False Alarm",
        f"{false_alarm * 100:.2f}%"
    )

    c3.metric(
        "Correct Predictions",
        f"{accuracy * 100:.2f}%"
    )

    st.divider()

    st.subheader("Evaluation Status")

    metrics = pd.DataFrame({
        "Metric": [
            "Probability of Detection",
            "Probability of False Alarm",
            "Correct Predictions",
            "Mean Intercept Rate",
            "Average Intercept Time Error",
            "Average Reward / Cost Function"
        ],
        "Status": [
            "Illustrative calculation",
            "Illustrative calculation",
            "Illustrative calculation",
            "Not implemented",
            "Not implemented",
            "Not implemented"
        ]
    })

    st.dataframe(metrics, use_container_width=True)

    st.warning(
        "A real ML model and a validated scheduling "
        "experiment are not implemented in this version."
    )

# ---------------- WORKFLOW ----------------

elif page == "Workflow":

    st.title("System Workflow")

    steps = [
        ("01", "Simulated RF Environment",
         "Create a fictional multi-band environment."),
        ("02", "Receiver Simulation",
         "Represent a virtual receiver in software."),
        ("03", "Observation Collection",
         "Collect generated sample observations."),
        ("04", "ML-Based Scheduler",
         "Planned research module; not implemented in V1."),
        ("05", "Detection Feedback",
         "Represent feedback using synthetic sample data."),
        ("06", "Model Evaluation",
         "Display available demonstration metrics.")
    ]

    for number, title, description in steps:
        with st.container(border=True):
            st.markdown(f"### {number} | {title}")
            st.write(description)

# ---------------- ABOUT ----------------

elif page == "About":

    st.title("About SMARTSCAN AI")

    st.subheader("Smart India Hackathon 2026")

    st.write("**Problem ID:** SIH26055")
    st.write("**Problem:** Smart Scan Strategy for Electronic Warfare")
    st.write("**Team:** AetherX")
    st.write("**Theme:** Robotics and Drones")
    st.write("**Category:** Software")

    st.divider()

    st.subheader("Project Objective")

    st.write("""
    To study intelligent adaptive scan scheduling
    through a software-based simulation and
    synthetic multi-band observations.
    """)

    st.info(
        "This is an educational research prototype. "
        "It does not interface with real RF hardware."
    )

    st.caption("Developed for SIH 2026 | Team AetherX")
