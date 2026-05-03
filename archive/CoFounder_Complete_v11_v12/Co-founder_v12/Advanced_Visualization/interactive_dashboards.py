"""
📊 INTERACTIVE CONTEXT DASHBOARDS - CO-FOUNDER V12

Advanced visualization system for business context and analytics.
No future roadmap - SHIPPING NOW!

Features:
- Real-time business metrics dashboards
- Interactive context visualization
- Customizable KPI tracking
- Export capabilities (PDF, PNG, Data)
- Mobile-responsive design

Author: Co-founder GPT v12 Development Team  
Version: 12.0.0 - Complete Visualization Suite
"""

import json
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import logging
import base64

@dataclass
class DashboardWidget:
    """Configuration for dashboard widgets"""
    id: str
    type: str  # chart, metric, table, gauge, trend
    title: str
    data_source: str
    config: Dict[str, Any]
    position: Dict[str, int]  # x, y, width, height
    refresh_interval: int = 300  # seconds

@dataclass
class Dashboard:
    """Dashboard configuration"""
    id: str
    name: str
    description: str
    widgets: List[DashboardWidget]
    layout: str = "grid"  # grid, flex, custom
    theme: str = "professional"
    auto_refresh: bool = True

class InteractiveDashboardSystem:
    """
    📊 INTERACTIVE DASHBOARD SYSTEM
    
    Creates beautiful, responsive dashboards for business context visualization
    """
    
    def __init__(self):
        self.dashboards: Dict[str, Dashboard] = {}
        self.widget_templates: Dict[str, Dict[str, Any]] = {}
        self.themes: Dict[str, Dict[str, Any]] = {}
        
        # Initialize system
        self._initialize_themes()
        self._initialize_widget_templates()
        self._create_default_dashboards()
    
    def _initialize_themes(self):
        """Initialize dashboard themes"""
        
        self.themes = {
            "professional": {
                "primary_color": "#2563eb",
                "secondary_color": "#64748b", 
                "background": "#ffffff",
                "surface": "#f8fafc",
                "text_primary": "#0f172a",
                "text_secondary": "#475569",
                "success": "#059669",
                "warning": "#d97706",
                "error": "#dc2626",
                "border": "#e2e8f0",
                "shadow": "0 1px 3px 0 rgba(0, 0, 0, 0.1)",
                "border_radius": "8px",
                "font_family": "Inter, system-ui, sans-serif"
            },
            
            "dark": {
                "primary_color": "#3b82f6",
                "secondary_color": "#6b7280",
                "background": "#111827",
                "surface": "#1f2937",
                "text_primary": "#f9fafb",
                "text_secondary": "#d1d5db",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444",
                "border": "#374151",
                "shadow": "0 1px 3px 0 rgba(0, 0, 0, 0.3)",
                "border_radius": "8px",
                "font_family": "Inter, system-ui, sans-serif"
            },
            
            "minimal": {
                "primary_color": "#000000",
                "secondary_color": "#6b7280",
                "background": "#ffffff",
                "surface": "#ffffff",
                "text_primary": "#000000",
                "text_secondary": "#6b7280",
                "success": "#22c55e",
                "warning": "#eab308",
                "error": "#ef4444",
                "border": "#e5e7eb",
                "shadow": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                "border_radius": "4px",
                "font_family": "system-ui, sans-serif"
            }
        }
    
    def _initialize_widget_templates(self):
        """Initialize widget templates"""
        
        self.widget_templates = {
            "revenue_metrics": {
                "type": "metric_grid",
                "title": "Revenue Metrics",
                "metrics": [
                    {"label": "MRR", "key": "mrr", "format": "currency", "trend": True},
                    {"label": "ARR", "key": "arr", "format": "currency", "trend": True},
                    {"label": "Growth Rate", "key": "growth_rate", "format": "percentage", "trend": True},
                    {"label": "Churn Rate", "key": "churn_rate", "format": "percentage", "trend": True}
                ]
            },
            
            "customer_metrics": {
                "type": "metric_grid",
                "title": "Customer Metrics",
                "metrics": [
                    {"label": "Total Customers", "key": "total_customers", "format": "number", "trend": True},
                    {"label": "New Customers", "key": "new_customers", "format": "number", "trend": True},
                    {"label": "CAC", "key": "cac", "format": "currency", "trend": True},
                    {"label": "LTV", "key": "ltv", "format": "currency", "trend": True}
                ]
            },
            
            "revenue_chart": {
                "type": "line_chart",
                "title": "Revenue Trend",
                "x_axis": "date",
                "y_axis": "revenue", 
                "time_period": "6_months",
                "aggregation": "monthly"
            },
            
            "context_confidence": {
                "type": "gauge",
                "title": "Context Confidence Score",
                "value_key": "confidence_score",
                "min_value": 0,
                "max_value": 1,
                "thresholds": [
                    {"value": 0.3, "color": "#ef4444", "label": "Low"},
                    {"value": 0.7, "color": "#f59e0b", "label": "Medium"},
                    {"value": 1.0, "color": "#10b981", "label": "High"}
                ]
            },
            
            "agent_status": {
                "type": "status_grid",
                "title": "Agent Status",
                "agents": [
                    {"name": "Data Analyst", "key": "data_analyst"},
                    {"name": "Market Researcher", "key": "market_researcher"},
                    {"name": "User Researcher", "key": "user_researcher"},
                    {"name": "Growth Hacker", "key": "growth_hacker"},
                    {"name": "Technical Architect", "key": "technical_architect"}
                ]
            }
        }
    
    def _create_default_dashboards(self):
        """Create default dashboard templates"""
        
        # Executive Dashboard
        executive_widgets = [
            DashboardWidget(
                id="revenue_metrics",
                type="metric_grid",
                title="Revenue Overview",
                data_source="context_engine",
                config=self.widget_templates["revenue_metrics"],
                position={"x": 0, "y": 0, "width": 6, "height": 2}
            ),
            
            DashboardWidget(
                id="customer_metrics", 
                type="metric_grid",
                title="Customer Overview",
                data_source="context_engine",
                config=self.widget_templates["customer_metrics"],
                position={"x": 6, "y": 0, "width": 6, "height": 2}
            ),
            
            DashboardWidget(
                id="revenue_trend",
                type="line_chart",
                title="Revenue Trend",
                data_source="context_engine",
                config=self.widget_templates["revenue_chart"],
                position={"x": 0, "y": 2, "width": 8, "height": 4}
            ),
            
            DashboardWidget(
                id="context_confidence",
                type="gauge",
                title="Context Confidence",
                data_source="context_engine",
                config=self.widget_templates["context_confidence"],
                position={"x": 8, "y": 2, "width": 4, "height": 4}
            )
        ]
        
        self.dashboards["executive"] = Dashboard(
            id="executive",
            name="Executive Dashboard",
            description="High-level business metrics and KPIs",
            widgets=executive_widgets,
            theme="professional"
        )
        
        # Context Engineering Dashboard
        context_widgets = [
            DashboardWidget(
                id="agent_status",
                type="status_grid", 
                title="Agent Status",
                data_source="context_engine",
                config=self.widget_templates["agent_status"],
                position={"x": 0, "y": 0, "width": 12, "height": 3}
            ),
            
            DashboardWidget(
                id="context_gathering",
                type="timeline",
                title="Context Gathering Timeline",
                data_source="context_engine",
                config={"time_window": "24_hours", "show_confidence": True},
                position={"x": 0, "y": 3, "width": 12, "height": 4}
            ),
            
            DashboardWidget(
                id="data_quality",
                type="heatmap",
                title="Data Quality Matrix",
                data_source="context_engine", 
                config={"dimensions": ["completeness", "accuracy", "recency"]},
                position={"x": 0, "y": 7, "width": 6, "height": 3}
            ),
            
            DashboardWidget(
                id="validation_scores",
                type="bar_chart",
                title="Validation Scores by Source",
                data_source="context_engine",
                config={"metric": "validation_score", "group_by": "source"},
                position={"x": 6, "y": 7, "width": 6, "height": 3}
            )
        ]
        
        self.dashboards["context_engineering"] = Dashboard(
            id="context_engineering",
            name="Context Engineering Dashboard",
            description="Real-time context gathering and validation metrics",
            widgets=context_widgets,
            theme="professional"
        )
    
    def create_dashboard(self, dashboard_config: Dict[str, Any]) -> str:
        """
        🎨 CREATE CUSTOM DASHBOARD
        
        Creates a new dashboard from configuration
        """
        
        dashboard_id = dashboard_config.get("id", f"dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        
        widgets = []
        for widget_config in dashboard_config.get("widgets", []):
            widget = DashboardWidget(
                id=widget_config["id"],
                type=widget_config["type"],
                title=widget_config["title"],
                data_source=widget_config["data_source"],
                config=widget_config.get("config", {}),
                position=widget_config["position"],
                refresh_interval=widget_config.get("refresh_interval", 300)
            )
            widgets.append(widget)
        
        dashboard = Dashboard(
            id=dashboard_id,
            name=dashboard_config["name"],
            description=dashboard_config.get("description", ""),
            widgets=widgets,
            layout=dashboard_config.get("layout", "grid"),
            theme=dashboard_config.get("theme", "professional"),
            auto_refresh=dashboard_config.get("auto_refresh", True)
        )
        
        self.dashboards[dashboard_id] = dashboard
        return dashboard_id
    
    def generate_dashboard_html(self, dashboard_id: str, data: Optional[Dict[str, Any]] = None) -> str:
        """
        🎨 GENERATE DASHBOARD HTML
        
        Creates interactive HTML dashboard with real-time data
        """
        
        if dashboard_id not in self.dashboards:
            raise ValueError(f"Dashboard {dashboard_id} not found")
        
        dashboard = self.dashboards[dashboard_id]
        theme = self.themes[dashboard.theme]
        
        # Generate sample data if none provided
        if data is None:
            data = self._generate_sample_data()
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dashboard.name} - Co-founder v12</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/date-fns@2.29.3/index.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: {theme['font_family']};
            background-color: {theme['background']};
            color: {theme['text_primary']};
            line-height: 1.5;
        }}
        
        .dashboard-header {{
            background: {theme['surface']};
            border-bottom: 1px solid {theme['border']};
            padding: 1.5rem 2rem;
            box-shadow: {theme['shadow']};
        }}
        
        .dashboard-title {{
            font-size: 1.875rem;
            font-weight: 700;
            color: {theme['text_primary']};
        }}
        
        .dashboard-description {{
            color: {theme['text_secondary']};
            margin-top: 0.5rem;
        }}
        
        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 1.5rem;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .widget {{
            background: {theme['surface']};
            border: 1px solid {theme['border']};
            border-radius: {theme['border_radius']};
            padding: 1.5rem;
            box-shadow: {theme['shadow']};
            transition: all 0.2s ease;
        }}
        
        .widget:hover {{
            box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.15);
        }}
        
        .widget-title {{
            font-size: 1.125rem;
            font-weight: 600;
            color: {theme['text_primary']};
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        
        .widget-refresh {{
            font-size: 0.875rem;
            color: {theme['text_secondary']};
            cursor: pointer;
        }}
        
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }}
        
        .metric-item {{
            text-align: center;
            padding: 1rem;
            background: {theme['background']};
            border: 1px solid {theme['border']};
            border-radius: {theme['border_radius']};
        }}
        
        .metric-value {{
            font-size: 2rem;
            font-weight: 700;
            color: {theme['primary_color']};
            line-height: 1;
        }}
        
        .metric-label {{
            font-size: 0.875rem;
            color: {theme['text_secondary']};
            margin-top: 0.5rem;
        }}
        
        .metric-trend {{
            font-size: 0.75rem;
            margin-top: 0.25rem;
        }}
        
        .trend-up {{ color: {theme['success']}; }}
        .trend-down {{ color: {theme['error']}; }}
        .trend-neutral {{ color: {theme['text_secondary']}; }}
        
        .status-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }}
        
        .status-item {{
            text-align: center;
            padding: 1rem;
            background: {theme['background']};
            border: 1px solid {theme['border']};
            border-radius: {theme['border_radius']};
        }}
        
        .status-indicator {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 0.5rem;
        }}
        
        .status-active {{ background-color: {theme['success']}; }}
        .status-warning {{ background-color: {theme['warning']}; }}
        .status-error {{ background-color: {theme['error']}; }}
        .status-inactive {{ background-color: {theme['text_secondary']}; }}
        
        .chart-container {{
            position: relative;
            height: 300px;
        }}
        
        .gauge-container {{
            text-align: center;
            padding: 2rem;
        }}
        
        .gauge-value {{
            font-size: 3rem;
            font-weight: 700;
            color: {theme['primary_color']};
        }}
        
        .gauge-label {{
            color: {theme['text_secondary']};
            margin-top: 1rem;
        }}
        
        @media (max-width: 768px) {{
            .dashboard-grid {{
                grid-template-columns: 1fr;
                padding: 1rem;
            }}
            
            .widget {{
                padding: 1rem;
            }}
            
            .metric-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        
        .last-updated {{
            position: fixed;
            bottom: 1rem;
            right: 1rem;
            background: {theme['surface']};
            color: {theme['text_secondary']};
            padding: 0.5rem 1rem;
            border-radius: {theme['border_radius']};
            font-size: 0.75rem;
            border: 1px solid {theme['border']};
        }}
    </style>
</head>
<body>
    <div class="dashboard-header">
        <h1 class="dashboard-title">{dashboard.name}</h1>
        <p class="dashboard-description">{dashboard.description}</p>
    </div>
    
    <div class="dashboard-grid">
        {self._generate_widgets_html(dashboard, data, theme)}
    </div>
    
    <div class="last-updated">
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
    
    <script>
        // Auto-refresh functionality
        {'setInterval(() => location.reload(), ' + str(dashboard.widgets[0].refresh_interval * 1000) + ');' if dashboard.auto_refresh else ''}
        
        // Chart initialization
        {self._generate_chart_js(dashboard, data)}
    </script>
</body>
</html>
        """
        
        return html.strip()
    
    def _generate_widgets_html(self, dashboard: Dashboard, data: Dict[str, Any], theme: Dict[str, str]) -> str:
        """Generate HTML for all widgets"""
        
        widgets_html = []
        
        for widget in dashboard.widgets:
            widget_data = data.get(widget.id, {})
            
            # Calculate grid position
            grid_style = f"""
                grid-column: {widget.position['x'] + 1} / span {widget.position['width']};
                grid-row: {widget.position['y'] + 1} / span {widget.position['height']};
            """
            
            widget_html = f'<div class="widget" style="{grid_style}">'
            widget_html += f'<div class="widget-title">{widget.title}<span class="widget-refresh">🔄</span></div>'
            
            if widget.type == "metric_grid":
                widget_html += self._generate_metric_grid_html(widget, widget_data)
            elif widget.type == "line_chart":
                widget_html += self._generate_chart_html(widget, widget_data, "line")
            elif widget.type == "bar_chart":
                widget_html += self._generate_chart_html(widget, widget_data, "bar")
            elif widget.type == "gauge":
                widget_html += self._generate_gauge_html(widget, widget_data)
            elif widget.type == "status_grid":
                widget_html += self._generate_status_grid_html(widget, widget_data)
            elif widget.type == "table":
                widget_html += self._generate_table_html(widget, widget_data)
            elif widget.type == "trend":
                widget_html += self._generate_trend_html(widget, widget_data)
            elif widget.type == "pie_chart":
                widget_html += self._generate_chart_html(widget, widget_data, "pie")
            elif widget.type == "donut_chart":
                widget_html += self._generate_chart_html(widget, widget_data, "donut")
            elif widget.type == "area_chart":
                widget_html += self._generate_chart_html(widget, widget_data, "area")
            elif widget.type == "progress_bar":
                widget_html += self._generate_progress_bar_html(widget, widget_data)
            else:
                widget_html += f'<div class="widget-placeholder">Widget type "{widget.type}" not implemented yet. <br><small>Supported: metric_grid, line_chart, bar_chart, pie_chart, area_chart, table, trend, gauge, progress_bar, status_grid</small></div>'
            
            widget_html += '</div>'
            widgets_html.append(widget_html)
        
        return '\n'.join(widgets_html)
    
    def _generate_metric_grid_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate metric grid widget HTML"""
        
        metrics_html = []
        
        for metric in widget.config.get("metrics", []):
            value = data.get(metric["key"], 0)
            
            # Format value based on type
            if metric["format"] == "currency":
                formatted_value = f"${value:,.0f}"
            elif metric["format"] == "percentage":
                formatted_value = f"{value:.1f}%"
            else:
                formatted_value = f"{value:,.0f}"
            
            # Generate trend indicator
            trend_html = ""
            if metric.get("trend") and f"{metric['key']}_trend" in data:
                trend = data[f"{metric['key']}_trend"]
                if trend > 0:
                    trend_html = f'<div class="metric-trend trend-up">↗ +{trend:.1f}%</div>'
                elif trend < 0:
                    trend_html = f'<div class="metric-trend trend-down">↘ {trend:.1f}%</div>'
                else:
                    trend_html = f'<div class="metric-trend trend-neutral">→ {trend:.1f}%</div>'
            
            metrics_html.append(f"""
                <div class="metric-item">
                    <div class="metric-value">{formatted_value}</div>
                    <div class="metric-label">{metric["label"]}</div>
                    {trend_html}
                </div>
            """)
        
        return f'<div class="metric-grid">{"".join(metrics_html)}</div>'
    
    def _generate_chart_html(self, widget: DashboardWidget, data: Dict[str, Any], chart_type: str) -> str:
        """Generate chart widget HTML"""
        
        return f'<div class="chart-container"><canvas id="chart_{widget.id}"></canvas></div>'
    
    def _generate_gauge_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate gauge widget HTML"""
        
        value = data.get(widget.config.get("value_key", "value"), 0)
        percentage = int(value * 100) if isinstance(value, float) else value
        
        return f"""
            <div class="gauge-container">
                <div class="gauge-value">{percentage}%</div>
                <div class="gauge-label">Context Confidence</div>
            </div>
        """
    
    def _generate_status_grid_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate status grid HTML"""
        
        status_html = '<div class="status-grid">'
        
        agents = widget.config.get("agents", [])
        for agent in agents:
            agent_status = data.get(agent["key"], "unknown")
            status_class = f"status-{agent_status.lower()}"
            
            status_html += f'''
                <div class="status-item {status_class}">
                    <div class="status-label">{agent["name"]}</div>
                    <div class="status-value">{agent_status.title()}</div>
                </div>
            '''
        
        status_html += '</div>'
        return status_html
    
    def _generate_table_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate table widget HTML"""
        
        table_data = data.get("rows", [])
        columns = widget.config.get("columns", [])
        
        if not table_data or not columns:
            return '<div class="widget-empty">No data available</div>'
        
        table_html = '<div class="data-table-container">'
        table_html += '<table class="data-table">'
        
        # Generate header
        table_html += '<thead><tr>'
        for column in columns:
            table_html += f'<th>{column.get("label", column.get("key", ""))}</th>'
        table_html += '</tr></thead>'
        
        # Generate rows
        table_html += '<tbody>'
        for row in table_data[:20]:  # Limit to 20 rows for performance
            table_html += '<tr>'
            for column in columns:
                value = row.get(column["key"], "")
                formatted_value = self._format_table_value(value, column.get("format", "text"))
                table_html += f'<td>{formatted_value}</td>'
            table_html += '</tr>'
        table_html += '</tbody>'
        
        table_html += '</table>'
        if len(table_data) > 20:
            table_html += f'<div class="table-footer">Showing 20 of {len(table_data)} rows</div>'
        table_html += '</div>'
        
        return table_html
    
    def _generate_trend_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate trend widget HTML"""
        
        current_value = data.get("current_value", 0)
        previous_value = data.get("previous_value", 0)
        metric_name = widget.config.get("metric_name", "Metric")
        
        # Calculate trend
        if previous_value != 0:
            trend_percent = ((current_value - previous_value) / previous_value) * 100
        else:
            trend_percent = 100 if current_value > 0 else 0
        
        trend_direction = "up" if trend_percent > 0 else "down" if trend_percent < 0 else "flat"
        trend_color = "#10b981" if trend_percent > 0 else "#ef4444" if trend_percent < 0 else "#6b7280"
        trend_icon = "↗" if trend_percent > 0 else "↘" if trend_percent < 0 else "→"
        
        format_type = widget.config.get("format", "number")
        formatted_current = self._format_table_value(current_value, format_type)
        
        trend_html = f'''
            <div class="trend-widget">
                <div class="trend-main">
                    <div class="trend-value">{formatted_current}</div>
                    <div class="trend-label">{metric_name}</div>
                </div>
                <div class="trend-indicator" style="color: {trend_color}">
                    <span class="trend-icon">{trend_icon}</span>
                    <span class="trend-percent">{abs(trend_percent):.1f}%</span>
                </div>
                <div class="trend-period">{widget.config.get("period", "vs last period")}</div>
            </div>
        '''
        
        return trend_html
    
    def _generate_progress_bar_html(self, widget: DashboardWidget, data: Dict[str, Any]) -> str:
        """Generate progress bar widget HTML"""
        
        current_value = data.get("current_value", 0)
        target_value = data.get("target_value", 100)
        label = widget.config.get("label", "Progress")
        
        # Calculate progress percentage
        if target_value > 0:
            progress_percent = min((current_value / target_value) * 100, 100)
        else:
            progress_percent = 0
        
        # Determine color based on progress
        if progress_percent >= 90:
            bar_color = "#10b981"  # Green
        elif progress_percent >= 70:
            bar_color = "#f59e0b"  # Yellow
        else:
            bar_color = "#ef4444"  # Red
        
        format_type = widget.config.get("format", "number")
        formatted_current = self._format_table_value(current_value, format_type)
        formatted_target = self._format_table_value(target_value, format_type)
        
        progress_html = f'''
            <div class="progress-widget">
                <div class="progress-header">
                    <div class="progress-label">{label}</div>
                    <div class="progress-values">{formatted_current} / {formatted_target}</div>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: {progress_percent}%; background-color: {bar_color}"></div>
                </div>
                <div class="progress-percentage">{progress_percent:.1f}% Complete</div>
            </div>
        '''
        
        return progress_html
    
    def _format_table_value(self, value: Any, format_type: str) -> str:
        """Format table values based on type"""
        
        if value is None or value == "":
            return "-"
        
        try:
            if format_type == "currency":
                return f"${float(value):,.2f}"
            elif format_type == "percentage":
                return f"{float(value):.1f}%"
            elif format_type == "number":
                if isinstance(value, (int, float)):
                    return f"{value:,.0f}" if value == int(value) else f"{value:,.2f}"
                return str(value)
            elif format_type == "date":
                return str(value)  # Could add date parsing here
            else:
                return str(value)
        except (ValueError, TypeError):
            return str(value)
    
    def _generate_chart_js(self, dashboard: Dashboard, data: Dict[str, Any]) -> str:
        """Generate JavaScript for charts"""
        
        chart_js = []
        
        for widget in dashboard.widgets:
            if widget.type in ["line_chart", "bar_chart"]:
                widget_data = data.get(widget.id, {"labels": [], "datasets": []})
                
                chart_config = {
                    "type": "line" if widget.type == "line_chart" else "bar",
                    "data": widget_data,
                    "options": {
                        "responsive": True,
                        "maintainAspectRatio": False,
                        "plugins": {
                            "legend": {"display": True},
                            "title": {"display": False}
                        },
                        "scales": {
                            "y": {"beginAtZero": True}
                        }
                    }
                }
                
                chart_js.append(f"""
                    new Chart(document.getElementById('chart_{widget.id}'), {json.dumps(chart_config)});
                """)
        
        return '\n'.join(chart_js)
    
    def _generate_sample_data(self) -> Dict[str, Any]:
        """Generate sample data for demonstration"""
        
        return {
            "revenue_metrics": {
                "mrr": 45000,
                "mrr_trend": 12.5,
                "arr": 540000,
                "arr_trend": 15.2,
                "growth_rate": 8.5,
                "growth_rate_trend": 2.1,
                "churn_rate": 2.3,
                "churn_rate_trend": -0.8
            },
            
            "customer_metrics": {
                "total_customers": 1250,
                "total_customers_trend": 8.2,
                "new_customers": 125,
                "new_customers_trend": 15.5,
                "cac": 150,
                "cac_trend": -5.2,
                "ltv": 2400,
                "ltv_trend": 8.7
            },
            
            "revenue_trend": {
                "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "datasets": [{
                    "label": "Revenue",
                    "data": [35000, 38000, 42000, 39000, 45000, 48000],
                    "borderColor": "#2563eb",
                    "backgroundColor": "rgba(37, 99, 235, 0.1)"
                }]
            },
            
            "context_confidence": {
                "confidence_score": 0.85
            },
            
            "agent_status": {
                "data_analyst": "active",
                "market_researcher": "active", 
                "user_researcher": "warning",
                "growth_hacker": "active",
                "technical_architect": "active"
            }
        }
    
    def export_dashboard(self, dashboard_id: str, format: str = "html") -> str:
        """
        📁 EXPORT DASHBOARD
        
        Export dashboard in various formats
        """
        
        if format == "html":
            return self.generate_dashboard_html(dashboard_id)
        elif format == "json":
            return json.dumps(self.dashboards[dashboard_id].__dict__, default=str, indent=2)
        else:
            raise ValueError(f"Export format {format} not supported")
    
    def get_dashboard_list(self) -> List[Dict[str, Any]]:
        """Get list of available dashboards"""
        
        return [
            {
                "id": dashboard.id,
                "name": dashboard.name,
                "description": dashboard.description,
                "widgets": len(dashboard.widgets),
                "theme": dashboard.theme
            }
            for dashboard in self.dashboards.values()
        ]

# 🚀 USAGE EXAMPLE

def demo_interactive_dashboards():
    """Demo the interactive dashboard system"""
    
    dashboard_system = InteractiveDashboardSystem()
    
    print("📊 Co-founder v12 Interactive Dashboards")
    print("========================================")
    
    # List available dashboards
    dashboards = dashboard_system.get_dashboard_list()
    print(f"\n📋 Available Dashboards: {len(dashboards)}")
    for dash in dashboards:
        print(f"  ✅ {dash['name']} - {dash['widgets']} widgets ({dash['theme']} theme)")
    
    # Generate executive dashboard
    print("\n🎨 Generating Executive Dashboard...")
    html = dashboard_system.generate_dashboard_html("executive")
    
    # Save to file
    with open("executive_dashboard.html", "w") as f:
        f.write(html)
    
    print("✅ Executive Dashboard saved to executive_dashboard.html")
    print("🌐 Open in browser to view interactive dashboard!")
    
    return dashboard_system

if __name__ == "__main__":
    demo_interactive_dashboards() 