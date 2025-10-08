#!/usr/bin/env python3
"""
Test script for RFP Agents

This script demonstrates how to use the different RFP agents:
- RFP Creation Agent
- RFP Validation Agent
- RFP Orchestrator Agent
"""

import os
import sys
from dotenv import load_dotenv

# Add the rag module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'rag'))

from rag.agent_registry import get_agent, list_available_agents, get_agent_descriptions

load_dotenv()

def test_agent_availability():
    """Test that all agents are available and properly configured."""
    print("🔍 Testing Agent Availability...")
    print("=" * 50)
    
    available_agents = list_available_agents()
    descriptions = get_agent_descriptions()
    
    for agent_name in available_agents:
        try:
            agent = get_agent(agent_name)
            print(f"✅ {agent_name}: {descriptions[agent_name]}")
            print(f"   Model: {agent.model}")
            print(f"   Tools: {len(agent.tools)} tool(s)")
            print()
        except Exception as e:
            print(f"❌ {agent_name}: Error - {e}")
            print()

def test_rfp_orchestrator():
    """Test the RFP Orchestrator Agent with sample queries."""
    print("🎯 Testing RFP Orchestrator Agent...")
    print("=" * 50)
    
    try:
        orchestrator = get_agent("rfp_orchestrator")
        
        # Test queries
        test_queries = [
            "I want to create an RFP for a new e-commerce website",
            "Please validate this RFP for compliance",
            "What should be included in an RFP?",
            "Help me understand RFP guidelines"
        ]
        
        for query in test_queries:
            print(f"Query: {query}")
            print("Response: [Agent would respond here in actual usage]")
            print("-" * 30)
            
    except Exception as e:
        print(f"❌ Error testing orchestrator: {e}")

def test_rfp_creation():
    """Test the RFP Creation Agent with sample project details."""
    print("📝 Testing RFP Creation Agent...")
    print("=" * 50)
    
    try:
        creation_agent = get_agent("rfp_creation")
        
        # Sample project details
        project_details = {
            "name": "Digital Transformation Project",
            "description": "Modernize legacy systems and implement cloud-based solutions",
            "budget": "$500,000 - $750,000",
            "timeline": "6-9 months",
            "requirements": ["Cloud migration", "API development", "Security compliance"]
        }
        
        print("Sample Project Details:")
        for key, value in project_details.items():
            print(f"  {key}: {value}")
        print()
        print("Response: [Agent would create RFP here in actual usage]")
        
    except Exception as e:
        print(f"❌ Error testing creation agent: {e}")

def test_rfp_validation():
    """Test the RFP Validation Agent with sample RFP content."""
    print("✅ Testing RFP Validation Agent...")
    print("=" * 50)
    
    try:
        validation_agent = get_agent("rfp_validation")
        
        # Sample RFP content
        sample_rfp = """
        REQUEST FOR PROPOSAL
        Digital Transformation Project
        
        1. Project Overview
        We are seeking proposals for a digital transformation project.
        
        2. Scope of Work
        - Cloud migration
        - API development
        - Security implementation
        
        3. Timeline
        6 months
        
        4. Budget
        $500,000
        """
        
        print("Sample RFP Content:")
        print(sample_rfp)
        print("Response: [Agent would validate RFP here in actual usage]")
        
    except Exception as e:
        print(f"❌ Error testing validation agent: {e}")

def main():
    """Main test function."""
    print("🚀 RFP Agents Test Suite")
    print("=" * 60)
    print()
    
    # Check environment variables
    if not os.getenv("RAG_CORPUS"):
        print("❌ RAG_CORPUS environment variable not set!")
        print("Please run the prepare_corpus_and_data.py script first.")
        return
    
    print(f"✅ RAG_CORPUS: {os.getenv('RAG_CORPUS')}")
    print()
    
    # Run tests
    test_agent_availability()
    test_rfp_orchestrator()
    test_rfp_creation()
    test_rfp_validation()
    
    print("🎉 Test suite completed!")
    print()
    print("To use these agents in practice:")
    print("1. Use 'adk run rag' for the original RAG agent")
    print("2. Use 'adk run rfp_creation' for RFP creation")
    print("3. Use 'adk run rfp_validation' for RFP validation")
    print("4. Use 'adk run rfp_orchestrator' for general RFP guidance")

if __name__ == "__main__":
    main()
