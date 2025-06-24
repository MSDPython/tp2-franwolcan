import subprocess

def test_pepe_commit_exists():
    try:
        # Get all commit messages
        result = subprocess.run(
            ["git", "log", "--pretty=format:%s"],  # %s = commit subject
            capture_output=True,
            text=True,
            check=True
        )
        commit_messages = result.stdout.splitlines()
        
        # Check if any message contains "pepe commit"
        assert any("pepe commit" in msg for msg in commit_messages), \
            "No commit message containing 'pepe commit' was found."

    except subprocess.CalledProcessError as e:
        raise AssertionError("Failed to run git log") from e
