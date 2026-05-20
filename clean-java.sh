#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")" && pwd)"

echo "Cleaning Java build artifacts in: $repo_root"

deleted_class_count=0
deleted_out_count=0
deleted_build_count=0

while IFS= read -r -d '' class_file; do
  rm -f "$class_file"
  deleted_class_count=$((deleted_class_count + 1))
done < <(find "$repo_root" -type f -name "*.class" -print0)

while IFS= read -r -d '' out_dir; do
  rm -rf "$out_dir"
  deleted_out_count=$((deleted_out_count + 1))
done < <(find "$repo_root" -type d -name "out" -print0)

while IFS= read -r -d '' build_dir; do
  rm -rf "$build_dir"
  deleted_build_count=$((deleted_build_count + 1))
done < <(find "$repo_root" -type d -name "build" -print0)

echo "Removed .class files: $deleted_class_count"
echo "Removed out/ directories: $deleted_out_count"
echo "Removed build/ directories: $deleted_build_count"
