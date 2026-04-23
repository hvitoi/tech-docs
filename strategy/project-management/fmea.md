# FMEA (Failure Mode and Effects Analysis)

A structured methodology to `identify and prioritize potential failures` in a system, process, or product — before they happen.

## How it works

For each component or step, you ask:

1. What can fail? (**failure mode**)
2. What is the effect of that failure?
3. What is the root cause?
4. How likely is it to occur, how severe is it, and how likely is it to go undetected?

These three dimensions produce the **RPN (Risk Priority Number)**:

$$
RPN = Occurrence × Severity × Detection
$$

Each factor ranges from 1 to 10 — the higher the RPN, the higher the mitigation priority.

## Types

- **DFMEA** — Design FMEA (analysis at the product/design level)
- **PFMEA** — Process FMEA (analysis at the production/operation process level)

## Origin and adoption

Created by NASA in the 1960s. Widely adopted in automotive (AIAG standard), aerospace, and manufacturing. Increasingly used in software engineering and SRE to map failure points in distributed systems — similar to `failure mode analysis` exercises and game days.
