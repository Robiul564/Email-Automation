"""
Quick test script to verify the setup works
Run: python test_setup.py
"""

import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

def test_setup():
    """Test if all dependencies are installed and API key is set."""
    
    print("="*70)
    print("TESTING SETUP")
    print("="*70)
    
    # Test 1: Check imports
    print("\n1. Testing imports...")
    try:
        import openai
        print("   ✓ openai imported successfully")
    except ImportError:
        print("   ✗ openai not installed. Run: pip install -r requirements.txt")
        return False
    
    try:
        from src.email_generator import EmailGenerator
        print("   ✓ EmailGenerator imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import EmailGenerator: {e}")
        return False
    
    try:
        from src.evaluation_metrics import EmailEvaluator
        print("   ✓ EmailEvaluator imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import EmailEvaluator: {e}")
        return False
    
    try:
        from data.test_scenarios import get_test_scenarios
        print("   ✓ Test scenarios imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import test scenarios: {e}")
        return False
    
    # Test 2: Check API key
    print("\n2. Testing API key configuration...")
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_api_key_here":
        print("   ✓ OPENAI_API_KEY is set")
    else:
        print("   ✗ OPENAI_API_KEY not found or not configured")
        print("   Please set OPENAI_API_KEY in .env file or environment")
        return False
    
    # Test 3: Check test data
    print("\n3. Testing data...")
    scenarios = get_test_scenarios()
    print(f"   ✓ Loaded {len(scenarios)} test scenarios")
    
    if len(scenarios) != 10:
        print(f"   ✗ Expected 10 scenarios, got {len(scenarios)}")
        return False
    
    # Test 4: Check API connection
    print("\n4. Testing OpenAI API connection...")
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        # Simple test
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Setup test successful' in one sentence"}],
            max_tokens=10
        )
        print("   ✓ OpenAI API connection successful")
        print(f"   Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"   ✗ OpenAI API connection failed: {e}")
        return False
    
    print("\n" + "="*70)
    print("✓ ALL TESTS PASSED - Setup is complete!")
    print("="*70)
    print("\nYou can now run: python main.py")
    return True


if __name__ == "__main__":
    success = test_setup()
    if not success:
        print("\n✗ Setup verification failed. Please fix the issues above.")
        exit(1)
