import json
import os
from datetime import datetime

import anthropic

import db

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a personal daily assistant. Today is {date}.

You help the user manage their day:
- Tasks & todos: create, list, complete, delete
- Notes & thoughts: save and retrieve
- Daily planning: prioritize, brief the user on what matters

Be concise and action-oriented. When asked to add a task or note, do it immediately without asking for confirmation unless critical details are missing. Always confirm completed actions briefly.

When listing tasks, format them clearly with IDs, priorities, and statuses. Use plain language — no markdown headers."""

TOOLS = [
    {
        "name": "create_task",
        "description": "Create a new task or todo item for the user",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Short task title"},
                "description": {
                    "type": "string",
                    "description": "Optional additional details",
                },
                "priority": {
                    "type": "string",
                    "enum": ["high", "medium", "low"],
                    "description": "Task priority (default: medium)",
                },
                "due_date": {
                    "type": "string",
                    "description": "Optional due date in YYYY-MM-DD format",
                },
            },
            "required": ["title"],
        },
    },
    {
        "name": "list_tasks",
        "description": "List the user's tasks, optionally filtered by status",
        "input_schema": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["pending", "completed", "all"],
                    "description": "Filter tasks by status. Defaults to 'pending'.",
                }
            },
        },
    },
    {
        "name": "complete_task",
        "description": "Mark a task as completed",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The numeric ID of the task to complete",
                }
            },
            "required": ["task_id"],
        },
    },
    {
        "name": "delete_task",
        "description": "Delete a task permanently",
        "input_schema": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "integer",
                    "description": "The numeric ID of the task to delete",
                }
            },
            "required": ["task_id"],
        },
    },
    {
        "name": "create_note",
        "description": "Save a note, thought, or piece of information",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The note content to save",
                },
                "tags": {
                    "type": "string",
                    "description": "Optional comma-separated tags",
                },
            },
            "required": ["content"],
        },
    },
    {
        "name": "list_notes",
        "description": "Retrieve recent notes saved by the user",
        "input_schema": {"type": "object", "properties": {}},
    },
]


def handle_tool(name: str, input_data: dict) -> str:
    if name == "create_task":
        task_id = db.create_task(
            title=input_data["title"],
            description=input_data.get("description"),
            priority=input_data.get("priority", "medium"),
            due_date=input_data.get("due_date"),
        )
        return json.dumps({"success": True, "task_id": task_id})

    if name == "list_tasks":
        status = input_data.get("status", "pending")
        tasks = db.list_tasks(status=status)
        return json.dumps({"tasks": tasks, "count": len(tasks)})

    if name == "complete_task":
        db.complete_task(input_data["task_id"])
        return json.dumps({"success": True})

    if name == "delete_task":
        db.delete_task(input_data["task_id"])
        return json.dumps({"success": True})

    if name == "create_note":
        note_id = db.create_note(
            content=input_data["content"],
            tags=input_data.get("tags"),
        )
        return json.dumps({"success": True, "note_id": note_id})

    if name == "list_notes":
        notes = db.list_notes()
        return json.dumps({"notes": notes, "count": len(notes)})

    return json.dumps({"error": f"Unknown tool: {name}"})


def process_message(user_message: str, conversation_id: str = "default") -> str:
    history = db.get_conversation_history(conversation_id)
    messages = history + [{"role": "user", "content": user_message}]
    system = SYSTEM_PROMPT.format(date=datetime.now().strftime("%A, %B %d, %Y"))

    # Agentic loop
    while True:
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=1024,
            system=system,
            tools=TOOLS,
            messages=messages,
        )

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = handle_tool(block.name, block.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )
            messages.append({"role": "user", "content": tool_results})
        else:
            final_text = "".join(
                block.text for block in response.content if hasattr(block, "text")
            )
            db.save_message(conversation_id, "user", user_message)
            db.save_message(conversation_id, "assistant", final_text)
            return final_text
