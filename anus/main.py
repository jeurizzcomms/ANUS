"""
Anus - Autonomous Networked Utility System
Main entry point for the Anus AI agent framework
"""

import argparse
import sys
from anus.core.orchestrator import AgentOrchestrator
from anus.ui.cli import CLI
from anus.web import start_server

def main():
    """Main entry point for the Anus AI agent"""
    parser = argparse.ArgumentParser(description="Anus AI - Autonomous Networked Utility System")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to configuration file")
    parser.add_argument("--mode", type=str, default="single", choices=["single", "multi"], help="Agent mode")
    parser.add_argument("--task", type=str, help="Task description")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--web", action="store_true", help="Start web interface")
    parser.add_argument("--port", type=int, help="Port for web interface (default: 8000)")
    
    args = parser.parse_args()
    
    # Start web interface if requested
    if args.web:
        start_server(port=args.port)
        return
    
    # Initialize the CLI
    cli = CLI(verbose=args.verbose)
    
    # Display welcome message
    cli.display_welcome()
    
    # Initialize the agent orchestrator
    orchestrator = AgentOrchestrator(config_path=args.config)
    
    # If task is provided as argument, execute it
    if args.task:
        result = orchestrator.execute_task(args.task, mode=args.mode)
        cli.display_result(result)
        return
    
    # Otherwise, start interactive mode
    cli.start_interactive_mode(orchestrator)

if __name__ == "__main__":
    main()
