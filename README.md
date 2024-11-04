# Salon Database Analysis 💇‍♀️📊

> Leveraging SQL to unlock insights into customer behavior, membership impact, and spending trends at the salon.

This project analyzes a comprehensive salon database, focusing on customer details, memberships, appointment patterns, and spending behavior. By querying and visualizing this data, we aim to identify factors that influence customer loyalty and revenue, ultimately providing actionable insights to boost the salon's economic performance.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Data Structure](#data-structure)
- [Key Questions](#key-questions)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [Visualizations](#visualizations)

---

## 💡 Project Overview

The salon’s dataset includes detailed information about customer demographics, memberships, appointment types and durations, discounts, and spending patterns. This data is used to answer key questions about revenue drivers, customer loyalty, and appointment trends, helping the salon understand its customer base and prioritize growth strategies.

## 📂 Data Structure

The database consists of several customer and appointment-related tables. Here’s a quick overview:

- **Customers**: Contains unique customer IDs, demographic information, and other personal details.
- **Memberships**: Details on membership types, discounts offered, and benefits associated with each membership.
- **Appointments**: Records of each appointment, including `spatreatmentid`, `customerid`, and appointment duration.
- **Transactions**: Tracks total spending by customers on each visit, inclusive of any discounts applied based on memberships.

This structure allows for targeted analysis on customer preferences, appointment choices, and revenue contributions from memberships.

---

## 🔍 Key Questions

The analysis addresses the following strategic questions to provide insights into the salon's operations and potential growth areas:

1. **Which membership types drive the highest customer spending?**
   - This query examines how different membership levels contribute to overall revenue, helping to assess the value of membership programs.

2. **What is the average duration of various types of spa treatments?**
   - Analyzing treatment durations can inform scheduling efficiency and help optimize appointment slots.

3. **Which customers spend the most, and how does membership influence spending?**
   - Identifying high-spending customers and evaluating membership impact on spending patterns.

4. **How frequently do customers with memberships visit compared to non-members?**
   - This helps determine membership effectiveness in encouraging repeat visits.
     
---

## 🚀 Getting Started


## 2. Set Up Database

Run `SQL_tables.csv` to set up the necessary tables for the analysis. This establishes the data structure required for the salon database.

---

## 3. Execute Analysis Queries

Run `3_analysis_queries.sql` to obtain insights on customer spending, membership value, and appointment patterns.

---

## 🗂️ File Structure

- **sql_queries**: Contains SQL scripts to set up the database, analyze the data, and optionally clean up after.
- **visualizations**: Stores Python code for generating graphs that visually represent the key findings from the analysis.

---

## 📊 Visualizations

To complement the SQL analysis, visualizations provide a clear view of the trends:

- **Membership Revenue**: Shows how different membership types contribute to overall revenue.
- **Appointment Durations**: Highlights the average duration of each spa treatment type for optimal scheduling.
- **Customer Spending Patterns**: Displays spending trends to identify high-value customers and the influence of memberships on spending.

These visuals aid in understanding customer behavior, spending habits, and service demand.

---

> This analysis provides data-driven recommendations to support customer retention, revenue growth, and operational efficiency for a salon business.
