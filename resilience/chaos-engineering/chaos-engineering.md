# Chaos Engineering

> Break something on purpose to validate your assumptions/hypotheses!

- Resilience testing = **Chaos testing**
- Improve resilience and performance
- Uncover hidden issues
- Expose blind spots

## Phases

1. `Nothing`
1. `Learning`
1. `Rehearse`
1. `Experimentation`
    - Inject failure
    - Failure mode analysis: Define hypothesis
    - Validate the assertions
1. `Validation tests`
    - Assert the hypotheses
1. `Continuous fault injection`
    - Experiment in a loop

## Game Days

- It's a kind of chaos testing, but focused people components (operational procedures)
  - Did everyone know what to do?
  - Were runbooks correct and complete?
  - Did it recover on the expected time?
- It works like a training mechanism! (Train on-calls)

## Types of validation tests

- Dependency isolation
- Recovery actions
- Alarm sensitivity
- Sufficient capacity

## Process

Chaos engineering is about identifying the `Steady State` of a system (the stable state of a system)

1. Hypothesis for a failure
2. Run experiment using fault injection
3. Verify results
4. Improve the system
