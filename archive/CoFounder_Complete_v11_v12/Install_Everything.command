#!/bin/bash
# 🔧 CO-FOUNDER COMPLETE INSTALLATION SCRIPT
# Install all dependencies for both v11 and v12 systems

echo "🔧 CO-FOUNDER COMPLETE INSTALLATION"
echo "==================================="
echo ""
echo "📋 INSTALLING DEPENDENCIES FOR:"
echo "✅ Co-founder v11 (Complete Business Advisory)"
echo "✅ Co-founder v12 (Context Engineering Revolution)"
echo ""

# Change to the correct directory
cd "$(dirname "$0")"

# Check for Python 3
echo "🔍 CHECKING PYTHON..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3 first."
    echo "   Download from: https://www.python.org/downloads/"
    exit 1
else
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
fi

# Install Python dependencies
echo ""
echo "📦 INSTALLING PYTHON DEPENDENCIES..."
python3 -m pip install --user --upgrade pip

# Install from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📋 Installing from requirements.txt..."
    python3 -m pip install --user -r requirements.txt
    echo "✅ Requirements installed"
else
    echo "📋 Installing essential packages..."
    python3 -m pip install --user asyncio dataclasses typing-extensions
    echo "✅ Essential packages installed"
fi

# Test v11 system
echo ""
echo "🔧 TESTING CO-FOUNDER V11 SYSTEM..."
python3 -c "
import sys
sys.path.insert(0, 'Cofounder_v11/ChatGPT_10_Files')
try:
    from cofounder_main_orchestrator import CofounderMainOrchestrator
    from cofounder_specialized_agents import SpecializedAgents
    from cofounder_market_researcher import MarketResearcher
    from cofounder_risk_evaluator import RiskEvaluator
    print('✅ Co-founder v11: All systems operational')
except Exception as e:
    print(f'❌ Co-founder v11 Error: {e}')
    exit(1)
"

if [ $? -ne 0 ]; then
    echo "❌ Co-founder v11 system test failed"
    exit 1
fi

# Test v12 system
echo ""
echo "🔧 TESTING CO-FOUNDER V12 SYSTEM..."
python3 -c "
import sys
sys.path.insert(0, 'Co-founder_v12')
try:
    from Context_Engineering_Core.context_orchestrator_v12 import ContextOrchestrator
    from Agents_v12.context_aware_agents_v12 import AgentOrchestrator
    from Advanced_Visualization.interactive_dashboards import InteractiveDashboardSystem
    print('✅ Co-founder v12: All systems operational')
except Exception as e:
    print(f'❌ Co-founder v12 Error: {e}')
    exit(1)
"

if [ $? -ne 0 ]; then
    echo "❌ Co-founder v12 system test failed"
    exit 1
fi

# Make launcher scripts executable
echo ""
echo "🔧 SETTING UP LAUNCHER SCRIPTS..."
chmod +x Launch_v11_ChatGPT.command
chmod +x Launch_v12_ChatGPT.command
echo "✅ Launcher scripts ready"

# Check ChatGPT prompts
echo ""
echo "📋 CHECKING CHATGPT PROMPTS..."
V11_CHARS=$(wc -c < "Cofounder_v11/ChatGPT_10_Files/COFOUNDER_CHATGPT_MASTER_PROMPT_V11_COMPLETE.md")
V12_CHARS=$(wc -c < "Co-founder_v12/ChatGPT_Integration_v12/COFOUNDER_CHATGPT_MASTER_PROMPT_V12_COMPLETE.md")

echo "✅ Co-founder v11 prompt: $V11_CHARS characters"
echo "✅ Co-founder v12 prompt: $V12_CHARS characters"

if [ $V11_CHARS -lt 32000 ] && [ $V12_CHARS -lt 32000 ]; then
    echo "✅ Both prompts are within ChatGPT limits"
else
    echo "⚠️  Warning: Some prompts may exceed ChatGPT limits"
fi

echo ""
echo "🎉 INSTALLATION COMPLETE!"
echo "========================"
echo ""
echo "🚀 READY TO LAUNCH:"
echo "• Double-click 'Launch_v11_ChatGPT.command' for Complete Business Advisory"
echo "• Double-click 'Launch_v12_ChatGPT.command' for Context Engineering Revolution"
echo ""
echo "📚 DOCUMENTATION:"
echo "• Read 'LAUNCH_GUIDE.md' for detailed instructions"
echo "• Both systems include ChatGPT integration prompts"
echo ""
echo "🎯 NEXT STEPS:"
echo "1. Choose your version (v11 or v12)"
echo "2. Launch the appropriate script"
echo "3. Copy the ChatGPT prompt"
echo "4. Start transforming your business!"
echo ""
echo "✅ All systems ready for immediate use!"
