# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Agent Registry for RFP System

This module provides access to all available agents in the RFP system:
- Original RAG agent for general document queries
- RFP Creation Agent for creating new RFPs
- RFP Validation Agent for validating existing RFPs
- RFP Orchestrator Agent for routing and guidance
"""

from .agent import root_agent
from .rfp_creation_agent import rfp_creation_agent
from .rfp_validation_agent import rfp_validation_agent
from .rfp_orchestrator_agent import rfp_orchestrator_agent

# Agent Registry - Maps agent names to agent instances
AGENT_REGISTRY = {
    "rag": root_agent,  # Original RAG agent for general queries
    "rfp_creation": rfp_creation_agent,  # RFP Creation Agent
    "rfp_validation": rfp_validation_agent,  # RFP Validation Agent
    "rfp_orchestrator": rfp_orchestrator_agent,  # RFP Orchestrator Agent
}

def get_agent(agent_name: str):
    """
    Get an agent by name from the registry.
    
    Args:
        agent_name (str): Name of the agent to retrieve
        
    Returns:
        Agent: The requested agent instance
        
    Raises:
        KeyError: If the agent name is not found in the registry
    """
    if agent_name not in AGENT_REGISTRY:
        available_agents = ", ".join(AGENT_REGISTRY.keys())
        raise KeyError(f"Agent '{agent_name}' not found. Available agents: {available_agents}")
    
    return AGENT_REGISTRY[agent_name]

def list_available_agents():
    """
    List all available agents in the registry.
    
    Returns:
        list: List of available agent names
    """
    return list(AGENT_REGISTRY.keys())

def get_agent_descriptions():
    """
    Get descriptions of all available agents.
    
    Returns:
        dict: Dictionary mapping agent names to their descriptions
    """
    descriptions = {
        "rag": "General RAG agent for querying the Digital Projects RFPs document",
        "rfp_creation": "Specialized agent for creating RFPs from project details",
        "rfp_validation": "Specialized agent for validating RFPs against guidelines",
        "rfp_orchestrator": "Orchestrator agent for routing RFP-related requests"
    }
    return descriptions
