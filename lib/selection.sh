# shellcheck shell=bash

agents=()
requested_skills=()
selected_skill_dirs=()
agents_filtered=false
skills_filtered=false

selection_error() {
  local command_name="$1"
  local message="$2"

  printf '%s: %s\n' "$command_name" "$message" >&2
  exit 2
}

selection_usage() {
  local command_name="$1"

  cat <<EOF
Usage: ./$command_name [--agent codex|claude|copilot]... [--skill NAME]...

Repeat --agent and --skill to select multiple agents or skills. Omitting
--agent selects all agents; omitting --skill selects all skills.
EOF
}

parse_selection_args() {
  local command_name="$1"
  local selected_agent
  local selected_skill
  local already_selected
  shift

  agents=(codex claude copilot)
  requested_skills=()
  agents_filtered=false
  skills_filtered=false

  while (($# > 0)); do
    case "$1" in
      --agent)
        (($# >= 2)) || selection_error "$command_name" "--agent requires a value"
        case "$2" in
          codex|claude|copilot) ;;
          *) selection_error "$command_name" "unknown agent '$2' (choose codex, claude, or copilot)" ;;
        esac
        if [[ "$agents_filtered" == false ]]; then
          agents=()
          agents_filtered=true
        fi
        already_selected=false
        for selected_agent in "${agents[@]}"; do
          if [[ "$selected_agent" == "$2" ]]; then
            already_selected=true
            break
          fi
        done
        if [[ "$already_selected" == false ]]; then
          agents+=("$2")
        fi
        shift 2
        ;;
      --skill)
        (($# >= 2)) || selection_error "$command_name" "--skill requires a value"
        [[ "$2" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || selection_error "$command_name" "invalid skill name '$2'"
        skills_filtered=true
        already_selected=false
        for selected_skill in "${requested_skills[@]}"; do
          if [[ "$selected_skill" == "$2" ]]; then
            already_selected=true
            break
          fi
        done
        if [[ "$already_selected" == false ]]; then
          requested_skills+=("$2")
        fi
        shift 2
        ;;
      --help|-h)
        selection_usage "$command_name"
        exit 0
        ;;
      *)
        selection_error "$command_name" "unknown argument '$1' (use --help for usage)"
        ;;
    esac
  done
}

resolve_skill_dirs() {
  local command_name="$1"
  local repo_dir="$2"
  local skill_name
  local skill_dir
  local -a all_skill_dirs

  shopt -s nullglob
  all_skill_dirs=("$repo_dir"/skills/*)
  selected_skill_dirs=()

  if [[ "$skills_filtered" == true ]]; then
    for skill_name in "${requested_skills[@]}"; do
      skill_dir="$repo_dir/skills/$skill_name"
      [[ -d "$skill_dir" ]] || selection_error "$command_name" "unknown skill '$skill_name'"
      selected_skill_dirs+=("$skill_dir")
    done
  else
    for skill_dir in "${all_skill_dirs[@]}"; do
      [[ -d "$skill_dir" ]] || continue
      selected_skill_dirs+=("$skill_dir")
    done
  fi
}
