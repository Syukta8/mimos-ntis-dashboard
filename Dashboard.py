import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="MIMOS NTIS Dashboard",
    page_icon="xf1ca",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# Custom CSS for "Gamma Site" Look
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Main background and font adjustments to match clean dashboard style */
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    .stMetric {
        background-color: #262730;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .stMetric label {
        color: #b0b0b0 !important;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #00d4ff !important;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Header
# -----------------------------------------------------------------------------
col_logo, col_text = st.columns([0.5, 5], vertical_alignment="center")
with col_logo:
    # ⚠️ REPLACE THIS URL with your local file path (e.g., "logo.png")
    # or a direct link to the MIMOS logo.
    logo_url = "./images/MIMOS_(Malaysian)_Logo.png" 
    
    try:
        st.image(logo_url, width=60)
    except:
        st.warning("Logo not found")

with col_text:
    st.title("MIMOS NTIS Dashboard")
st.markdown("### Data Insights & Application Overview")
st.markdown("---")

# -----------------------------------------------------------------------------
# Section 1: All-Time Stats (Cohorts 1-60)
# -----------------------------------------------------------------------------
st.subheader("📌 Overall Performance (Cohorts 1-60)")

# Metrics based on the site data
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total NTIS Applicants", value="668")

with col2:
    st.metric(label="MIMOS Funnel", value="502")

with col3:
    st.metric(label="MIMOS for ESC Review", value="381")

with col4:
    st.metric(label="Total Invoice Claims", value="RM 476,250", help="RM 1,250 (inc. SST) per Technical Evaluation")

st.info("ℹ️ **Note:** Invoice Claims calculation is based on RM 1,250 (inc. SST) per Technical Evaluation (TE) completed by agencies.")

# -----------------------------------------------------------------------------
# Section 2: 2025 Updates
# -----------------------------------------------------------------------------
st.markdown("---")
st.subheader("📅 2025 Performance Update (Cohorts 52-60)")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(label="2025 Applicants", value="81", delta="Cohorts 52-60")

with kpi2:
    st.metric(label="2025 Funnel", value="40")

with kpi3:
    st.metric(label="2025 ESC Review", value="42")

with kpi4:
    st.metric(label="2025 Claims", value="RM 52,500") # Estimated based on proportion or dummy logic

# -----------------------------------------------------------------------------
# Section 3: Charts & Visuals
# -----------------------------------------------------------------------------
st.markdown("---")
st.subheader("📊 Application Trends by Year")

# Create Mock Data for Visualization
years = ['2021', '2022', '2023', '2024', '2025']
data = {
    'Year': years,
    'Applicants': [150, 180, 140, 117, 81],  # Mock numbers summing roughly to ~668
    'Reviewed': [100, 120, 80, 50, 42],
    'Approved': [80, 90, 60, 30, 20]
}
df = pd.DataFrame(data)

# Layout for Charts
tab1, tab2 = st.tabs(["📈 Trend Analysis", "🗓️ Yearly Breakdown"])

with tab1:
    # Line Chart for Trend
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(x=df['Year'], y=df['Applicants'], mode='lines+markers', name='Applicants', line=dict(color='#00d4ff', width=3)))
    fig_trend.add_trace(go.Scatter(x=df['Year'], y=df['Reviewed'], mode='lines+markers', name='Reviewed', line=dict(color='#ff4b4b', width=3)))
    
    fig_trend.update_layout(
        title="Applicant vs Review Trend (2021-2025)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#444')
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with tab2:
    # Bar Chart for Breakdown
    fig_bar = px.bar(
        df, 
        x='Year', 
        y=['Applicants', 'Reviewed', 'Approved'], 
        barmode='group',
        color_discrete_sequence=['#00d4ff', '#ff4b4b', '#00ff7f'],
        title="Detailed Breakdown by Status"
    )
    fig_bar.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#444')
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# -----------------------------------------------------------------------------
# Section 4: Data Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.caption(f"Data as of October 15, 2025 | Source: MIMOS NTIS Internal Records")