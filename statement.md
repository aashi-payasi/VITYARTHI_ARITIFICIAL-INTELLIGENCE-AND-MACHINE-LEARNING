# Problem Statement

## Title
ATM Interface System with ML-Based Fraud Detection

## Objective
To design and implement a console-based ATM system in Python that
replicates real-world ATM functionality — secure login, balance inquiry,
deposits, and withdrawals — while applying core programming concepts such
as functions, conditional statements, loops, and file/module management.

The project is further extended with a Machine Learning component so that
it goes beyond simulating an ATM's basic operations: it also learns to
recognise transaction patterns and flag activity that looks abnormal for
the account, similar to fraud-detection systems used by real banks.

## Problem Description
Traditional ATM simulation projects only validate transactions using fixed
rules (e.g. "block if amount > X"). This does not reflect how real-world
financial fraud detection works, where systems must learn from data rather
than rely purely on hardcoded thresholds.

This project solves that gap by:
1. Implementing the standard ATM operations (login, deposit, withdraw,
   balance check) using core Python.
2. Training an unsupervised Isolation Forest model on transaction data
   (amount, time of day, day of week, and amount-to-balance ratio) to
   learn what a "normal" transaction looks like.
3. Using that trained model to score every live transaction and flag ones
   that appear statistically unusual, logging them for review.

## Scope
- Single in-memory account (PIN, balance) for demonstration purposes.
- Fraud detection trained on synthetic data representing typical vs.
  unusual ATM transaction patterns.
- Console-based interface; no GUI or persistent database.

## Core Python Concepts Used
- Functions — modular code for login, deposit, withdraw, balance check, and fraud checking.
- Conditional statements — validating PINs, amounts, and balances.
- Loops — the main menu loop and login attempt loop.
- File/module management — separate `.py` files per feature, imported into `main.py`; log files for transactions and fraud alerts.
- datetime module — timestamps for balance summaries and fraud alerts.

## Machine Learning Concepts Used
- Unsupervised anomaly detection using Isolation Forest (scikit-learn).
- Feature engineering: transaction amount, hour of day, day of week,
  account balance before the transaction, and amount-to-balance ratio.
- Feature scaling with StandardScaler before model training/inference.
- Model persistence using joblib, so the model is trained once and reused
  across ATM sessions.

## Expected Outcome
A working ATM console application that:
- Correctly handles login, deposits, withdrawals, and balance checks.
- Flags and logs transactions that are statistically unusual for the
  account, demonstrating a practical, lightweight application of machine
  learning to a financial security use case.
