# LLM Comprehension Evaluation

This directory contains research and evaluation tools for testing how well LLMs understand different data formats.

## ⚠️ Requirements

- OpenAI API key (set `OPENAI_API_KEY` environment variable)
- Internet connection for API calls
- These tests **cost money** to run (OpenAI API usage)

## Test Files

### Core Evaluation Scripts

- `test_llm_comprehension.py` - Deep-TOON format LLM comprehension test
- `test_llm_comprehension_original_toon.py` - Original TOON format test  
- `test_llm_comprehension_3way.py` - 3-way comparison (JSON vs Deep-TOON vs Original TOON)

### Support Files

- `test_data_questions.py` - Modular test data and questions (16 simple + 4 complex)

## Usage

```bash
# Basic Deep-TOON evaluation
python evaluation/test_llm_comprehension.py

# Compare against Original TOON
python evaluation/test_llm_comprehension_original_toon.py

# Full 3-way comparison
python evaluation/test_llm_comprehension_3way.py

# With cost controls and debug options
python evaluation/test_llm_comprehension.py --max-calls 50 --debug
python evaluation/test_llm_comprehension_3way.py --max-calls 100 --analyze-failures
```

## Test Structure

**Simple Tests (16 questions)**: Basic field retrieval, content search
- ✅ Originally achieved 100% success rate
- Tests fundamental format parsing capabilities

**Complex Tests (4 questions)**: Advanced analytics, aggregation, filtering  
- More challenging - tests format limitations
- Helps identify improvement areas

## Cost Control

All tests have built-in API call limits:
- Default: 50 calls (~$0.01)
- 3-way test: 100 calls (~$0.02) 
- With failure analysis: 150 calls (~$0.03)

## Results Interpretation

- **Compression**: Token savings compared to JSON
- **Equivalence**: LLM-as-judge determines if responses match
- **Confidence**: Judge's confidence in equivalence decision
- **Roundtrip**: Format can encode/decode without data loss

## Not for CI/Build

These are **research tools**, not unit tests:
- Don't run automatically in CI
- Require manual execution with API keys
- Take time and cost money to run