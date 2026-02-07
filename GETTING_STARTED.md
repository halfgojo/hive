# Getting Started with Aden Hive

**Congratulations!** You've successfully set up the Aden Hive development environment. This guide will help you take your next steps, from verifying your installation to building your first AI agent.

---

## ✅ Verify Your Setup

First, let's make sure everything is working correctly:

```bash
# Activate the virtual environment (if not already activated)
source .venv/bin/activate

# Verify framework installation
python -c "import framework; print('✓ Framework installed')"

# Verify tools installation  
python -c "import aden_tools; print('✓ Tools installed')"
```

**Expected output:**
```
✓ Framework installed
✓ Tools installed
```

---

## 🚀 Run Your First Agent

The quickest way to see Hive in action is to run an example agent:

```bash
# Navigate to the examples directory
cd examples/recipes/search_agent

# Run the search agent example
python agent.py
```

This will start an interactive agent that can search the web and provide answers based on real-time information.

### Other Example Agents

Explore more examples in the `examples/` directory:

- **`recipes/`** - Pre-built agent recipes for common use cases
- **`templates/`** - Starting templates for custom agents

---

## 📚 Understand the Project Structure

Here's a quick overview of the repository:

```
hive/
├── core/              # Core agent framework
│   ├── framework/     # Agent runtime, MCP server, credentials
│   └── ...
├── tools/             # Tool integrations (web search, file ops, etc.)
│   └── src/aden_tools/
├── examples/          # Example agents and templates  
│   ├── recipes/       # Ready-to-use agent examples
│   └── templates/     # Agent templates for custom builds
├── DEVELOPER.md       # Complete developer guide
├── ENVIRONMENT_SETUP.md   # Setup and configuration details
└── quickstart.sh      # Automated setup script (you just ran this!)
```

---

## 🛠️ Build Your Own Agent

Ready to create a custom agent? You have several options:

### Option 1: Use Claude Code (Recommended)

If you have Claude Code installed:

```bash
# Open Claude Code in this directory
claude

# Use the agent-building workflow
/agent-workflow
```

### Option 2: Start from a Template

```bash
# Copy a template to get started
cp -r examples/templates/basic_agent my_agent
cd my_agent

# Edit agent.py to customize behavior
```

### Option 3: Manual Creation

Follow the detailed guide in [DEVELOPER.md](DEVELOPER.md#creating-agents) for step-by-step instructions on building agents from scratch.

---

## 🔧 Common Next Steps

### Configure API Keys

Most agents require LLM API access. If you haven't already:

```bash
# Add your API key to .env
echo "ANTHROPIC_API_KEY=your-key-here" >> .env

# Or set it in your environment
export ANTHROPIC_API_KEY="your-key-here"
```

Supported providers:
- Anthropic (Claude)
- OpenAI (GPT)
- Google Gemini
- Groq, Cerebras, Mistral, and more

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md#api-keys-optional) for details.

### Explore Tools

Hive comes with built-in tools for common tasks:

```bash
# See all available tools
ls tools/src/aden_tools/tools/
```

Popular tools include:
- `web_search` - Search the web with Brave or Google
- `file_operations` - Read/write files
- `python_execution` - Execute Python code safely
- `browser` - Automated browser interactions

---

## 📖 Further Reading

- **[DEVELOPER.md](DEVELOPER.md)** - Complete development guide
- **[ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)** - Environment configuration details  
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to Hive
- **[ROADMAP.md](ROADMAP.md)** - Project roadmap and future plans

---

## ❓ Troubleshooting

### Import Errors

If you see `ModuleNotFoundError`:

```bash
# Make sure you're in the venv
source .venv/bin/activate

# Re-run sync if needed
uv sync
```

### API Key Issues

If agents fail with authentication errors:

```bash
# Check if your key is set
echo $ANTHROPIC_API_KEY

# Verify it's in .env
cat .env | grep ANTHROPIC_API_KEY
```

### Example Agent Not Found

If `cd examples/recipes/search_agent` fails:

```bash
# Check what example agents are available
ls examples/recipes/
```

For more troubleshooting, see [ENVIRONMENT_SETUP.md - Troubleshooting](ENVIRONMENT_SETUP.md#troubleshooting).

---

## 💬 Get Help

- **GitHub Issues:** [adenhq/hive/issues](https://github.com/adenhq/hive/issues)
- **Discord:** Join the Hive community
- **Documentation:** Full guides in `DEVELOPER.md` and `ENVIRONMENT_SETUP.md`

---

**Happy building! 🚀**
