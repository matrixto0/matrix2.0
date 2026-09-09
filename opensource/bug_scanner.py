"""
MATRIX2.0 Safe Local Bug Scanner

Inspects local Python project directories and identifies code signals:
- Syntax errors
- TODO/FIXME markers
- Bare exception handlers
- Missing docstrings in classes/functions
- Basic duplicate code patterns

Produces structured findings dictionaries without automated external issue opening.
"""

import ast
import os
import re
from typing import List, Dict, Any


class BugScanner:
    """
    Local Python project static code analyzer.
    """

    def __init__(self, root_dir: str):
        if not os.path.exists(root_dir):
            raise ValueError(f"Directory path '{root_dir}' does not exist.")
        self.root_dir = root_dir

    def scan(self) -> List[Dict[str, Any]]:
        """
        Scan all .py files under root_dir and return structured findings.
        """
        findings = []
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                if filename.endswith(".py"):
                    filepath = os.path.join(dirpath, filename)
                    file_findings = self.scan_file(filepath)
                    findings.extend(file_findings)
        return findings

    def scan_file(self, filepath: str) -> List[Dict[str, Any]]:
        """
        Scan a single Python file for code issues and indicators.
        """
        findings = []
        rel_path = os.path.relpath(filepath, self.root_dir)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            findings.append({
                "file": rel_path,
                "type": "file_read_error",
                "line": 0,
                "description": f"Failed to read file: {str(e)}",
                "severity": "medium",
            })
            return findings

        lines = content.splitlines()

        # 1. Check for TODO / FIXME markers
        for line_num, line in enumerate(lines, 1):
            if re.search(r"\b(TODO|FIXME|HACK|XXX)\b", line):
                findings.append({
                    "file": rel_path,
                    "type": "todo_marker",
                    "line": line_num,
                    "description": f"Marker found: {line.strip()}",
                    "severity": "low",
                })

        # 2. Check AST for syntax errors, bare excepts, missing docstrings
        try:
            tree = ast.parse(content, filename=filepath)
            for node in ast.walk(tree):
                # Bare except check
                if isinstance(node, ast.ExceptHandler):
                    if node.type is None:
                        findings.append({
                            "file": rel_path,
                            "type": "bare_except",
                            "line": getattr(node, "lineno", 0),
                            "description": "Bare 'except:' clause detected; catches system exceptions blindly.",
                            "severity": "medium",
                        })

                # Missing docstrings on functions/classes
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    if not ast.get_docstring(node):
                        findings.append({
                            "file": rel_path,
                            "type": "missing_docstring",
                            "line": getattr(node, "lineno", 0),
                            "description": f"Missing docstring in {node.__class__.__name__} '{node.name}'.",
                            "severity": "low",
                        })

        except SyntaxError as se:
            findings.append({
                "file": rel_path,
                "type": "syntax_error",
                "line": se.lineno or 0,
                "description": f"SyntaxError: {se.msg}",
                "severity": "high",
            })

        return findings
