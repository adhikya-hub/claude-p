#!/usr/bin/env python3
import sys
import json

# Read the tool input from stdin (Claude Code passes it as JSON)
try:
    tool_input = json.load(sys.stdin)
    command = tool_input.get('command', '')
except:
    sys.exit(0)

# Block git push to main
if 'git' in command and 'push' in command and 'main' in command:
    print("❌ Error: Pushing to main is blocked. Please create a PR instead.", file=sys.stderr)
    sys.exit(1)

sys.exit(0)
