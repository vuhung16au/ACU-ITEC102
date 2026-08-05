import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, MagicMock
from main import get_llm_response

def test_get_llm_response():
    """
    Test the get_llm_response function using a mocked OpenAI client
    to avoid hitting the actual API during tests.
    """
    mock_client = MagicMock()
    
    # Set up the mock response structure
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Mocked Response"
    
    mock_client.chat.completions.create.return_value = mock_response
    
    prompt = "Test prompt"
    result = get_llm_response(prompt, mock_client)
    
    # Verify the mocked response
    assert result == "Mocked Response"
    
    # Verify the client was called with correct parameters
    mock_client.chat.completions.create.assert_called_once_with(
        model="deepseek-v4-pro",
        messages=[{"role": "user", "content": prompt}]
    )
