## Overview

This project demonstrates how enterprise AI agents can automate financial compliance and fraud detection workflows.

The system uses a multi-agent architecture built on Azure AI Foundry and Databricks.

## Agents

Customer Data Agent  
Loads transaction data from Databricks Lakehouse.

Risk Analyzer Agent  
Uses Azure AI models to detect suspicious patterns.

Compliance Report Agent  
Generates regulatory audit reports.

Fraud Alert Agent  
Triggers alerts and integrates with external systems.

## Architecture

Databricks Lakehouse  
↓  
Customer Data Agent  
↓  
Risk Analyzer Agent  
↓  
Compliance Agent + Fraud Alert Agent
