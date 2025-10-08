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

import os
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag
from dotenv import load_dotenv
from .prompts import return_instructions_rfp_validation

load_dotenv()

# RFP Validation Agent - Validates RFPs against guidelines
rfp_validation_retrieval = VertexAiRagRetrieval(
    name='retrieve_rfp_validation_guidelines',
    description=(
        'Use this tool to retrieve RFP validation guidelines and requirements from the Digital Projects RFPs document. '
        'This helps validate if the provided RFP meets all necessary requirements and follows proper guidelines.'
    ),
    rag_resources=[
        rag.RagResource(
            rag_corpus=os.environ.get("RAG_CORPUS")
        )
    ],
    similarity_top_k=15,
    vector_distance_threshold=0.5,
)

rfp_validation_agent = Agent(
    model='gemini-2.5-flash',
    name='rfp_validation_agent',
    instruction=return_instructions_rfp_validation(),
    tools=[
        rfp_validation_retrieval,
    ]
)
