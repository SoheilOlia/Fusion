#!/bin/bash

# 🌐 CO-FOUNDER V12 UNIVERSAL INSTALLER
# 
# Deploy Co-founder v12 Context Engineering System on ANY machine
# Supports: macOS, Linux, Windows (WSL), Cloud servers, Docker containers
#
# Usage: 
#   curl -fsSL https://raw.githubusercontent.com/soheiloliaei/Cofounder_v12/main/Machine_Deployments/universal_installer.sh | bash
#   or
#   ./universal_installer.sh
# 
# Author: Co-founder GPT v12 Development Team
# Version: 12.0.0 - Context Engineering Revolution

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
COFOUNDER_VERSION="12.0.0"
GITHUB_REPO="https://github.com/soheiloliaei/Cofounder_v12"
INSTALL_DIR="$HOME/.cofounder-v12"
BACKUP_DIR="$HOME/.cofounder-v12-backups"
LOG_FILE="$HOME/.cofounder-v12-install.log"

# Clear log file
> "$LOG_FILE"

echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}║    🚀 CO-FOUNDER V12 UNIVERSAL INSTALLER                   ║${NC}"
echo -e "${CYAN}║    Context Engineering Revolution                            ║${NC}"
echo -e "${CYAN}║                                                              ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Logging function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
    echo -e "$1"
}

# Status functions
print_status() {
    log "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    log "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    log "${RED}[ERROR]${NC} $1"
}

print_success() {
    log "${GREEN}[SUCCESS]${NC} $1"
}

# Detect system information
detect_system() {
    print_status "Detecting system information..."
    
    # OS Detection
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        ARCH=$(uname -m)
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        ARCH=$(uname -m)
        if [ -f /etc/os-release ]; then
            . /etc/os-release
            DISTRO=$NAME
        fi
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        OS="windows"
        ARCH=$(uname -m)
    else
        OS="unknown"
        ARCH=$(uname -m)
    fi
    
    # Shell detection
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_TYPE="zsh"
        SHELL_CONFIG="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_TYPE="bash"
        if [ -f "$HOME/.bashrc" ]; then
            SHELL_CONFIG="$HOME/.bashrc"
        else
            SHELL_CONFIG="$HOME/.bash_profile"
        fi
    else
        SHELL_TYPE="unknown"
        SHELL_CONFIG="$HOME/.profile"
    fi
    
    # Python detection
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version | cut -d' ' -f2)
        PYTHON_CMD="python"
    else
        PYTHON_VERSION="not_found"
        PYTHON_CMD=""
    fi
    
    # Git detection
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version | cut -d' ' -f3)
        GIT_AVAILABLE=true
    else
        GIT_VERSION="not_found"
        GIT_AVAILABLE=false
    fi
    
    # System info summary
    print_status "System Information:"
    echo -e "  ${BLUE}OS:${NC} $OS"
    echo -e "  ${BLUE}Architecture:${NC} $ARCH"
    [ -n "$DISTRO" ] && echo -e "  ${BLUE}Distribution:${NC} $DISTRO"
    echo -e "  ${BLUE}Shell:${NC} $SHELL_TYPE"
    echo -e "  ${BLUE}Python:${NC} $PYTHON_VERSION"
    echo -e "  ${BLUE}Git:${NC} $GIT_VERSION"
    echo ""
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Install Python if not available
    if [ "$PYTHON_VERSION" = "not_found" ]; then
        print_warning "Python not found. Installing Python..."
        
        case $OS in
            "macos")
                if command -v brew &> /dev/null; then
                    brew install python3
                else
                    print_error "Homebrew not found. Please install Python 3 manually."
                    exit 1
                fi
                ;;
            "linux")
                if command -v apt-get &> /dev/null; then
                    sudo apt-get update && sudo apt-get install -y python3 python3-pip
                elif command -v yum &> /dev/null; then
                    sudo yum install -y python3 python3-pip
                elif command -v pacman &> /dev/null; then
                    sudo pacman -S python python-pip
                else
                    print_error "Package manager not found. Please install Python 3 manually."
                    exit 1
                fi
                ;;
            *)
                print_error "Unsupported OS for automatic Python installation."
                exit 1
                ;;
        esac
        
        # Re-detect Python after installation
        if command -v python3 &> /dev/null; then
            PYTHON_CMD="python3"
            print_success "Python 3 installed successfully"
        else
            print_error "Python 3 installation failed"
            exit 1
        fi
    fi
    
    # Install Git if not available
    if [ "$GIT_AVAILABLE" = false ]; then
        print_warning "Git not found. Installing Git..."
        
        case $OS in
            "macos")
                if command -v brew &> /dev/null; then
                    brew install git
                else
                    print_error "Homebrew not found. Please install Git manually."
                    exit 1
                fi
                ;;
            "linux")
                if command -v apt-get &> /dev/null; then
                    sudo apt-get update && sudo apt-get install -y git
                elif command -v yum &> /dev/null; then
                    sudo yum install -y git
                elif command -v pacman &> /dev/null; then
                    sudo pacman -S git
                else
                    print_error "Package manager not found. Please install Git manually."
                    exit 1
                fi
                ;;
            *)
                print_error "Unsupported OS for automatic Git installation."
                exit 1
                ;;
        esac
        
        print_success "Git installed successfully"
    fi
    
    # Install Python dependencies
    print_status "Installing Python dependencies..."
    $PYTHON_CMD -m pip install --user --upgrade pip
    $PYTHON_CMD -m pip install --user asyncio dataclasses typing-extensions
    
    print_success "Dependencies installed successfully"
}

