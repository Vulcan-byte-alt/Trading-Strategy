#!/usr/bin/env python3
"""
Startup script for Quantum Momentum Strategy
"""

import sys
import os

# Add base path for imports
base_path = os.path.join(os.path.dirname(__file__), '..', 'base-bot-template')
if not os.path.exists(base_path):
    base_path = '/app/base'
sys.path.insert(0, base_path)

# Import and register strategy
from your_strategy import QuantumMomentumStrategy, register_strategy

# Strategy is auto-registered via register_strategy() call in your_strategy.py

if __name__ == "__main__":
    print("✅ Quantum Momentum Strategy loaded successfully")
    print("   Strategy: Ultimate Asymmetric")
    print("   Assets: BTC-USD, ETH-USD")
    print("   Position Size: 55% (max)")
    print("   Ready for backtesting!")
