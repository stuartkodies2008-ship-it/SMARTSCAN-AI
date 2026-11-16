
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
st.markdown("""
<style>
.main {
    background-color: #0b1220;
}
h1, h2, h3 {
    color: #38bdf8;
}
[data-testid="stMetric"] {
    background-color: #17243a;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📡 SMARTSCAN AI")
st.sidebar.caption("SIH 2026 | AetherX")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Simulation", "Performance", "Workflow", "About"]
)

st.sidebar.divider()
st.sidebar.info(
    "Educational prototype using synthetic data only."
)

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
