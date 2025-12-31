# Multi-Factor Regression Model – NIFTY 50 (2025)

This project implements an **interpretable multi-factor regression framework** to explain **monthly NIFTY 50 returns** using key market and macroeconomic factors. The objective is **factor attribution and explainability**, rather than price prediction.

## Project Objective
To quantify how different factors contribute to stock market index returns by decomposing NIFTY 50 performance into additive, interpretable components.

## Factors Used
- **India VIX** – captures market volatility and risk sentiment  
- **USD/INR Exchange Rate** – represents macroeconomic conditions and foreign capital flow dynamics  

## Methodology
- Daily financial data is aligned to a **monthly frequency**
- NIFTY 50 is converted to **monthly returns**
- India VIX is aggregated using **monthly averages**
- USD/INR is sampled at **month-end levels**
- Features are standardized prior to modeling
- **Ridge Regression** is used to ensure coefficient stability in the presence of correlated factors

## Model Evaluation
The model is evaluated using:
- R-squared  
- RMSE/MSE
- Correlation between actual and predicted returns  
- Residual analysis to check for systematic bias  

## Factor Attribution
Monthly NIFTY returns are decomposed into:
- Volatility-driven contribution (India VIX)
- Currency-driven contribution (USD/INR)
- Intercept component  

This allows each return to be explained additively rather than treated as a black-box output.

## Outputs
- **Time-based visualizations** of factor contributions  
- **Machine-readable JSON** containing coefficients, diagnostics, and total factor contributions  
- **Human-readable summary report** explaining findings and limitations  

## Key Insights
- Higher market volatility is associated with weaker equity performance  
- Currency movements capture macroeconomic and foreign capital flow effects  
- The framework provides transparent and interpretable return attribution  

## Limitations
- Linear model does not capture regime shifts or non-linear dynamics  
- Limited factor set; additional macro variables could improve explanatory power  

## Use Case
This project demonstrates how **explainable AI and quantitative modeling** can be applied to financial markets for **return attribution, risk analysis, and macro-factor understanding**, making it suitable for AI Engineer, Quant Research, and Financial Analytics roles.
