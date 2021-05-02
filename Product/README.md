# Product Related Problems

## Interview Basics

1. What are interviewers lookin for and what is a good answer
   - Structure: you may systematic approach
   - Comprehebsiveness: Cover the all the important aspects of the problem
   - Feasible: The solution should be practical to be implemented
2. Product development cycles:
   1. Comming up with initial product ideas
   2. Select the subset of ideas using quantitative analysis to choose which ideas worth spend, often refers to [oppotunity sizing](https://medium.com/related-works-inc/intro-to-opportunity-sizing-ce9d7e5a29c4)
   3. Experimental design: involving with selecting success and guardrail sucess, running sanity check, choosing randomization units...etc. Need to consider alternatives when A/B testing is unachievable.
   4. Making launch decision based on experiment results. Diagnosing problems and evaluating tradeoffs.

## Metrics Frameworks

Through out the product development cycle, we need to decide the most important thing, the **metrics**.

### 1. Metrics

1. Overview metrics:
Overall, a good metric should be
    - simple: easy to understand and calculate. People are able to remember and discuss it easily.
    - clear: the definition is explicit and no ambiguity in interpretation.
    - actionable: can be moved by improving products and not easily gamed.
    - Taxonomy of metrics
        - Success metrics
            - Click through rate (CTR)
            - Call to action (CTA) -> CTR
            - Daily active users (DAU)
            - Monthly active users(MAU)
            - Bookins / subscription
            - Purchase
            - Revenue
            - Conversion rate (CVR) (refers to call to action)
        - Guardail metrics
            - Customer Churn - cancellation / unsubscription rate, bounce rate
            - latency
            - Initial customer acquisition cost (CAC)
    - Common Metric Framework to cover the business
        - General funnel metrics: track "user journey"
            - AARRR growth metrics framework
            - Conversion funnels (B2C):
                - Number of visitors to webpage
                - Number of logged in users
                - Number of users click particular parts of logged in pages
                - Number of users visit checkout page
                - Number of users who purchase
            - Conversion funnels (B2B):
                - Number of visitors to webpage
                - Number of visitors requests for free trials
                - Number of leads to which the sales team proactively reach out
                - Number of contract
                - Number of paid customers who made recurrent purchases
        - Input-output Metrics Frameworks
            - Input / driver metrics: metrics that track the activities and resources used to work towards to outcome.
                - Common: CTR, avg spent time on particular section
                - Fraud detection: FP/FN rate of models, transaction amount
            - Output metrics: metrcs that demostrate the outcome of an initiative
                - Common: session per user, advertisement revenue
                - Fraud detection: fraud loss volumes, loss prevented, revenue...etc.
        - Domain Specific
            - AARRR growth metrics framework
                - Acquisition: getting customer sign up, which requires product awaireness.
                - Activation: Customer get familiar with products.
                - Rentention: customers come back on regualr basis
                - Referral: Customer share the product to others
                - Revenue: customer paid more and more

        - Platform Metrics (Customer Support, Trust and Safety, Payments, Infrastructure, Operations, etc.)

            - Cost of infra / operations:
            - Sucess / Failure rate: payment
            - FP / FN / TP / Fraud loss metrics: fraud
            - Vendor costs: telemarketing
