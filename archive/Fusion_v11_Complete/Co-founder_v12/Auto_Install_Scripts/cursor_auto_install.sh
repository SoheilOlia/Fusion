#!/bin/bash

# 🚀 CO-FOUNDER V12 AUTO-INSTALL FOR CURSOR
# 
# This script automatically installs Co-founder v12 across ALL Cursor projects
# (current and future) with context engineering capabilities.
#
# Usage: ./cursor_auto_install.sh
# 
# Author: Co-founder GPT v12 Development Team
# Version: 12.0.0 - Context Engineering Revolution

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
COFOUNDER_VERSION="12.0.0"
INSTALL_DIR="$HOME/.cursor/cofounder-v12"
GLOBAL_CONFIG_DIR="$HOME/.cursor/global-configs"
BACKUP_DIR="$HOME/.cursor/backups/cofounder-v12"

# Current directory (where this script is located)
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(dirname "$CURRENT_DIR")"  # Parent directory of Auto_Install_Scripts

echo -e "${BLUE}🚀 CO-FOUNDER V12 AUTO-INSTALL FOR CURSOR${NC}"
echo -e "${BLUE}====================================${NC}"
echo ""

# Function to print status
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on macOS or Linux
detect_os() {
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "linux"
    else
        echo "unknown"
    fi
}

# Create necessary directories
create_directories() {
    print_status "Creating installation directories..."
    
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$GLOBAL_CONFIG_DIR"
    mkdir -p "$BACKUP_DIR"
    
    print_status "✅ Directories created successfully"
}

# Backup existing installation
backup_existing() {
    if [ -d "$INSTALL_DIR" ]; then
        print_warning "Existing Co-founder installation found. Creating backup..."
        
        BACKUP_NAME="cofounder-v12-backup-$(date +%Y%m%d-%H%M%S)"
        cp -r "$INSTALL_DIR" "$BACKUP_DIR/$BACKUP_NAME"
        
        print_status "✅ Backup created at $BACKUP_DIR/$BACKUP_NAME"
    fi
}

