#!/usr/bin/env python3
"""
Cursor Fusion v15 Integration
Provides seamless Fusion v15 experience in Cursor
"""

import asyncio
from typing import List, Optional
from pathlib import Path

# Global Fusion components
fusion_memory = None
fusion_telemetry = None
fusion_orchestrator = None
agent_registry = {}

def initialize_fusion():
    """Initialize Fusion v15 components."""
    global fusion_memory, fusion_telemetry, fusion_orchestrator, agent_registry
    
    try:
        from fusion_core.memory.agent_memory import AgentMemory
        from fusion_core.telemetry.agent_telemetry import AgentTelemetryLogger
        from fusion_core.orchestration.multi_agent_orchestrator import MultiAgentOrchestrator
        from agents_combined import AGENT_REGISTRY
        
        fusion_memory = AgentMemory
        fusion_telemetry = AgentTelemetryLogger()
        agent_registry = AGENT_REGISTRY
        
        print("✅ Fusion v15 initialized successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Fusion initialization failed: {e}")
        return False

def ask(prompt: str, agent_name: str = "auto") -> str:
    """Ask a question to a specific agent."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        if agent_name == "auto":
            return ask_auto(prompt)
        
        if agent_name in agent_registry:
            agent_class = agent_registry[agent_name]
            agent = agent_class()
            result = asyncio.run(agent.run(prompt))
            
            # Log to telemetry
            fusion_telemetry.log_event(agent_name, prompt, result, confidence=0.9)
            
            return result
        else:
            return f"❌ Agent '{agent_name}' not found. Available agents: {list(agent_registry.keys())}"
            
    except Exception as e:
        return f"❌ Error: {e}"

def ask_auto(prompt: str) -> str:
    """Automatically select the best agent for the task."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        # Simple agent selection logic
        if "design" in prompt.lower():
            return ask(prompt, "vp_design")
        elif "evaluate" in prompt.lower():
            return ask(prompt, "evaluator")
        elif "creative" in prompt.lower():
            return ask(prompt, "creative_director")
        elif "product" in prompt.lower():
            return ask(prompt, "vp_of_product")
        else:
            return ask(prompt, "vp_design")  # Default to VP Design
            
    except Exception as e:
        return f"❌ Auto-selection error: {e}"

def ask_chain(prompt: str, agents: List[str]) -> str:
    """Run multiple agents in sequence."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        results = []
        for agent_name in agents:
            result = ask(prompt, agent_name)
            results.append(f"[{agent_name}]: {result}")
        
        return "\n\n".join(results)
        
    except Exception as e:
        return f"❌ Chain execution error: {e}"

def get_agent_memory(agent_name: str) -> str:
    """Get memory for a specific agent."""
    if not fusion_memory:
        initialize_fusion()
    
    try:
        memory = fusion_memory(agent_name)
        context = memory.get_context()
        return context if context else "No memory found for this agent."
        
    except Exception as e:
        return f"❌ Memory error: {e}"

def get_telemetry() -> str:
    """Get current telemetry data."""
    if not fusion_telemetry:
        initialize_fusion()
    
    try:
        stats = fusion_telemetry.get_session_stats()
        return f"📊 Telemetry: {stats}"
        
    except Exception as e:
        return f"❌ Telemetry error: {e}"

# Auto-initialize when imported
initialize_fusion()
