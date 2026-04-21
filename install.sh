#!/usr/bin/env bash
#
# Installs the CLIs + Claude Code skills this repo depends on.
#
# Binaries: each tool ships an installer that downloads the right binary for
# the current platform (macos-arm64, macos-amd64, linux-amd64, windows-amd64)
# and places it in /usr/local/bin.
#
# Skills: each CLI repo ships a SKILL.md that teaches Claude how to use the
# CLI. We fetch them into .claude/skills/<name>-agent/ (gitignored — re-fetch
# by re-running this script).

set -eu

# repo_slug:skill_name
tools=(
  "pubmed-cli:pubmed-agent"
  "fooddate-cli:fooddata-agent"
  "migros-cli:migros-agent"
  "iherb-cli:iherb-agent"
  "reddit-cli:reddit-agent"
)

repo_root=$(cd "$(dirname "$0")" && pwd)
skills_dir="${repo_root}/.claude/skills"
mkdir -p "$skills_dir"

bold=$(tput bold 2>/dev/null || true)
reset=$(tput sgr0 2>/dev/null || true)

echo "${bold}Installing health-dossier CLI tools${reset}"
echo "Targets: $(printf '%s ' "${tools[@]%:*}")"
echo

failed=()
for entry in "${tools[@]}"; do
  repo="${entry%:*}"
  skill="${entry#*:}"

  echo "${bold}→ ${repo}${reset}"

  installer_url="https://raw.githubusercontent.com/SeverinAlexB/${repo}/master/install.sh"
  if ! curl -fsSL "$installer_url" | bash; then
    echo "  binary installer for ${repo} failed"
    failed+=("${repo} (binary)")
    echo
    continue
  fi

  skill_url="https://raw.githubusercontent.com/SeverinAlexB/${repo}/master/skills/${skill}/SKILL.md"
  mkdir -p "${skills_dir}/${skill}"
  if curl -fsSL "$skill_url" -o "${skills_dir}/${skill}/SKILL.md"; then
    echo "  skill installed → .claude/skills/${skill}/"
  else
    echo "  skill fetch for ${repo} failed"
    failed+=("${repo} (skill)")
  fi
  echo
done

if [ ${#failed[@]} -ne 0 ]; then
  echo "${bold}Some installers failed:${reset} ${failed[*]}"
  exit 1
fi

echo "${bold}All tools and skills installed.${reset}"
echo "Verify with: pubmed-cli --version && fooddata-cli --version && migros-cli --version && iherb-cli --version && reddit-cli --version"
