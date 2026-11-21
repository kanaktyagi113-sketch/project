# E-commerce Sales Analysis

Data analysis of 250 Indian e-commerce orders using Python, Pandas and Matplotlib.

## Project structure
- `data/raw/` - original Excel file (never edited)
- `data/processed/` - cleaned CSV
- `notebooks/` - analysis notebook
- `images/` - saved charts
- `scripts/` - cleaning script

## Key findings
- Total sales: Rs 35.85 lakh across 250 orders
- Electronics gives about 73% of sales
- Orders with more than 20% discount have higher returns
- Average customer feedback is 2.81 out of 5

## How to run
1. `pip install -r requirements.txt`
2. `python scripts/clean_data.py`
3. Open `notebooks/ecommerce_sales_analysis.ipynb` in VS Code