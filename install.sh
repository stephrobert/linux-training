#!/usr/bin/env bash
pipx install pytest
pipx inject pytest pytest-testinfra
