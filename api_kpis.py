import streamlit as st


def kpi(title, icon, value):
    st.markdown(
        f"""
    <div class="kpi-card">
        <div class="kpi-title">{icon} {title}</div>
        <div class="kpi-value">{value:,}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ---- KPI LAYOUT FUNCTION ----

#Creas una funcion dnde le pasas el datafream filtrado de la hoja de main
def plot_kpis(df):
    total_countries = len(df) #cuantos paises hay
    total_population = df["population"].sum()
    avg_population = int(df["population"].mean())
    largest_area = df["area"].max()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi("Total Countries", "🌍", total_countries)

    with c2:
        kpi("Total Population", "👥", total_population)

    with c3:
        kpi("Avg Population", "📊", avg_population)

    with c4:
        kpi("Largest Area (km²)", "🌐", largest_area)