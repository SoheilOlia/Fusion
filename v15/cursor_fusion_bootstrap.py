#!/usr/bin/env python3
"""
Cursor Fusion v15 Auto-Bootstrap
Automatically loads Fusion v15 in any Cursor environment
"""

import sys
import os
from pathlib import Path

def bootstrap_fusion():
    """Bootstrap Fusion v15 for Cursor."""
    try:
        # Add current directory to Python path
        current_dir = Path.cwd()
        if str(current_dir) not in sys.path:
            sys.path.insert(0, str(current_dir))
        
        # Import Fusion components
        from fusion_core.memory.agent_memory import AgentMemory
        from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger
        from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator
        
        # Import agents
        from agents_combined import AGENT_REGISTRY
        
        print("✅ Fusion v15 loaded successfully!")
        print("🎯 Available functions:")
        print("   - ask(prompt, agent_name)")
        print("   - ask_auto(prompt)")
        print("   - ask_chain(prompt, [agent1, agent2])")
        print("   - get_agent_memory(agent_name)")
        print("   - get_telemetry()")
        
        return True
        
    except Exception as e:
        print(f"⚠️ Fusion bootstrap failed: {e}")
        return False

# Auto-bootstrap when imported
if __name__ == "__main__":
    bootstrap_fusion()
