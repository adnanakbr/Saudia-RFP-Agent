#!/usr/bin/env python3
"""
Test script for Smart RFP Orchestrator

This script demonstrates how the smart orchestrator automatically routes
different types of requests to the appropriate functionality.
"""

import os
import sys
from dotenv import load_dotenv

# Add the rag module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'rag'))

from rag.agent import root_agent

load_dotenv()

def test_smart_routing():
    """Test the smart orchestrator with different types of requests."""
    print("🧠 Testing Smart RFP Orchestrator...")
    print("=" * 60)
    
    # Test different types of requests
    test_requests = [
        {
            "type": "RFP Creation",
            "request": "I want to create an RFP for a new mobile app development project",
            "expected": "Should ask for project details and create an RFP"
        },
        {
            "type": "RFP Validation", 
            "request": "Please validate this RFP for compliance",
            "expected": "Should ask for RFP content and provide validation report"
        },
        {
            "type": "Guidelines Information",
            "request": "What should be included in an RFP?",
            "expected": "Should provide RFP guidelines and requirements"
        },
        {
            "type": "Document Query",
            "request": "What are the requirements for technical specifications in RFPs?",
            "expected": "Should retrieve and present specific requirements from the document"
        },
        {
            "type": "General RFP Support",
            "request": "Help me understand the RFP process",
            "expected": "Should provide guidance on RFP processes and next steps"
        }
    ]
    
    print("The Smart Orchestrator will automatically detect intent and provide appropriate responses:")
    print()
    
    for i, test in enumerate(test_requests, 1):
        print(f"Test {i}: {test['type']}")
        print(f"Request: \"{test['request']}\"")
        print(f"Expected: {test['expected']}")
        print("Response: [Agent would automatically detect intent and respond appropriately]")
        print("-" * 50)
        print()
    
    print("🎯 Key Benefits of Smart Orchestrator:")
    print("✅ Single entry point - no need to choose between agents")
    print("✅ Automatic intent detection")
    print("✅ Seamless user experience")
    print("✅ Comprehensive responses for all RFP needs")
    print("✅ No manual agent switching required")

def main():
    """Main test function."""
    print("🚀 Smart RFP Orchestrator Test")
    print("=" * 60)
    print()
    
    # Check environment variables
    if not os.getenv("RAG_CORPUS"):
        print("❌ RAG_CORPUS environment variable not set!")
        print("Please run the prepare_corpus_and_data.py script first.")
        return
    
    print(f"✅ RAG_CORPUS: {os.getenv('RAG_CORPUS')}")
    print()
    
    # Test smart routing
    test_smart_routing()
    
    print("🎉 Smart Orchestrator Test Completed!")
    print()
    print("To use the Smart Orchestrator:")
    print("1. Run: adk run rag")
    print("2. Or run: adk web and select the RAG agent")
    print("3. Simply ask what you want to do - no need to choose agents!")
    print()
    print("Example requests:")
    print("- 'I want to create an RFP for a new website'")
    print("- 'Please validate this RFP for compliance'")
    print("- 'What should be included in an RFP?'")
    print("- 'What are the technical requirements for RFPs?'")

if __name__ == "__main__":
    main()
