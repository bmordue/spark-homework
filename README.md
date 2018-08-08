Run tests
---
1. `pip install -r requirements.txt`
2. `python main.py`

Description of test cases
---

1. Get tariffs for a user without a current Spark account, combined quote, no smart meter, based on size of house (current supplier not known). Verify tariff names offered and projections.
2. As above, but get a quote for electricity only for a single bedroom in a different post code.
3. Using the quote type and usage as above, select the 'Super Tracker'. Verify that the details for tariff are shown.
