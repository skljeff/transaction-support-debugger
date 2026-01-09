# Transaction Support Debugger (Prototype)

## What is this?
A small Python prototype that simulates how fintech support teams diagnose transaction issues.

## Problem
Support teams often spend time checking multiple systems to understand:
- Where a transaction is stuck
- Why it is delayed
- What the next action should be
- How to explain it clearly to the customer

## Solution
This tool allows support to:
- Enter a transaction ID
- Instantly see the transaction status
- Understand the reason for the delay
- Get a suggested next action
- Generate a ready-to-send customer reply

## Example
Input:
TX1002

Output:
- Status: Compliance Check  
- Reason: Additional documents required  
- Next action: Ask customer to upload invoice  

## How to run
```bash
python3 transaction_checker.py
