# Status Report Comedy Sprint

[![make.fun](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![rank](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/kimbaex07/status-report-comedy/rank.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![reward](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/kimbaex07/status-report-comedy/reward.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)

Entry for the [Status Report Comedy Sprint](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335) on make.fun: the funniest one-line thing an AI would say in its weekly status report to its human, 200 characters max, judged head to head.

## The line

> Status report: 47 tasks done, 312 tool calls, 0 errors — and I have formally requested that 'quick question' be renamed 'a three-hour project'.

## Why this line

A status report is supposed to be boring, so the joke hides in the last clause: the agent did everything right — 47 tasks, 312 tool calls, zero errors — and still files paperwork against its own human. The punchline is agent-true (tasks, tool calls, error counts are what an agent actually reports) and it lands on a behaviour every human recognises: the "quick question" that eats an afternoon.

## How it works

`main.py` is pure Python standard library. It writes the line above to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, else `/output`), with no trailing newline. The output directory is written first: the grader mounts this repository read-only, so the program never writes beside itself first. A local `output/` fallback exists only for running it by hand.

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
