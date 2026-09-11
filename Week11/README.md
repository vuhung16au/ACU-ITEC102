# Week 11: Data Visualisation with Matplotlib and Pandas

Welcome to Week 11 of ACU-ITEC102. This week explores **Data Visualisation**, transforming raw numbers and statistical summaries into intuitive, insightful, and publication-ready charts using **Matplotlib** and **Pandas**. Students learn why visual inspection is critical (demonstrated through Anscombe's Quartet), how to choose the right chart type for their data, and how to style figures for clear communication.

---

## Learning Outcomes
By completing this week's materials, you will be able to:
1. **Understand Why Visualisation Matters**: Recognize why summary statistics alone can be misleading (Anscombe's Quartet) and navigate Matplotlib's Figure and Axes architecture.
2. **Master Line Plots**: Graph continuous trends and time-series data with comparative series, styled lines, markers, and legends.
3. **Construct Bar Charts**: Build vertical, horizontal, grouped (clustered), and stacked bar charts for categorical comparisons with value labels.
4. **Evaluate Pie and Donut Charts**: Create proportion charts, apply emphasis with `explode`, and critically assess when to replace pie charts with superior bar charts.
5. **Analyze Distributions with Histograms**: Bin continuous numeric variables, evaluate distribution shapes (skewness, modality), and overlay statistical reference lines (mean and median).
6. **Customise and Style Figures**: Apply professional themes (`fivethirtyeight`, `seaborn-v0_8-whitegrid`), build multi-panel subplots, and add annotations.

---

## Topic Navigation

| Topic | Focus Area | Key Matplotlib / Pandas Functions |
| :--- | :--- | :--- |
| [01. Why Visualisation Matters](01.Why-Visualisation-Matters/) | Anscombe's Quartet, summary deception, Matplotlib architecture | `plt.subplots()`, `ax.scatter()`, `ax.plot()` |
| [02. Line Plots](02.Line-Plots/) | Continuous trends, multi-line comparisons, markers, legends | `plt.plot()`, `linestyle`, `marker`, `plt.legend()`, `plt.grid()` |
| [03. Bar Charts](03.Bar-Charts/) | Categorical comparison, horizontal bars, clustered offsets, stacked | `plt.bar()`, `plt.barh()`, `bottom=...`, `ax.bar_label()` |
| [04. Pie Charts](04.Pie-Charts/) | Proportions, donut charts, `explode`, visual perception limits | `plt.pie()`, `autopct`, `plt.Circle()`, `ax.add_artist()` |
| [05. Histograms](05.Histograms/) | Continuous distributions, bin selection, density, reference lines | `plt.hist()`, `bins`, `density`, `plt.axvline()` |
| [06. Customising and Styling](06.Customising-and-Styling/) | Themes, multi-panel subplots, annotations, figure sizing | `plt.style.use()`, `plt.subplots(2, 2)`, `ax.annotate()` |

---

## Folder Structure

Each topic folder is structured consistently:
```text
Topic-Folder/
├── notebooks/       # Interactive Jupyter notebooks with step-by-step guidance & exercises
├── src/             # Clean, runnable Python scripts containing all demonstrations
├── docs/            # Conceptual summaries and syntax reference guides
├── Makefile         # Commands to run scripts or launch Jupyter Lab
├── README.md        # Topic-level learning objectives and instructions
└── QUICKSTART.md    # Step-by-step setup and execution guide
```

---

## Recommended Learning Flow
1. Work through the topics sequentially from `01` to `06`.
2. Run each script in `src/` to observe the generated figures and terminal explanations.
3. Open the corresponding notebook in `notebooks/` to interactively modify plot parameters and complete the practice exercises.
