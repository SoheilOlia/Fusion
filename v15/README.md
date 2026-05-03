# Fusion v15 - AI Agentic Operating System

This project is now powered by **Fusion v15** - the most advanced AI agentic operating system with 32 specialized agents.

## 🚀 Quick Start

### In Cursor
```python
# Auto-loaded functions
ask("Design a mobile app", "vp_design")
ask_auto("Create a design system")
ask_chain("Evaluate this design", ["evaluator", "creative_director"])
```

### Manual Launch
```bash
# Start API server
python fusion_api.py

# Launch Web GUI
streamlit run web_app.py

# Use CLI
python fusion.py run vp_design "Design a mobile app"
```

## 🎯 32 Specialized Agents

### Core Design Agents
- `vp_design` - VP of Design leadership
- `creative_director` - Creative direction and vision
- `principal_designer` - Principal design architect

### AI & Interaction Agents
- `ai_native_ux_designer` - AI-native UX design
- `ai_interaction_designer` - AI-human interaction design

### Evaluation & Quality Agents
- `evaluator` - Quality assessment and critique
- `design_judgment_engine` - Design judgment analysis

### Product & Strategy Agents
- `vp_of_product` - Product strategy leadership
- `product_navigator` - Product navigation

### And 24+ more specialized agents...

## 🧠 Memory System
```python
# Get agent memory
get_agent_memory("vp_design")

# Get telemetry
get_telemetry()
```

## 📡 API Endpoints
- `GET /status` - System status
- `POST /run` - Run single agent
- `POST /run_parallel` - Run multiple agents
- `GET /agents` - List all agents

## 🎨 Web GUI
- Real-time dashboard
- Agent runner interface
- Telemetry explorer
- Memory browser

---

**Fusion v15** - Where AI agents work together seamlessly ✨
