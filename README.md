# Airport Passenger CRM AI Agent

An intelligent AI agent for managing airport passenger services, built with LangChain and Streamlit.

## Features

- 🔍 **Passenger Lookup**: Search passenger information by email
- ✈️ **Booking Management**: View and manage flight bookings
- 📊 **Flight Status**: Real-time flight status tracking
- 🎫 **Service Requests**: Request lounge access, wheelchair assistance, and more
- 💎 **Loyalty Program**: Track frequent flyer status and miles

## Quick Start

### 1. Installation

```bash
# Clone or download the project
cd airport-crm-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Get API Key

You need either:
- **OpenAI API Key**: Get from https://platform.openai.com/api-keys
- **Anthropic API Key**: Get from https://console.anthropic.com/

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 4. Configuration

In the sidebar:
1. Choose your API provider (OpenAI or Anthropic)
2. Enter your API key
3. Select the model
4. Start chatting!

## Demo Data

The application comes with pre-populated demo data:

**Passengers:**
- Email: john.smith@email.com (Gold tier, 45,000 miles)
- Email: sarah.j@email.com (Platinum tier, 87,000 miles)
- Email: m.brown@email.com (Bronze tier, 5,000 miles)

**Bookings:**
- BK001 (John Smith - AA101, JFK to LAX)
- BK002 (Sarah Johnson - UA202, ORD to MIA)

**Flights:**
- AA101 (JFK to LAX - On Time)
- UA202 (ORD to MIA - Delayed 30 minutes)

## Example Queries

Try asking:
- "Check my booking BK001"
- "What's the status of flight AA101?"
- "Look up passenger john.smith@email.com"
- "I need wheelchair assistance for my flight"
- "Request lounge access for PAX001"

## Project Structure

```
airport-crm-agent/
├── app.py                 # Main Streamlit application
├── agent/
│   ├── crm_agent.py      # AI agent implementation
│   ├── tools.py          # Custom tools for the agent
│   └── prompts.py        # System prompts
├── database/
│   ├── models.py         # SQLAlchemy models
│   └── db_handler.py     # Database operations
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Deployment

### Streamlit Cloud (Free)
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your repository
4. Deploy!

### Docker
```bash
docker build -t airport-crm-agent .
docker run -p 8501:8501 airport-crm-agent
```

### Local Network
```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

## Customization

### Adding New Tools
Edit `agent/tools.py` to add new capabilities:
```python
def my_new_tool(param: str) -> str:
    # Your logic here
    return "Result"

tools.append(
    Tool(
        name="MyNewTool",
        func=my_new_tool,
        description="What this tool does"
    )
)
```

### Changing Database
Replace SQLite with PostgreSQL in `database/db_handler.py`:
```python
db_url='postgresql://user:password@localhost/airport_crm'
```

### Modifying System Prompt
Edit `agent/prompts.py` to change agent behavior and personality.

## Cost Considerations

**OpenAI:**
- GPT-4: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens
- GPT-3.5: ~$0.001 per 1K input tokens, ~$0.002 per 1K output tokens

**Anthropic Claude:**
- Claude Sonnet: ~$0.003 per 1K input tokens, ~$0.015 per 1K output tokens
- Claude Haiku: ~$0.00025 per 1K input tokens, ~$0.00125 per 1K output tokens

Average conversation cost: $0.05 - $0.20

## Troubleshooting

**Issue: "No module named 'agent'"**
- Make sure you're running from the project root directory
- Ensure `__init__.py` files exist in agent/ and database/ folders

**Issue: "API key not found"**
- Enter your API key in the sidebar
- Check that you're using the correct provider (OpenAI vs Anthropic)

**Issue: Database errors**
- Delete `airport_crm.db` file and restart the app
- The database will be recreated with demo data

## Support

For issues or questions:
1. Check the demo data is loaded correctly
2. Verify your API key is valid
3. Check the Streamlit logs for error messages

## License

MIT License - Feel free to use for your projects!

## Next Steps

- Add authentication for production use
- Integrate with real airline APIs (Amadeus, Sabre)
- Add payment processing for services
- Implement email notifications
- Add multi-language support
- Create mobile app version

Happy building! 🚀
