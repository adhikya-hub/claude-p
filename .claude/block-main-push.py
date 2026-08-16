#!/usr/bin/env python3
import sys
import json

# Read hook context from stdin
try:
    data = json.load(sys.stdin)
    command = data.get('input', {}).get('command', '')
except:
    sys.exit(0)

# Check for git push to main
if 'git' in command and 'push' in command:
    if 'main' in command or 'origin main' in command or 'main:' in command or ':main' in command:
        print("❌ Error: Pushing to main is blocked. Please create a PR instead.", file=sys.stderr)
        sys.exit(1)

# Allow the command to proceed
sys.exit(0)
