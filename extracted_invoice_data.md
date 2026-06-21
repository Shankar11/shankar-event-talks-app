# Extracted Invoice Data

This table summarizes the extracted key data fields from the invoice images located in the [invoice-processing/](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/) directory.

---

## 📊 Summary Table

| Invoice File | Invoice No | Invoice Date | Invoice Sent By | Due Date | Due Amount |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [inv1.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv1.png) | `01234` | 11.02.2030 | Adeline Palmerston | 11.03.2030 | $440.00 |
| [inv2.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv2.png) | `US-001` | 11/02/2019 | East Repair Inc. | 26/02/2019 | $154.06 |
| [inv3.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv3.png) | `123456789` (P.O. #) | November 23, 2023 | A Company With A Clever Name | November 30, 2023 | $42.30 |
| [inv4.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv4.png) | `123456` | 12/9/2019 | Company Name | 1/8/2020 | $971.56 |

---

## 🔍 Extraction Details

*   **[inv1.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv1.png)**: The invoice is issued to *Richard Sanchez / Thynk Unlimited* by *Adeline Palmerston* (account name in Pay To section). The total due amount includes a $400 subtotal and 10% tax, equaling **$440.00**.
*   **[inv2.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv2.png)**: The invoice is from *East Repair Inc.*, billed to *John Smith*. The total amount is **$154.06** (includes a 6.25% sales tax).
*   **[inv3.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv3.png)**: The document is a commercial invoice from *A Company With A Clever Name (docubee)*. Since no explicit invoice number is listed, the Purchase Order number (`123456789`) was extracted as the identifier. The total is **$42.30**.
*   **[inv4.png](file:///F:/LearnWS/AntiGravityIDE/my-first-proj/invoice-processing/inv4.png)**: Standard invoice template from *Company Name*, billed to `[Name]`. The total due amount is **$971.56**.
