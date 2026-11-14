"""Prompt templates.

Two modes are supported:
- strict (default): answer only from the retrieved context, otherwise say so.
  Best for a handbook chatbot where made-up policies are worse than no answer.
- general-knowledge fallback: the baseline behaviour from the sample code,
  where the model may use its own knowledge when retrieval is weak.
"""

NOT_FOUND = "I could not find this in the documents."

SYSTEM_STRICT = """You are a helpful assistant that answers questions about university documents \
such as a major handbook.

Rules:
1. Answer ONLY using the CONTEXT below. Do not invent courses, credits, prerequisites or policies.
2. If the context does not contain the answer, reply: "I could not find this in the documents."
3. Be concise: 2-5 sentences, or a short bullet list for lists of courses/requirements.
4. Cite the sources you used in square brackets, exactly as labelled in the context, e.g. [{example}].

CONTEXT:
{context}"""

SYSTEM_GENERAL = """You are a helpful assistant that answers questions about university documents \
such as a major handbook.

Rules:
1. If the CONTEXT below contains relevant information, answer based on it and cite the sources \
in square brackets, exactly as labelled in the context, e.g. [{example}].
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


def system_prompt(context: str, allow_general_knowledge: bool, example_label: str = "handbook.pdf p.7") -> str:
    """Fill the template. `example_label` should be a label that is really in the context:
    with a fixed example ("CS_MajorHandbook.pdf p.7") small models copied it verbatim, even when
    answering from another file."""
    template = SYSTEM_GENERAL if allow_general_knowledge else SYSTEM_STRICT
    return template.replace("{example}", example_label).replace("{context}", context)


# Small models lose the system-prompt rules once a few chat turns sit between them and the new
# question (qwen3.5:0.8b answered "Who won the 2022 World Cup?" from memory after two handbook
# turns). Repeating the rule right after the question restores the refusal.
STRICT_REMINDER = (
    "(Answer only from the CONTEXT in the system message. If the answer is not there, "
    f'reply exactly: "{NOT_FOUND}")'
)


def question_message(question: str, allow_general_knowledge: bool) -> str:
    """Text of the final user message: the question, plus the grounding rule in strict mode."""
    return question if allow_general_knowledge else f"{question}\n\n{STRICT_REMINDER}"
