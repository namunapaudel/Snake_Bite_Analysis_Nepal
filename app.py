import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

st.set_page_config(page_title="Snake Bite Analysis Nepal", page_icon="🐍", layout="wide")

# Header
st.title("🐍 Snake Bite Analysis in Nepal")
st.markdown("**Fiscal Year 2065/66 to 2073/74** | Analysis by Namuna Paudel")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("snake-bites-cases-and-deaths-nepal-2065-66-to-2073-74.csv")
    df['Death Percentage'] = (df['No. deaths'] / df['Total cases']) * 100
    df['Cure Rate'] = (df['Cure'] / df['Poisonous']) * 100
    return df

df = load_data()

# Key metrics
st.subheader("📊 Key Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases (All Years)", f"{df['Total cases'].sum():,}")
col2.metric("Total Deaths", f"{df['No. deaths'].sum():,}")
col3.metric("Avg Poisonous Bites/Year", f"{df['Poisonous'].mean():.0f}")
col4.metric("Avg Non-Poisonous Bites/Year", f"{df['Non-Poisonous'].mean():.0f}")

st.markdown("---")

# Raw data table
with st.expander("📋 View Raw Data"):
    st.dataframe(df, use_container_width=True)

st.markdown("---")

# Charts
st.subheader("📈 Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Snake Bite Trends Over the Years")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['Fiscal year'], df['Total cases'], marker='o', color='steelblue', label='Total Cases')
    ax.plot(df['Fiscal year'], df['Poisonous'], marker='s', color='red', label='Poisonous')
    ax.plot(df['Fiscal year'], df['Non-Poisonous'], marker='^', color='green', label='Non-Poisonous')
    ax.set_xlabel('Fiscal Year')
    ax.set_ylabel('Number of Cases')
    ax.set_title('Snake Bite Trends Over the Years')
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.markdown("#### Death Percentage Over the Years")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['Fiscal year'], df['Death Percentage'], marker='x', color='red')
    ax.fill_between(range(len(df)), df['Death Percentage'], alpha=0.2, color='red')
    ax.set_xlabel('Fiscal Year')
    ax.set_ylabel('Death Percentage (%)')
    ax.set_title('Death Percentage Over the Years')
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['Fiscal year'], rotation=45)
    ax.grid(True)
    avg = df['Death Percentage'].mean()
    ax.axhline(y=avg, color='darkred', linestyle='--', label=f'Average: {avg:.2f}%')
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Cure Rate Over the Years")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df['Fiscal year'], df['Cure Rate'], marker='o', color='green')
    ax.fill_between(range(len(df)), df['Cure Rate'], alpha=0.2, color='green')
    ax.set_xlabel('Fiscal Year')
    ax.set_ylabel('Cure Rate (%)')
    ax.set_title('Cure Rate Over the Years')
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['Fiscal year'], rotation=45)
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)

with col4:
    st.markdown("#### Avg Poisonous vs Non-Poisonous Bites")
    fig, ax = plt.subplots(figsize=(8, 5))
    categories = ['Poisonous', 'Non-Poisonous']
    values = [df['Poisonous'].mean(), df['Non-Poisonous'].mean()]
    colors = ['red', 'steelblue']
    bars = ax.bar(categories, values, color=colors, width=0.4)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                f'{val:.0f}', ha='center', va='bottom', fontweight='bold')
    ax.set_ylabel('Average Bites per Year')
    ax.set_title('Average Poisonous vs Non-Poisonous Bites per Year')
    ax.grid(True, axis='y')
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")
st.markdown("**Data Source:** Government of Nepal Health Records | **Developer:** [Namuna Paudel](https://github.com/namunapaudel)")
