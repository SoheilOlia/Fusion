#!/usr/bin/env python3
"""
Fusion v15 Fallback Web Interface
Simple web interface when streamlit is not available
"""

import http.server
import socketserver
import json
import os
import socket
from pathlib import Path

# HTML template for the Fusion dashboard
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fusion v15 - AI Agentic Operating System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }
        .card:hover {
            transform: translateY(-4px);
        }
        .card h3 {
            color: #667eea;
            margin-bottom: 16px;
            font-size: 1.4rem;
        }
        .agent-list {
            list-style: none;
            margin-top: 16px;
        }
        .agent-list li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .agent-list li:last-child {
            border-bottom: none;
        }
        .status {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        .status.online { background: #d4edda; color: #155724; }
        .status.offline { background: #f8d7da; color: #721c24; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }
        .stat {
            background: white;
            border-radius: 8px;
            padding: 16px;
            text-align: center;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            margin-top: 4px;
        }
        .run-agent {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .run-agent h3 {
            color: #667eea;
            margin-bottom: 16px;
        }
        .form-group {
            margin-bottom: 16px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }
        .form-group input, .form-group select, .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #eee;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.2s ease;
        }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .result {
            margin-top: 20px;
            padding: 16px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧠 Fusion v15</h1>
            <p>AI Agentic Operating System</p>
        </div>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number">32</div>
                <div class="stat-label">Specialized Agents</div>
            </div>
            <div class="stat">
                <div class="stat-number">∞</div>
                <div class="stat-label">Memory System</div>
            </div>
            <div class="stat">
                <div class="stat-number">⚡</div>
                <div class="stat-label">Real-time Telemetry</div>
            </div>
        </div>
        
        <div class="dashboard">
            <div class="card">
                <h3>🎯 Core Design Agents</h3>
                <ul class="agent-list">
                    <li><span>vp_design</span><span class="status online">Online</span></li>
                    <li><span>creative_director</span><span class="status online">Online</span></li>
                    <li><span>principal_designer</span><span class="status online">Online</span></li>
                </ul>
            </div>
            
            <div class="card">
                <h3>🤖 AI & Interaction Agents</h3>
                <ul class="agent-list">
                    <li><span>ai_native_ux_designer</span><span class="status online">Online</span></li>
                    <li><span>ai_interaction_designer</span><span class="status online">Online</span></li>
                    <li><span>evaluator</span><span class="status online">Online</span></li>
                </ul>
            </div>
            
            <div class="card">
                <h3>📊 Product & Strategy Agents</h3>
                <ul class="agent-list">
                    <li><span>vp_of_product</span><span class="status online">Online</span></li>
                    <li><span>product_navigator</span><span class="status online">Online</span></li>
                    <li><span>strategy_pilot</span><span class="status online">Online</span></li>
                </ul>
            </div>
        </div>
        
        <div class="run-agent">
            <h3>🚀 Run Agent</h3>
            <form id="agentForm">
                <div class="form-group">
                    <label for="agent">Select Agent:</label>
                    <select id="agent" name="agent">
                        <option value="vp_design">VP Design</option>
                        <option value="creative_director">Creative Director</option>
                        <option value="principal_designer">Principal Designer</option>
                        <option value="ai_native_ux_designer">AI Native UX Designer</option>
                        <option value="ai_interaction_designer">AI Interaction Designer</option>
                        <option value="evaluator">Evaluator</option>
                        <option value="vp_of_product">VP of Product</option>
                        <option value="product_navigator">Product Navigator</option>
                        <option value="strategy_pilot">Strategy Pilot</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="prompt">Prompt:</label>
                    <textarea id="prompt" name="prompt" rows="4" placeholder="Enter your prompt here..."></textarea>
                </div>
                
                <button type="submit" class="btn">🚀 Run Agent</button>
            </form>
            
            <div id="result" class="result" style="display: none;"></div>
        </div>
    </div>
    
    <script>
        document.getElementById('agentForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const agent = document.getElementById('agent').value;
            const prompt = document.getElementById('prompt').value;
            const resultDiv = document.getElementById('result');
            
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = `
                <h4>🤖 Running ${agent}...</h4>
                <p><strong>Prompt:</strong> ${prompt}</p>
                <p><em>Agent is processing your request...</em></p>
            `;
            
            // Simulate agent response (in real implementation, this would call the API)
            setTimeout(() => {
                resultDiv.innerHTML = `
                    <h4>✅ ${agent} Response</h4>
                    <p><strong>Prompt:</strong> ${prompt}</p>
                    <p><strong>Response:</strong> This is a simulated response from the ${agent} agent. In the full Fusion v15 system, this would be the actual agent output with real AI processing and memory integration.</p>
                `;
            }, 2000);
        });
    </script>
</body>
</html>
'''

class FusionHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode())
        else:
            super().do_GET()

def find_free_port(start_port=8080):
    """Find a free port starting from start_port."""
    for port in range(start_port, start_port + 10):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return start_port

if __name__ == "__main__":
    PORT = find_free_port(8080)
    
    try:
        with socketserver.TCPServer(("", PORT), FusionHandler) as httpd:
            print(f"🌐 Fusion v15 Fallback Web Interface running on http://localhost:{PORT}")
            print("🎯 Open your browser to see the Fusion dashboard")
            httpd.serve_forever()
    except OSError as e:
        print(f"❌ Failed to start web server: {e}")
        print("💡 Try running the launcher again or check if another process is using the port")
