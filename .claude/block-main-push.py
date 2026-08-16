#!/usr/bin/env python3
import sys
import os

# Get the command from environment variable set by the hook
command = os.environ.get('CLAUDE_TOOL_INPUT', '')

# Check for git push to main
if 'git' in command and 'push' in command:
    if 'main' in command or 'origin main' in command or 'main:' in command or ':main' in command:
        print("❌ Error: Pushing to main is blocked. Please create a PR instead.", file=sys.stderr)
        sys.exit(1)

# Allow the command to proceed
sys.exit(0)
