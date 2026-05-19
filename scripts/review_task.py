from __future__ import annotations

import argparse
import sys

from delegation_lib import DelegationError, approve_task, reject_task


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review a completed delegated task.")
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--decision", required=True, choices=["approved", "rejected"])
    parser.add_argument("--reason", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.decision == "approved":
            path = approve_task(args.task_id, args.reason)
        else:
            path = reject_task(args.task_id, args.reason)
        print(f"Review saved: {path}")
        return 0
    except DelegationError as exc:
        print(f"review error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
