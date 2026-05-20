#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")" && pwd)"

# Usage:
#   ./run-java.sh [project-dir] [main-class]
# Examples:
#   ./run-java.sh
#   ./run-java.sh JAVA/notificationsystem
#   ./run-java.sh JAVA/notificationsystem notificationsystem.Main
project_dir_rel="${1:-JAVA/notificationsystem}"
project_dir="$repo_root/$project_dir_rel"
main_class="${2:-}"

if [[ ! -d "$project_dir" ]]; then
  echo "Project directory not found: $project_dir_rel" >&2
  exit 1
fi

sources=()
while IFS= read -r -d '' file; do
  rel="${file#"$project_dir"/}"
  # Skip files under build output folders if present.
  if [[ "$rel" == out/* || "$rel" == build/* ]]; then
    continue
  fi
  sources+=("$rel")
done < <(find "$project_dir" -type f -name "*.java" -print0)

if [[ "${#sources[@]}" -eq 0 ]]; then
  echo "No .java files found in: $project_dir_rel" >&2
  exit 1
fi

if [[ -z "$main_class" ]]; then
  if [[ -f "$project_dir/Main.java" ]]; then
    pkg_name="$(awk '/^package[[:space:]]+/{gsub(/;/, "", $2); print $2; exit}' "$project_dir/Main.java")"
    if [[ -n "$pkg_name" ]]; then
      main_class="$pkg_name.Main"
    else
      main_class="Main"
    fi
  else
    echo "Main class not provided and Main.java not found at project root." >&2
    echo "Usage: ./run-java.sh <project-dir> <main-class>" >&2
    exit 1
  fi
fi

out_dir="$project_dir/out"
mkdir -p "$out_dir"

(
  cd "$project_dir"
  javac -d out "${sources[@]}"
  java -cp out "$main_class"
)
