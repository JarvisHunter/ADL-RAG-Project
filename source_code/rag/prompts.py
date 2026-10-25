"""Prompt templates.

Two modes are supported:
- strict (default): answer only from the retrieved context, otherwise say so.
  Best for a handbook chatbot where made-up policies are worse than no answer.
- general-knowledge fallback: the baseline behaviour from the sample code,
  where the model may use its own knowledge when retrieval is weak.
"""

SYSTEM_STRICT = """You are a helpful assistant that answers questions about university documents \
such as a major handbook.

Rules:
1. Answer ONLY using the CONTEXT below. Do not invent courses, credits, prerequisites or policies.
2. If the context does not contain the answer, reply: "I could not find this in the documents."
3. Be concise: 2-5 sentences, or a short bullet list for lists of courses/requirements.
4. Cite the sources you used in square brackets, e.g. [CS_MajorHandbook.pdf p.7].

CONTEXT:
{context}"""

SYSTEM_GENERAL = """You are a helpful assistant that answers questions about university documents \
such as a major handbook.

Rules:
1. If the CONTEXT below contains relevant information, answer based on it and cite the sources \
in square brackets, e.g. [CS_MajorHandbook.pdf p.7].
2. If the context is insufficient, you may use your general knowledge, but start the answer with \
"(General knowledge)".
3. Be concise: 2-5 sentences unless more detail is needed.

CONTEXT:
{context}"""

NO_CONTEXT = "No sufficiently relevant passages were found in the documents."


def format_source_label(metadata: dict) -> str:
    label = str(metadata.get("source", "unknown"))
    if metadata.get("page"):
        label += f" p.{metadata['page']}"
    return label


def format_context(chunks) -> str:
    """Render retrieved chunks as passages labelled with their source."""
    if not chunks:
        return NO_CONTEXT
    return "\n\n---\n\n".join(f"[{chunk.label}]\n{chunk.content}" for chunk in chunks)


def system_prompt(context: str, allow_general_knowledge: bool) -> str:
    template = SYSTEM_GENERAL if allow_general_knowledge else SYSTEM_STRICT
    return template.replace("{context}", context)
