# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal technical knowledge base. All content is Markdown files organized into topic directories at the root. The primary usage pattern is searching by filename or grepping for a keyword/topic to find a reference.

## Structure

Top-level directories group content by broad technical domain (e.g. `cloud/`, `language/`, `networking/`, `algorithms/`). The structure is intentionally fluid — directories and nesting evolve over time. Use `ls` or file search to discover the current layout rather than assuming it.

## Content conventions

- Each topic is either a standalone `.md` file or a directory with a `<topic>.md` overview plus subtopic files.
- Images are stored in `.images/` directories co-located with the Markdown files that reference them.
- Code snippets (algorithm implementations, CLI examples) can be embedded directly in Markdown or stored as standalone source files (`.py`, `.clj`, `.go`, `.rs`, etc.) alongside the relevant `.md`. These source files are also reference material, not runnable projects.
