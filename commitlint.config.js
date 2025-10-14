export default {
    ignores: [
        // Allow commit messages that start with `[pre-commit.ci]`
        (message) => message.startsWith('[pre-commit.ci]'),
        // Allow commits from GitHub Copilot
        (message) => message.includes('Co-authored-by:'),
    ]
}
