from __future__ import annotations

import argparse
import json
import sys

from delegation_lib import (
    DelegationError,
    build_messages,
    call_chat_completion,
    extract_output_text,
    load_providers,
    merged_env,
    new_task_record,
    read_prompt_text,
    resolve_provider,
    write_task,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Delegate a bounded task to a worker model.")
    parser.add_argument("--provider", required=True, choices=["minimax", "minimax-fast", "mimo"])
    parser.add_argument("--type", required=True, choices=["research", "summary", "risk-check"])
    parser.add_argument("--title", required=True)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-output-tokens", type=int, default=1200)
    parser.add_argument("--timeout", type=int, default=120)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        env = merged_env()
        providers = load_providers()
        provider = resolve_provider(args.provider, providers, env, require_key=not args.dry_run)
        prompt_text = read_prompt_text(args.prompt, args.prompt_file)
        messages = build_messages(args.type, prompt_text, args.source)
        record = new_task_record(provider, args.type, args.title, prompt_text, args.source)
        pending_path = write_task(record, "pending")

        if args.dry_run:
            print(f"Dry run task saved: {pending_path}")
            return 0

        response = call_chat_completion(provider, messages, args.max_output_tokens, args.timeout)
        record["worker_output"] = extract_output_text(response)
        record["raw_response"] = response
        completed_path = write_task(record, "completed")
        pending_path.unlink(missing_ok=True)
        print(f"Completed task saved: {completed_path}")
        return 0
    except DelegationError as exc:
        print(f"delegation error: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"json error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
