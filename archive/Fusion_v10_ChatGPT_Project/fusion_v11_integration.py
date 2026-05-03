"""
🚀 Fusion v11 Integration for Cursor Projects

Easy-to-use interface for Fusion v11 in your Cursor project.
"""

import sys
import os
from pathlib import Path

# Add Fusion v11 to path
fusion_path = Path(__file__).parent / ".fusion-v11"
sys.path.insert(0, str(fusion_path))

try:
    from fusion_v11_complete_implementation import FusionV11System
    from execution_mode_manager import ExecutionModeManager
    from personality_perspective_overlay import PersonalityOverlay
    from creative_tension_pairing import CreativeTensionPairing
    from design_craft_metrics import DesignCraftMetrics
except ImportError as e:
    print(f"⚠️  Fusion v11 not properly installed: {e}")
    print("Run the deployment script again or check installation.")

class FusionV11:
    """Main interface for Fusion v11 in Cursor projects"""
    
    def __init__(self):
        """Initialize Fusion v11 system"""
        self.system = FusionV11System()
        self.execution_manager = ExecutionModeManager()
        self.personality_overlay = PersonalityOverlay()
        self.tension_pairing = CreativeTensionPairing()
        self.metrics = DesignCraftMetrics()
        
        print("🚀 Fusion v11 initialized for your Cursor project!")
        print("✅ 15 agents ready")
        print("✅ 10 personality overlays active")
        print("✅ 4 execution modes available")
    
    def process_challenge(self, challenge, mode="simulate", personality="jobs", 
                         tension="innovation_vs_practicality", agent=None):
        """
        Process a design challenge with Fusion v11
        
        Args:
            challenge (str): The design challenge to solve
            mode (str): Execution mode (simulate, ship, critique, advisory_board)
            personality (str): Personality overlay (jobs, bezos, musk, ive, nadella, etc.)
            tension (str): Creative tension to balance
            agent (str): Specific agent to use (optional)
        
        Returns:
            dict: Results with innovation score, design quality, recommendations
        """
        # Set execution mode
        self.execution_manager.set_mode(mode)
        
        # Apply personality overlay
        self.personality_overlay.apply_personality(personality)
        
        # Set creative tension
        self.tension_pairing.set_tension(tension)
        
        # Process with the system
        result = self.system.process_challenge(
            challenge=challenge,
            execution_mode=mode,
            personality=personality,
            tension=tension,
            specific_agent=agent
        )
        
        # Calculate metrics
        metrics = self.metrics.evaluate_result(result)
        
        return {
            "challenge": challenge,
            "mode": mode,
            "personality": personality,
            "tension": tension,
            "result": result,
            "metrics": metrics,
            "innovation_score": metrics.get("innovation_score", 0),
            "design_quality": metrics.get("design_quality", 0),
            "technical_feasibility": metrics.get("technical_feasibility", 0),
            "user_experience": metrics.get("user_experience", 0),
            "business_impact": metrics.get("business_impact", 0)
        }
    
    def process_complex_challenge(self, challenge, execution_mode="advisory_board",
                                 agents=None, personalities=None, tensions=None,
                                 frameworks=None):
        """
        Process complex challenges with multiple agents and perspectives
        
        Args:
            challenge (str): Complex design challenge
            execution_mode (str): How to execute (advisory_board recommended)
            agents (list): List of specific agents to involve
            personalities (list): Multiple personalities for diverse thinking
            tensions (list): Multiple creative tensions to balance
            frameworks (list): Strategic frameworks to apply
        
        Returns:
            dict: Comprehensive results from multi-agent processing
        """
        return self.system.process_complex_challenge(
            challenge=challenge,
            execution_mode=execution_mode,
            agents=agents or ["strategy", "design", "innovation"],
            personalities=personalities or ["jobs", "bezos"],
            tensions=tensions or ["innovation_vs_practicality"],
            frameworks=frameworks or ["first_principles"]
        )
    
    def get_agent_recommendations(self, project_type="general"):
        """Get recommended agents for your project type"""
        recommendations = {
            "saas_product": ["saas", "strategy", "design", "technical"],
            "mobile_app": ["mobile", "ux", "design", "strategy"],
            "healthcare": ["healthcare", "compliance", "ux", "strategy"],
            "fintech": ["fintech", "security", "compliance", "strategy"],
            "ecommerce": ["ecommerce", "conversion", "ux", "strategy"],
            "general": ["strategy", "design", "innovation", "technical"]
        }
        
        return recommendations.get(project_type, recommendations["general"])
    
    def list_available_options(self):
        """List all available options for easy reference"""
        return {
            "execution_modes": ["simulate", "ship", "critique", "advisory_board"],
            "personalities": [
                "jobs", "bezos", "musk", "ive", "nadella", 
                "cook", "chesky", "dorsey", "hastings", "benioff"
            ],
            "creative_tensions": [
                "innovation_vs_practicality",
                "simplicity_vs_functionality", 
                "speed_vs_quality",
                "features_vs_simplicity",
                "vision_vs_execution",
                "user_needs_vs_business_goals",
                "security_vs_convenience"
            ],
            "industry_agents": ["saas", "healthcare", "fintech", "ecommerce", "edtech"],
            "frameworks": [
                "first_principles", "jobs_to_be_done", "design_thinking",
                "lean_startup", "working_backwards", "blue_ocean"
            ]
        }

# Quick usage examples
if __name__ == "__main__":
    print("🚀 Fusion v11 Integration Examples")
    print("=" * 40)
    
    print("""
# Basic Usage
fusion = FusionV11()

# Simple challenge
result = fusion.process_challenge(
    challenge="Design a user onboarding flow",
    mode="simulate",
    personality="jobs"
)

# Complex challenge  
result = fusion.process_complex_challenge(
    challenge="Create a revolutionary fintech app",
    execution_mode="advisory_board",
    agents=["fintech", "strategy", "design"],
    personalities=["bezos", "musk"]
)

# Get recommendations
options = fusion.list_available_options()
agents = fusion.get_agent_recommendations("saas_product")
""")
