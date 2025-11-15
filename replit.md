# Application Modernization Dashboard

## Overview

This is a Streamlit-based dashboard application for visualizing and reporting on an Application Modernization project. The dashboard tracks the migration and transformation of 349 applications across two phases (Phase 1: 2568-2570 and Phase 2: 2570-2571). It provides interactive visualizations and metrics for different modernization strategies including Rehost, Replatform, Repurchase, Retain, Retire, Re-architect, and Refactor.

The application uses Thai language for content and descriptions, targeting a Thai-speaking audience for enterprise application modernization planning and tracking.

**Recent Update (November 2025):**
- Redesigned with modern card-based UI layout
- Implemented pastel color scheme with colored left borders on category cards
- Enhanced visual hierarchy with custom CSS styling
- Improved data presentation with clearer typography
- All pages now feature consistent design language

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack:**
- **Streamlit** - Primary web framework for building the interactive dashboard
- **Plotly** - Visualization library for creating interactive charts and graphs
- **Pandas** - Data manipulation and analysis

**Structure:**
- Multi-page application using Streamlit's native page routing
- Main entry point (`app.py`) provides overview and project summary
- Separate page modules under `/pages` directory for each phase:
  - `1_📈_Phase_1_(2568-2570).py` - Phase 1 detailed view
  - `2_📊_Phase_2_(2570-2571).py` - Phase 2 detailed view

**Design Decisions:**
- **Wide layout mode** - Chosen to maximize screen real estate for data visualization
- **Card-based layout** - Custom CSS-styled cards with colored left borders for visual distinction
- **Pastel color palette** - Soft, professional colors for each category (blues, greens, purples, pinks)
- **Multi-column layouts** - Leverages Streamlit's column system for responsive dashboard design
- **Custom CSS styling** - Inline HTML/CSS for modern, polished UI with shadows and gradients
- **Typography hierarchy** - Clear visual hierarchy with varying font sizes and weights

### Data Management

**Approach:**
- **In-memory data structures** - Uses Python dictionaries converted to Pandas DataFrames
- **Static data** - Currently hardcoded within each page module
- **No database** - Data is embedded in the application code

**Rationale:**
- Simplifies deployment and reduces infrastructure requirements
- Appropriate for relatively static reporting data
- Quick prototyping and iteration

**Future Considerations:**
- Could be migrated to external data sources (CSV, Excel, or database) for easier updates
- Database integration would enable historical tracking and user input

### Application Categories

The system tracks six modernization strategies:

1. **Rehost** - Lift and shift migration (keeping existing architecture)
2. **Replatform** - Lift and reshape (platform changes with minimal code changes)
3. **Repurchase** - Replace with SaaS or commercial solutions
4. **Re-architect** - Significant architectural redesign
5. **Refactor** - Code-level improvements and optimization
6. **Retain** - Keep as-is (Phase 1 only)
7. **Retire** - Decommission applications

### Page Structure

**Main Dashboard (`app.py`):**
- Project overview with gradient info card showing total application count (349 apps)
- Two phase summary cards with colored borders
- Phase timeline information
- Category definitions and explanations
- Modern, centered layout with clean typography

**Phase Pages:**
- Card-based category display with icons, subtitles, and descriptions
- Each card features: category name, count, percentage, and Thai description
- Colored left borders (pastel colors) for visual category identification
- Interactive pie charts and bar charts with matching color schemes
- Data tables for detailed information
- Phase-specific statistics and summaries

## External Dependencies

### Python Packages

**Core Dependencies:**
- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive visualization library

**Purpose of Each:**
- **Streamlit**: Provides the web interface, routing, and UI components without requiring HTML/CSS/JavaScript knowledge
- **Pandas**: Handles data transformation and tabular data structures for easy manipulation
- **Plotly**: Creates interactive graphs and charts (likely used for pie charts, bar charts showing category distributions)

### Configuration

- **Page configuration** set via `st.set_page_config()`:
  - Custom page titles and icons for each page
  - Wide layout mode for better data presentation
  - Emoji icons for visual navigation

### No External Services

This application currently operates as a standalone Streamlit app with:
- No database connections
- No external APIs
- No authentication/authorization system
- No third-party service integrations

The application is suitable for internal reporting and can be deployed on Streamlit Cloud, Replit, or any Python-capable hosting platform.