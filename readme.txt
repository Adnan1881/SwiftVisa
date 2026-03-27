SwiftVisa-AI-Based-Visa-Eligibility-Screening-Agent-Batch13
Milestone 1: Visa Policy Knowledge Base Construction

Description

In this milestone, we build the knowledge base for the SwiftVisa project.
The knowledge base acts as the foundational data layer that stores all visa-related information in a structured and machine-understandable format.
The main objective of Milestone-1 is to convert visa rules into a searchable semantic database.
This enables the AI system to retrieve correct immigration policies when a user asks a question.

It requires:

 1.Clean and structured information

 2. Meaningful knowledge units

 3. Numerical representation of text

This milestone prepares visa data in a format suitable for AI retrieval systems such as RAG and chat assistants.

Steps Involved

1. Data Collection

Visa information is collected from official government immigration portals of different countries.

For each country, the following visa categories are considered:

Student
Tourist
Work
Family

2. Identify Required Information

For every country and visa category, the required details are extracted:

Eligibility fields
Required documents
Official source

3. Structured Storage (JSON)

All collected visa information is stored in a structured file:
visa_data.json

The dataset contains:

Country name
Visa type
Visa category
Eligibility fields
Required documents
Official source link

4. Text Conversion

Structured JSON data is converted into readable text so that AI models can understand it.

Example:

Country: Germany
Visa Type: Student Visa
Eligibility Fields: Passport, Admission Letter
Documents Required: Passport Copy, Blocked Account Proof

5. Semantic Chunking
The readable text is divided into smaller meaningful units called chunks.

In this project:
One visa policy = One chunk

Reason:
Each visa rule is independent
Improves retrieval accuracy
Avoids unnecessary context mixing

Chunk Size: One visa record
Overlap: 0

6. Embedding Generation

Each chunk is converted into a numerical vector using a sentence-transformer embedding model.

These vectors represent the semantic meaning of the text.

This allows the system to understand similar phrases such as:

financial proof ≈ bank balance
student visa ≈ study permit

7. Vector Database (FAISS)

All embeddings are stored inside a FAISS vector database.

FAISS enables:

Fast similarity search

Semantic retrieval

Natural language querying

FAISS stores vectors only, so original readable text is mapped using a metadata file.

Final Outcome

At the end of Milestone-1 we obtain:

A structured visa dataset

Semantic embeddings of visa policies

A FAISS vector knowledge base

This knowledge base will be used in Milestone-2 to:

Retrieve relevant visa policies

Provide context to the AI decision model (RAG pipeline)

Summary

Milestone-1 builds the semantic retrieval foundation of the SwiftVisa system by transforming visa rules into an AI-searchable knowledge base.