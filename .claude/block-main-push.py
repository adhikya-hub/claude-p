#!/usr/bin/env python3
import sys
import json
import os

# Try to read hook context from stdin
command = ''
try:
    input_data = sys.stdin.read()
    if input_data:
        data = json.loads(input_data)
        command = data.get('input', {}).get('command', '')
except Exception as e:
    pass

# Also check environment variables
if not command:
    command = os.environ.get('CLAUDE_COMMAND', '')

# Also check argv
if not command and len(sys.argv) > 1:
    command = ' '.join(sys.argv[1:])

# Debug: write what we received to a file for inspection
with open('/tmp/hook_debug.log', 'a') as f:
    f.write(f"Command detected: {command}\n")
    f.write(f"Env vars: {os.environ.keys()}\n\n")

# Check for git push to main
if command and 'git' in command and 'push' in command:
    if 'main' in command or 'origin main' in command or 'main:' in command or ':main' in command:
        print("❌ Error: Pushing to main is blocked. Please create a PR instead.", file=sys.stderr)
        sys.exit(1)

# Allow the command to proceed
sys.exit(0)
