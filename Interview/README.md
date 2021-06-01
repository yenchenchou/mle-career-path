# **Cracking Interviews**

## **Data Engineer**

## **Data Scientist**

1. Preparation before Data Scientist Interviews
    - ask if not specified: the topic of the interview, how long, how it will be conducted, availability
    - companies can wait
    - research
        - What metrics it could be
        - What is the company's problem
    - read your resume again
        - Useful whebn talking about the project
            - high level:
                - goal
                - why your work is impactful
            - Detail:
                - the type of data
                - property and uniqueness of the data
                - How I process the data
                - What method
                - interesting insight

## **Machine Learning Enigneer**

## Behavioral Questions

1. Self intro
2. Tell me about a time when you solve the difficulty.
    - telemarketing
    - issue: data collections quality
        - accuracy
        - completeness - feedback for each call, no phone recording
        - consistency - the standard of defining whether it is a bad/neutral result is unclear.
        - timeless
        - validity
        - uniqueness

3. Tell me a challenge that you solve
    - Data Scientist
        - telemarketing - redpass
        - Issue:
            - convertion rate drop in a week
        - Problem finding:
            - Look at metrics related to internal factors
                - wrong about the experiment
                - ml process
                    - predicted accuracy/recall didn't changed
            - Look at the metrics related to external factors
                - Contacts Per Hour dropped
                - Sales Per Hour dropped
                - Average Wrap Time (AWT) increased
                - Return on Investment per call dropped
                -> so we start to ask what has changed after we deliver the api
                    -> complex interface
        - Solution:
            - Remove the new features and advice on the UI
            - advice on the UI, use graph and replace table and text
        - Result:
            - regain the 5% dropped rate

4. Can you describe your most difficult customer and how you were able to handle their needs? Or tell a experience that you persuade others
    - Data Scientist
        - telemarketing - recommended items
        - Issue:
            the customer stragegy team insist to put 100+ columns of info to the telemarketers but it was proved that telemarketers' performance were affected at the same time.
        - Solution:
            - Prioritize the importance of the 100+ columns
            - use graphs instead table
                - recommended items into barplots and only show top/lowest numbers per graph according business scenario
                    - Showing Items that simaliar customers bought but they didn't
                - only shows items they view many times but didn't buy

        - Result:
            - Saved 60% time for preparation
            - enhanced dials per hour from 7 to 9