# Copy Co-founder v12 files
install_cofounder_files() {
    print_status "Installing Co-founder v12 files..."
    
    # Copy all files from source directory
    cp -r "$SOURCE_DIR"/* "$INSTALL_DIR/"
    
    # Set proper permissions
    chmod +x "$INSTALL_DIR/Auto_Install_Scripts"/*.sh
    
    print_status "✅ Co-founder v12 files installed successfully"
}

# Create global Cursor configuration
create_global_config() {
    print_status "Creating global Cursor configuration..."
    
    # Create global settings file
    cat > "$GLOBAL_CONFIG_DIR/cofounder-v12-settings.json" << EOF
{
    "cofounder_version": "$COFOUNDER_VERSION",
    "install_path": "$INSTALL_DIR",
    "auto_load": true,
    "context_engineering": true,
    "global_access": true,
    "agents": {
        "data_analyst": true,
        "market_researcher": true,
        "user_researcher": true,
        "growth_hacker": true,
        "technical_architect": true
    },
    "features": {
        "context_orchestrator": true,
        "real_time_validation": true,
        "multi_agent_coordination": true,
        "continuous_learning": true
    },
    "installation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "auto_update": true
}
EOF
    
    print_status "✅ Global configuration created"
}

# Create Cursor workspace template
create_workspace_template() {
    print_status "Creating Cursor workspace template..."
    
    mkdir -p "$GLOBAL_CONFIG_DIR/workspace-templates"
    
    # Create workspace settings template
    cat > "$GLOBAL_CONFIG_DIR/workspace-templates/cofounder-v12-workspace.json" << EOF
{
    "name": "Co-founder v12 Workspace",
    "description": "Automatically configured workspace with Co-founder v12 context engineering",
    "settings": {
        "python.defaultInterpreterPath": "$(which python3)",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "editor.formatOnSave": true,
        "files.autoSave": "afterDelay",
        "cofounder.enabled": true,
        "cofounder.contextEngineering": true,
        "cofounder.autoAnalysis": true
    },
    "extensions": {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "ms-toolsai.jupyter"
        ]
    },
    "folders": [
        {
            "name": "Co-founder v12",
            "path": "$INSTALL_DIR"
        }
    ]
}
EOF
    
    print_status "✅ Workspace template created"
}

# Create auto-loader script
create_auto_loader() {
    print_status "Creating auto-loader for new projects..."
    
    # Create the auto-loader script
    cat > "$INSTALL_DIR/cursor_auto_loader.py" << 'EOF'
#!/usr/bin/env python3
"""
🚀 CO-FOUNDER V12 AUTO-LOADER

Automatically loads Co-founder v12 in new Cursor projects with context engineering.
"""

import os
import sys
import json
import shutil
from pathlib import Path

def setup_project_cofounder(project_path):
    """Setup Co-founder v12 in a new project"""
    
    # Create .cofounder directory in project
    cofounder_dir = Path(project_path) / ".cofounder"
    cofounder_dir.mkdir(exist_ok=True)
    
    # Create project-specific configuration
    config = {
        "version": "12.0.0",
        "project_path": str(project_path),
        "context_engineering": True,
        "auto_analysis": True,
        "global_install_path": os.path.expanduser("~/.cursor/cofounder-v12")
    }
    
    with open(cofounder_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    # Create project launcher script
    launcher_script = f"""#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser('~/.cursor/cofounder-v12'))

# Import Co-founder v12 modules
from Context_Engineering_Core.context_orchestrator_v12 import ContextOrchestrator
from Agents_v12.context_aware_agents_v12 import AgentOrchestrator

# Initialize Co-founder v12 for this project
print("🚀 Co-founder v12 Context Engineering - Ready!")
print("Project: {project_path}")
print("Context Engineering: ✅ Enabled")
print("Agents: ✅ Available")
"""
    
    with open(cofounder_dir / "launch_cofounder.py", "w") as f:
        f.write(launcher_script)
    
    # Make launcher executable
    os.chmod(cofounder_dir / "launch_cofounder.py", 0o755)
    
    print(f"✅ Co-founder v12 setup complete for {project_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        setup_project_cofounder(sys.argv[1])
    else:
        print("Usage: python cursor_auto_loader.py <project_path>")
EOF
    
    chmod +x "$INSTALL_DIR/cursor_auto_loader.py"
    
    print_status "✅ Auto-loader script created"
}

# Create global access script
create_global_access_script() {
    print_status "Creating global access script..."
    
    # Create global command script
    cat > "$INSTALL_DIR/cofounder" << EOF
#!/bin/bash
# 🚀 CO-FOUNDER V12 GLOBAL ACCESS SCRIPT

INSTALL_DIR="$INSTALL_DIR"

# Check if we're in a project directory
if [ -f ".cofounder/config.json" ]; then
    echo "🎯 Loading Co-founder v12 for current project..."
    python3 .cofounder/launch_cofounder.py
else
    echo "🚀 Co-founder v12 Context Engineering"
    echo "======================================"
    echo ""
    echo "Available commands:"
    echo "  cofounder init     - Initialize Co-founder in current project"
    echo "  cofounder analyze  - Run context analysis"
    echo "  cofounder agents   - List available agents"
    echo "  cofounder help     - Show help"
    echo ""
    
    case "\$1" in
        "init")
            python3 "\$INSTALL_DIR/cursor_auto_loader.py" "\$(pwd)"
            ;;
        "analyze")
            python3 "\$INSTALL_DIR/Context_Engineering_Core/context_orchestrator_v12.py"
            ;;
        "agents")
            python3 "\$INSTALL_DIR/Agents_v12/context_aware_agents_v12.py"
            ;;
        "help"|*)
            echo "For detailed help, visit: https://github.com/soheiloliaei/Cofounder_v12"
            ;;
    esac
fi
EOF
    
    chmod +x "$INSTALL_DIR/cofounder"
    
    print_status "✅ Global access script created"
}

# Add to PATH
add_to_path() {
    print_status "Adding Co-founder v12 to PATH..."
    
    # Determine shell configuration file
    if [ -f "$HOME/.zshrc" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -f "$HOME/.bashrc" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -f "$HOME/.bash_profile" ]; then
        SHELL_CONFIG="$HOME/.bash_profile"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    
    # Check if already in PATH
    if ! grep -q "cofounder-v12" "$SHELL_CONFIG" 2>/dev/null; then
        echo "" >> "$SHELL_CONFIG"
        echo "# Co-founder v12 Global Access" >> "$SHELL_CONFIG"
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$SHELL_CONFIG"
        echo "alias cofounder=\"$INSTALL_DIR/cofounder\"" >> "$SHELL_CONFIG"
        
        print_status "✅ Added to PATH in $SHELL_CONFIG"
        print_warning "Please run: source $SHELL_CONFIG"
    else
        print_status "✅ Already in PATH"
    fi
}

# Create uninstall script
create_uninstall_script() {
    print_status "Creating uninstall script..."
    
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/bin/bash
# 🗑️ CO-FOUNDER V12 UNINSTALLER

echo "🗑️ Uninstalling Co-founder v12..."

# Remove installation directory
rm -rf "$HOME/.cursor/cofounder-v12"

# Remove global configurations
rm -rf "$HOME/.cursor/global-configs"

# Remove from shell configuration
for config in "$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile"; do
    if [ -f "$config" ]; then
        sed -i.bak '/Co-founder v12 Global Access/,+2d' "$config"
    fi
done

echo "✅ Co-founder v12 uninstalled successfully"
echo "Please restart your terminal or run: source ~/.zshrc"
EOF
    
    chmod +x "$INSTALL_DIR/uninstall.sh"
    
    print_status "✅ Uninstall script created"
}

# Verify installation
verify_installation() {
    print_status "Verifying installation..."
    
    # Check if all required files exist
    required_files=(
        "$INSTALL_DIR/Context_Engineering_Core/context_orchestrator_v12.py"
        "$INSTALL_DIR/Agents_v12/context_aware_agents_v12.py"
        "$INSTALL_DIR/cofounder"
        "$INSTALL_DIR/cursor_auto_loader.py"
        "$GLOBAL_CONFIG_DIR/cofounder-v12-settings.json"
    )
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            print_error "Missing file: $file"
            exit 1
        fi
    done
    
    print_status "✅ All required files present"
    
    # Test Python imports
    if python3 -c "import sys; sys.path.insert(0, '$INSTALL_DIR'); from Context_Engineering_Core.context_orchestrator_v12 import ContextOrchestrator; print('✅ Context Orchestrator import successful')" 2>/dev/null; then
        print_status "✅ Python modules working correctly"
    else
        print_warning "Python modules may need dependency installation"
    fi
}

# Main installation function
main() {
    echo -e "${BLUE}Starting Co-founder v12 installation...${NC}"
    echo ""
    
    # Detect OS
    OS=$(detect_os)
    print_status "Detected OS: $OS"
    
    # Run installation steps
    create_directories
    backup_existing
    install_cofounder_files
    create_global_config
    create_workspace_template
    create_auto_loader
    create_global_access_script
    add_to_path
    create_uninstall_script
    verify_installation
    
    echo ""
    echo -e "${GREEN}🎉 CO-FOUNDER V12 INSTALLATION COMPLETE!${NC}"
    echo ""
    echo -e "${BLUE}🚀 Quick Start:${NC}"
    echo "1. Restart your terminal or run: source ~/.zshrc"
    echo "2. Navigate to any project directory"
    echo "3. Run: cofounder init"
    echo "4. Start using context engineering: cofounder analyze"
    echo ""
    echo -e "${BLUE}📚 Documentation:${NC}"
    echo "- Installation guide: $INSTALL_DIR/README.md"
    echo "- ChatGPT integration: $INSTALL_DIR/ChatGPT_Integration_v12/"
    echo "- Context engineering: $INSTALL_DIR/Context_Engineering_Core/"
    echo ""
    echo -e "${BLUE}🔧 Configuration:${NC}"
    echo "- Global settings: $GLOBAL_CONFIG_DIR/cofounder-v12-settings.json"
    echo "- Workspace templates: $GLOBAL_CONFIG_DIR/workspace-templates/"
    echo ""
    echo -e "${BLUE}🗑️ Uninstall:${NC}"
    echo "- Run: $INSTALL_DIR/uninstall.sh"
    echo ""
    echo -e "${GREEN}Welcome to the future of AI-powered business intelligence!${NC}"
}

# Run main installation
main "$@" 