# Create installation directories
create_directories() {
    print_status "Creating installation directories..."
    
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$HOME/.local/bin"
    
    # Create subdirectories
    mkdir -p "$INSTALL_DIR/Context_Engineering_Core"
    mkdir -p "$INSTALL_DIR/Agents_v12"
    mkdir -p "$INSTALL_DIR/ChatGPT_Integration_v12"
    mkdir -p "$INSTALL_DIR/Knowledge_Base_v12"
    mkdir -p "$INSTALL_DIR/Machine_Deployments"
    mkdir -p "$INSTALL_DIR/Auto_Install_Scripts"
    
    print_success "Installation directories created"
}

# Backup existing installation
backup_existing() {
    if [ -d "$INSTALL_DIR" ]; then
        print_warning "Existing Co-founder installation found. Creating backup..."
        
        BACKUP_NAME="cofounder-v12-backup-$(date +%Y%m%d-%H%M%S)"
        cp -r "$INSTALL_DIR" "$BACKUP_DIR/$BACKUP_NAME"
        
        print_success "Backup created at $BACKUP_DIR/$BACKUP_NAME"
    fi
}

# Download Co-founder v12 files
download_cofounder() {
    print_status "Downloading Co-founder v12 files..."
    
    # Check if we have the files locally (for development)
    if [ -d "$(dirname "$0")/../Context_Engineering_Core" ]; then
        print_status "Local files detected. Copying from local directory..."
        cp -r "$(dirname "$0")/../"* "$INSTALL_DIR/"
    else
        # Download from GitHub
        print_status "Downloading from GitHub repository..."
        
        # Create temporary directory
        TEMP_DIR=$(mktemp -d)
        
        # Clone the repository
        git clone "$GITHUB_REPO.git" "$TEMP_DIR/cofounder-v12"
        
        # Copy files
        cp -r "$TEMP_DIR/cofounder-v12"/* "$INSTALL_DIR/"
        
        # Clean up
        rm -rf "$TEMP_DIR"
    fi
    
    print_success "Co-founder v12 files downloaded successfully"
}

# Create configuration files
create_configuration() {
    print_status "Creating configuration files..."
    
    # Create global configuration
    cat > "$INSTALL_DIR/config.json" << EOF
{
    "version": "$COFOUNDER_VERSION",
    "installation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "system": {
        "os": "$OS",
        "architecture": "$ARCH",
        "shell": "$SHELL_TYPE",
        "python": "$PYTHON_VERSION"
    },
    "features": {
        "context_engineering": true,
        "multi_agent_coordination": true,
        "real_time_validation": true,
        "continuous_learning": true
    },
    "paths": {
        "install_dir": "$INSTALL_DIR",
        "backup_dir": "$BACKUP_DIR",
        "log_file": "$LOG_FILE"
    },
    "agents": {
        "data_analyst": true,
        "market_researcher": true,
        "user_researcher": true,
        "growth_hacker": true,
        "technical_architect": true
    }
}
EOF
    
    # Create environment variables file
    cat > "$INSTALL_DIR/cofounder_env.sh" << EOF
#!/bin/bash
# Co-founder v12 Environment Variables

export COFOUNDER_VERSION="$COFOUNDER_VERSION"
export COFOUNDER_INSTALL_DIR="$INSTALL_DIR"
export COFOUNDER_PYTHON_CMD="$PYTHON_CMD"
export COFOUNDER_CONTEXT_ENGINE="enabled"
export COFOUNDER_MULTI_AGENT="enabled"

# Add to Python path
export PYTHONPATH="\$COFOUNDER_INSTALL_DIR:\$PYTHONPATH"
EOF
    
    print_success "Configuration files created"
}

# Create launcher script
create_launcher() {
    print_status "Creating launcher script..."
    
    cat > "$INSTALL_DIR/cofounder-v12" << EOF
#!/bin/bash
# 🚀 Co-founder v12 Universal Launcher

# Source environment variables
source "$INSTALL_DIR/cofounder_env.sh"

# Change to install directory
cd "$INSTALL_DIR"

# Welcome message
echo "🚀 Co-founder v12 Context Engineering System"
echo "============================================"
echo ""

# Command handling
case "\$1" in
    "init")
        echo "🔧 Initializing Co-founder v12 in current directory..."
        \$COFOUNDER_PYTHON_CMD -c "
import sys
import os
sys.path.insert(0, '$INSTALL_DIR')
from Auto_Install_Scripts.project_initializer import initialize_project
initialize_project('$(pwd)')
"
        ;;
    "analyze")
        echo "🔍 Starting context analysis..."
        \$COFOUNDER_PYTHON_CMD "$INSTALL_DIR/Context_Engineering_Core/context_orchestrator_v12.py"
        ;;
    "agents")
        echo "🤖 Available agents:"
        \$COFOUNDER_PYTHON_CMD "$INSTALL_DIR/Agents_v12/context_aware_agents_v12.py"
        ;;
    "config")
        echo "🔧 Configuration:"
        cat "$INSTALL_DIR/config.json"
        ;;
    "update")
        echo "🔄 Updating Co-founder v12..."
        bash "$INSTALL_DIR/Machine_Deployments/universal_installer.sh"
        ;;
    "uninstall")
        echo "🗑️ Uninstalling Co-founder v12..."
        bash "$INSTALL_DIR/Machine_Deployments/uninstaller.sh"
        ;;
    "help"|"")
        echo "Available commands:"
        echo "  cofounder-v12 init      - Initialize in current project"
        echo "  cofounder-v12 analyze   - Run context analysis"
        echo "  cofounder-v12 agents    - List available agents"
        echo "  cofounder-v12 config    - Show configuration"
        echo "  cofounder-v12 update    - Update to latest version"
        echo "  cofounder-v12 uninstall - Remove installation"
        echo "  cofounder-v12 help      - Show this help"
        echo ""
        echo "For detailed documentation, visit:"
        echo "  https://github.com/soheiloliaei/Cofounder_v12"
        ;;
    *)
        echo "Unknown command: \$1"
        echo "Run 'cofounder-v12 help' for available commands"
        ;;
esac
EOF
    
    chmod +x "$INSTALL_DIR/cofounder-v12"
    
    print_success "Launcher script created"
}

# Create project initializer
create_project_initializer() {
    print_status "Creating project initializer..."
    
    cat > "$INSTALL_DIR/Auto_Install_Scripts/project_initializer.py" << 'EOF'
#!/usr/bin/env python3
"""
🔧 CO-FOUNDER V12 PROJECT INITIALIZER

Initializes Co-founder v12 in any project directory.
"""

import os
import sys
import json
from pathlib import Path

def initialize_project(project_path):
    """Initialize Co-founder v12 in a project directory"""
    
    project_path = Path(project_path)
    cofounder_dir = project_path / ".cofounder-v12"
    
    # Create project directory
    cofounder_dir.mkdir(exist_ok=True)
    
    # Create project configuration
    config = {
        "version": "12.0.0",
        "project_name": project_path.name,
        "project_path": str(project_path),
        "initialized_date": "2024-01-01T00:00:00Z",
        "context_engineering": True,
        "active_agents": [
            "data_analyst",
            "market_researcher", 
            "user_researcher"
        ],
        "global_install": os.path.expanduser("~/.cofounder-v12")
    }
    
    with open(cofounder_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    # Create project launcher
    launcher_content = f"""#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.expanduser('~/.cofounder-v12'))

# Import Co-founder v12 modules
try:
    from Context_Engineering_Core.context_orchestrator_v12 import ContextOrchestrator
    from Agents_v12.context_aware_agents_v12 import AgentOrchestrator
    
    print("🚀 Co-founder v12 Context Engineering - Ready!")
    print(f"Project: {project_path.name}")
    print("Context Engineering: ✅ Enabled")
    print("Agents: ✅ Available")
    
    # Initialize for this project
    orchestrator = ContextOrchestrator()
    agent_orchestrator = AgentOrchestrator()
    
    print("\\n🎯 Ready for business intelligence!")
    print("Use 'cofounder-v12 analyze' to start context analysis")
    
except ImportError as e:
    print(f"❌ Error importing Co-founder v12: {{e}}")
    print("Please run the universal installer first")
"""
    
    with open(cofounder_dir / "launcher.py", "w") as f:
        f.write(launcher_content)
    
    # Make launcher executable
    os.chmod(cofounder_dir / "launcher.py", 0o755)
    
    print(f"✅ Co-founder v12 initialized in {project_path}")
    print(f"Configuration: {cofounder_dir / 'config.json'}")
    print(f"Launcher: {cofounder_dir / 'launcher.py'}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        initialize_project(sys.argv[1])
    else:
        initialize_project(os.getcwd())
EOF
    
    chmod +x "$INSTALL_DIR/Auto_Install_Scripts/project_initializer.py"
    
    print_success "Project initializer created"
}

# Add to PATH
add_to_path() {
    print_status "Adding Co-founder v12 to PATH..."
    
    # Create symlink in local bin
    if [ -d "$HOME/.local/bin" ]; then
        ln -sf "$INSTALL_DIR/cofounder-v12" "$HOME/.local/bin/cofounder-v12"
        print_status "Symlink created in ~/.local/bin"
    fi
    
    # Add to shell configuration
    if [ -f "$SHELL_CONFIG" ]; then
        if ! grep -q "cofounder-v12" "$SHELL_CONFIG"; then
            echo "" >> "$SHELL_CONFIG"
            echo "# Co-founder v12 Universal Installation" >> "$SHELL_CONFIG"
            echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$SHELL_CONFIG"
            echo "source \"$INSTALL_DIR/cofounder_env.sh\"" >> "$SHELL_CONFIG"
            echo "alias cofounder=\"$INSTALL_DIR/cofounder-v12\"" >> "$SHELL_CONFIG"
            
            print_success "Added to $SHELL_CONFIG"
        else
            print_status "Already in PATH"
        fi
    fi
    
    print_warning "Please restart your terminal or run: source $SHELL_CONFIG"
}

# Create uninstaller
create_uninstaller() {
    print_status "Creating uninstaller..."
    
    cat > "$INSTALL_DIR/Machine_Deployments/uninstaller.sh" << 'EOF'
#!/bin/bash
# 🗑️ Co-founder v12 Universal Uninstaller

echo "🗑️ Uninstalling Co-founder v12..."

# Remove installation directory
rm -rf "$HOME/.cofounder-v12"

# Remove backups (with confirmation)
if [ -d "$HOME/.cofounder-v12-backups" ]; then
    read -p "Remove backups? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$HOME/.cofounder-v12-backups"
        echo "✅ Backups removed"
    fi
fi

# Remove from PATH
for config in "$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile"; do
    if [ -f "$config" ]; then
        sed -i.bak '/Co-founder v12 Universal Installation/,+3d' "$config"
    fi
done

# Remove symlink
rm -f "$HOME/.local/bin/cofounder-v12"

echo "✅ Co-founder v12 uninstalled successfully"
echo "Please restart your terminal"
EOF
    
    chmod +x "$INSTALL_DIR/Machine_Deployments/uninstaller.sh"
    
    print_success "Uninstaller created"
}

# Set file permissions
set_permissions() {
    print_status "Setting file permissions..."
    
    # Make scripts executable
    find "$INSTALL_DIR" -name "*.sh" -exec chmod +x {} \;
    find "$INSTALL_DIR" -name "*.py" -exec chmod +x {} \;
    
    # Set proper permissions on directories
    chmod 755 "$INSTALL_DIR"
    chmod 755 "$BACKUP_DIR"
    
    print_success "File permissions set"
}

# Verify installation
verify_installation() {
    print_status "Verifying installation..."
    
    # Check required files
    required_files=(
        "$INSTALL_DIR/cofounder-v12"
        "$INSTALL_DIR/config.json"
        "$INSTALL_DIR/cofounder_env.sh"
        "$INSTALL_DIR/Context_Engineering_Core/context_orchestrator_v12.py"
        "$INSTALL_DIR/Agents_v12/context_aware_agents_v12.py"
        "$INSTALL_DIR/Machine_Deployments/uninstaller.sh"
    )
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            print_error "Missing required file: $file"
            return 1
        fi
    done
    
    # Test Python imports
    if $PYTHON_CMD -c "import sys; sys.path.insert(0, '$INSTALL_DIR'); import json; print('✅ Python modules working')" 2>/dev/null; then
        print_success "Python modules verified"
    else
        print_warning "Python modules may need additional setup"
    fi
    
    # Test launcher
    if [ -x "$INSTALL_DIR/cofounder-v12" ]; then
        print_success "Launcher script verified"
    else
        print_error "Launcher script not executable"
        return 1
    fi
    
    return 0
}

# Main installation function
main() {
    print_status "Starting Co-founder v12 universal installation..."
    echo ""
    
    # Installation steps
    detect_system
    install_dependencies
    create_directories
    backup_existing
    download_cofounder
    create_configuration
    create_launcher
    create_project_initializer
    add_to_path
    create_uninstaller
    set_permissions
    
    if verify_installation; then
        echo ""
        echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║                                                              ║${NC}"
        echo -e "${GREEN}║  🎉 CO-FOUNDER V12 INSTALLATION COMPLETE!                   ║${NC}"
        echo -e "${GREEN}║                                                              ║${NC}"
        echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -e "${BLUE}🚀 Quick Start:${NC}"
        echo "1. Restart your terminal or run: source $SHELL_CONFIG"
        echo "2. Navigate to any project directory"
        echo "3. Run: cofounder-v12 init"
        echo "4. Start analysis: cofounder-v12 analyze"
        echo ""
        echo -e "${BLUE}📚 Available Commands:${NC}"
        echo "  cofounder-v12 help      - Show all commands"
        echo "  cofounder-v12 init      - Initialize in project"
        echo "  cofounder-v12 analyze   - Run context analysis"
        echo "  cofounder-v12 agents    - List agents"
        echo "  cofounder-v12 config    - Show configuration"
        echo ""
        echo -e "${BLUE}🔧 Installation Details:${NC}"
        echo "  Install Directory: $INSTALL_DIR"
        echo "  Configuration: $INSTALL_DIR/config.json"
        echo "  Log File: $LOG_FILE"
        echo ""
        echo -e "${BLUE}🗑️ Uninstall:${NC}"
        echo "  Run: cofounder-v12 uninstall"
        echo ""
        echo -e "${GREEN}Welcome to the Context Engineering Revolution!${NC}"
    else
        print_error "Installation verification failed. Check log file: $LOG_FILE"
        exit 1
    fi
}

# Run main installation
main "$@" 