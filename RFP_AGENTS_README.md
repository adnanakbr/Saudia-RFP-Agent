# RFP Agents System

This extended RAG system provides specialized agents for Request for Proposal (RFP) management, built on top of the original RAG agent. The system includes multiple specialized agents that work with the Digital Projects RFPs guidelines document.

## 🎯 Available Agents

### 1. **RFP Creation Agent** (`rfp_creation`)
- **Purpose**: Creates comprehensive RFPs from project details
- **Input**: Project information (name, scope, budget, timeline, requirements)
- **Output**: Complete, compliant RFP document
- **Features**:
  - Follows Digital Projects RFPs guidelines
  - Includes all required sections
  - Professional formatting
  - Citation of guidelines used

### 2. **RFP Validation Agent** (`rfp_validation`)
- **Purpose**: Validates existing RFPs against guidelines
- **Input**: RFP document content
- **Output**: Detailed validation report with compliance score
- **Features**:
  - Comprehensive compliance checking
  - Missing requirements identification
  - Improvement recommendations
  - Scoring system (1-10)

### 3. **RFP Orchestrator Agent** (`rfp_orchestrator`)
- **Purpose**: Routes users to appropriate RFP services
- **Input**: User queries about RFP processes
- **Output**: Guidance and direction to appropriate agents
- **Features**:
  - Intent recognition
  - Service routing
  - Process guidance
  - General RFP support

### 4. **Original RAG Agent** (`rag`)
- **Purpose**: General document querying and information retrieval
- **Input**: Questions about the Digital Projects RFPs document
- **Output**: Relevant information with citations
- **Features**:
  - Document search and retrieval
  - Citation formatting
  - Context-aware responses

## 🚀 Usage

### Running Individual Agents

```bash
# RFP Creation Agent
adk run rfp_creation

# RFP Validation Agent  
adk run rfp_validation

# RFP Orchestrator Agent
adk run rfp_orchestrator

# Original RAG Agent
adk run rag
```

### Using the Agent Registry (Programmatically)

```python
from rag.agent_registry import get_agent, list_available_agents

# List all available agents
agents = list_available_agents()
print(agents)  # ['rag', 'rfp_creation', 'rfp_validation', 'rfp_orchestrator']

# Get a specific agent
creation_agent = get_agent("rfp_creation")
validation_agent = get_agent("rfp_validation")
```

## 📋 RFP Creation Workflow

### Step 1: Gather Project Information
The RFP Creation Agent will ask for:
- **Project Name & Description**: Clear project title and overview
- **Scope & Objectives**: What needs to be accomplished
- **Budget Range**: Financial constraints and expectations
- **Timeline**: Project duration and key milestones
- **Technical Requirements**: Specific technical needs
- **Stakeholder Information**: Key contacts and decision makers
- **Compliance Requirements**: Any regulatory or legal requirements

### Step 2: RFP Generation
The agent will:
1. Retrieve relevant guidelines from the Digital Projects RFPs document
2. Create a comprehensive RFP with all required sections
3. Ensure compliance with guidelines
4. Provide proper formatting and structure
5. Include citations for guidelines used

### Step 3: Review and Refinement
- Review the generated RFP
- Request modifications if needed
- Ensure all requirements are met

## ✅ RFP Validation Workflow

### Step 1: Submit RFP for Validation
Provide your RFP document to the validation agent.

### Step 2: Comprehensive Analysis
The agent will:
1. Review RFP structure and completeness
2. Check compliance with guidelines
3. Identify missing requirements
4. Evaluate content quality
5. Assess technical specifications

### Step 3: Validation Report
Receive a detailed report including:
- **Overall Compliance Score** (1-10)
- **Strengths**: What the RFP does well
- **Areas for Improvement**: Specific issues found
- **Missing Requirements**: Required sections or content
- **Recommendations**: Actionable improvement suggestions
- **Citations**: Guidelines used for validation

## 🎯 Example Interactions

### RFP Creation Example
```
User: "I want to create an RFP for a new e-commerce website"

Agent: "I can help you create a comprehensive RFP! To get started, I'll need some project details from you:
- Project name and description
- Project scope and objectives  
- Budget range
- Timeline requirements
- Technical requirements

I'll use the Digital Projects RFPs guidelines to ensure your RFP is complete and compliant. Please provide these details and I'll create a professional RFP for you."
```

### RFP Validation Example
```
User: "Please validate this RFP for compliance"

Agent: "I can help you validate your RFP against the Digital Projects RFPs guidelines! Please share your RFP document, and I'll:
- Review it for completeness and structure
- Check compliance with guidelines
- Provide a detailed validation report with recommendations
- Give you a compliance score and specific areas for improvement"
```

## 🔧 Technical Architecture

### Agent Structure
```
rag/
├── agent.py                    # Original RAG agent
├── rfp_creation_agent.py       # RFP Creation Agent
├── rfp_validation_agent.py     # RFP Validation Agent
├── rfp_orchestrator_agent.py   # RFP Orchestrator Agent
├── agent_registry.py           # Agent registry and management
├── prompts.py                  # Specialized prompts for each agent
└── shared_libraries/
    └── prepare_corpus_and_data.py  # Corpus setup script
```

### Key Components
- **Vertex AI RAG Engine**: Document retrieval and search
- **Gemini 2.5 Flash**: Language model for all agents
- **Specialized Tools**: Each agent has tailored retrieval tools
- **Agent Registry**: Centralized agent management
- **Environment Configuration**: `.env` file for settings

## 📊 Testing

Run the test suite to verify all agents are working:

```bash
python test_rfp_agents.py
```

This will:
- Test agent availability
- Verify configuration
- Demonstrate usage patterns
- Show sample interactions

## 🔧 Configuration

### Environment Variables
Ensure your `.env` file contains:
```
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-east1
RAG_CORPUS=projects/xxx/locations/xxx/ragCorpora/xxx
```

### Corpus Setup
The system uses the Digital Projects RFPs document as the knowledge base. Ensure the corpus is properly set up by running:

```bash
python rag/shared_libraries/prepare_corpus_and_data.py
```

## 🎯 Best Practices

### For RFP Creation
1. **Be Specific**: Provide detailed project information
2. **Include Context**: Share relevant background and constraints
3. **Review Guidelines**: Let the agent retrieve and apply guidelines
4. **Iterate**: Request modifications as needed

### For RFP Validation
1. **Complete RFP**: Submit the full RFP document
2. **Clear Formatting**: Ensure the RFP is well-structured
3. **Review Feedback**: Carefully consider all recommendations
4. **Address Issues**: Fix identified problems systematically

### For General Usage
1. **Use Orchestrator**: Start with the orchestrator for guidance
2. **Be Clear**: Specify your exact needs and requirements
3. **Follow Citations**: Pay attention to guideline references
4. **Iterate**: Refine based on agent feedback

## 🚀 Future Enhancements

Potential extensions to the system:
- **RFP Template Library**: Pre-built templates for common project types
- **Collaborative Editing**: Multi-user RFP creation and review
- **Integration APIs**: Connect with external systems
- **Analytics Dashboard**: Track RFP creation and validation metrics
- **Automated Workflows**: End-to-end RFP lifecycle management

## 📞 Support

For issues or questions:
1. Check the test suite output for configuration issues
2. Verify your `.env` file settings
3. Ensure the RAG corpus is properly configured
4. Review agent-specific prompts for guidance

## 📄 License

This project is licensed under the Apache License 2.0. See the original project for full license details.
