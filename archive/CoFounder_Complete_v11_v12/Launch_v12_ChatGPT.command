#!/bin/bash
# 🚀 CO-FOUNDER V12 CHATGPT LAUNCHER
# Launch Co-founder v12 Context Engineering System

echo "🚀 CO-FOUNDER V12 - CONTEXT ENGINEERING REVOLUTION"
echo "=================================================="
echo ""
echo "📋 SYSTEM STATUS:"
echo "✅ Context Engineering Framework"
echo "✅ Multi-Agent Intelligence Coordination"
echo "✅ Real-time Validation & Adaptation"
echo "✅ Evidence-based Strategy Generation"
echo "✅ Continuous Learning System"
echo ""

# Change to the correct directory
cd "$(dirname "$0")"

# Test Python availability
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3 first."
    exit 1
fi

# Test system components
echo "🔧 VALIDATING SYSTEM COMPONENTS:"
python3 -c "
import sys
sys.path.insert(0, 'Co-founder_v12')
try:
    from Context_Engineering_Core.context_orchestrator_v12 import ContextOrchestrator
    print('✅ Context Orchestrator: Ready')
    
    from Agents_v12.context_aware_agents_v12 import AgentOrchestrator
    print('✅ Agent Orchestrator: Ready')
    
    from Advanced_Visualization.interactive_dashboards import InteractiveDashboardSystem
    print('✅ Dashboard System: Ready')
    
    print('\\n�� CO-FOUNDER V12 CONTEXT ENGINEERING OPERATIONAL!')
except Exception as e:
    print(f'❌ System Error: {e}')
    exit(1)
"

if [ $? -eq 0 ]; then
    echo ""
    echo "📖 CHATGPT INTEGRATION READY:"
    echo "1. Copy the prompt from: Co-founder_v12/ChatGPT_Integration_v12/COFOUNDER_CHATGPT_MASTER_PROMPT_V12_COMPLETE.md"
    echo "2. Paste into ChatGPT as system prompt"
    echo "3. Start with any business challenge"
    echo ""
    echo "🎯 CONTEXT ENGINEERING FEATURES:"
    echo "• Dynamic context gathering before advice"
    echo "• Multi-agent specialist coordination"
    echo "• Evidence-based recommendations"
    echo "• Real-time validation framework"
    echo "• Continuous learning and adaptation"
    echo ""
    echo "🚀 Ready for Context Engineering Revolution!"
    
    # Open the ChatGPT prompt file
    if command -v open &> /dev/null; then
        open "Co-founder_v12/ChatGPT_Integration_v12/COFOUNDER_CHATGPT_MASTER_PROMPT_V12_COMPLETE.md"
    fi
else
    echo "❌ System validation failed. Please check the installation."
    exit 1
fi
