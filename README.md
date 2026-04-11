# Snake Bite Analysis in Nepal
### Fiscal Year 2065/66 to 2073/74

A data analysis and visualization project analyzing snake bite cases, deaths, and cure rates in Nepal over 9 fiscal years using Python, Pandas, and Matplotlib.

## Live Dashboard
 **[Click here to explore the interactive dashboard](https://snakebiteanalysisnepal-app.streamlit.app/)**

## What's Analyzed
- **Snake bite trends** over the years
- **Death percentage** over the years
- **Cure rate** over the years
- **Average poisonous vs non-poisonous** bites per year

## Key Findings
- Total of **96,141** snake bite cases recorded over 9 years
- Average of **958** poisonous bites per year
- Average of **9,724** non-poisonous bites per year
- Death percentage significantly dropped from **11.3%** (2065/66) to **3.6%** (2073/74)
- Cure rate improved significantly over the years

## Tech Stack
- **Python**
- **Pandas** — data manipulation
- **Matplotlib** — data visualization
- **Streamlit** — interactive web dashboard

## Project Structure
```
Snake_Bite_Analysis_Nepal/
├── app.py                          ← Streamlit dashboard
├── requirements.txt                ← Python dependencies
├── SnakeBite Data Analysis Nepal.ipynb  ← Original analysis notebook
└── Data/
    └── snake-bites-cases-and-deaths-nepal-2065-66-to-2073-74.csv
```

## Run Locally
```bash
# Clone the repository
git clone https://github.com/namunapaudel/Snake_Bite_Analysis_Nepal.git
cd Snake_Bite_Analysis_Nepal

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Data Source
Government of Nepal — Ministry of Health and Population
Snake bite cases and deaths records from fiscal year 2065/66 to 2073/74.

## Developer
**Namuna Paudel**
- GitHub: [@namunapaudel](https://github.com/namunapaudel)
- 🍄 Other Project: [Oyster Mushroom Disease Classification](https://github.com/namunapaudel/Oyester-Mushroom-Disease-Classification)
