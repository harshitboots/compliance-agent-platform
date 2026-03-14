# Azure AI Foundry Integration

This project uses Azure AI Foundry as the core AI engine powering the intelligent compliance agents.

## Model Deployment

Model: GPT-4.1-mini  
Deployment Platform: Azure AI Foundry  
Region: Sweden Central

## Usage in Agents

Azure AI Foundry models are used in:

Risk Analyzer Agent  
Analyzes financial transactions and assigns fraud risk scores.

Compliance Report Agent  
Generates compliance reports explaining detected anomalies.

Fraud Alert Agent  
Creates fraud alerts and escalation messages.

## Example Code

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-12-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a financial fraud detection AI."},
        {"role": "user", "content": "Analyze this transaction for fraud risk."}
    ]
)
